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
#calling functions
print(x.launch())
print(y.launch())
print(y.getMaker())