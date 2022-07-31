class MemberList:
    year = 2020
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place

    def addAge(self):
        self.age = self.age + 1

    def relocate(self,place):
        self.place = place

    def display(self):
        print("Year: ",str(MemberList.year))
        print("Name :",self.name)
        print("Age :",str(self.age))
        print("Place :",self.place)

    @classmethod
    def addYear(cls):
        cls.year = cls.year + 1
        
    @staticmethod
    def displayWelcome():
        print("Welcome")    
        
MemberList.displayWelcome()

x = MemberList("Ajmi",22,"TVM")
y = MemberList("Anu",23,"EKM")

x.display()
y.display()

#after one yr, age increases
print("---------------------------")
#MemberList.year = MemberList.year + 1
MemberList.addYear()
x.addAge()
y.addAge()
x.relocate("USA")
y.relocate("UAE")
x.display()
y.display()

#after another yr, age increases
print("---------------------------")
#MemberList.year = MemberList.year + 1
MemberList.addYear()
x.addAge()
y.addAge()
x.relocate("ENG")
y.relocate("China")
x.display()
y.display()