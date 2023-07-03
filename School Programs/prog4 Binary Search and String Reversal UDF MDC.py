def binsearch(l):
    n=len(l)
    start,end,st=0,n-1,0 #st=status checker
    l.sort()
    chk=int(input("Enter the number to be searched in the list:"))
    while start<=end:
        mid=(start+end)//2
        if l[mid]==chk: #Data is EXACTLY at the middle position
            st=1
            break
        elif l[mid]>chk:
            end=mid-1
        else:
            start=mid+1
    if st==1:
        print(chk,"is found at the",mid+1,"position.")
    else:
        print(chk,"is not found in the list.")

def rev(a):
    return a[::-1]

while True:
    sel=int(input('''1 - Binary Search
2 - String Reversal
3 - Exit'''))
    
    if sel==1:
        l=[]
        n=int(input("Enter the number of elements:"))
        for i in range(n):
            l.append(int(input("Enter the number:")))
        binsearch(l)
    
    if sel==2:
        x=input("Enter the string:")
        print(rev(x))

    if sel==3:
        break
