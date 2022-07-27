from abc import ABC, abstractmethod
from decimal import DivisionByZero

class calculate(ABC):
    @abstractmethod
    def calculation(self,num1,num2):
        pass
   
    @property
    def valid_num1(self):
        return self.__num1
    @property
    def valid_num2(self):
        return self.__num2  

    @valid_num1.setter
    def valid_num1(self,num1):
        if type(num1) == int or type(num1) == float:
            self.__num1=num1
           
    @valid_num2.setter
    def valid_num2(self,num2):
        if type(num2) == int or type(num2) == float:
            self.__num2=num2

class calcsum(calculate):
    def calculation(self):
        print(f"Sum of {self.valid_num1} and {self.valid_num2}:",self.valid_num1+self.valid_num2)
   
class calcdiff(calculate):
    def calculation(self):
        print(f"Difference is {self.valid_num1} and {self.valid_num2}:",self.valid_num1-self.valid_num2)

class calcprod(calculate):
    def calculation(self):
        print(f"Product is {self.valid_num1} and {self.valid_num2}:",self.valid_num1*self.valid_num2)

class calcquo(calculate):
    def calculation(self):
        print(f"Quotient is {self.valid_num1} and {self.valid_num2}:",self.valid_num1/self.valid_num2)
        #method overriding
        @calculate.valid_num2.setter
        def valid_num2(self,num2):
            if num2 == 0:
                raise DivisionByZero("Divide by zero error")   
            else:
                calculate.valid_num2.fset(self, num2)
                

add = calcsum()
diff = calcdiff()
pro = calcprod()
quo = calcquo()

num1=int(input("Enter the first no:"))
num2=int(input("Enter the second no:"))
add.valid_num1 =num1
add.valid_num2 =num2
add.calculation()
diff.valid_num1 =num1
diff.valid_num2 =num2
diff.calculation()
pro.valid_num1 =num1
pro.valid_num2 =num2
pro.calculation()
quo.valid_num1 =num1
quo.valid_num2 =num2
quo.calculation()