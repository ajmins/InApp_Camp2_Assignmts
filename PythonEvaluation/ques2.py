"""
Q2. Create a Patient management system python console application that manages records of the patients in a hospital. You may use the MSSQL database

• Implement basic CRUD operations for this scenario using dictionary in python.
• There are four operations that are performed, namely, add patient record, update patient record, delete patient record and list with search for patient records.
• The fields are patientId(int), patientName, gender, age, bloodGroup (string) for every patient.
• Keep directory with patientId as key and rest as value array corresponding to each key.
• Prompt user for the operation. 1. Add, 2.Update, 3.Delete, 4.List and Search. Make sure to alert user if a non int or blank value for patientId and blank for other fields.
• All values should be received using user input only.


"""

import pyodbc
import functools

conString = 'Driver={SQL Server};Server=DESKTOP-CJEOG7N\SQLEXPRESS;Database=Camp2;Trusted_Connection=yes;'

#decorator for connecting db and python
def connectdb(myFunc):
    @functools.wraps(myFunc)
    def innerWrapper(*args):
        try:
            myConn = pyodbc.connect(conString)
            myCursor = myConn.cursor()
            result = myFunc(myCursor, *args)
            myConn.commit()
            myConn.close()
            return result
        except Exception as e:
            print("Not connected because of :\n")
            print(e)
            print(f"{type(e).__name__}")
    return innerWrapper


@connectdb
def addPatient(myCursor):
    patName,patGen,patAge,patBG = getDetails()
    myCursor.execute('INSERT INTO patient(patientName,gender,age,bloodGroup) VALUES (?,?,?,?);',(patName,patGen,patAge,patBG)) 
    print(f'Patient added successfully')
            
@connectdb
def updatePatient(myCursor):
    pid = int(input("Enter patient ID: "))
    patName,patGen,patAge,patBG = getDetails()
    myCursor.execute('UPDATE patient SET patientName=?,gender=?,age=?,bloodGroup=? WHERE patientId = ?',(patName,patGen,patAge,patBG, pid)) 
    print(f'Patient Updated successfully')

@connectdb
def deletePatient(myCursor: pyodbc.Cursor):
    pid = int(input("Enter patient ID: "))
    try:
        myCursor.execute('DELETE FROM patient WHERE patientId = ?;',(pid))
        print(myCursor.rowcount)
        print("Deleted Successfully")
    except Exception as e:
        print(e)
        print(f"{type(e).__name__}")

@connectdb
def listAllPatients(myCursor):
    myCursor.execute('SELECT * FROM patient')
    print("Patient Details")
    patientsDirectory = myCursor.fetchall()
    for patientId,patientName,gender,age,bloodGroup in patientsDirectory:
        print(f'''
        Patient Id: {patientId}
        Patient Name: {patientName}
        Gender: {gender}
        Age: {age}
        Blood Group: {bloodGroup}''')

@connectdb
def viewPatient(myCursor):
    pid = int(input("Enter patient ID: "))
    myCursor.execute('SELECT * FROM patient WHERE patientId = ?', (pid))
    print("Patient Details")
    patientList = myCursor.fetchall()
    for patientId,patientName,gender,age,bloodGroup in patientList:
        print(f'''
        Patient Id: {patientId}
        Patient Name: {patientName}
        Gender: {gender}
        Age: {age}
        Blood Group: {bloodGroup}''')

@connectdb
def searchPatients(myCursor):
    status = False
    pid = int(input("Enter patient ID: "))
    myCursor.execute('SELECT * FROM patient WHERE patientId = ?', (pid))
    print("Patient Details")
    status = True
    patientList = myCursor.fetchall()
    for patientId,patientName,gender,age,bloodGroup in patientList:
        if pid == patientId:
            status = True
            print(f'''
            Patient Id: {patientId}
            Patient Name: {patientName}
            Gender: {gender}
            Age: {age}
            Blood Group: {bloodGroup}''')
    if status == False:
        print(" Not Found")

def getDetails():
    patName = input("Enter patient's name:")
    patGen = input("Enter patient's gender:")
    patAge = int(input("Enter patient's age:"))
    patBG = input("Enter patient's blood group:")
    return patName, patGen, patAge, patBG


while(1):
    ch =int(input("""
    Patient Management System
    1. Add a Patient
    2. Update a Patient
    3. Delete a Patient
    4. List All Patients
    5. View a Patient Details
    6. Search a Patient
    7. Exit
    """))
    match(ch):
        case 1: addPatient()
        case 2: updatePatient()     
        case 3: deletePatient()
        case 4: listAllPatients()
        case 5: viewPatient()
        case 6: searchPatients()
        case 7:
            exit()
        case _:
            print('Invalid input')
