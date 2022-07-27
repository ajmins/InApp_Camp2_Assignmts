#(Python Exception Handling
# error in Python: syntax error and Exceptions
# Syntax: worng syntax, leads to termination of program
# Exception: progrm is syntactically correct, but code result an error. 
# ->It Does not stop the execution of prgrm, but changes the normal flow of the prgrm)
#(exceptions handled ny python using try, except and finally statements
# try: statements have some error probably
# except: optional, this block handles when try block has any error
# finally: python will always execute this code)

from logging import raiseExceptions


try:
    div = 4 //0
    print(div)

#blocks will handle exception raised, can have multiple of them
except ZeroDivisionError:
    print("Attempting to divide by zero")

except:
    print("Some other exception occured")

#will always be executed no matter exception raised or not
finally:
    print("This is code of finally clause")
"""
Attempting to divide by zero
This is code of finally clause
"""
print("-------------------Eg 2---------------------------")
#example 2
try:
    div = 5 //0
    print(div)

#blocks will handle exception raised, can have multiple of them
except Exception as e:
    print("You are trying to divide by zero")
    print(f"{type(e).__name__}") #to get the exception error name alone
    print(e) #Print details of exception

#will always be executed no matter exception raised or not
finally:
    print("This is code of finally clause")
"""
Eg 2
You are trying to divide by zero
ZeroDivisionError
integer division or modulo by zero
This is code of finally clause
"""
print("--------------------------Eg 3--------------------------")
try:
    div = 8 //2
    print(div)

#blocks will handle exception raised, can have multiple of them
except Exception as e:
    print("You are trying to divide by zero")
    print(f"{type(e).__name__}") #to get the exception error name alone
    print(e) #Print details of exception
#else will work if the try statements are successful
else:
    print("Division completed and result is ", div)
#will always be executed no matter exception raised or not
finally:
    print("This is code of finally clause")
"""
4
Division completed and result is  4
This is code of finally clause
"""

print("--------------------------Eg 4-----------------------------")
#file handling
#we r trying to open an non existing file
#nested try except statements
try:
    f = open("nonexistingfile.txt")
    try:
        f.write("Hello world")
    except:
        print("some problem with writing to a file")
    finally:
        f.close()
except:
    print("The file cannot be opened")

"""
The file cannot be opened
"""
print("------------------------------Eg 5--------------------------")
try:
    f = open("sample.txt")
    try:
        f.write("Hello world")
    except:
        print("some problem with writing to a file")
    finally:
        f.close()
except:
    print("The file cannot be opened")

"""
some problem with writing to a file
"""

print("------------------------------Eg 6--------------------------")

#user can raise exception, if a condition occurs
#to throw or raise an excepotion,use "raise" keyword
"""
x = 0
if x == 0:
    raise Exception("Sorry,zero is not allowed") #this will raise exception and progrm may terminates


#print(" statement after exception")

#to handle it we have to put it inside the try block
y = 'hello world'
if not type(y) is int:
    raise TypeError("Only numbers are allowed")
"""
print("------------------------------Eg 7--------------------------")
#creating user defined exception classes 
#(need to be created from the built-in "exception class"
# inheriting a class containing constructor and disply method)

#class myError is extended from super class Exception
class myError(Exception):
    #constructor method
    def __init__(self, value):
        self.value = value
    #__str__ display dunder function
    def __str__(self):
        return(repr(self.value))

#(__repr__ is a built in functopn used to compute " offiicial" string representation of an object,
# __str__ is a built in function(magic function) that computes the "informal" string representations of an object)

#(using the class that created )
try:
    n = 0
    if n == 0:
        raise (myError("Number cannot be zero"))
except myError as error:
    print("New exception occured ", error)

print("Statement after exception")

#thr exception derived class being inherited by another class
class myError(Exception):
    #base class for exceptions
    pass

class divideByZero(myError):
    pass

try:
    n = 0
    if n == 0:
        raise divideByZero
except divideByZero:
    print("A New exception occured ")

print("Statement after exception class")






































