"PROG 16"

print("OUTPUT")

def Push():
    n=int(input('Enter number:'))
    st.append(n)
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
1. Push
2. Pop
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
    
'''OUTPUT
MENU
1. Push
2. Pop
3. Display Stack
4. Peek
5. Exit
Enter option:1
Enter number:2
Enter option:1
Enter number:3
Enter option:1
Enter number:7
Enter option:3
7->3->2->
Enter option:4
7
Enter option:2
Enter option:3
3->2->
Enter option:5
Exited'''
