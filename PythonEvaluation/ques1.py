"""
Q1. Maintain a list of products in categories for the dealer ABC Enterprises which should be managed in the memory without DB. A product has name, category name (‘Hygiene’, ‘Health’, ‘Staples’, ‘Sports’, ‘Fashion’), product code, basic price, tax%, discount, MRP. Work out all calculations as needed based on information given below. 

Name of Product in a category should be only characters, are not case sensitive and at least three characters long. Categories have limited capacity and the user should be alerted if the capacity is exceeded. The capacity of the category is same for all categories and is taken from user. 

Product code is auto generated based on product details
Product code is eight character long and should be unique
First two characters are the first two characters of the category, Next two characters are first two characters of the product name. Fifth character should be a number which depends on whether the first 4 characters are already existing. If yes, it should represent the n-1th occurrence.

 Eg: If CAPR1 is the first five chars of the existing code, then the new code with category code CA and Product code PR should be CAPR2. If CAPR is the first occurrence then it should be zero and the first five characters and the code will be CAPR0

Last three characters should be a random number generated

Price entered can be Price before tax or MRP. If user chooses to Price before tax, assume tax criteria as 'tax extra' and add tax amount to the basic price to arrive on the MRP. If price entered is MRP, then assume tax criteria as 'includes tax' and reduce the calculated tax amount from the MRP to arrive on the basic price. All price elements should be displayed rounded to the second decimal point. 

Discount can be set as percentage or amount and user should be able to choose how to set discount. Whichever way, it is set, the % and amount of discount should be displayed. Discounts are to be applied on the MRP. 

List out the final product list with Product name, tax%, tax amount, MRP, discount %, discount amount and selling price. 

Find the solution to this problem and implement it as a separate functionality in the same program: The MRP of a product of manufacturer XYZ Corp was 742 inclusive of 18% GST. The manufacturer XYZ Corp increased the MRP by 8%. After some months the MRP was again increased by 10%. The new MRP is rounded to the nearest whole number. The product is given to the dealer ABC Enterprises by the manufacturer at a 40% discount on the MRP. What is the price before tax that will be invoiced to the dealer by the manufacturer? 

Display the 40% discount price also. Do the minimum calculation steps required to arrive at the answer

NB: Choose best technical methodology to solve this problem. Follow all coding conventions and standards. Any points not mentioned in the question can be assumed. Indicate any extra assumptions that you make in the UI to make the output unambiguous to the user. Include all needed validations to ensure robustness of the software
"""

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
        while 1:
            try:
                p1 = input("Enter Product Name: ")
                p2 = input("Enter Product Category: ")
                p3 = productCode()
                p4 = int(input("Enter Product Basic Price: "))
                p5 = int(input("Enter Tax of Product in %: "))
                p6 = int(input("Enter Discount of Product in %: "))
                p7 = int(input("Enter MRP of Product: "))
                return self(p1,p2,p3,p4,p5,p6,p7)
            except:
                print('Invalid input!')
                break

           
class productCode(AllProducts):
    
    @property
    def properCode(self):
        return self.__productCode
    @properCode.setter
    def properCode(self,productCode):
        prodCode = []
        lst=list(self.get_user_input.p2)
        for i in lst[0:3]:
            prodCode = lst.append(i)
            self.__productCode = prodCode

obj1 = AllProducts.get_user_input()
"""
("prod1",'Hygiene','CAPR1',50,5,2,70)
p1 = input("Enter Product Name: ")
obj1.properName(p1)
p2 = input("Enter Product Category: ")
p3 = input("Enter Product Code: ")
p4 = int(input("Enter Product Basic Price: "))
p5 = int(input("Enter Tax of Product in %: "))
p6 = int(input("Enter Discount of Product in %: "))
p7 = int(input("Enter MRP of Product: "))
obj1.properName()
"""







