def Factorial(n):
    f=1
    for j in range(1,n+1):
        f*=j
    return f
def Power(n,m):
    return n**m
while True:
    print('1. x^1/2!-x^3/4!+x^5/6!+.. n terms')
    print('2. x^1/3!-x^3/5!+x^5/7!+.. n terms')
    print('3. Exit')
    ch=int(input('Enter option'))
    if ch==3:
        break
    elif ch==1:
        s=0
        x=int(input('Enter x value:'))
        n=int(input('Enter n value:'))
        sign=1
        for k in range(1,n+1):
            s+=Power(x,2*k-1)/Factorial(2*k)*sign
            sign*=-1
        print('Sum is:',round(s,2))
    elif ch==2:
        s=0
        x=int(input('Enter x value:'))
        n=int(input('Enter n value:'))
        sign=1
        for k in range(1,n+1):
            s+=Power(x,2*k-1)/Factorial(2*k+1)*sign
            sign*=-1
        print('Sum is:',round(s,2))
    else:
        print('Invalid Option')
