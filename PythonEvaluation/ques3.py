"""
Q3. The currencyListminations in Indian currency are:
|1, |2, |5, |10, |,20, |50, |100, |200, |500, |2000.
Given an amount N, print how many coins/notes make up N
Sample input:
Enter the amount: 2640
Output:
2000 1
500 1
100 1
10 4
Also test your program with N:3781, 4928, and 5134
"""

currencyList = {2000 : 0, 500 : 0, 200 : 0, 100 : 0, 50 : 0, 20 : 0, 10 : 0, 5 : 0, 2 : 0, 1 : 0}

def denominationOfCurrency(amount):
    while (amount != 0):
        if (amount >= 2000):
            amount = amount - 2000
            currencyList[2000] += 1
             
        elif (amount >= 500):
            amount = amount - 500
            currencyList[500] += 1
             
        elif (amount >= 200):
            amount = amount - 200
            currencyList[200] += 1
             
        elif (amount >= 100):
            amount = amount - 100
            currencyList[100] += 1
             
        elif (amount >= 50):
            amount = amount - 50
            currencyList[50] += 1
             
        elif (amount >= 20):
            amount = amount - 20
            currencyList[20] += 1
             
        elif (amount >= 10):
            amount = amount - 10
            currencyList[10] += 1
             
        elif (amount >= 5):
            amount = amount - 5
            currencyList[5] += 1
             
        elif (amount >= 2):
            amount = amount - 2
            currencyList[2] +=1
             
        elif (amount >= 1):
            amount = amount - 1
            currencyList[1] += 1
             
        else:             
            break

amount = int(input("Enter the amount: "))
denominationOfCurrency(amount)

print(f"""Number of coins/notes make up {amount} are... 
2000 : {currencyList.get(2000)}
500 : {currencyList.get(500)}
200 : {currencyList.get(200)}
100 : {currencyList.get(100)}
50 : {currencyList.get(50)}
20 : {currencyList.get(20)}
10 : {currencyList.get(10)}
5 : {currencyList.get(5)}  
2 : {currencyList.get(2)}  
1 : {currencyList.get(1)}    
""")

