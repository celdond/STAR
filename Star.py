import Steam
import os
import sqlite3 as sql3

def build_user()->str:
    new_database = input("Please Enter A Username.\n")
    user_base = sql3.connect('user_base.db')
    cur_base = user_base.cursor()
    cur_base.execute(""" CREATE TABLE IF NOT EXISTS users (
                        name text PRIMARY KEY,
                        password text,
                    ); """)

    cur_base.execute("SELECT count(*) FROM users WHERE name = ?", (new_database))
    if cursor.fetchall()[0] != 0:
        print("Username taken.")
        user_base.close()
        return

    new_password = input("Please Add A Password.\n")
    cur_base.execute(" INSERT INTO users(name, password) SELECT ?, ?", (new_database, new_password))
    user_base.commit()
    user_base.close()

    this_dir = os.getcwd()
    database_path = os.path.join(this_dir, "Profiles", new_database)
    database_path = os.mkdir(database_path)
    conn = sql3.connect(os.path.join(database_path, new_database) + '.db')
    conn.close()

    return new_database

def sign_in():
    user_name = input("Username: \n")
    password = input("Password: \n");
    cwd = os.getcwd()
    
    return

def main():
    
    print("Star\n")
    print("New User - N\nReturning User - R\n")

    choice = input()

    if choice == 'N':
        build_user()
    elif choice == 'R':
        sign_in()

    return


main()