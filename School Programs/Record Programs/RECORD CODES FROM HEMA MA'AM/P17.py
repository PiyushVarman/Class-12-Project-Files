'''17. STACK OPERATIONS - 2
AIM : To implement a stack using a list where each element in the list has Country name and
Capital. The related operations are performed using user defined options.
METHODOLOGY: The stack operations namely Insert, Delete, Peek, Display Stack Status are
performed on a nested list using user defined options
Note: The menu options to be displayed:
MENU
1. Insert
2. Delete
3. Display Stack
4. Peek
5. Exit'''
def Push():
    n=input('Enter country name:')
    m=input('Enter capital:')
    st.append([n,m])
def Pop():
    if st:
        st.pop()
    else:
        print('Underflow')
def Display():
    if st:
        for i in range(len(st)-1,-1,-1):
            print(st[i],end='->')
        print()
    else:
        print('Underflow')
def Peek():
    if st:
        print(st[-1])
    else:
        print('Underflow')
st=[]
print('''MENU
1. Insert
2. Delete
3. Display Stack
4. Peek
5. Exit''')
while True:
    ch=int(input('Enter option:'))
    if ch==1:Push()
    elif ch==2:Pop()
    elif ch==3:Display()
    elif ch==4:Peek()
    elif ch==5:
        print('Exited')
        break
    else:print('Invalid option')
'''MENU
1. Insert
2. Delete
3. Display Stack
4. Peek
5. Exit
Enter option:1
Enter country name:India
Enter capital:Delhi
Enter option:1
Enter country name:Algeria
Enter capital:Algiers
Enter option:1
Enter country name:Bangladesh
Enter capital:Dhaka
Enter option:3
['Bangladesh', 'Dhaka']->['Algeria', 'Algiers']->['India', 'Delhi']->
Enter option:4
['Bangladesh', 'Dhaka']
Enter option:2
Enter option:3
['Algeria', 'Algiers']->['India', 'Delhi']->
Enter option:5
Exited'''
