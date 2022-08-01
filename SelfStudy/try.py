
import re
from abc import ABC, abstractmethod

class AllProducts(ABC):
    def __init__(self, productName, categoryName, ProductCode, basicPrice, tax, discount, MRP):
        self.productName = productName
        self.categoryName = categoryName
        self.ProductCode = ProductCode
        self.basicPrice = basicPrice
        self.tax = tax
        self.discount = discount
        self.MRP = MRP

    @property
    def properName(self):
        return self.__productName

    @properName.setter
    def properName(self,productName):
        if (productName.isalnum()) == True:
            if len(productName)>=3:
                self.__productName = productName
                print(f"Proper Product Name:{productName}")

    def properCategory(self):
        maxCategory = int(input("Enter the maximum capacity of category: "))
        categoryList = {'Hygiene':0,'Health':0,'Staples':0,'Sports':0,'Fashion':0}

    @classmethod
    def get_user_input(self):
        while(True):
            try:
                p1 = input("Enter Product Name: ")
                p2 = input("Enter Product Category: ")
                p4 = int(input("Enter Product Basic Price: "))
                p5 = int(input("Enter Tax of Product in %: "))
                p6 = int(input("Enter Discount of Product in %: "))
                p7 = int(input("Enter MRP of Product: "))
                #p3 = productCode()
                return self(p1,p2,p4,p5,p6,p7)
            except:
                print('Invalid input!')
                break
        productCode()

           
class productCode(AllProducts):
    
    def show(self):
        p1,p2,p4,p5,p6,p7 = AllProducts.get_user_input(self)
    
    @property
    def properCode(self):
        return self.__productCode
    @properCode.setter
    def properCode(self):        
        productCode.show()
        prodCode = []
        lst=list(self.get_user_input.p2)
        for i in lst[0:3]:
            prodCode = lst.append(i)
            self.__productCode = prodCode

obj1 = AllProducts.get_user_input()