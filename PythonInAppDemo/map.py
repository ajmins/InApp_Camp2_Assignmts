#(25/07/2022
# Higher-order functions
# take functions as a parameter and return a function as the result
# Reduce(), map(), filter() 
# can do complex operations when paired with simple functions)

def greet(name):
    return "Hello, {}!".format(name)

def print_greet(f,n):
    print(f(n))

name = input("Enter your name please... ")
print_greet(greet, name)

#(the functions like map(), reduce(), filter() etc , all do the same thing, they each take a function and a list of elements. 
# and then return the result of applying the function to each element in the list )

#MAP() :accepts another function and a sequence of iterables as parameters.
#provides output after applying the function to each iterable in the sequence.
#syntax map(function, iterable)

def myMapFun(a):
    return a*a

x = map(myMapFun, (1,2,3,4)) #x is the map object
print(tuple(x)) #covert x to tuple or set and print
print(x)
#output
"""
(1, 4, 9, 16)
<map object at 0x000001D161D6BAC0>
"""
#(map fun with lambda
# fun with no name are called lambda function
# frequently used as unput to other functions
# integrating lambda fun into map() function)
y = map(lambda y:y*y, (1,2,3,4))
print(tuple(y))

#(filter() fun : to generate an output list of values that return true when the fun is called.
# will filter the result based on condition
# syntax filter(function, iterables))
def funC(x):
    if x>=35:
        return x
y = filter(funC, (0,1,2,3,4,5))
z = filter(funC, range(1,200))
print(list(y))#convert to tuple or set or list and print
print(list(z))
print(y)
#output
"""
[]
[35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199]
<filter object at 0x00000135BA65BA30>
"""

#(filter fun with lambda
# )
w = filter(lambda w:(w>=3),(1,2,3,4))
print(list(w)) #[3, 4]

#(reduce(): applies a provided fun(preferably a lambda fun) to iterables and returns a single value
# syntax reduce(function, iterables))
from functools import reduce
x = reduce(lambda a,b: a+b, [23,21,45,98])
print(x)
"""
187
how?(23+21 = 44; 44+45 = 89; 89+98 = 187)
"""



