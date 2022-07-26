import pyodbc
#create a connection string
conString = 'Driver={SQL Server};Server=DESKTOP-CJEOG7N\SQLEXPRESS;Database=employee_db1;Trusted_Connection=yes;'

#create a connection with the connection string
myConn = pyodbc.connect(conString)

try:
    #get the cursor object
    myCursor = myConn.cursor()

    #using cursor, execute SQL commands
    #myCursor.execute("INSERT INTO EmployeeMaster VALUES ('E0001', 'Hulk', 'IT', 'TVM', 4000)")
    #TO Prevent SQL injection, not mandatory but recommended
    myCursor.execute("INSERT INTO EmployeeMaster VALUES(?,?,?,?,?)", ('E00785', 'Den', 'IT', 'TVM', 9000))

except Exception as e:
    print("Cannot create the table because : ")
    #print(e) #to get the entire details about the exception
    print(f"{type(e).__name__} was occured") #to get the the name of exception only


myConn.commit()
myConn.close()