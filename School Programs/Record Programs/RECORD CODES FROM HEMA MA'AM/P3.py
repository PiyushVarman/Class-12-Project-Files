def fact(k):
    f=1
    for i in range(1,k+1):
        f*=i
    return f
def fibo(m):
    f1,f2=-1,1
    for j in range(m):
        f3=f1+f2
        f1=f2
        f2=f3
        print(f3,end='  ')
    print()
while True:
    print('''MENU
1. Factorial of a number
2. Generate ‘N’ numbers of Fibonacci series
3. Exit''')
    ch=int(input('Enter choice :'))
    if ch==3:
        break
    elif ch==2:
        n=int(input('Enter number of terms:'))
        print('Fibonacci Series')
        fibo(n)
    elif ch==1:
        n=int(input('Enter number:'))
        print('Factorial of',n,'is :',fact(n))
    else:
        print('Invalid Option')
