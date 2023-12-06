'''6. MENU DRIVEN CODE – TUPLES
AIM : To perform the menu options on a tuple of values read as input.
METHODOLOGY: The menu options are displayed. As per the user’s choice, within each of the
menu options, a tuple is read as input and the appropriate functions are called. The first
menu option, reads a tuple of ‘n’ words, calls a function that takes the tuple as parameter
which checks if each word has all the 5 vowels in any case and returns a tuple of such words.
The second menu option reads a nested tuple having height, weight of ‘n’ persons, calls a
function that takes as parameter, each element of the nested tuple, which calculates the BMI
and returns both the BMI and the result as OBESE /OVERWEIGHT/NORMAL/UNDERWEIGHT.
The returned values are displayed in the main function for each person.
Note: The displayed menu should be as follows:
MENU

i) Display words with all vowels
ii) Check BMI
iii) Exit
To check BMI(computed as Kg/m2

) and return OBESE /OVERWEIGHT/NORMAL/UNDERWEIGHT,

use the following data:
BMI >= 30 Obese;
>25 Overweight
18.5 – 25 Normal.
<18.5 – Underweight'''
def display_vowels(t):
    t1=()
    for i in t:
        m=i.lower()
        if 'a' in m and 'e' in m and 'i' in m and 'o' in m and 'u' in m:
            t1+=i,
    return t1
def BMI(t):
    bmi=round(t[1]/(t[0]**2),2)
    if bmi>=30:
        return bmi,'OBESE'
    elif bmi>25:
        return bmi,'OVERWEIGHT'
    if bmi>18.5:
        return bmi,'NORMAL'
    else:
        return bmi,'UNDERWEIGHT'
while True:
    print('''MENU
1. Display words with all vowels
2. Check BMI
3. Exit''')
    ch=int(input('Enter choice :'))
    if ch==3:
        break
    elif ch==1:
        T=()
        n=int(input('Enter number of words :'))
        for k in range(n):
            x=input('Enter word:')
            T+=x,
        t=display_vowels(T)
        if t:
            print('The words are:',t)
        else:
            print('No such words')
    elif ch==2:
        T=()
        n=int(input('Enter number of persons :'))
        for k in range(n):
            print('Enter height of person',k+1,'in metres :',end='')
            h=float(input())
            print('Enter weight of person',k+1,'in kgs:',end='')
            w=float(input())
            t=h,w
            T+=t,
        for j in range(n):
            x,y=BMI(T[j])
            print('BMI of',j+1,'person is:',x)
            print('Your BMI indicates you are:',y)
    else:
        print('Invalid Option')









