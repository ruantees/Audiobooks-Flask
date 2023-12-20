import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",  # Use the newly created user
    password="Kipo7as22nirem!",  # Use the password for the new user
)

cursor = db.cursor()
cursor.execute("SHOW DATABASES")

for database in cursor:
    print(database)

db.close()  # Close the connection when done
