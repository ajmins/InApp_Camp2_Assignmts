#(ENCAPSULATION
# wrapping data methods within it)
#defining base class
class Rocket:
    #defining the constructor
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance
        self.__myPrivateVar = "test"
    #defining a member function
    def launch(self):
        return "%s has reached %s"%(self.name, self.distance)
#creating a sub class
class MarsRover(Rocket): #inherting from the base class
    def __init__(self, name, distance, maker, vehicleCode):
        Rocket.__init__(self, name, distance)
        self.maker = maker
        #define a private variable using __
        self.__vehicleCode = vehicleCode
    def getMaker(self):
        return "%s has launched by  %s"%(self.name, self.maker)
    def getVehicleCode(self):
        return self.__vehicleCode
    def getPrivate(self):
        return self.__myPrivate
    


#creating object
x = Rocket("Appollo II","till stratosphere")
y = MarsRover("Mars Lander","till Mars", "ISRO", "1234335")


#calling functions
print(x.launch())
print(y.launch())
print(y.getMaker())
#proper way of accessing a member private
print(y.getVehicleCode())
#due to encapsulation we cannot access a private variable directly
#print(y.__vehicleCode)

#access the private directly from the class using object
print(y._Rocket__myPrivateVar)