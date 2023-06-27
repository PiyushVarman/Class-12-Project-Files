def vcount():
    f=open("proverb.txt")
    count=0
    x=f.read()
    for i in x.lower():
        if i in 'aeiou':
            count+=1
    print("The number of vowels in the text file is",count,".")
    f.close()

def aprint():
    f=open("proverb.txt")
    x=f.read()
    if x[0]=='A':
        print(x)
    f.close()

def findthethis():
    f=open("proverb.txt")
    count=0
    x=((f.read()).lower()).split()
    for i in x:
        if i=='the' or i=='this':
            count+=1
    print("The number of occurances of 'The' and 'This' is",count,".")
    f.close()

def uppercopy():
    f=open("proverb.txt")
    x=open('uppercase.txt','w')
    z=(f.read()).upper()
    x.write(z)
    f.close()
    x.close()

def wordpal():
    f=open("proverb.txt")
    x=open("abc.txt",'w')
    z=(f.read()).lower()
    y=z.split()
    wp=[]
    for i in y:
        if i==i[::-1]:
            wp.append(i+'\n')
    x.writelines(wp)
    f.close()
    x.close()

vcount()
aprint()
findthethis()
uppercopy()
wordpal()
