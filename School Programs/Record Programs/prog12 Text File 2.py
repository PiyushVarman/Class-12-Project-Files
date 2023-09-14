'''12. TEXT FILE 2
AIM: To create a text file with ‘N’ lines of text and perform the operations in the menu
according to the user’s choice
METHODOLOGY: A text file is created by ‘N’ lines of text. A menu is then displayed and the
related operations are performed on the text file, depending on user’s choice.'''

f=open("tf2.txt","a+")
chk='y'
l=[]
while chk[0]=='y':
    l.append(input("Enter the line to enter in the list:")+'\n')
    chk=input("Would you like to continue? (y/n)")
f.writelines(l)
f.close()

def wordcount():
    f=open("tf2.txt","r+")
    count=0
    l=f.readlines()
    for i in l:
        x=i.split()
        count+=len(x)
    print(count)
    f.close()

def wordpal():
    f=open("tf2.txt","r+")
    l=f.readlines()
    for i in l:
        x=i.split()
        for j in x:
            if j.lower()==j.lower()[::-1]:
                print(j,"is a palindrome")
    f.close()

def vowelword():
    f=open("tf2.txt","r+")
    l=f.readlines()
    for i in l:
        x=i.split()
        for j in x:
            if j[0].lower() in 'aeiou' and j[-1].lower() in 'aeiou':
                print(j,"is a vowel word")
    f.close()

while True:
    sel=int(input('''\n1- Count the number of words
2- Display palindromic words
3- Display words starting and ending with vowels
4- Exit
Choose your option:'''))
    if sel==1:
        wordcount()
    elif sel==2:
        wordpal()
    elif sel==3:
        vowelword()
    elif sel==4:
        print("Program terminated.")
        break
