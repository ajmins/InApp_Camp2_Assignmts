#(Python is not so strict in OOP concepts. But has the concept.
# Class :user defined prototype for an object that defines a set of attributes that chracterize any object of the class
#       attributes are data memebers or variables and methods or functions
# Objects
# Inhertiance: transfering the chracteristics of a class to classes that are derived from it
#       instance : an individual object of a certain class
#       instantiation :process of creating an instance of class
#       method: special kind of function 
# Encapsulation
# Polymorphism
# )
#----------------------------------------#
#(Classes and objects
# Eg: Car class
#       Car Objects: (green, ford, mustang, gasoline)
#                    (red, toyota, pirus, electricity)
# 
# public class Car()
# {
#   private string color;
#   private string model;
#   private string makeType;
#   private string fuelType;
#   
#   public void start(){
#   ----
#   }
#   public void Stop(){
#   ----
#   }
# }
# )
#creating class
class Employee:
    'common base class for all employees'
    #defining a global variable or data member
    empCount = 0 #class variable (global) shared among the instances of this class and accessed using dot operator
    
    #fist method is __init__() :special method called class constructor or initialization method
    #that the python calls when create a new instance of this class
    #defining a constructor
    #that can accept teo values name and salary
    #save those values into self(self is an instance of the class)
    def __init__(self, name, salary): #self is the fst argument so that accessing objects using self
        #declare other class methods like normal functions with the exception that fst argument to each method is self
        self.name = name #can call across the class
        self.salary = salary #can call across the class
        #no need to declare name and salary in the class just we can use it in constructor is enough
        Employee.empCount += 1 #increment when a new object is created
    
    #define a simple member function
    def displayEmployeeCount(self): #we need to use self here then only we can access those variables idefined in the constructor
        print("Employee Count: ", Employee.empCount) #here global variable, so overwriting is there
    #define a simple member function
    def displayEmployeeDetails(self): 
        print("Name: ", self.name) #here no need of overwriting, in each call 
        print("Salary: ", self.salary)

#create an object of employee class
employee1 = Employee("Tom", 2000)
employee1.displayEmployeeCount() 
"""Employee Count:  1"""
employee2 = Employee("Jerry", 5000)
employee2.displayEmployeeCount()
"""Employee Count:  2"""

#call function using dot operator (object)
employee1.displayEmployeeCount()
employee2.displayEmployeeCount()
employee1.displayEmployeeDetails()
employee2.displayEmployeeDetails()
""" Employee Count:  2
    Employee Count:  2
    Name:  Tom
    Salary:  2000
    Name:  Jerry
    Salary:  5000 """

#we can access employeecount outside the class(ie directly from the class) but not recommended in OOP concept
print("Total number of Employee : ", Employee.empCount) #Total number of Employee :  2


#creating a dog class

"""class Dog():
    def __init__(self,name,age):
        
        #Initialize name and age attributes.
        self.name = name
        self.age = age
    
    def sit(self):
        print


    def rollOver(self):
"""







