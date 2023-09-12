'''11. TEXT FILE 1
AIM: To create a text file with contents entered by the user as long as the user wishes to and
perform the operations in the menu according to the user’s choice
METHODOLOGY: A text file is created by reading one line at a time and asking is the user
wants to input more lines with a Y/N choice. A menu is then displayed and the related
operations are performed on the text file, depending on user’s choice.'''

f=open("textfile.txt","a")
l=[]
chk='y'
c=0
while chk[0]=='y':
    l.append(input("Enter the line to be inputted in the file:")+"\n")
    chk=input("enter choice:").strip().lower()
else:
    f.writelines(l)
    f.close()
    
def lenwords():
    f=open("textfile.txt","r")
    print(len(f.readlines()))
    f.close()
    
def copywords():
    f=open("textfile.txt","r+")
    l=f.readlines()
    z=[]
    for i in l:
        for x in i.split():
            if 'u' in x:
                z.append(x+'\n')     
    p=open("utextfile.txt","r+")
    p.writelines(z)
    p.seek(0)
    print(p.read())

def casewords():
    f=open("textfile.txt","r+")
    l=f.readlines()
    for i in range(len(l)):
        l[i]=l[i].swapcase()
    f.seek(0)
    f.writelines(l)
    f.seek(0)
    print("The Modified file is:\n",f.read())
    
while True:
    sel=int(input('''1- Display Number of lines
2- Copy words
3- Convert Case of letters
4- Exit
Choose your option:'''))
    
    if sel==1:
        lenwords()
    elif sel==2:
        copywords()
    elif sel==3:
        casewords()
    elif sel==4:
        print("Program terminated.")
        break
