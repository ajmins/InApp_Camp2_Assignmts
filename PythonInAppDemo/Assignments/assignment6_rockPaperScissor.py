#Rock-Paper_Scissor Game (2 player)
import random
#intialise count and points
count = 0
humanPlayer = 0
computerPlayer = 0
print("""
    1.Rock
    2.Paper
    3.Scissor
    4.Exit
    """)
#Rock()
def rock():
    global count, humanPlayer, computerPlayer, temp
    if(temp == 1):
        print("Computer entered Rock")
        pass
    elif(temp == 2):
        print("Computer entered Paper")
        computerPlayer = computerPlayer + 1
        count = count + 1
    elif(temp ==3):
        print("Computer entered Scissor")
        humanPlayer = humanPlayer + 1
        count = count + 1
#Paper()
def paper():
    global count, humanPlayer, computerPlayer, temp
    if(temp == 1):
        print("Computer entered Rock")
        humanPlayer = humanPlayer + 1
        count = count + 1
    elif(temp == 2):
        print("Computer entered Paper")
        pass
    elif(temp ==3):
        print("Computer entered Scissor")
        computerPlayer = computerPlayer + 1
        count = count + 1
#Scissor()
def scissor():
    global count, humanPlayer, computerPlayer, temp
    if(temp == 1):
        print("Computer entered Rock")
        computerPlayer = computerPlayer + 1
        count = count + 1
    elif(temp == 2):
        print("Computer entered Paper")
        humanPlayer = humanPlayer + 1
        count = count + 1
    elif(temp ==3):
        print("Computer entered Scissor")
        pass

#choice selection
while(count < 5):
    ch = int(input("Enter your choice: "))
    temp =  random.choice([1, 2, 3])
    if ch in (1,2,3,4):
        if ch == 1:
            print("You entered Rock")
            rock()
        elif ch == 2:
            print("You entered Paper")
            paper()
        elif ch == 3:
            print("You entered Scissor")
            scissor()
        elif ch == 4:
            exit()
    else:
        print("Invalid Input. Try Again!")
 
print("""Points
        Computer: {}
        You: {}""".format(computerPlayer,humanPlayer))
if(computerPlayer>humanPlayer):
    print("Computer Wins!!!!")
elif(computerPlayer<humanPlayer):
    print("You Wins!!!!")
else:
    print("Tie")