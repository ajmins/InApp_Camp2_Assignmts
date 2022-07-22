#PYTHON FUNCTIONS
#PRE-WRITTEN CODE TO PERFORM CERTAIN TASK
#(built in functions like print(), upper() etc
# keywords "def" and "return"
# def functionName(parameters):
#   code inside
#   return[expression])

#function to add two numbers
def findSum(a , b):
    sum = a + b
    return sum

print(findSum(2,3))
print("\n-----------------------------------------\n")
#function to check whether a number is prime or not
def checkIfPrime(numberTocheck):
    for x in range(2, numberTocheck):
        if(numberTocheck % x == 0):
            return False
    return True
       
numberTocheck = int(input("Enter the number to check whether it is prime or not: "))
resultP = checkIfPrime(numberTocheck) 
if(resultP == False):
    print("Number is not Prime")
elif(resultP == True):
    print("Number is Prime")

print("\n-----------------------------------------\n")
#Function return : execution ending and returns the value back to the caller
#(It can return all types of values and it return notheing when there is no expression
# There can be multiple return statements in afunction but only a single stattement is called for any specified invocation of the function)

def calculations(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return(add, sub, mul, div)

output = calculations(49,45)
print("Addition: ", output[0])
print("Subtraction: ", output[1])
print("Multi: ", output[2])
print("Division: ", output[3])

print("\n-----------------------------------------\n")
#python yield : generator are defined by using yield
#it convert a normal python function into a generator
#generator: function that returns an iterator than we can iterate upon
def calculationsYield(a, b):
    add = a + b
    yield add
    sub = a - b
    yield sub
    mul = a * b
    yield mul
    div = a / b
    yield div
#generator runs with for loop for getting all values
for value in calculationsYield(49,50):
    print(value)


#(python function as first class objects
# rights of a function in python
# is similar to the rights of a variable)

# [1] asssign fun to a variable
def myFun1():
    print("This is myfunc1")
#assign to a variable
myFuncVariable = myFun1
#call both
myFun1() #call fun directly
myFuncVariable() #call fun via the variable
"""
This is myfunc1
This is myfunc1
"""
# [2] pass fun to a another fun
def myFunc2(receivedFn):
    receivedFn()
myFunc2(myFun1) #passing function as argument
"""
This is myfunc1
"""
# [3] return a fun from another function
#return upper() fun of str
def returnToUpper():
    return str.upper
#store reference to returned fun in variable
toUpperFunRef = returnToUpper()
#use variable to call the function
print(toUpperFunRef("Hello world"))
"""
HELLO WORLD
"""
#[4] define a fun inside another function
#such fun called as inner fun or nested fun
def outer():
    print("outer function")

    def firstInner():
        print("First Inner Function")

    def secondInner():
        print("second Inner Function")

    firstInner()
    secondInner()
outer()
"""
outer function
First Inner Function
second Inner Function
"""

#[5] inner function can access variables in the enclosing function
# this pattern is known as a Closure
# child can inherit from parent

def myOuter(myGreeting):
    print("The outer function says ", myGreeting)

    def myFirstInnerFunc():
        print("My First Inner Func says", myGreeting)
    
    return myFirstInnerFunc
myOuterFuncVariable = myOuter("Peace to the world")
myOuterFuncVariable()

"""
The outer function says  Peace to the world
My First Inner Func says Peace to the world

"""

#(DECORATIONS ---> THESE RIGHTS CAN BE DONE USING TO DECORATIONS)
#fun that takes another fun as an argument and extends its behaviour without explicitly modifying it
#(usages like : logging debugging, authentication, meauring execution time etc
# for eg: we have a critical fun inside oour python program, we want authenticated users to access them.
# so we need to check whether a user is authenticated before proceeding with the rest of the code in the function
# either call a seperate authentication() fun inside our fun or we can use decorators)

#(func = decorator(func)
# a function which accepts another function, enhance it with a wrapper function and return the enhanced function back)

#define the decorator function, which accepts another function as the argument
def myDecorator(myFunc):
    def innerWrapper(): #wrapper function "decorates" the fun received
        print("Before the Function Call")
        myFunc()
        print("After the Function Call")

    return innerWrapper

#(now a function "myFnToPass" is passed into this decorator, so it now points to the wrapper function returned by the decorator)
def myFntoPass():
    print("Passing into decorator and printing")

myDecoratorDemo = myDecorator(myFntoPass)
myDecoratorDemo()

"""
Before the Function Call
Passing into decorator and printing
After the Function Call
"""

#(to use this decorator by providing syntactic sugar with the @ symbol
# Syntactic sugar is syntax within a programming language that is desogned to make things easier to read or to express)
@myDecorator
def myFnToPass():
    print("Passing into decorator and printing")

myFnToPass()
""" these two sentences are not needed for this
myDecoratorDemo = myDecorator(myFntoPass)
myDecoratorDemo()
and when we use the @ we can get only the enhanced version of the original function. 
"""
print("\n--------------------------------\n")
#(Keeping name of ecorated fucntion
# when we decorate a fun its identity is chnaged to the wrapper function
# we will try to print the docstring from the help function and the correct name from the __name__ attribute)
@myDecorator
def mynewFnToPass():
    """this is a doc string to describe myFnToPass fn""" #docstring
    print("Passing into decorator and printing")
mynewFnToPass()
print(mynewFnToPass.__name__)
help(mynewFnToPass)
#Typically when passsing a fn into a decorator, it will print the name and docstring of the wrapper function and not the mynewfntopass fun

#output
"""Before the Function Call
Passing into decorator and printing
After the Function Call
innerWrapper
Help on function innerWrapper in module __main__:

innerWrapper()
"""
print("\n--------------------------------\n")
#(to fix this we need to use another decorator called wraps on the arapper function.
# The wraps decorator is imported from the in-built functools modules.
# this will define the decorator function, which accepts another fun as the argument)

import functools
def myDecorator (myFunc):
    @functools.wraps(myFunc)
    def innerWrapper(): #wrapper function "decorates" the fun received
        print("Before the Function Call")
        myFunc()
        print("After the Function Call")

    return innerWrapper

@myDecorator
def mynewFnToPass2():
    """this is a doc string to describe myFnToPass fn""" #docstring
    print("Passing into decorator and printing")
mynewFnToPass2()
print(mynewFnToPass2.__name__)
help(mynewFnToPass2)

#output
"""Before the Function Call
Passing into decorator and printing
After the Function Call
mynewFnToPass2
Help on function mynewFnToPass in module __main__:

mynewFnToPass2()
    this is a doc string to describe myFnToPass fn
"""
#here shows the reusability of decorator

print("\n--------------------------------\n")
print("\n--------------------------------\n")
#to pass arguments into wrapper/decorator
#but will keep us bounded to using our decorator for functions with only one argument

import functools
def myDecorator (myFunc):
    @functools.wraps(myFunc)
    def innerWrapper(myString): #wrapper function "decorates" the fun received
        print("Before the Function Call")
        myFunc(myString)
        print("After the Function Call")

    return innerWrapper

@myDecorator
def mynewFnToPass3(myString):
    """this is a doc string to describe myFnToPass3 fn""" #docstring
    print("Passing into decorator and printing: " + myString)
mynewFnToPass3("just some test string")
print(mynewFnToPass3.__name__)
help(mynewFnToPass3)
#output
"""Before the Function Call
Passing into decorator and printing: just some test string
After the Function Call
mynewFnToPass3
Help on function mynewFnToPass3 in module __main__:

mynewFnToPass3(myString)
    this is a doc string to describe myFnToPass3 fn"""

#(here if we use mynewFnToPass3() without any arguments will throw an error becz we have defined the wrap function with a string value in it.)
print("\n------------###############--------------------\n")
print("\n-------------##################-------------------\n")

#(passing variable arguments into wrapper/decorator)
#(*args is used )

import functools
def myDecorator (myFunc):
    @functools.wraps(myFunc)
    def innerWrapper(*args): #here with this no need to change the decorator but we can call this decorator with multiple arguments
        print("Before the Function Call")
        myFunc(*args)
        print("After the Function Call")

    return innerWrapper

@myDecorator
def mynewFnToPass4(myString1, myString2):
    """this is a doc string to describe myFnToPass4 fn""" #docstring
    print("Passing into decorator and printing: " + myString1 + myString2)
mynewFnToPass4("just some test string" , " next string")
print(mynewFnToPass4.__name__)
help(mynewFnToPass4)
#output
"""
Before the Function Call
Passing into decorator and printing: just some test string next string
After the Function Call
mynewFnToPass4
Help on function mynewFnToPass4 in module __main__:

mynewFnToPass4(myString1, myString2)
    this is a doc string to describe myFnToPass4 fn
"""
print("\n------------###############--------------------\n")
print("\n-------------##################-------------------\n")
#(returning values from the decorators
# we cannot have the return becz wrapper fun here is not returning any value)
@myDecorator
def mynewFnToPass5(myString1, myString2):
    """this is a doc string to describe myFnToPass5 fn""" 
    returnString = ("new strings : " + myString1 + myString2)
    return returnString

returnString = mynewFnToPass5("test1", " test2")
print(returnString)

#output
"""Before the Function Call
After the Function Call
None"""

print("\n------------###############--------------------\n")
print("\n------------#(To return values from decorators)------------------\n")
#(To return values from decorators)

def myDecorator (myFunc):
    @functools.wraps(myFunc)
    def innerWrapper(*args): #here with this no need to change the decorator but we can call this decorator with multiple arguments
        print("Before the Function Call")
        #myFunc(*args) #if we give this function execution here, the fun will execute twice and its not necessary
            #value = myFunc(*args) #in this also the fun is executing once
        print("After the Function Call")
        return myFunc(*args)
            #return value #here when we assgn the fun to a variable and return that variable
    return innerWrapper

@myDecorator
def mynewFnToPass6(myString1, myString2):
    """this is a doc string to describe myFnToPass6 fn""" 
    returnString = ("new strings : " + myString1 + myString2)
    return returnString

returnString = mynewFnToPass6("test1", " test2")
print(returnString)

#output
"""
------------#(To return values from decorators)------------------

Before the Function Call
After the Function Call
new strings : test1 test2
"""
print("\n------------###############--------------------\n")
print("\n------------#(passing arguments directly into decorators)------------------\n")

#(passing arguments directly into decorators
# can pass arguments to a decorator by wrapping them inside of another decorator func)
def acceptDecorator(myString3): 
    def myDecorator (myFunc):
        @functools.wraps(myFunc)
        def innerWrapper(*args): #here with this no need to change the decorator but we can call this decorator with multiple arguments
            print("Before the Function Call")
            #myFunc(*args)
            print("After the Function Call")
            return myFunc(*args)
        return innerWrapper
    return myDecorator


#give new decorator name instead of the decorator
@acceptDecorator("testing string into new decorator")
def mynewFnToPass7(myString1, myString2):
    """this is a doc string to describe myFnToPass7 fn""" 
    returnString = ("new strings : " + myString1 + myString2)
    return returnString

returnString = mynewFnToPass7("test1 in ", " test2 in ")
print(returnString)





