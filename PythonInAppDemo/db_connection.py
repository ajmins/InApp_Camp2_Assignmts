#importing pyodbc module
import pyodbc as pd
#ODBC connection, but now it's not using, nowadays using ORM
"""
Set-ExecutionPolicy -Scope CurrentUser 
-ExecutionPolicy Unrestricted
"""
#create a connection string
#conString = 'Driver={SQL Server};Server=DESKTOP-CJEOG7N\SQLEXPRESS;Database=employee_db1;Trusted_Connection=yes;'
conString2 = 'Drive={ODBC Driver 17 for SQL Server};Server=LAPTOP-R5LS4JCT\SQLEXPRESS;Database=employee_db1;Trusted_Connection=yes;'

#create a connection with the connection string
#myConn = pyodbc.connect(conString)
myConn2 = pd.connect(conString2)

#get the cursor object
#myCursor = myConn.cursor()
myCursor2 = myConn2.cursor()

#using cursor, execute SQL commands
#myCursor.execute('SELECT * FROM EmployeeMaster')
myCursor2.execute('SELECT * FROM Employee_det')

#to get the data
for i in myCursor2:
    print(i)

myCursor2.execute('SELECT name FROM sys.tables')
for i in myCursor2:
    print(i)

#commiting the transaction (required for all write/update/delete statements)
myConn2.commit()
myConn2.close()