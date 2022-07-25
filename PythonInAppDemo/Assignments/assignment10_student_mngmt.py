# 2. Student report card management system
# ---------------------------------------
# 
# This project requires managing student records. A student record contains a roll number,
# name and marks obtained in maths, physics, chemistry, english and prgraming. The system
# should be able to do the following
#   1. create a student record
#   2. delete a student record based on the roll number
#   3. modify the marks in a student record given in roll number
#   4. display all student records
#   5. display a students record based on the roll number




class Student:
	# Constructor
	def __init__(self, Name, Rollno, MatMark, PhyMark, ChemMark, EngMark, PrgrmMark):
		self.Name = Name
		self.Rollno = Rollno
		self.MatMark = MatMark
		self.PhyMark = PhyMark
		self.ChemMark = ChemMark
		self.EngMark = EngMark
		self.PrgrmMark = PrgrmMark		
	# Function to create and append new student
	def accept(self, Name, Rollno, MatMark, PhyMark, ChemMark, EngMark, PrgrmMark ):
		# use ' int(input()) ' method to take input from user
		obj = Student(Name, Rollno, MatMark, PhyMark, ChemMark, EngMark, PrgrmMark )
		ls.append(obj)

	# Function to display student details	
	def display(self, obj):
		print("Name :{}".format(obj.Name))
		print("RollNo : ", obj.Rollno)
		print("MatMark : ", obj.MatMark)
		print("PhyMark : ", obj.PhyMark)
		print("ChemMark : ", obj.ChemMark)
		print("EngMark : ", obj.EngMark)
		print("PrgrmMark : ", obj.PrgrmMark)
		print("\n")	
		
	# Search Function	
	def search(self, rn):
		for i in range(ls.__len__()):
			if(ls[i].rollno == rn):
				return i	

	# Delete Function								
	def delete(self, rn):
		i = obj.search(rn)
		del ls[i]

	# Update Function
	def update(self, rn, No):
		i = obj.search(rn)
		roll = No
		ls[i].rollno = roll
obj = Student(a, b, c, d, e, f, g)			
while(1):
	print("\nOperations used.. ")
	print("\n1.Create Student details\n2.Display Student Details\n""3.Search Details of a Student\n4.Delete Details of Student""\n5.Update Student Details\n6.Exit")
	ch = int(input("Enter choice:"))
	# an object of Student class

	# Create a list to add Students
	ls =[]
	if(ch == 1):
		obj.accept(obj.Name, obj.Rollno, obj.MatMark, obj.PhyMark, obj.ChemMark, obj.EngMark, obj.PrgrmMark)
		a = (input("Enter name: "))
		b = int(input("Enter the roll number: "))
		c = int(input("Enter the maths mark: "))
		d = int(input("Enter the physics mark: "))
		e = int(input("Enter the chemistry mark: "))
		f = int(input("Enter the english mark: "))
		g = int(input("Enter the programing mark: "))

	elif(ch == 2):
		print("\n")
		print("\nList of Students\n")
		for i in range(ls.__len__()):	
			obj.display(ls[i])
				
	elif(ch == 3):
		print("\n Student Found, ")
		s = obj.search(2)
		obj.display(ls[s])
				
	elif(ch == 4):
		obj.delete(2)
		print(ls.__len__())
		print("List after deletion")
		for i in range(ls.__len__()):	
			obj.display(ls[i])
				
	elif(ch == 5):
		obj.update(3, 2)
		print(ls.__len__())
		print("List after updation")
		for i in range(ls.__len__()):	
			obj.display(ls[i])
				
	else:
		print("Invalid Input")
			
