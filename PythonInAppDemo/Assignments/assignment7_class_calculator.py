#create class Calculator
#pass two numbers, call objects

class Calculator():
    #constructor
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    #defining functions
    def add(self):
        Result = self.num1 + self.num2
        print("Addition\nSum of {} and {} is {}".format(self.num1, self.num2,Result))
    def multiply(self):
        Result = self.num1 * self.num2
        print("Multiplication\nProduct of {} and {} is {}".format(self.num1, self.num2,Result))
    def divide(self):
        if(self.num2 == 0):
            print("divide by Zero Error")
            exit()
        Result = self.num1 / self.num2
        print("Division\nQuotient of {} and {} is {}".format(self.num1, self.num2,Result))

#creating object
a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
num = Calculator(a,b)

#calling functions
num.add()
num.multiply()
num.divide()