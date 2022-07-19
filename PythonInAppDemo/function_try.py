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