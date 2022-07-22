#(to build a simple clinic management system using python which can perform following operations inside the class CMS
# admit 
# listPatients
# search
# delete
# update
# create inherited class 'OP' and 'NonOP' should have the additional Admit function and 'NonOp' a function to generate an OP Ticket with incrementing no for every patient)

#base class
class CMS:
    def __init__(self, opTicket):
        self.opTicket = opTicket
    def admit(self, name, gender, age, dob, bloodGroup, patientID):
        patientID = patientID + 1
        self.name = name
        self.gender = gender
        self.age = age
        self.dob = dob
        self.bloodGroup = bloodGroup
        self.patientID = patientID




















