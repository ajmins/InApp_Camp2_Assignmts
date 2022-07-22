#(decorating methods of a class
# method: fun in object's namespace, accessible as an attribute
# regular(instance) method: gets the instance(call it self) as the implicit first argument
# built in decorators to use with the methods of a class
#       -> class method: gets the class (call it as cls) as the implicit frst argument
#       -> static method: gets no implicit fst argument(like a regular fun)
#       -> property: used to create getters and setters for class attributes
#(the main purpose of using getters and setters in object-oriented programs is to ensure data encapsulation)
# ) 
#(@class method : to change the behaviour of the method based on which subclass is calling the method
# we have to reference tto the calling class in a class method
# but while using statis the bahvaiour to remain unchanged across subclasses)

#base class
class Hero:
    #define the decorator @classmethod 
    @classmethod
    def sayClassHello(cls): #will receive class ref as implicit fst argument
        if(cls.__name__ =="HeroSon"):
            print("Hi Prince, called from HeroSon")
        elif(cls.__name__ =="HeroDaughter"):
            print("Hi Princess, called from HeroDaughter")
    #define the decorator @staticmethod 
    @staticmethod
    def sayHello():
        print("hello...")


#(subclass)
class HeroSon(Hero):
    def saySonHello(self): #regular method so no cls, only have self as its fst implicit argument
        print("Hello Son, from sub class HeroSon")

class HeroDaughter(Hero):
    def sayDaughterHello(self):
        print("Hello Daughter, from sub class HeroDaughter")



#defining objects       
testSon = HeroSon() #instance of HeroSOn
testSon.sayClassHello() #instance of HeroSon calling sayClassHello of Hero class
testSon.sayHello()
testSon.saySonHello()
"""
Output
Hi Prince, called from HeroSon
hello...
Hello Son, from sub class HeroSon
"""

testDaughter = HeroDaughter()
testDaughter.sayClassHello()
testDaughter.sayHello()
testDaughter.sayDaughterHello()
"""
Output
Hi Princess, called from HeroDaughter
hello...
Hello Daughter, from sub class HeroDaughter
"""


#(@property
# 
# to define getters, setters, and deleters
# 
# getters: to access value of the attribute
# setters: to set the value of the attribute
# deleters: to delete the instance attribute)

#(consider house class (at the moment the class has only a price instance attribute defined)
# since the attribute is currently public, we can access and modifed the attribute directly in other parts of the program using dot notation)

class House:
    def __init__(self, price):
        self.price = price

#typical access and update will be like this:
house = House(50000.0) #creaye obj
print(house.price) #access the value
house.price = 1000000 #modifying the value

#(to keep the price as private
# or as protected(non-public) and validate the new value before acessing it 
# for that put an underscore)
class House1:
    def __init__(self, price1):
        self.__price1 = price1 #keeping price as private use __

#house1 = House1(50000.0) #creaye obj
#print(house1.__price1) #access the value
#house1.price1 = 1000000
#(Output
# AttributeError: 'House1' object has no attribute 'price1')

#(to access this use getter method from @property)
#getter -> for fetching attribuute value in the class
#it should be inside the class
class House2:
    def __init__(self, price2):
        self.__price2 = price2 #keeping price as private use __

    @property #getter
    def price2(self):
        return self.__price2
    #(setter
    # for saving the attribute value in a class)

    @price2.setter #setter
    def price2(self, newPrice):
        if(newPrice > 0 ):
            self.__price2 = newPrice
        else:
            print("Please enter a valid price")
    #(deleter -> will delete the attribute)
    @price2.deleter
    def price2(self):
        del self.__price2
#getter
house2 = House2(50000) #create obj
print(house2.price2) #access the object -> 50000
#setter
house2.price2 = 1000000 #change the object
print(house2.price2) #1000000
#deleter
del house2.price2
#print(house2.price2) #AttributeError: 'House2' object has no attribute '_House2__price2'










