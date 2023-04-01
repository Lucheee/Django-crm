import mysql.connector

DATABASE = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Oluchie51@'
)

cursorObject = DATABASE.cursor()

#create the database
cursorObject.execute("CREATE DATABASE Oluchi")

print("Created sucessfully!")