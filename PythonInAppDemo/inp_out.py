#INPUT and OUTPUT functions in python
#input()
"""

StdName = input("Please enter your name: ")
StdAge = int(input("Please enter your age: "))
#print() - output function
print(StdName)
print(type(StdName))
print(StdAge)
print(type(StdAge))

#print() in 3 ways...

print("Student name is",StdName,"and is",StdAge,"years old") #no need of adding space explicitly
#Student name is Ajmi and is 22 years old
print("Student name is %s and is %d years old" %(StdName, StdAge))
#Student name is Ajmi and is 22 years old
print("Student name is {} and is {} years old".format(StdName, StdAge))
#Student name is Ajmi and is 22 years old
"""

#triple Quotes and Escape characters
#print in multiple line
print(""" HEllo world
How are you
""")

print('''Hai
world''')

#print a new line
print('Hello \n World')

#adding extra backslash to tell the interpreter to ignore one
print('this is backslash \\')

#print('I am 5' and 5" ') cannot be used like this
print('I am 5\' and 5\" tall ') #I am 5' and 5" tall

#PYTHON COMPARSION OPERATORS
#(equality ==
# non equality !=
# greater than >
# less than <
# greater than or equal to >=
# less than or equal to <= )

#PYTHON LOGICAL OPERATORS
#(and
# or
# not)