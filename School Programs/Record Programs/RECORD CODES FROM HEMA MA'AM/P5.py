import random
L=[]
def Generate(a,b):
    L.clear()
    while len(L)<5:
        X=random.randint(a,b)
        if X not in L:
            L.append(X)
    print('The generated list is:',L)
def Max_SecMax():
    max=L[0]
    for i in L:
        if i>max:
            max=i
    l=[]
    for i in L:
        if i!=max:
            l.append(i)
    max1=l[0]
    for j in l:
        if j>max1 and j<max:
            max1=j
    print('Largest number is:',max)
    print('Second largest number is:',max1)
def Prime():
    l=[]
    for i in L:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            if i>1:
                l+=[i]
    if l:
        print('Prime numbers in the list are:',l)
    else:
        print('No prime numbers in the generated list')
print('''MENU
1. Generate random numbers between the given limits
2. Find the largest and second largest numbers in the list
3. Find the prime numbers in the list
4. Exit''')
while True:
    ch=int(input('Enter choice :'))
    if ch==4:
        print('Exited')
        break
    elif ch==1:
        a=int(input('Enter lower limit:'))
        b=int(input('Enter upper limit:'))
        Generate(a,b)
    elif ch==2:
        Max_SecMax()
    elif ch==3:
        Prime()
    else:
        print('Invalid Option')

