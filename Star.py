import Steam
import sqlite3 as sql3

def setup_user_base():
    conn = sql3.connect('user_base.db')

    conn.close()

def build_user():
    new_database = input("Please Enter A Username.\n")
    user_base = sql3.connect('user_base.db')
    cur_base = user_base.cursor()
    cur_base.execute(""" CREATE TABLE IF NOT EXISTS users (
                        name text PRIMARY KEY,
                        password text,
                    ); """)
    new_password = input("Please Add A Password.\n")
    cur_base.execute(" INSERT INTO users(name, password) SELECT ?, ?", (new_database, new_password,))
    user_base.commit()
    user_base.close()

    conn = sql3.connect(new_database + '.db')
    conn.close()
    return

def sign_in():
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