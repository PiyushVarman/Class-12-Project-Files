'''11. TEXT FILE 1
AIM: To create a text file with contents entered by the user as long as the user wishes to and
perform the operations in the menu according to the user’s choice
METHODOLOGY: A text file is created by reading one line at a time and asking is the user
wants to input more lines with a Y/N choice. A menu is then displayed and the related
operations are performed on the text file, depending on user’s choice.
Note: The menu options to be as follows:
MENU
1. Display number of lines
2. Copy the words containing ‘U’ into another file and display the new file
3. Convert the case of the letters(lower to upper and vice versa) in the original text file and
display the contents
4. Exit'''
with open('data.txt','w') as f:
    while True:
        s=input('Enter a line:')
        f.write(s+'\n')
        ch=input('Do you wish to continue?(Y/N)')
        if ch.upper()=='N':
            print('File created successfully')
            break
while True:
    print('''MENU
1. Display number of lines
2. Copy the words containing ‘U’ into another file and display the new file
3. Convert the case of the letters(lower to upper and vice versa) in the original text file and
display the contents
4. Exit''')
    ch=int(input('Enter option:'))
    if ch==1:
        with open('data.txt','r') as f:
            print('Number of lines',len(f.readlines()))
    elif ch==2:
        with open('data.txt','r') as f,open('new.txt','w') as f1:
            s=f.readline()
            while s:
                for k in s.split():
                    if 'U' in k:
                        f1.write(k+'\n')
                s=f.readline()
        with open('new.txt','r') as f1:
            print('Words containing U')
            for i in f1.readlines():
                print(i,end='')
    elif ch==3:
        with open('data.txt','r') as f:
            s=f.readline()
            while s:
                print(s.swapcase(),end='')
                s=f.readline()
    elif ch==4:
        break
    else:
        print('Invalid option')
'''OUTPUT:
Enter a line:Hello World
Do you wish to continue?(Y/N)Y
Enter a line:Ubuntu is good
Do you wish to continue?(Y/N)Y
Enter a line:How are U?
Do you wish to continue?(Y/N)N
File created successfully
MENU
1. Display number of lines
2. Copy the words containing ‘U’ into another file and display the new file
3. Convert the case of the letters(lower to upper and vice versa) in the original text file and
display the contents
4. Exit
Enter option:3
hELLO wORLD
uBUNTU IS GOOD
hOW ARE u?
MENU
1. Display number of lines
2. Copy the words containing ‘U’ into another file and display the new file
3. Convert the case of the letters(lower to upper and vice versa) in the original text file and
display the contents
4. Exit
Enter option:4








