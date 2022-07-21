#Phone Book Operations

phoneBook = dict(Leya = 9874569852, Sibi = 8598741203, Manu = 7895632014, Arun = 8564001296)
#to list all contacts in albhabetical order
def list():
    print("Name - Phone Number")
    for i in sorted(phoneBook.items()):
        print(i[0],"-",i[1])

#to add a new contact
def add():
    name = input("Enter the name of new contact: ")
    num = input("Enter the phone number: ")
    phoneBook.update({name: num})
    print("Updated PhoneBook is: ")
    list()
#to remove a contact
def delete():
    name = input("Enter the name of contact to delete: ")
    del phoneBook[name]
    print("Updated PhoneBook is: ")
    list()

#to search a contact by name
def searchName():
    name = input("Enter the name of contact to search: ")
    if name in phoneBook.keys():
        print("Contact Found\n{} - {}".format(name, phoneBook[name]))
    else:
        print("Contact not found")

#to search a contact by number
def searchNo():
    num = int((input("Enter the phone number to search: ")))
    for name,numbers in phoneBook.items():
        if(num == numbers):
            print("Contact Found\n{}-{}".format(name,numbers))
            break
        else:
            print("Contact not found")
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






