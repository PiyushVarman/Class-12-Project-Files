def fibo(n):
    a,b=-1,1
    for i in range(n):
        print(a+b,end=' ')
        a,b=b,a+b
x=int(input("Enter number of terms:"))
fibo(x)
