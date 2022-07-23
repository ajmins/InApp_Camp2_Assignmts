"""
1 1. Create a number guessing game.
2 ---------------------------------
3 System will generate a number randomly between 1 and 10 and keep it
4 The user have to guess this number in 5 attempts.
5 If the guess is +- 9,8 numbers away, it is 'very cold'
6 If the guess is +- 7,6 numbers away, it is 'cold'
7 If the guess is +- 5,4 numbers away, it is 'neutral'
8 If the guess is +- 3 numbers away, it is 'warm'
9 If the guess is +- 2 numbers away, it is 'hot'
10 If the guess is a match, should give the message 'Its a match! Congrats', play again
11 The response of the computer should be like
12
13 1.Start the Game
14 2.Exit
15
16 I've already guessed one.
17 Enter your guess: 2
18
19
20 Your guess is warm from left and cold from right. Try again
21 Enter your guess: 3
22
23 Your guess is cold from left and warm from right. Try again
24 Enter your guess: 4
25
26 Your guess is cold from left and warm from right. Try again
27 Enter your guess: 6
28
29 Its a match! Congrats
30 1.Play again
31 2.Exit

"""
import random as r
flag = 0
def game():
    flag = 1
    num = r.randint(1,10)
    print("I have already guessed one.", num)
    
    for i in range(5):
        while(1):
            guess = int(input("Enter your guess: "))
            if guess in range(1,11):
                break
            else:
                print("Invalid input!!")
                break
        diff = abs(num-guess)
        if diff == 0:
            print("Its a match! Congrats")
            return
        elif diff in [9, 8]:
            condition = 'cold'
        elif diff in [7, 6]:
            condition = 'cold'
        elif diff in [5, 4]:
            condition = 'neutral'
        elif diff == 3:
            condition = 'warm'
        elif diff < 2:
            condition = 'warm'

        if guess < num:
            print("Your guess is cold from left and {} from right. Try again".format(condition))
        else:
            print("Your guess is {} from left and cold from right. Try again".format(condition))

while(True):
    print('1. Play again' if flag else '1. Start the Game')
    print('2. Exit')
    ch = int(input('Enter: '))
    if ch == 1:
        game()
    elif ch == 2:
        break
    else:
        print("Invalid Input")














