import sqlite3

def connect_sqlite3(dbname):
    connection = sqlite3.connect(dbname)
    return connection

def db_query(connection,sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows

connection = connect_sqlite3('Our_data.db')
sql = "SELECT * FROM employee_records"
rows = db_query(connection,sql)
print(rows)