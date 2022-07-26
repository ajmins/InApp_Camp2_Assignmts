#(Python Exception Handling
# error in Python: syntax error and Exceptions
# Syntax: worng syntax, leads to termination of program
# Exception: progrm is syntactically correct, but code result an error. 
# ->It Does not stop the execution of prgrm, but changes the normal flow of the prgrm)
#(exceptions handled ny python using try, except and finally statements
# try: statements have some error probably
# except: optional, this block handles when try block has any error
# finally: python will always execute this code)

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





























































