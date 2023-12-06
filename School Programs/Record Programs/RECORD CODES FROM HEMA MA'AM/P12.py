'''12. TEXT FILE 2
AIM: To create a text file with ‘N’ lines of text and perform the operations in the menu
according to the user’s choice
METHODOLOGY: A text file is created by ‘N’ lines of text. A menu is then displayed and the
related operations are performed on the text file, depending on user’s choice.
Note: The menu options to be as follows:
MENU
1. Count the number of words
2. Display Palindrome words
3. Display words starting and ending with a vowel
4. Exit'''
with open('data.txt','w') as f:
    n=int(input('Enter number of lines:'))
    for i in range(n):
        s=input('Enter a line:')
        f.write(s+'\n')
    print('File created successfully')
while True:
    print('''MENU
1. Count the number of words
2. Display Palindrome words
3. Display words starting and ending with a vowel
4. Exit''')
    ch=int(input('Enter option:'))
    if ch==1:
        with open('data.txt','r') as f:
            print('Number of words:',len(f.read().split()))
    elif ch==2:
        flag=0
        with open('data.txt','r') as f:
            for i in f.read().split():
                if i==i[::-1]:
                    print(i)
                    flag=1
        if flag==0:
            print('No palindromes')
    elif ch==3:
        flag=0
        with open('data.txt','r') as f:
            for i in f.read().split():
                m=i.lower()
                if m[0] in 'aeiou' and m[-1] in 'aeiou':
                    print(i)
                    flag=1
        if flag==0:
            print('No such words')
    elif ch==4:
        break
    else:
        print('Invalid option')
'''Enter number of lines:2
Enter a line:Hello guys
Enter a line:malayalam is ooe
File created successfully
MENU
1. Count the number of words
2. Display Palindrome words
3. Display words starting and ending with a vowel
4. Exit
Enter option:1
Number of words: 5
MENU
1. Count the number of words
2. Display Palindrome words
3. Display words starting and ending with a vowel
4. Exit
Enter option:2
malayalam
MENU
1. Count the number of words
2. Display Palindrome words
3. Display words starting and ending with a vowel
4. Exit
Enter option:3
ooe
MENU
1. Count the number of words
2. Display Palindrome words
3. Display words starting and ending with a vowel
4. Exit
Enter option:4
'''
