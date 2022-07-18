message = "Hello World!"
print(message)

""" 
x = x + 2
w += 2
y = y - 2
z -= 2

""" 

a = 20
b = 25

print(a)
#del a, b
print (a)

int_eg = 10
float_eg = 100.05

print(int(float_eg))
print(float(int_eg))
print(str(int_eg))
print(str(float_eg))

h = 'I informed that, "Python is easy to learn" '
print(h)

name = 'aju' 
print(name.title())
print(name.upper())
print(name.lower())

f_name = 'aju'
l_name = 'aji'
my_name = f"{f_name} {l_name}"
print(my_name) #aju aji
print(f"Hello, {my_name.title()}!") #Hello, Aju Aji!

make = 'Dell'
dollarrate = 70.6
myText = ' the amount for %s is %d usd and exchange rate is %f.2f usd to 1 inr' %(make, 1299, dollarrate)
print(myText) # the amount for Dell is 1299 usd and exchange rate is 70.600000.2f usd to 1 inr

myText2 = 'the amount for {} is {} usd and exchange rate is {} usd to 1 inr'.format(make, 1299, dollarrate)
print(myText2)  #the amount for Dell is 1299 usd and exchange rate is 70.6 usd to 1 inr

myText3 = '{0} is easier than {1}'.format('Python', 'Java')
print(myText3) #Python is easier than Java
myText3 = '{1} is easier than {0}'.format('Python', 'Java')
print(myText3) #Java is easier than Python

#count()
print('Hello Good Mornuing'.count('d'))