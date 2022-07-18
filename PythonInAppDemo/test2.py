#Exercise

#formatiing
name = "India"
text = "{} is my country. All {}ns are my brothers and sisters.".format(name, name)

print(text)
#India is my country. All Indians are my brothers and sisters.


#endswith()
num = text.count('India')
print(num) #2

myString = " superman"

print(myString.endswith('man')) #True
print(myString.endswith('man', 3)) #True
print(myString.endswith('man', 2, 6)) #False
print("postman".endswith(('man','ma'),2,6)) #True


#find() & index()

myString2 = "Hello Good Morning"
print(myString2.find('Go')) #6
print(myString2.find('Go', 4)) #6
print(myString2.find('Go',4, 15)) #6
print(myString2.find('kk')) #-1
#print(myString2.index('kk')) #ValueError: substring not found

#isalnum()

print('Hello123'.isalnum()) #True
print('H e l l o 1 2 3'.isalnum()) #False
print('Hello'.isalnum()) 

#isalpha()

#isdigit()

#islower()
#isupper()
#istitle()

#join() method used to join in a tuple with a seperator
Seperator = '*'
myTuple = ('h','e','l','l','o')
myNewString = Seperator.join(myTuple)
print(myNewString) #h*e*l*l*o
print(myNewString.lower())
print(myNewString.upper())

#replace()
print('Hello world'.replace('o', 'i')) #Helli wirld
myStr = 'Helo world'
print(myStr.replace('o', 'i', 2)) #Heli wirld
print('Hello world'.split(' ')) #['Hello', 'world']
print(myStr.split(' ')) #['Helo', 'world']

import re

txt = "bits of paper bits"
x = re.search("bi", txt)
print(x)