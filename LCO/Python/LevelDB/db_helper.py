import sqlite3

db="mytodo.db"
table_name="task"

conn=sqlite3.connect(db)
c=conn.cursor()

def create_table():
    sql='CREATE TABLE IF NOT EXISTS ' + table_name \
      + '(ID INTEGER PRIMARY KEY AUTOINCREMENT, TASKNAME text)'
    c.execute(sql)

def data_entry(task):
    c.execute('INSERT INTO ' + table_name + ' (TASKNAME) VALUES (?)', [task])
    conn.commit()
    print("Task is added in the database")

def printData():
    sql="SELECT * FROM " + table_name
    c.execute(sql)
    for row in c.fetchall():
        print(row[0], "---->", row[1])

def deleteTask(index):
    sql="DELETE FROM " + table_name + " WHERE ID=? ", (index, )
    c.execute(sql)
    print("Task is deleted from database")

def closeCursor():
    c.close()
    conn.close()