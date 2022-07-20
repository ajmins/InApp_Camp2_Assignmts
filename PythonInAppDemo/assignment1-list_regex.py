#AJMI N S

import re

#LIST QUESTIONS

#Q1. Sort the list in ascending order and print the first element in the list
newlist = [618, 21, 23, 20, 921, 90]
newlist.sort()
element = newlist[0]
print("sorted list is {} and the first element in the sorted list is {}".format(newlist, element))

#Q2. Python program to find second largest number in a list

newlist1 = [618, 21, 23, 20, 978, 90]
newlist1.sort()
scnd_element = newlist1[1]
print("The second largest element in the list is {}".format(scnd_element))


#Q3. Python program to print odd numbers & even numbers seperately in a list of [1,2,3,4,5,6,7,8,9,10]
newList3 =  [1,2,3,4,5,6,7,8,9,10]
oddList = newList3[::2]
evenList = newList3[1:10:2]
print("The odd numbers list are: {} and the even number list are {}".format(oddList, evenList))


#Q4. Program for reversing a list
newlist4 = [618, 21, 23, 20, 921, 90]
newlist4.reverse()
print("The list in reverse oder : {}".format(newlist4))

#Q5. Program to print all odd numbers from 1-50
for i in range(1,50,2):
    print(i)
print("\n")
#Q6. Program to count even and odd numbers in a list
newlist5 =[618, 21, 23, 20, 921, 90]
oddC=0
evenC=0
for i in newlist5:
    #print(i)
    if (i % 2 == 0):
        oddC = oddC + 1
    else:
        evenC = evenC + 1
print("count of odd number is: {} and count of even number is {}".format(oddC, evenC))



#REGEX QUESTIONS
#Q1. Write a python program to remove zeros from an IP address("216.08.094.196")
txt1 = "216.08.094.196"
n1 = re.sub("0", " ", txt1)
print("IP address without zeroes is {} ".format(n1))


#Q2. Write a python program that matches a string that has an 'a' followed by anything, ending in 'b'
txt2 = "ananab"
n2 =  re.findall(".*a.*b$", txt2)
print(n2) #['ananab']


#Q3. Replace all occurrences of 6 with 'six' and 10 with 'ten' for the given string 'They ate 6 apples and 10 banana'.
txt3 = 'They ate 6 apples and 10 banana'
print(txt3.replace('6', 'six').replace('10', 'ten')) #They ate six apples and ten banana