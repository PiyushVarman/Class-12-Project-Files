'''11. TEXT FILE 1'''
with open('data.txt','w') as f:
    while True:
        s=input('Enter a line:')
        f.write(s+'\n')
        ch=input('Do you wish to continue?(Y/N):')
        if ch.upper()=='N':
            print('File created successfully.')
            break
while True:
    ch=int(input('''\n1- Display number of lines
2- Copy the words containing ‘U’ into another file and display the new file
3- Convert the case of the letters(lower to upper and vice versa) in the original text file and
display the contents
4- Exit
Select your option:'''))
    if ch==1:
        with open('data.txt','r') as f:
            print('Number of lines:',len(f.readlines()))
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
        print("Program Terminated.")
        break
    else:
        print('Invalid option.')


'''Enter a line:Hello World
Do you wish to continue?(Y/N):y
Enter a line:Ubuntu is an OS
Do you wish to continue?(Y/N):y
Enter a line:Welcome to Earth
Do you wish to continue?(Y/N):n
File created successfully.

1- Display number of lines
2- Copy the words containing ‘U’ into another file and display the new file
3- Convert the case of the letters(lower to upper and vice versa) in the original text file and
display the contents
4- Exit
Select your option:1
Number of lines: 3

1- Display number of lines
2- Copy the words containing ‘U’ into another file and display the new file
3- Convert the case of the letters(lower to upper and vice versa) in the original text file and
display the contents
4- Exit
Select your option:2
Words containing U
Ubuntu

1- Display number of lines
2- Copy the words containing ‘U’ into another file and display the new file
3- Convert the case of the letters(lower to upper and vice versa) in the original text file and
display the contents
4- Exit
Select your option:3
hELLO wORLD
uBUNTU IS AN os
wELCOME TO eARTH

1- Display number of lines
2- Copy the words containing ‘U’ into another file and display the new file
3- Convert the case of the letters(lower to upper and vice versa) in the original text file and
display the contents
4- Exit
Select your option:4
Program Terminated.
'''





