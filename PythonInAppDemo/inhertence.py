#(create an object from another object
# class DErivedClassName (BaseClassName)
# )

#creating base classs
from decimal import ROUND_CEILING

#defining base class
class Rocket:
    #defining the constructor
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance
    #defining a member function
    def launch(self):
        return "%s has reached %s"%(self.name, self.distance)

#creating a sub class
class MarsRover(Rocket): #inherting from the base class
    def __init__(self, name, distance, maker):
        Rocket.__init__(self, name, distance)
        self.maker = maker
    def getMaker(self):
        return "%s has launched by  %s"%(self.name, self.maker)




#creating object
x = Rocket("Appollo II","till stratosphere")
y = MarsRover("Mars Lander","till Mars", "ISRO")
"""rName = list()
rDistance = list()
rMake = list()
rName[].append()
for i in range(0,2):
    rName[i] = input("Enter the rocket name: ")
    rDistance[i] = input("Enter the distance: ") 
    rMake[i] = input("Enter the maker name: ")

print(rName)
print(rDistance)
print(rMake)

x = Rocket(rName[0], rDistance[0])
y = MarsRover(rName[1], rDistance[1], rMake[1])   """
#calling functions
print(x.launch())
print(y.launch())
print(y.getMaker())