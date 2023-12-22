# Run this file only if database is not yet created
import mysql.connector
from mysqlconfig import HOST, USER, PASSWORD

mydb = mysql.connector.connect(
    host=HOST,
    user=USER,
    passwd=PASSWORD,
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE introverse")

# Can run this bit below too if you want to see all the databases in your MySQL (and will confirm creation of new one)
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)