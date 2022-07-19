#Python Sets
#unordered collection, some memory can be saved 
#no index, so we can't access them directly
#create using set() or {}

"""
#method 1
months = {"January", "February", "March", "April"}
print(months) #{'January', 'February', 'April', 'March'}
print(type(months)) #<class 'set'>

#method2
mon = set(["jan","feb","mar"])
print(mon) #{'feb', 'jan', 'mar'}

#declare an empty set
day = set()
#add values one by one only
day.add("monday")
day.add("tuesday")
day.add("wednesday")
print(day) #{'monday', 'wednesday', 'tuesday'}
"""

#day.add(["thursday", "friday"])
#print(day) #TypeError: unhashable type: 'list'
"""
#to add multiple items
day.update(["thursday", "friday"]) 
print(day)
#{'friday', 'monday', 'tuesday', 'thursday', 'wednesday'}


print("the set selements are:")
for i in months:
    print(i)
    #(the set selements are:
    # January
    # February
    # April
    # March)


#remove items
#discard() : remove item and donot display error if not exists
day.discard("thursday")
print(day) #{'tuesday', 'wednesday', 'friday', 'monday'}

#remove() : remove item and will display error if not exists
#day.remove("thursday")
#print(day) #KeyError: 'thursday'

#loop through 
for days in day:
    print(days)
    #(friday
    # monday
    # wednesday
    # tuesday)

#clear the elements in the set
day.clear()
print(day) #set() : empty set is displayed

"""
#SET operations
#union() :  exclude duplicates but combine both sets
#calculated using pipe(|) operator or union() function
#if two pipes (||) caleed as pipeline
m1 = {"Jan","Feb","Mar"}
m2 = set(["Mar","Apr","May"])

m3 = m1 | m2
print(m3) #{'Feb', 'Apr', 'Jan', 'May', 'Mar'}

for m in m3:
    print(m)

#intersection() 
#using & operator or the intersection() function
m4 = m1 & m2
print(m4) #{'Mar'}

m5 = m1.intersection(m2)
print(m5) #{'Mar'}

#intersect_update()
#will remove values that are not in other sets
a = {"tom", "jerry", "mickey"}
b = {"jerry", "tom", "donald"}
c = {"winne", "mickey", "tom"}
a.intersection_update(b,c)
print(a) #{'tom'}

#difference()
#using - operator or difference() method
m6 = m1 - m2
print(m6) #{'Jan', 'Feb'}
m7 = m2 - m1
print(m7) #{'May', 'Apr'}

#symmetric diffrence: remove elements in both sets 
#calculated by ^ operator or symmetric_difference() method
m8 = m1 ^ m2
print(m8) #{'Feb', 'Jan', 'May', 'Apr'}

#calculated by ^ operator or symmetric_difference() method
m9 = m1.symmetric_difference(m2)
print(m9)

#symmetric_difference_update()