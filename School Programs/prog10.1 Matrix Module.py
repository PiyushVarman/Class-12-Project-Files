def matprint(l):
    print()
    for i in range(len(l)):
        for j in range(len(l[i])):
            print(l[i][j],end=' ')
        print()
    print()
def SWAP(l):
    print("\nThe Matrix you have entered is:")
    matprint(l)
    for i in range(len(l)):
        x1,y1,x2,y2=0,0,0,0
        temp1,temp2=0,0
        for j in range(len(l[i])):
            if i==j:
                temp1=l[i][j]
                x1,y1=i,j
            if i+j==2:
                temp2=l[i][j]
                x2,y2=i,j
        l[x2][y2]=temp1
        l[x1][y1]=temp2
    print("The modified Matrix is:")
    matprint(l)
def SORTROWCOL(l):
    for i in range(len(l)):
        for j in range(len(l[i])):
            for z in range(j,len(l[i])):
                if l[i][j]>l[i][z]:
                    l[i][j],l[i][z]=l[i][z],l[i][j]
    print("The Matrix sorted by rows is:")
    matprint(l)
    
    for i in range(len(l)):
        for j in range(len(l[i])):
            for z in range(j,len(l[i])):
                if l[j][i]>l[z][i]:
                    l[j][i],l[z][i]=l[z][i],l[j][i]
    print("The Matrix sorted by columns is:")
    matprint(l)
