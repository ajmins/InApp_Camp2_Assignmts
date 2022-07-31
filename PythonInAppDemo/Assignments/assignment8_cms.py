#(to build a simple clinic management system using python which can perform following operations inside the class CMS
# admit 
# listPatients
# search
# delete
# update
# create inherited class 'OP' and 'NonOP' should have the additional Admit function and 'NonOp' a function to generate an OP Ticket with incrementing no for every patient)

#patient class
from sys import flags


class Patient:
    def __init__(self, patientID, name, gender, age, dob, bloodGroup):
        self.patientID = patientID
        self.name = name
        self.gender = gender
        self.age = age
        self.dob = dob
        self.bloodGroup = bloodGroup
        
    def detailsOfPatients(self):
        print(f""" 
              Patient ID :- {self.patientID}
              Name :- {self.name}
              Age :- {self.age}
              Date of Birth :- {self.dob}
              Blood Group :- {self.bloodGroup}
              """)
    def updateDetailsOfPatients(self, name, gender, age, dob, bloodGroup, patientID):
        self.patientID = patientID
        self.name = name
        self.gender = gender
        self.age = age
        self.dob = dob
        self.bloodGroup = bloodGroup
        
#OP class inherited from patient class

class NonOP(Patient):
    def __init__(self, name, gender, age, dob, bloodGroup, patientID, causeOfAdmit, admitDays):
        super().__init__(name, gender, age, dob, bloodGroup, patientID)
        self.causeOfAdmit = causeOfAdmit
        self.admitDays = admitDays
        
    def detailsOfINPatients(self):
        self.detailsOfPatients()
        print(f"""
              Cause of Admit :- {self.causeOfAdmit}
              Admitted Days :- {self.admitDays}
              """)

#main class
class CMS:
    listPatients = []
    pID = 1
    patientIN = []
    ticketOP = 1
    
    def registerPatients(self):
        name = input("Please enter patient's name: ")
        gender = input("Enter your gender (M/F/O): ")
        age = input("Enter your age: ")
        dob = input("Enter your date of birth: ")
        bloodGroup = input("Enter your blood group: ")
        #creating an object for Patient class
        patient = Patient(self.pID, name, gender, age, dob, bloodGroup)
        self.listPatients.append(patient)
        self.pID += 1
        print("Successfully Added!!")
    
    def showPatientDetails(self):
        print("Patient Details\n")
        for patient in self.listPatients:
            patient.detailsOfPatients()
    
    def showAdmittedPatients(self):
        print("Patient Details\n")
        for patient in self.patientIN:
            patient.detailsOfINPatients()
    
    def searchPatients(self):
        flag = False
        pid = int(input("Enter a petient ID to search: "))
        for patient in self.listPatients:
            if patient.patientID == pid:
                print("Details of patient \n")
                flag = True
        if flag == False:
            print("Patient ID not found.")
    
    def admitPatients(self):
        flag = False
        pid = int(input("Enter the registered petient ID to admit: "))  
        for patient in self.listPatients:
            if patient.patientID == pid:
                print("Details of patient \n")  
                causeOfAdmit = input("Enter the cause for the admission: ")
                admitDays = int(input("Enter the number of days to be admitted: "))
                inpatient = NonOP(patient.name, patient.gender, patient.age, patient.dob, patient.bloodGroup, patient.patientID, causeOfAdmit, admitDays)
                self.patientIN.append(inpatient)
                flag = True
        if flag == False:
            print("Patient ID not found.")

    def deletePatients(self):
        flag = False
        pid = int(input("Enter patient ID to be deleted: "))
        for patient in self.listPatients:
            if patient.patientId == pid:
                self.listPatients.remove(patient)
                flag = True
        if flag == False:
            print("Patient details deleted!")

    def OPTicketGeneration(self):
        print(f"OP ticket: {self.ticketOP}")
        self.ticketOP += 1

    def PatientDetailsUpdate(self):
        flag = False
        pid = int(input("Enter patient ID to be updated: "))
        for patient in self.listPatients:
            if patient.patientId == pid:
                name = input("\nPlease enter the new name: ")
                gender = input("Enter new Gender(M/F/O): ")
                age = int(input("Enter new age: "))
                dob = input("Enter new date of birth (dd-mm-yy): ")
                bloodGroup = input("Enter new Blood group: ")
                patient.updateDetailsOfPatients(name, gender, age, dob, bloodGroup)
                flag = True
        if flag == False:
            print("Patient ID not found")

clinic = CMS()
while(True):
    ch = int(input(""" 
    Enter your choice
    1. Create OP Tickets
    2. Register Patients
    3. Admit Patients
    4. List All Patients
    5. List Admitted Patients
    6. Search Patients
    7. Delete Patients
    8. Exit               
    """))
    match(ch):
        case 1: clinic.OPTicketGeneration()
        case 2: clinic.registerPatients()
        case 3: clinic.admitPatients()      
        case 4: clinic.showPatientDetails()
        case 5: clinic.showAdmittedPatients()
        case 6: clinic.searchPatients()
        case 7: clinic.deletePatients()
        case 8: exit()
        case _: print("Invalid Option")  





