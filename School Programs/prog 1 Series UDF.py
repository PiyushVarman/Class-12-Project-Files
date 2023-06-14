#Sum of Series using UDF and Menu Driven
#1) x/2!-x3/4!+x5/6!...n
#2) x/3!-x3/5!+x5/7!-x7/9!..n
#3) Exit

def fac(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f

def s1(x,n):
    s=0
    for i in range(n+1):
        z=fac((2*i)+2)
        if i%2==0:
            s+=x**((2*i)+1)/z
        else:
            s-=x**((2*i)+1)/z
    return s

def s2(x,n):
    s=0
    for i in range(n+1):
        z=fac((2*i)+3)
        if i%2==0:
            s+=x**((2*i)+1)/z
        else:
            s-=x**((2*i)+1)/z
    return s

while True:
    sel=int(input('''1- Series 1
2- Series 2
3- Exit
Select your option:'''))
    if sel==1:
        x=int(input("Enter the x value:"))
        n=int(input("Enter the n value:"))
        print("The sum of the series is",s1(x,n))

    elif sel==2:
        x=int(input("Enter the x value:"))
        n=int(input("Enter the n value:"))
        print("The sum of the series is",s2(x,n))

    elif sel==3:
        break
