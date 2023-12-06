def stat(l):
    s=sum(l)
    n=len(l)
    mean=s/n
    m=sorted(l)
    if n%2==0:
        median=(m[int(n/2)]+m[int((n/2)-1)])/2
    else:
        median=m[int((n-1)/2)]
    d={}
    for j in l:
        if j not in d:
            d[j]=0
        else:
            d[j]+=1
    max=0
    for k in d:
        if d[k]>max:
            max=d[k]
    l1=[]
    for k in d:
        if d[k]==max:
            l1+=[k]
    if len(l1)==len(set(l1)):
        mode=['No mode exists as all are unique values']
    else:
        mode=l1
    return mean,median,mode
n=int(input('Enter number of elements :'))
L=[]
for k in range(n):
    L.append(int(input('Enter number')))
a,b,c=stat(L)
print('Mean :',a,'Median:',b,'Mode:',end='')
if len(c)==1:
    print(c[0])
else:
    for j in range(len(c)-1):
        print(c[j],',',end='')
    print(c[-1])
