import os
import re
#to list all contacts in alphabetical order
def list():
    lst=[]
    newLst=[]
    try:
        with open('contacts\contacts.txt', 'r') as f:
            for line in f:
                lst.append(line)
            for i in lst:
                if i != 'Name - Phone Number\n':
                    newLst.append(i.strip())
            newLst.sort()
            for i in newLst:
                print(i)
    except:
        print("Oops! something error")
#to add a new contact
def add():
    name = input("Enter the name of new contact: ")
    num = input("Enter the phone number: ")
    try:
        f = open("contacts\contacts.txt", "a")
        phoneBook = name + " - " + num
        f.write(phoneBook)
        f.write("\n")
        f.close()
        print("Added Successfully")
    except:
        print("Oops! something error")
    print("\nUpdated PhoneBook is: ")
    list()

#to remove a contact
def delete():
    flag = 0
    name = input("Enter the name of contact to delete: ")
    try:
        with open("contacts\contacts.txt", "r") as fr:
            lines = fr.readlines()
    
            with open('contacts\contacts.txt', 'w') as fw:
                for line in lines:
                    nam, phone = line.strip().split('-')
                    if nam.strip() == name:
                        print("Deleted successfully")
                        continue
                    fw.write(line)
                    
    except:
        print("Oops! something error")
    print("\nUpdated PhoneBook is: ")
    list()

#to search a contact by name
def searchName():
    name = input("Enter the name of contact to search: ")
    f = False
    try:
        with open("contacts\contacts.txt", "r") as fr:
            lines = fr.readlines()
            for line in lines:
                nam, phone = line.strip().split('-')
                if nam.strip() == name:
                    print('Name - Phone Number\n', line)
                    print("Found successfully")
                    f = True
        if not f:
            print("Not Found")
    except:
        print("Oops! something error")
        
#to search a contact by number
def searchNo():
    f = False
    num = (input("Enter the phone number to search: "))
    try:
        with open("contacts\contacts.txt", "r") as fr:
            lines = fr.readlines()
            for line in lines:
                nam, phone = line.strip().split('-')
                if phone.strip() == num:
                    print('Name - Phone Number\n', line)
                    print("Found successfully")
                    f = True
        if not f:
            print("Not Found")
    except:
        print("Oops! something error")

#choice selection
def accept():   
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

#print(os.getcwd())
#main program
if os.path.isdir("contacts") == True:
    if os.path.exists("contacts\contacts.txt"):
        accept()
    else:
        myFilePtr = open("contacts\contacts.txt","w")
        with open("contacts\contacts.txt", "a") as f:
            f.write("Name - Phone Number\n")
else:
    os.mkdir("contacts")
