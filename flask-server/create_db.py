from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv(override=True)

mydb = mysql.connector.connect(
    host=os.getenv("HOST"),
    user=os.getenv("USER"),
    passwd=os.getenv("PASSWORD"),
)

database = os.getenv("DATABASE")
test_database = os.getenv("TESTDB")
my_cursor = mydb.cursor()

def check_db_create_if_not_exist(dbname):
    """Will check if database already exists and create it if not"""
    my_cursor.execute(f"SHOW DATABASES LIKE '{dbname}';")
    for db in my_cursor:
        return f"{dbname} already exists"
    else:
        my_cursor.execute(f"CREATE DATABASE {dbname};")
        return f"{dbname} has been created"
    
print(check_db_create_if_not_exist(database))
print(check_db_create_if_not_exist(test_database))
