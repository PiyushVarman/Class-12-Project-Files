def lucky(a):   
    nsum,ssum=0,0
    ncount,scount=0,0
    for i in str(a):
        nsum+=int(i)
        ssum+=int(i)**2
    for i in range(1,nsum+1):
        if nsum%i==0:
            ncount+=1
    for i in range(1,ssum+1):
        if ssum%i==0:
            scount+=1
    return (ncount==2 and scount==2)
n=int(input("Enter the number:"))
x=lucky(n)
if x:
    print(n,"is a lucky number.")
else:
    print(n,"is not a lucky number.")
