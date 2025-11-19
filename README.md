# Data Insertion in MySQL using Python

This guide explains how to insert data into a MySQL database using Python. It covers installation, connection setup, cursor creation, writing insert queries, committing changes, and closing the connection. A real example is also included for better understanding.

### Install MySQL Connector
Before writing any code, install the MySQL connector package:
pip install mysql-connector-python

This package allows Python to communicate with MySQL databases.

### Connect Python to MySQL
To interact with a MySQL database, you must first create a connection using mysql.connector.connect().
Connection requires:

host

user

password

database name

If the connection is successful, Python can execute SQL commands inside that database.

Create a Cursor
After establishing a connection, a cursor object is created.
The cursor acts as a controller to run SQL queries like INSERT, SELECT, UPDATE, DELETE.

Example:
cursor = connection.cursor()

### Write INSERT Query
To add new records into a table, an INSERT INTO statement is used.
For example, if you have a table named students with fields (id, name, age), you can insert values using:
INSERT INTO students (name, age) VALUES (%s, %s)

Placeholders (%s) help write secure and clean queries.

### Execute the Query
Use cursor.execute(query, values) to run the insert command.
Example:
values = ("Rahul", 21)
cursor.execute(query, values)

### Commit the Changes
MySQL does not save changes permanently until commit() is called.
Use:
connection.commit()

Without commit(), inserted data will not appear in the database.

Close the Connection
Always close the connection using:
connection.close()

This is a good practice to free up resources and avoid unnecessary database usage.

Complete Example Code
Below is a full working example:

import mysql.connector

try:
connection = mysql.connector.connect(
host="localhost",
user="root",
password="yourpassword",
database="testdb"
)

if connection.is_connected():
    print("Connected to MySQL database")

    cursor = connection.cursor()

    query = "INSERT INTO students (name, age) VALUES (%s, %s)"
    values = ("Anant", 22)

    cursor.execute(query, values)
    connection.commit()

    print("Record inserted successfully")


except mysql.connector.Error as error:
print("Error:", error)

finally:
if connection.is_connected():
cursor.close()
connection.close()
print("MySQL connection closed")

### Best Practices

Always use placeholders (%s) for secure queries

Wrap code inside try–except for error handling

### Always call commit() after insert operations

Close connection in the finally block

Avoid hardcoding passwords (use environment variables in real projects)

This README gives you a complete idea of how to insert data into MySQL using Python with a clean and proper structure.
