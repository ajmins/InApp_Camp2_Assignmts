import pyodbc
#create a connection string
conString = 'Driver={SQL Server};Server=DESKTOP-CJEOG7N\SQLEXPRESS;Database=employee_db1;Trusted_Connection=yes;'

#create a connection with the connection string
myConn = pyodbc.connect(conString)

try:
    #get the cursor object
    myCursor = myConn.cursor()

    #using cursor, execute SQL commands
    myCursor.execute("""
       SELECT * FROM EmployeeMaster
        """)
except Exception as e:
    print("Cannot create the table because : ")
    #print(e) #to get the entire details about the exception
    print(f"{type(e).__name__} was occured") #to get the the name of exception only

for row in myCursor.fetchall(): 
    print(row)
#create a dictionary and save this into it
employees = [{' EmployeeCode':row[1], 'EmployeeName' : row[2], 'DepartmentCode' : row[3], 'LocationCode' : row[4], 'Salary' : row[5]}]
print(employees)


myConn.commit()
myConn.close()