#Python Lists and List Access Options

from xml.dom.pulldom import START_DOCUMENT


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





