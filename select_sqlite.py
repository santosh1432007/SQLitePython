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

def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_task_by_priority(conn, priority):
    cur = conn.cursor()
    cur.execute("SELECT *FROM tasks WHERE priority=?", (priority,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def main():
    database = r"C:\Users\santo\PycharmProjects\Sqlite\db\pysqlite.db"
    conn = create_connection(database)

    with conn:
        print("1. Query task by priority:")
        select_task_by_priority(conn, 1)

        print("2. Query all tasks:")
        select_all_tasks(conn)

if __name__ == '__main__':
    main()