# Run this file only if database is not yet created
from dotenv import load_dotenv
import os
import mysql.connector
# from mysqlconfig import HOST, USER, PASSWORD

load_dotenv()

mydb = mysql.connector.connect(
    host=os.getenv("HOST"),
    user=os.getenv("USER"),
    passwd=os.getenv("PASSWORD"),
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE introverse")

# Can run this bit below too if you want to see all the databases in your MySQL (and will confirm creation of new one)
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)