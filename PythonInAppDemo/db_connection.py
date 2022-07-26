#importing pyodbc module
import pyodbc
#ODBC connection, but now it's not using, nowadays using ORM
"""
Set-ExecutionPolicy -Scope CurrentUser 
-ExecutionPolicy Unrestricted
"""
#create a connection string
conString = 'Driver={SQL Server};Server=DESKTOP-CJEOG7N\SQLEXPRESS;Database=employee_db1;Trusted_Connection=yes;'

#create a connection with the connection string
myConn = pyodbc.connect(conString)

#get the cursor object
myCursor = myConn.cursor()

#using cursor, execute SQL commands
myCursor.execute('SELECT * FROM EmployeeMaster')

#to get the data
for i in myCursor:
    print(i)

myCursor.execute('SELECT name FROM sys.tables')
for i in myCursor:
    print(i)

#commiting the transaction (required for all write/update/delete statements)
myConn.commit()
myConn.close()