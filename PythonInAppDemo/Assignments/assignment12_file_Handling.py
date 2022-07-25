import os
#to list all contacts in alphabetical order
def list():
    with open('contacts\contacts.txt') as f:
        myList=sorted(f.readlines())
        print(f.splitlines()) 

        print(myList) 
        f.close()

#to add a new contact
def add():
    name = input("Enter the name of new contact: ")
    num = input("Enter the phone number: ")
    f = open("contacts\contacts.txt", "a")
    f.write(name + "-" + num)
    f.write("\n")
    f.close()
    print("Updated PhoneBook is: ")
    list()

def accept():
        #choice selection
    while(True):
        ch =int(input("""

    1.List all contacts
    2.Add a new contact
    3.Delete a contact
    4.Search by name
    5.Search by number
    6.Exit

    Enter the choice: 
    """))
        if ch in (1,2,3,4,5,6):
            if ch == 1:
                print("List all contacts")
                list()
            elif ch == 2:
                print("Add a new contact")
                add()
            elif ch == 3:
                print("Delete a contact")
                delete()
            elif ch == 4:
                print("Search by name")
                searchName()
            elif ch == 5:
                print("Search by number")
                searchNo()
            elif ch == 6:
                exit()
        else:
            print("Invalid Input. Try Again!")

print(os.getcwd())
#main program
if os.path.isdir("contacts") == True:
    if os.path.exists("contacts\contacts.txt"):
        accept()
    else:
        myFilePtr = open("contacts\contacts.txt","w")
        with open("contacts\contacts.txt", "a") as f:
            f.write("Name - Phone Number\n")
            f.close()
else:
    os.mkdir("contacts")
