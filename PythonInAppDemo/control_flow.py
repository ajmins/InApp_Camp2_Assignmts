#CONTROL FLOW STATEMENTS IN PYTHON
#(1. Conditional Statements : if, elif
# 2. Looping Statements : for, while, break, continue, try Except)

#IF statement
#uses indentaion to seperate blocks of code
#(if cond1: 
#   do A
# elif cond2:
#   do B
# elif cond3:
#   do C
# else:
#   do A)

from ast import match_case

"""

userInputNo = input("Enter either 1 or 2: ")
if(userInputNo == "1"):
    print("You entered 1")
    print("And you are the NO 1")
elif(userInputNo == "2"):
    print("You entered 2")
    print("Runner Up. Keep it up!")
else:
    print("You didn't enter 1 or 2")


#(Inline If statement
# do task A if condition is true else do task B)
B=12
A=12 if B==12 else 13 #12
#A=12 if B==10 else 13 #13
print(A)

print("B is ten" if B == 20 else "B is not 10") #B is not 10
print("B is ten" if B == 12 else "B is not 10") #B is ten


#(no SWITCH CASE STATEMENT
# FOR that we have to use some function method
# greater than 3.10 version we have Match-case statement)

#Match-case
#define a function
def http_status(status):
    match status:
        case 400:
            return "Bad request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Not Found"
        case _:
            return "Other error"
print(http_status(400))

"""
#Looping
#for loop : loop until the condition in the statement is no longer valid
#iterable: anything can be looped over like string, list or tuple
fruits = ['apple', 'orange', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
    #(apple
    # orange
    # banana
    # cherry)

#to display index also using enumerate method
#enumerate(): adds a counter to an iterable and returns it in a form of enumerating object
#enumerate(iterable, start=0)
for index, fruit in enumerate(fruits):
    print(index, fruit)
    #(0 apple
    # 1 orange
    # 2 banana
    # 3 cherry)
for index, fruit in enumerate(fruits, start = 2):
    print(index, fruit)
    #(2 apple
    # 3 orange
    # 4 banana
    # 5 cherry)

#range() function
for i in range(10):
    print(i) #from 0,1,2,...9
for i in range(4,10,2):
    print(i)

#while loop : repeatedly execute instruction inside loop while a certain condition remain valid
#(while condition is true:
# do A)

counter = 5
while counter >0:
    print("Counter = ", counter)
    counter = counter - 1
    #(Counter =  5
    # Counter =  4
    # Counter =  3
    # Counter =  2
    # Counter =  1)

#break & continue statements
#break
j = 0
for i in range(5):
    j = j + 2
    print('i = ', ', j = ', j)
    if j==6:
        break

#continue
j = 0
for i in range(5):
    j = j + 2
    print('i = ', i, ', j = ', j)
    if j==6:
        continue
    print('j value is ',j)
"""
j value is  2
i =  1 , j =  4
j value is  4
i =  2 , j =  6
i =  3 , j =  8
j value is  8
i =  4 , j =  10
j value is  10

"""
#try except statement: control how prgrm prcoceeds when an error occur

try:
    answer = 12/0
    print(answer)
except:
    print("An error occured") #An error occured