def listsort(l):
    i=0
    for i in range(len(l)):
        for j in range(i,len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
    print("The sorted list is:",l)
    
def bins(l):
    l.sort()
    start,end=0,len(l)-1
    s=input("Enter the country to be searched for:")
    mid=(start+end)//2
    while start<=end:
        if s==l[mid]:
            st=1
            break
        elif s>l[mid]:
            start=mid+1
        else:
            last=mid-1
    if st==1:
        print(s,"is found at",mid+1,"position.")
    else:
        print(s,"is not in the list.")

def large(l):
    print(l)
    fir=l[0]
    for i in l:
        if i>fir:
            fir=i
    for i in l:
        if i!=fir:
            sec=i
    for i in l:
        if i>sec and i!=fir:
            sec=i
    print("The largest number is:",fir,"\nThe second largest number is:",sec)


def series(x,n):
    s=0
    for i in range(1,n+1):
        fac=1
        for j in range(1,(2*i)+1):
            fac*=j
        if i%2!=0:
            s+=x**(2*n-1)/fac
        else:
            s-=x**(2*n-1)/fac
    print("The sum of the series is",s)

while True:
    sel=int(input('''1- Bubble Sort
2- Search for a country using binary search
3- Largest and second largest number
4- Sum of Series'''))

    if sel==1:
        L=eval(input("Enter the list to sort:"))
        listsort(L)

    elif sel==2:
        L=eval(input("Enter the list of countries:"))
        bins(L)

    elif sel==3:
        L=eval(input("Enter the list of numbers:"))
        large(L)

    elif sel==4:
        x=int(input("Enter the x value:"))
        n=int(input("Enter the n value:"))
        series(x,n)

    elif sel==5:
        print("Come back later!")
        break
