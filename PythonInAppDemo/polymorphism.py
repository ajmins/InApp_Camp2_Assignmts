#(POLYMORPHIDM
# ability of the function with the same name to carry differnt functionality altogether
# creates a structure that can use many forms of objects.)

class Rabbit():
    def age(self):
        print("this funct")












obj1 = Rabbit()


#this example has no inheritance.
#(even then, we can pack these two differnt objects into a tuple and iterate through using a common animal variable
# it's possible through polymorphism)

#example of method overriding
from math import pi

class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        pass
    def fact(self):
        return "I am two-dimentional shape"
    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length
    def area(self):
        return self.length**2
    def fact(self):
        return "Sqauares have each angle 90 degree "
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius 
    def area(self):
        return pi*self.radius**2

a = Square(4)
b = Circle(7)

print(b)
print(b.fact()) #circle do not have any fact method but will go to the parent class and inherited from it
print(a.fact()) #here aquare has its own fact method
print(b.area())
#(__str__ method in python represnts the class objects as a string
# the method __str__() will not be overridden in the child classess but are used directly from the parent classs