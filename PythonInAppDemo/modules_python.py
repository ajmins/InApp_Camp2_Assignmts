#(MODULES-PYTHON
# contain large no of built-in functions called as modules
# need to import them using keyword "import")

#to use randrange() function in the random module
import imp
import random
print(random.randrange(1,10))

#using aliases to cut short the module name
import math as m
print("square root: ", m.sqrt(25))


#importing only specific function from the module
#from moduleName import name1, name2,...

"""
from random import randrange,randint
print(randrange(1,10))
"""
print("\n-----------------------------------------\n")
#(RANDOM MODULE
# based on pseudo-random number generator function random(), which generates the float number btwn 0.0 and 1.0
# diff types :
# random(): float num btwn 0.0 and 1.0
# randint(beg, end): integer value btwn specified number
# choice(list or tuple): select from a non- empty sequence
# shuffle(list): randomly reorder elements in the list
# randrange(beg,end,step): number within range specified
# seed(): apply on the particular random number with the seed argument
# )

print("random:", random.random())
print("randint:", random.randint(5,20))
print("choice:", random.choice(['head', 'tail']))
myDressColours =  ['blue','red','black','yellow','green']
random.shuffle(myDressColours)
print("shuffle:", myDressColours)
print("random:", random.randrange(1,10,4))
random.seed(10)
print("seed:", random.random())
random.seed(10)
print("seed:", random.random())
random.seed(11)
print("seed:", random.random())

"""
random: 0.35830038754326377
randint: 10
choice: tail
shuffle: ['black', 'red', 'yellow', 'blue', 'green']
random: 9
seed: 0.5714025946899135
seed: 0.5714025946899135
seed: 0.4523795535098186
"""

print("\n-----------------------------------------\n")
#(Time MODULE
# time, date etc are objects in python
# to work with real dates and times
# we can import modules datetime, time, calendar)

import time as t
print(t.time()) #print the number of ticks/seconds spent since 12 AM, 1st Jan 1970; tick is the smallest unit of time
#1658294200.6730733
print(t.localtime(t.time())) #to get the multiple time values as a tuple
#time.struct_time(tm_year=2022, tm_mon=7, tm_mday=20, tm_hour=10, tm_min=46, tm_sec=40, tm_wday=2, tm_yday=201, tm_isdst=0)
#t.sleep(5) #wait for 5 seconds
print(t.asctime(t.localtime(t.time()))) #human readble form
#Wed Jul 20 10:49:44 2022

#use of sleep() in for loop
#for i in range(0,10):
    #print(i)
    #t.sleep(2) #delay the program execution by thespecified number of seconds


#(Python DATETIME module
# enables us to create the custom date objects, perform various operations ondate like the comparison, etc)

#get the datetime object representation for the current time
import datetime as dt
print(dt.datetime.now()) #return current date time object
#2022-07-20 10:58:34.199992

print("\n-----------------------------------------\n")

#CUSTOM datetime object bypassing the desired date in the datetime constructor

#creates and returns the datetime object for the specified date
birthDay = dt.datetime(2022,5,13)
print(birthDay) #2022-05-13 00:00:00
#to include time
birthDayT = dt.datetime(2022,5,13,11,31,50)
print(birthDayT) 
 #2022-05-13 11:31:50

##############################
#time comparison demo
from datetime import datetime as dt

#we can compare two dates using comparison operators
#if the time is in btwn 9AM and 6PM, then it prints working hours otherwise shift over
if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
    print("Working hours...")
else:
    print("Shift complete")

print("\n-----------------------------------------\n")
#calendar module : various methods to work with the calendars
import calendar as cl
myCalendar =  cl.month(2022,7) #get calendar for a month
print(myCalendar)

"""
     July 2022
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
"""
myCalendarF =  cl.prcal(2000) #get calendar for an year
print(myCalendarF)
print("\n-----------------------------------------\n")

"""
                                2000

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6             1  2  3  4  5
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       6  7  8  9 10 11 12
10 11 12 13 14 15 16      14 15 16 17 18 19 20      13 14 15 16 17 18 19
17 18 19 20 21 22 23      21 22 23 24 25 26 27      20 21 22 23 24 25 26
24 25 26 27 28 29 30      28 29                     27 28 29 30 31
31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2       1  2  3  4  5  6  7                1  2  3  4
 3  4  5  6  7  8  9       8  9 10 11 12 13 14       5  6  7  8  9 10 11
10 11 12 13 14 15 16      15 16 17 18 19 20 21      12 13 14 15 16 17 18
17 18 19 20 21 22 23      22 23 24 25 26 27 28      19 20 21 22 23 24 25
24 25 26 27 28 29 30      29 30 31                  26 27 28 29 30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                   1  2  3
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       4  5  6  7  8  9 10
10 11 12 13 14 15 16      14 15 16 17 18 19 20      11 12 13 14 15 16 17
17 18 19 20 21 22 23      21 22 23 24 25 26 27      18 19 20 21 22 23 24
24 25 26 27 28 29 30      28 29 30 31               25 26 27 28 29 30
31

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1             1  2  3  4  5                   1  2  3
 2  3  4  5  6  7  8       6  7  8  9 10 11 12       4  5  6  7  8  9 10
 9 10 11 12 13 14 15      13 14 15 16 17 18 19      11 12 13 14 15 16 17
16 17 18 19 20 21 22      20 21 22 23 24 25 26      18 19 20 21 22 23 24
23 24 25 26 27 28 29      27 28 29 30               25 26 27 28 29 30 31
30 31
None
"""


#(MATH module : mathematical functions like trig, representation func, log fun, etc
# contained mathematical constants, Pie and Euler number etc)
import math as m
num = 2e-7 #small value of x
#returns natural log of given number calculated based on e
print(m.log(m.fabs(num), 10)) #-6.698970004336019

#base 10 log or stad log of given number
n = 15
print(m.log10(n)) #1.1760912590556813

#math.exp() returns a floating point number after raising e to the given number
print('e^x(using exp() function) is :', m.exp(num)-1)

n2 =  m.pow(4,2)
print(n2)
n3 = m.floor(15.6826387) #will round to smallest digit
print(n3)
n4 = m.ceil(17.2397) # round to next digit
print(n4)
n5 = m.fabs(-11.7987) #return absolute
print(n5)
n6 = m.factorial(10) #return factorial
print(n6)
n7 = m.modf(3.14) #return integer and decimal part
print(n7) #(0.14000000000000012, 3.0)















