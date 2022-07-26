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
        CREATE TABLE EmployeeMasterNew
        (
            Id INT IDENTITY PRIMARY KEY,
            EmployeeCode VARCHAR(10),
            EmployeeName VARCHAR(25),
            DepartmentCode VARCHAR(10),
            LocationCode VARCHAR(10),
            Salary INT
        ) 
        """)
except Exception as e:
    print("Cannot create the table because : ")
    #print(e) #to get the entire details about the exception
    print(f"{type(e).__name__} was occured") #to get the the name of exception only
myConn.commit()
myConn.close()






















