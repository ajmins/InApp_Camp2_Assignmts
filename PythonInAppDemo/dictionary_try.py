#dictionary in Python
#declaration 
#method 1
myStud = {"Abhi" : 30, "Sibi" : 34, "subi" : "Not available"}
print(myStud) #{'Abhi': 30, 'Sibi': 34, 'subi': 'Not available'}

#method 2
mystud2 = dict(Abhi = 28, Sibi = 30, subi = " Not avaialable")
print(mystud2) 

#method 3
mystud3 = dict({"Abhi" : 30, "Sibi" : 34, "subi" : "Not available"})
print(mystud3) 

print(mystud3["Sibi"])
print(myStud)

#dictionary methods
#get()
print(myStud.get("Abhi")) #30
#items()
print(myStud.items()) #dict_items([('Abhi', 30), ('Sibi', 34), ('subi', 'Not available')])
#keys()
print(myStud.keys()) #dict_keys(['Abhi', 'Sibi', 'subi'])
#values()
print(myStud.values()) #dict_values([30, 34, 'Not available'])
#update()
day1 = {1: 'monday', 2:'tuesday'}
day2 = {1:'wednesday', 2:'thursday'}
day1.update(day2)
print(day1) #{1: 'wednesday', 2: 'thursday'}
#len()
print(len(day1))
#in operator
print("abhi" in myStud) #False
print(30 in myStud.values()) #True

#clear() : to delete al the items and return an empty set
day1.clear()
print(day1) #{}

#del : delete the entire dictionary
del day2
print(day2) #NameError: name 'day2' is not defined. Did you mean: 'day1'?