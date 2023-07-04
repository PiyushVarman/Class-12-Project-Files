import random

def generate(l,u):
    rl=[]
    for i in range(l,u+1):
        rl.append(random.randint(l,i))
    return rl

def max_secmax(l):
    large=l[0]
    n=len(l)
    for i in range(n):
        if l[i]>large:
            large=l[i]
    for i in range(n):
        if l[i]!=large:
            sec=l[i]
            break
    for i in range(n):
        if l[i]!=large and l[1]>sec:
            sec=l[i]
    print("The largest number is",large)
    print("The second largest number is",sec)

def prime(l):
    pl=[]
    for i in l:
        count=0
        for x in range(1,i+1):
            if i%x==0:
                count+=1
        if count==2:
            pl.append(i)
    return pl


l=int(input("Enter the lower limit:"))
u=int(input("Enter the upper limit:"))
x=generate(l,u)
max_secmax(x)
print("The list of prime numbers is",prime(x))
