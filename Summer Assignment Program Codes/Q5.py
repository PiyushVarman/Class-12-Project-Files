def prime(a,b):
    s=()
    for i in range(a,b+1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            s+=(i,)
    if len(s)==0:
        print("Sorry, there are no prime numbers in the range",a,"to",b)
    else:
        print("The prime numbers are:",s)
x=int(input("Enter the lower limit:"))
y=int(input("Enter the upper limit:"))
prime(x,y)
