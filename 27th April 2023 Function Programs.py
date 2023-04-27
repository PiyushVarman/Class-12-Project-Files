#WAP to make 2 lists, one having list elements div by 2 and the other div by 5
def div_list(a):
    d2,d5=[],[]
    for i in a:
        if i%2==0:
            d2.append(i)
        if i%5==0:
            d5.append(i)
    return d2,d5
x=eval(input())
print("The lists are:",div_list(x))

#WAP to accept a tuple of strings and count no. of occurances.
def count(x):
    d={}
    for i in x:
        for j in i:
            if j not in d:
                d[j]=1
            else:
                d[j]+=1
    return d
x=eval(input())
print("The count is:",count(x))
