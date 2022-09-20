import sqlite3 as sql
import random

def random_function(user_path: str, tables: list)->str:
    result = ''
    user_database = sql.connect(user_path)
    user_cursor = user_database.cursor()

    table_scraps = list()
    for x in tables:
        scrap = user_cursor.execute( "SELECT name FROM " + x + " ORDER BY RANDOM() LIMIT 1;").fetchall()
        table_scraps.append(scrap[0])

    result = random.choice(table_scraps)
    user_database.close()
    return result
