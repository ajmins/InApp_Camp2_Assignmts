class baseClass:
    def set_name(self, name):
        self.name = name
        #print("Hello")

       
        
        

class subClass(baseClass):
    def welcome(self):
        print("welcome")
    def display_name(self):
        print("name",self.name)



y = subClass()
 
y.welcome()  
y.set_name("ajmi")   
y.display_name()