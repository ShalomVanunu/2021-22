
import DBhandle
import hashlib

def hash_to_user(user):
    hash_md5 = hashlib.md5(user.encode())  # make hash MD5 to  string
    hash_user = hash_md5.hexdigest()
    return hash_user

def update_user_on_db(user,hashuser):
    connection = DBhandle.connect_sqlite3("hashfile.db")
    sql = """ CREATE TABLE IF NOT EXISTS usershash (
        id INTEGER PRIMARY KEY AUTOINCREMENT ,
        username TEXT,
        hash TEXT
        );
        """
    DBhandle.db_change(connection,sql)
    sql = f"INSERT INTO usershash (username,hash) VALUES ('{user}','{hashuser}')"
    DBhandle.db_change(connection, sql)



# main code
user = input(" Enter Your User : ")
hash_user  = hash_to_user(user)
update_user_on_db(user,hash_user)
