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














