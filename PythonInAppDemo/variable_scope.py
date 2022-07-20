#(20th July 2022
# Functions- Variable Scope
# Local Variable: acceccsible within the function
# Global Variable: accessed anywhere)

#declaring a global variable
m1 = "I am Global Variable"

def myfunction():
    print("\nInside the function")
    print(m1) #printing global variable
    m2 = "I am local variable" #declaring local variable
    print(m2)

myfunction() #calling the function
print("\nOutside")

print(m1)
#print(m2) #NameError: name 'm2' is not defined. Did you mean: 'm1'?

#modifying global variable within the function
m3 = "I am Global Variable"
def myfunction2():
    print("\nInside the function")
    print(m3) #printing global variable
    m4 = "I am local variable" #declaring local variable
    print(m4)
   # m3 = "Modifing the global variable"

myfunction2() #calling the function
print("\nOutside")

#print(m3) #UnboundLocalError: local variable 'm3' referenced before assignment
#so give a global variable to m3 then m3 can be modified

m31 = "I am Global Variable"
def myfunction2():
    global m31 #enable modification of lglobal variable inside the function
    print("\nInside the function")
    print(m31) #printing global variable
    m41= "I am local variable" #declaring local variable
    print(m41)
    m31 = "Modified the global variable"

myfunction2() #calling the function
print("\nOutside")

print(m31) 