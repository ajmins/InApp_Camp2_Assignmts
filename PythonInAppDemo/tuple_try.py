#Tuples in Python

months = ("Jan","Feb","Mar")
print(months[0]) #Jan
print(months[-1]) #Mar
#months[0] = "test" 
# #TypeError: 'tuple' object does not support item assignment
print(len(months)) #3
print("Jan" in months) #True
print("Jan" not in months) #False

#del months
#print(months) 
# #NameError: name 'months' is not defined. Did you mean: 'month'?


print(months + months) #('Jan', 'Feb', 'Mar', 'Jan', 'Feb', 'Mar')
print(months * 3) #('Jan', 'Feb', 'Mar', 'Jan', 'Feb', 'Mar', 'Jan', 'Feb', 'Mar')
