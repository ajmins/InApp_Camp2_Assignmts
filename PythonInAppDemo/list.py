#Python Lists and List Access Options

studAge = [18, 21, 23, 20, 21]
#non-destructive nature
print(studAge) #[18, 21, 23, 20, 21]
print(studAge[0]) #18
print(studAge[-1]) #21
print(studAge[2:4]) #[23, 20]
print(studAge[1:5:2]) #[21, 20]
print(studAge[:4]) #[18, 21, 23, 20]
print(studAge[::-1]) #[21, 20, 23, 21, 18]

#destructive nature
#append to add a value to the en of the list
studAge.append(20)
studAge.append("hi")
print(studAge) #[18, 21, 23, 20, 21, 20, 'hi']

#delete a value from the specified location
del studAge[-1]
print(studAge) #[18, 21, 23, 20, 21, 20]

#extend(), in, insert(), len()

#extend(): combine two lists
mylist1 = ['Anu', 'binu', 'Rinu']
studAge.extend(mylist1)
print(studAge) #[18, 21, 23, 20, 21, 20, 'Anu', 'binu', 'Rinu']

#in : to check if a variable is in the list 
#operator
print('Anu' in mylist1) #True
print('Anu' not in mylist1) #False
print('Anus' in mylist1) #False

#len(): to get the number of items in the list
print(len(studAge)) #9

#destructive nature
#reverse() list : it can permanently change the actual list 
print(studAge) 
studAge.reverse()
print(studAge)  #['Rinu', 'binu', 'Anu', 20, 21, 20, 23, 21, 18]

#sort the list alphabetically or numerically
newstudAge = [18, 21, 23, 20, 21]
newstudAge.sort()
print(newstudAge) #[18, 20, 21, 21, 23]
newstudName= ['hina', 'leya', 'aju', 'diya']
newstudName.sort()
print(newstudName) #['aju', 'diya', 'hina', 'leya']

#list concatenation using + operator
print(newstudName + newstudName) #['aju', 'diya', 'hina', 'leya', 'aju', 'diya', 'hina', 'leya']

#list dupliaction/multiplication using * operator
print(newstudName*3) #['aju', 'diya', 'hina', 'leya', 'aju', 'diya', 'hina', 'leya', 'aju', 'diya', 'hina', 'leya']  



#Python list comprehension: offers a shorter syntax or else we need a for loop

#create a copy of list with some processing/ condition checks without implementing the list comprehension
words = ['hello', 'world', 'how', 'are', 'you']
newlist = [] #all the words contain 'o'

for word in words:
    if 'o' in word:
        newlist.append(word)

print(newlist)

#list comprehension
#syntax :- [expression for item in iterable if condition == True]; 
#condition- optional, iterable like list, tuple or set

newlst = [word for word in words if 'o' in word]
print(newlst)

#iterables in python list comprehension
# without condition
numList = [x for x in range(20)]
print(numList)

#with condition
numList2 = [x for x in range(20) if x < 15]
print(numList2)

#Expressions
words = ['hello', 'world', 'how', 'are', 'you']
newlst2 = [word.upper() for word in words if 'o' in word]
print(newlst2)

# hello for all the items in a list
newlst3 = ['hello' for word in words]
print(newlst3)

#get rid of an item 
newlst4 = [word if word != 'hello' else 'hi' for word in words]
print(newlst4)














