def vcount(): #Counting the number of vowels in a given file
    f=open("proverb.txt")
    count=0
    x=f.read()
    for i in x.lower():
        if i in 'aeiou':
            count+=1
    print("The number of vowels in the text file is",count,".")
    f.close()

def aprint(): #Printing all the sentences that start with 'A'
    f=open("proverb.txt")
    x=f.readlines()
    for i in x:
        if i[0]=='A':
            print(i)
    f.close()

def findthethis(): #Print the number of occurances of "the" and "this"
    f=open("proverb.txt")
    count=0
    x=((f.read()).lower()).split()
    for i in x:
        if i=='the' or i=='this':
            count+=1
    print("The number of occurances of 'The' and 'This' is",count,".")
    f.close()

def uppercopy(): #Copy all the text from one file to another, in uppercase.
    f=open("proverb.txt")
    x=open('uppercase.txt','w')
    z=(f.read()).upper()
    x.write(z)
    f.close()
    x.close()

def wordpal(): #Write all the words that are palindromes in another file.
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
