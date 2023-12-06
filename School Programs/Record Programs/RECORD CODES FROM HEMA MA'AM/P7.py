'''7. MENU DRIVEN CODE – DICTIONARY
AIM: to create a dictionary to store details of ‘n’ subscribers and perform the menu
operations.
METHODOLOGY: The details of ‘n’ subscribers namely name and phone number are read and
stored in a dictionary. Using a menu and user’s choice, the operations like Add a subscriber
detail, View all subscribers, Modify name of a given subscriber, Delete an existing subscriber
are done using user defined functions.
Note: The menu to be display should be:
MENU
1. ADD
2. VIEW
3. MODIFY NAME
4. DELETE
5. EXIT
Creating the dictionary should be done only by calling option 1)ADD repeatedly.
In Modify and Delete, the input taken is the phone number. If the number does not exist in the
list, appropriate message should be shown'''
d={}
def add():
    no=int(input('Enter phone number:'))
    name=input('Enter name:')
    if len(str(no))==10:
        if no not in d:
            d[no]=name
        else:
            print('Phone number is already taken')
    else:
        print('Invalid Phone number')
def view():
    for k in d:
        print('Name:',d[k],'Phone Number:',k)
def modify():
    no=int(input('Enter number:'))
    if no in d:
        na=input('Enter new name:')
        d[no]=na
        print('Modified successfully')
    else:
        print('Phone number does not exist in record')
def delete():
    no=int(input('Enter number:'))
    if no in d:
        d.pop(no)
        print('Deletion successful')
    else:
        print('Phone number does not exist in record')
while True:
    print('''MENU
1. ADD
2. VIEW
3. MODIFY NAME
4. DELETE
5. EXIT''')
    ch=int(input('Enter choice :'))
    if ch==5:
        break
    elif ch==1:
        add()
    elif ch==2:
        view()
    elif ch==3:
        modify()
    elif ch==4:
        delete()
    else:
        print('Invalid Option')







                 
