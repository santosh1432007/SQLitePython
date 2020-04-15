import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_sqltable):

    try:
        c = conn.cursor()
        c.execute(create_sqltable)
    except Error as e:
        print(e)

def main():
    database = r"db\pysqlite.db"

    sql_project_table = """CREATE TABLE IF NOT EXISTS projects(
    id integer PRIMARY KEY, name text NOT NULL, begin_date text, end_date text);"""

    sql_task_table = """CREATE TABLE IF NOT EXISTS tasks(
    id integer PRIMARY KEY, name text NOT NULL, priority integer, status_id integer NOT NULL,
    project_id integer NOT NULL, begin_date text NOT NULL, end_date text NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects(id));"""

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_project_table)

        # create tasks table
        create_table(conn, sql_task_table)
    else:
        print("Error! The database connection couldn't be created.")
if __name__=='__main__':
    main()

