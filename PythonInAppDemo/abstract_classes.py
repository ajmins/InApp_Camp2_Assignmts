#(Python abstract Classes
# 
# EG:
# consider a zoo with 500 animal types, we need to write feeding fun)
class Lion:
    def giveFoodL(self):
        print("feeding Lion with raw meat!")
class Panda:
    def giveFoodP(self):
        print("feeding Panda with raw bamboo!")
class Snake:
    def giveFoodS(self):
        print("feeding Snake with raw mice!")
#etc classes for 500 animals

#creating object, plan to feed
simba = Lion()
kungFuPanda = Panda()
kingcobra = Snake()

#calling the fun tofeed 
simba.giveFoodL()
kungFuPanda.giveFoodP()
kingcobra.giveFoodS()
#it is very tedious to write and call these 500 animals one by one

#so for this we need to impose some restrictions and so that we can loop 
# through the functions for these animals
#for this we r using abstract classes.
#we can use same feed() fun fo all the classes. also we can create an abstract class Animal , 
# and every class that inherits from animal must implement abstract methods from animal called feed()
#use module ABC module and decorator @abstractorclass

from abc import ABC, abstractmethod

from time import time #inherit from ABC(abstract base class)

#declaring the Abtract base class inheriting from ABC
class Animal(ABC): 
    @abstractmethod #decorator to define an abstract method
    def feed(self):
        pass #pass is a placeholder for future code

#(if a class inherits from aBC, it must implement all it's abstract methods
# the method's name must be match)

#class and regular fun inheriting abstract class
class Lion(Animal):
    def feed(self):
        print("feeding Lion with raw meat!")
class Panda(Animal):
    def feed(self):
        print("feeding Panda with raw bamboo!")
class Snake(Animal):
    def feed(self):
        print("feeding Snake with raw mice!")
    def feedSnake(self):
        print("we can have another function but abstract method(feed()) is mandatory")

#creating object, plan to feed
simba = Lion()
kungFuPanda = Panda()
kingcobra = Snake()

#calling the fun tofeed 
simba.feed()
kungFuPanda.feed()
kingcobra.feed()

#we can implement this in a  for loop instead of repeating like above
#can have a list of classes
zoo = [Lion(),Snake(), Panda() ]
print("inside loop")
for animals in zoo:
    animals.feed() #now it's easy

"""
inside loop
feeding Lion with raw meat!
feeding Snake with raw mice!
feeding Panda with raw bamboo!
"""

#(Abstract method with parameters
# when an abstract method has parameters , the subclass implements the method it must contain 
# all the parameters.
# have "do" function and an "action" parameter)

class AnimalClass(ABC):
    @abstractmethod
    def do(self, action):
        pass

class LionClass(AnimalClass):
    def do(self, action, time): #mandatory to implement and time is additional parameter
        print(f"{action} a Lion! At {time}")
        #to have self.action and self.time, we need to have properties decorator getter and setter
    def feed(self):
        print("feeding Lion with raw meat!")
class PandaClass(AnimalClass):
    def feed(self):
        print("feeding Panda with raw bamboo!")
    def do(self, action, time): #mandatory to implement and time is additional parameter
        print(f"{action} a Panda! At {time}")
        #to have self.action and self.time, we need to have properties decorator getter and setter
class SnakeClass(AnimalClass):
    def feed(self):
        print("feeding Snake with raw mice!")
    def do(self, action, time): #mandatory to implement and time is additional parameter
        print(f"{action} a Snake! At {time}")

zooAnim = [LionClass(),SnakeClass(), PandaClass() ]
print("inside 2nd loop")
for animals in zooAnim:
    animals.feed()
    animals.do(action="feed", time="10:00AM") 

"""
inside 2nd loop
feeding Lion with raw meat!
feed a Lion! At 10:00AM
feeding Snake with raw mice!
feed a Snake! At 10:00AM
feeding Panda with raw bamboo!
feed a Panda! At 10:00AM
"""

#(Abstract properties
# create abstract propertie and force our subclass to implement those properties
# done by @property decorator along with a@abstractmethod
# animals have differet diet, define a diet method
# make foodEaten property and it's getter and setter)
print("-------------------################-----------------")
class AnimalClass1(ABC):
    @property
    @abstractmethod
    def diet(self): #define diet property
        pass
    
    @property
    def foodEaten(self):
        #define food eaten property
        #food eaten property's getter
        return self.__food

    #having setter for foodEaten
    #to save something to food use this
    @foodEaten.setter
    def foodEaten(self, food):
        if food in self.diet:
            self.__food = food
        else:
            raise ValueError(f"This animal doesn't eat this {food}")
    
    @abstractmethod
    def feed1(self, time):
        pass
class LionClass1(AnimalClass1):
    @property
    def diet(self):
        return["antelope","cheetah","buffalo"]
    def do(self, action, time): 
        print(f"{action} a Lion! At {time}")
    def feed1(self):
        print(f"feeding Lion with {self.foodEaten}!")
class PandaClass1(AnimalClass1):
    @property
    def diet(self):
        return["bamboo","leaves"]
    def feed1(self):
        print(f"feeding Panda with {self.foodEaten}!")
    def do(self, action, time):
        print(f"{action} a Panda! At {time}")

class SnakeClass1(AnimalClass1):
    @property
    def diet(self):
        return["mice","rabbit"]
    def feed1(self):
        print(f"feeding Snake with {self.foodEaten}!")
    def do(self, action, time): #mandatory to implement and time is additional parameter
        print(f"{action} a Snake! At {time}")

#calling the fun tofeed 
#we cannot loop it
simba1 = LionClass1()
simba1.foodEaten = "buffalo"
simba1.feed1()
kungFuPanda1 = PandaClass1()
kungFuPanda1.foodEaten = "bamboo"
kungFuPanda1.feed1()
kingcobra1 = SnakeClass1()
kingcobra1.foodEaten = "rabbit"
kingcobra1.feed1()