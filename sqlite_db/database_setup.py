#!/usr/bin/python

import sqlite3
from sqlite3 import Error
from sqlite_operations import sqlite_create_tables
from os.path import dirname, join



def get_root():
    return dirname(dirname(__file__))

# connect to the database file
# or create a new database file
def create_connection(db_path):
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        print("Connected to the database file")
        return conn

    except Error as e:
        print(e)


# execute all sqlite_create_tables sqlite commands defined in <sqlite_operations.py>
def create_tables(conn):
    if conn:
        for sqlite_create in sqlite_create_tables.values():
            try:
                cursor = conn.cursor()
                cursor.execute(sqlite_create)

            except Error as e:
                print(e)


# close connection
def close_connection(conn):
    if conn:
        conn.close()


if __name__ == "__main__":
    print("database_setup called!")
    db_path = join(get_root(), "sqlite_db", "database.db")
    conn = create_connection(db_path)
    create_tables(conn)
    close_connection(conn)
    print("database ready in:", db_path)


