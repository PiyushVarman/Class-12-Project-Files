def EOReplace(l):
    for i in range(len(l)):
        if l[i]%2==0:
            l[i]+=1
        else:
            l[i]-=1
    print("The modified list is:",l)
L=eval(input("Enter list:"))
EOReplace(L)
