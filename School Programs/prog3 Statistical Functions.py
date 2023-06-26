n=int(input("Enter the number of terms:"))
l=[]
for i in range(n):
    l.append(int(input("Enter the number:")))
l.sort()

def mean(l):
    s=0
    for i in l:
        s+=i
    return s/len(l)

def mode(l):
    d={}
    for i in l:
        if i not in d:
            d[i]=l.count(i)
    x=d.values()
    z=max(x)
    for i in d:
        if d[i]==z:
            return i

def median(l):
    if len(l)%2==0:
        z=(l[(len(l)//2)-1]+l[(len(l)//2)])/2
        return z
    else:
        return l[((len(l)+1)//2)-1]
    
print("The mean is:",mean(l))
print("The mode is:",mode(l))
print("The median is:",median(l))
