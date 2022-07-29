#(Dunder methods
# magic method : special methods that start and end with the double underscore -> called as dunder methods
# these methods carryout a procedure known as operator overloading: providing extended meaning beyond the predefined meaning to an operator
# use operational overloading to add custom behaviours to our classes so we can use them with Python's operators and built in function)

#(dunder methods begin and end with two underscores, __xxx__
# __init__ eg for a dunder method (in place of constructor, init is used)
# this allow the class to be initialized with special attributes of the class.
# It gets automatically called in the background by python eve if we declare it or not
# we r overriding it and create a constructor to do things in a certain way
# we can use dir() function to see the number of magic methods inherited by a class)

#to view the available dunder methods in a object, dir() is used
#eg: int is an object and to view its dunder methods
from re import S


print(dir(int))
#output
"""
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', 
'__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', 
'__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', 
'__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', 
'__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', 
'__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', 
'__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', 
'__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', 
'__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 
'__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 
'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
"""
print(dir(str))

#(String representation
# when we create a new object in Python, we impictly create a related object since all classes inherit from Object Class.
# the methods defined in the Object are inherited by our newly created class and are used in various situations like when an object is printed
# )
class Car:
    pass

car = Car()
print(car) #<__main__.Car object at 0x000001A75660AD40>

#(the object, which is the parent of all classes in Python, has a dunder method 
# called __repr__()(dunder repper)
# when we call the print(), it makes a call to the __repr__() from our Car object which was 
# inherited from the parent class Object, and return a value back to the main prgrm)

#(Math dunder methdos)

"""
class RandomNumbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

set_a = RandomNumbers(2,4)
set_b = RandomNumbers(3,5)

print(set_a + set_b)
"""
#output
""" 
TypeError: unsupported operand type(s) for +: 'RandomNumbers' and 'RandomNumbers'
this means the regular operation of + is concatnation but is overridden
"""
#(To avoid this, overriding this and make the + to concatenate)

class RandomNumbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    #override the __add__ dunder method
    def __add__(self,other):
        #returning the sum of teo left digits and two right digits converted into  random number object
        return RandomNumbers(other.a + self.a , other.b + self.b )

    #to represent as string using dunder __repr__()
    #overriding the dunder fun of random numbers 
    def __repr__(self):
        return f"{self.__class__.__qualname__} ({self.a},{self.b})"

#create objects for our RandomNumbers class
rand_obj_a = RandomNumbers(3,4)
rand_obj_b = RandomNumbers(5,6)

#trying to add two random numbers objects
print(rand_obj_a + rand_obj_b)

#(Dunder methods for classes
# 
# init : to create an instance of the class
# str : to use instances of our class in a print statement
# setitem : when assigning values in a dictionary
# getitem : to get values
# delitem: to delete values from dict or list
# len : no of elements in list or dict but not class
# contains: dictionary only, return value is a boolean)

#demonstrating the class under dunder methods
#CREATING A CLASS WITH AN EMPTY LIST OF SOFTWARES NAMES AND AN EMPTY 
#dictionary of softwares name and version as key value pair
class softwares:
    names = []
    versions = {}

    #defining(overriding) the constructor
    #invoked when we create an object and give the names list
    #sw1 = Softwares(['ps','msword','mspaint'])
    def __init__(self, names): #getting sw names as a list
        if names: #if names is not empty
            self.names = names.copy() #create a copy of the list
            for name in names: #looping through list
                self.versions[name] = 1
                #initialize sw version to 1 for all softwares
        else:
            raise Exception("names cannot be empty")
    
    #overriding the str dunder for displaying the list of softwares
    #will be invoked when calling print(objname)
    #sw1 = Softwares(['ps','msword','mspaint'])
    #print(sw1)
    def __str__(self):
        #loop through the dictionary and print the list
        s = "The list of softwares and its versions are :\n"
        for key, value in self.versions.items():
            s += f"{key}: version : {value} \n"
        return s

    #overriding the __setitem__ dunder method
    #will invoked when for example, p['msword']=2
    def __setitem__(self, name, version):
        if name in self.versions:
            self.versions[name] = version
        else:
            raise Exception("Software name doesn't exist")

    #overriding the __getitem__ dunder method
    #will be invoked when
    #print(sw1['msword'])
    def __getitem__(self,name):
        if name in self.versions:
            return self.versions[name]
        else:
            raise Exception("Software name doesn't exist")

    #(overriding the __delitem__ dunder method
    #will be invoked when
    # del sw1['msword])
    def __delitem__(self,name):
        if name in self.versions:
            #delete that item from the dictioary versions
            del self.versions[name]
            #delete the item from the names list
            self.names.remove(name) 
        else:
            raise Exception("Software name doesn't exist")

    #(overriding __len__ dunder method
    # will be invokde when calling print (len(sw1))
    # )
    def __len__(self):
        return len(self.names)

    #(override __contains__ dunder method
    # will be invoked when calling 
    # if 'msword in sw1: if yes, wil return true, else false)
    def __contains__(self, name):
        if name in self.versions:
            return True
        else:
            False


#creating the Software calss object
sw1 = softwares(['ps','msword','mspaint'])   
#print the softaware calss object
print(sw1)
#trying to set a new version for ms word
sw1['msword'] = 2
print(sw1)

#trying to get a  version number for ms word
print(sw1['msword'])
#delete item from dictioary
del sw1['msword']
print(sw1)
#print the length
print(len(sw1))

#checking if the given name in dictioanry
if 'msword' in sw1:
    print("Software Exists")
else:
    print("Software doesn't Exists")