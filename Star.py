import os
import sqlite3 as sql3
import configparser

def build_user(new_database: str, new_password: str)->str:
    user_base = sql3.connect('user_base.db')
    cur_base = user_base.cursor()
    cur_base.execute(""" CREATE TABLE IF NOT EXISTS users ( name text(255) PRIMARY KEY, password text(255)); """)

    cur_base.execute("SELECT count(*) FROM users WHERE name = ?", (new_database,))
    data = cur_base.fetchall()[0]
    if data[0] != 0:
        print("Username taken.")
        user_base.close()
        return '/0'

    cur_base.execute(" INSERT INTO users(name, password) SELECT ?, ?", (new_database, new_password,))
    user_base.commit()
    user_base.close()

    this_dir = os.getcwd()
    database_path = os.path.join(this_dir, "Profiles", new_database)
    os.mkdir(database_path)
    database_path = os.path.join(database_path, new_database + ".db")
    conn = sql3.connect(database_path)
    conn.close()

    return new_database

def sign_in(user_name: str, password: str)->str:
    user_base = sql3.connect('user_base.db')

    cur = user_base.cursor()
    cur.execute("SELECT password FROM users WHERE name = ?", (user_name,))
    data = cur.fetchall()[0]
    if data[0] != password:
        user_base.close()
        return '/0'
    user_base.close()
    return user_name

def fetch_profile(user_name: str, password: str)->str:
    s = sign_in(user_name, password)
    return s