n=int(input("Enter the number of terms:"))
def prime(z):
    fac=0
    if z==0 or z==1:
        print("neither prime nor composite.")
    else:
        for i in range(1,z+1):
            if z%i==0:
                fac+=1
        if fac==2:
            print("prime")
        else:
            print("composite")

def fibo(n):
    a,b=-1,1
    for i in range(n):
        s=a+b
        a=b
        b=s
        print(s,end='- ')
        prime(s)
fibo(n)
