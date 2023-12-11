'''13. BINARY FILE 1'''

print("OUTPUT")
import pickle
def topdet(l,st):
    if l:
        max=l[0][3]
        for k in l:
            if k[3]>=max:
                max=k[3]
        print(st,'stream toppers:')
        for k in l:
            if k[3]==max:
                print('Name:',k[1],'\nRoll no:',k[0])
        print('Highest total is:',max)
with open('STUDENT.dat','wb') as f:
    N=int(input('Enter number of students:'))
    for i in range(N):
        rno=int(input('Enter roll number:'))
        na=input('Enter name:')
        st=input('Enter stream:')
        t=int(input('Enter total:'))
        L=[rno,na,st,t]
        pickle.dump(L,f)
    print('File created successfully')
while True:
    print('''MENU
1. Display Stream wise topper detail
2. Increment the total by 3 marks for students in the biology stream and decrement by 2for
students in EG stream.
3. Exit''')
    ch=int(input('Enter option:'))
    if ch==1:
        with open('STUDENT.dat','rb') as f:
            LS,LC,LB,LE=[],[],[],[]
            try:
                while True:
                    l=pickle.load(f)
                    if l[2].lower()=='computer science':
                        LS+=[l]
                    elif l[2].lower()=='commerce':
                        LC+=[l]
                    elif l[2].lower()=='biology':
                        LB+=[l]
                    elif l[2].lower()=='eg':
                        LE+=[l]
            except EOFError:
                pass
        topdet(LS,'Computer Science')
        topdet(LB,'Biology')
        topdet(LC,'Commerce')
        topdet(LE,'Engineering Graphics')
    elif ch==2:
        with open('STUDENT.dat','rb+') as f:
            LS,LC,LB,LE=[],[],[],[]
            try:
                while True:
                    s=f.tell()
                    l=pickle.load(f)
                    if l[2].lower()=='biology':
                        l[3]+=3
                    elif l[2].lower()=='eg':
                        l[3]-=2
                    f.seek(s)
                    pickle.dump(l,f)
            except EOFError:
                pass
        print('Modified successfully')
        print('Modified file')
        with open('STUDENT.dat','rb') as f:
            try:
                while True:
                    l=pickle.load(f)
                    print('Name:',l[1],'Roll no:',l[0],'Stream:',l[2],'Total:',l[3])
            except EOFError:
                pass
    elif ch==3:
        break
    else:
        print('Invalid option')
        
'''OUTPUT
Enter number of students:3
Enter roll number:1
Enter name:Ram
Enter stream:Biology
Enter total:480
Enter roll number:2
Enter name:Sai
Enter stream:Computer Science
Enter total:499
Enter roll number:3
Enter name:Hari
Enter stream:Biology
Enter total:380
File created successfully
MENU
1. Display Stream wise topper detail
2. Increment the total by 3 marks for students in the biology stream and decrement by 2for
students in EG stream.
3. Exit
Enter option:1
Computer Science stream toppers:
Name: Sai 
Roll no: 2
Highest total is: 499
Biology stream toppers:
Name: Ram 
Roll no: 1
Highest total is: 480
MENU
1. Display Stream wise topper detail
2. Increment the total by 3 marks for students in the biology stream and decrement by 2for
students in EG stream.
3. Exit
Enter option:2
Modified successfully
Modified file
Name: Ram Roll no: 1 Stream: Biology Total: 483
Name: Sai Roll no: 2 Stream: Computer Science Total: 499
Name: Hari Roll no: 3 Stream: Biology Total: 383
MENU
1. Display Stream wise topper detail
2. Increment the total by 3 marks for students in the biology stream and decrement by 2for
students in EG stream.
3. Exit
Enter option:3'''
