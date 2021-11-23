
import sqlite3

def connect_sqlite3(dbname):
    connection = sqlite3.connect(dbname)
    return connection

def db_change(connection,sql):
    cursor = connection.cursor()
    cursor.execute(sql) # execute the SQl command
    connection.commit() #DO the command
    print( "SQL executed succesfully")

def db_query(connection,sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows


# create DB connection
connection = connect_sqlite3("Myfistdb.db")
#Create TABLE
#https://www.w3schools.com/sql/sql_create_table.asp
# SELECT, INSERT INTO, UPDATE, DELETE, CREATE TABLE
#https://inloop.github.io/sqlite-viewer/
sql = """ CREATE TABLE IF NOT EXISTS users(
    id INT,
    username TEXT,
    password TEXT
    );
"""
db_change(connection,sql)

sql = """INSERT INTO users VALUES (1,"shalomv","Password1");"""

db_change(connection,sql)

sql1 = """INSERT INTO users VALUES (2,"roni","Password2");"""
db_change(connection,sql1)

#sql_delete = """DELETE FROM users WHERE username="shalomv";"""
#db_change(connection,sql_delete)

sql = """SELECT * FROM users"""
rows = db_query(connection,sql)

for row in rows:
    print(row)