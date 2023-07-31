def fac(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f

def palindrome(t):
    l=[]
    found=0
    for i in t:
        x=str(i)
        if x==x[::-1]:
            found=1
            l.append(i)
    if found==0:
        print("There are no palindromic numbers in this tuple.")
    else:
        print("The list of palindromic numbers is:",l)

def special(l,u):
    z=[]
    found=0
    for i in range(l,u+1):
        s=0
        for j in str(i):
            s+=fac(int(j))
        if s==i:
            z.append(i)
            found=1
    if found==0:
        print("There are no special numbers from",l,"to",u)
    else:
        print("The list of special numbers are:",z)
