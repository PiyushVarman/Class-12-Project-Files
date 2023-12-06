def search(n,l):
    start=0
    stop=len(l)-1
    while start<=stop:
        mid=(start+stop)//2
        if l[mid]==n:
            print('Found at',mid+1,'position')
            break
        elif l[mid]>n:
            stop=mid-1
        else:
            start=mid+1
    else:
        print('No such number in given list')
def reverse(s):
    return s[::-1]
while True:
    print('''MENU
1. Binary Search in a list of integers
2. Reversing a string
3. Exit''')
    ch=int(input('Enter choice :'))
    if ch==3:
        break
    elif ch==1:
        L=[]
        print('Enter numbers in ascending order')
        n=int(input('Enter number of elements :'))
        for j in range(n):
            L.append(int(input('Enter number')))
        m=int(input('Enter number to search:'))
        search(m,L)
    elif ch==2:
        string=input('Enter string :')
        print('Reversed string:',reverse(string))
    else:
        print('Invalid Option')
