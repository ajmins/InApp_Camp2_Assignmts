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