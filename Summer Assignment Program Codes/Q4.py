def pattern(n):
    z,p=65,1
    for i in range(1,n+1):
        count=i
        if i%2==0:
            k="*"
        else:
            k="#"
        z+=2*count
        while count>=1:
            print(chr(z-2),end='')
            count-=1
            print(k,end='')
            z-=2
        print(str(p))
        p+=2
pattern(int(input()))
