'''7. MENU DRIVEN CODE – DICTIONARY
AIM: to create a dictionary to store details of ‘n’ subscribers and perform the menu
operations.
METHODOLOGY: The details of ‘n’ subscribers namely name and phone number are read and
stored in a dictionary. Using a menu and user’s choice, the operations like Add a subscriber
detail, View all subscribers, Modify name of a given subscriber, Delete an existing subscriber
are done using user defined functions.'''

def add(d):
    x=input("Enter the name to be added:")
    d[x]=int(input("Enter the phone number:"))

def view(d):
    print("The dictionary is:")
    for i in d:
        print(i,d[i],sep=' - ')

def modify(d):
    x=int(input("Enter the phone number:"))
    if x in d.values():
        for i in d.items():
            if i[1]==x:
                chk=i[0]
        print("Current name:",chk)
        z=input("Enter the name that you would like to update:")
        d[z]=x
        del d[chk]
        print("The updated dictionary is:",d)
    else:
        print("This number doesn't exist in the dictionary.")

def delete(d):
    x=int(input("Enter the phone number:"))
    if x in d.values():
        for i in d.items():
            if i[1]==x:
                chk=i[0]
        del d[chk]
        print("The updated dictionary is:",d)
    else:
        print("This number doesn't exist in the dictionary.")

d={}
while True:
    sel=int(input('''1 - Add
2 - View
3 - Modify Name
4 - Delete
5 - Exit

Choose your option:'''))

    if sel==1:
        add(d)

    elif sel==2:
        view(d)

    elif sel==3:
        modify(d)

    elif sel==4:
        delete(d)

    elif sel==5:
        print("Program Terminated.")
        break
