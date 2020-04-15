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

def create_project(conn, project):
    sql = '''INSERT INTO projects(name, begin_date, end_date)
              VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid

    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid

def create_task(conn, task):

   sql = '''INSERT INTO tasks(name, priority, status_id, project_id, begin_date, end_date)
   VALUES(?, ?, ?, ?, ?, ?)'''
   cur = conn.cursor()
   cur.execute(sql, task)
   return cur.lastrowid

def main():
    database = r"db\pysqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # Create a new project
        project = ('SQLite & Python', '2020-01-01', '2010-01-30');
        project_id = create_project(conn, project)

        # tasks
        event1 = ('Requirement Analysis', 1, 1, project_id, '2020-01-01', '2020-01-03')
        event2 = ('User Requirement', 1, 1, project_id, '2020-01-04', '2020-01-06')
        event3 = ('User Interface', 1, 1, project_id, '2020-02-01', '2020-02-10')
        event4 = ('Backend Development', 1, 1, project_id, '2020-03-01', '2020-03-30')
        event5 = ('Finalize Development', 1, 1, project_id, '2020-04-01', '2020-04-30')

        # Create tasks
        create_task(conn, event1)
        create_task(conn, event2)
        create_task(conn, event3)
        create_task(conn, event4)
        create_task(conn, event5)

if __name__=='__main__':
    main()