#LOOP ASSIGNMENT
#(Q. Print the list of numbers which are divisible by 5 and multiple of 8 between 2000 and 2500 (both included)

for i in range(2000,2501):
    if(i % 5 == 0 and i % 8 ==0):
        print(i) #13 numbers

#(Q.write a python program to create the multiplication table (from 1 to 10) of a number getting input from the user)
num = int(input("Enter a number: "))
for i in range(1,11):
    pro = i * num
    print(i, "x", num, "=", pro)