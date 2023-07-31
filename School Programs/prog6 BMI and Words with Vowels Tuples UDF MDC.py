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
'''
print("OUTPUT")
def vowelword(n):
    t=()
    for i in n:
        vcount=0
        for j in "aeiou":
            if j in i.lower():
                vcount+=1
        if vcount>=5:
            t+=(i,)
    return t

def BMI(x):
    for i in x:
        print(i,end=' - ')
        if i>=30:
            print("Obese")
        elif i>25:
            print("Overweight")
        elif i>=18.5:
            print("Normal")
        else:
            print("Underweight")
    
            
while True:
    sel=int(input('''1 - Enter the tuple of words
2 - BMI Scale
3 - Exit
Choose your option:'''))

    if sel==1:
        x=eval(input("Enter the tuple of words:"))
        print("The tuple of words is:",vowelword(x))
    elif sel==2:
        x=eval(input("Enter a tuple of weights:"))
        BMI(x)
    else:
        print("Program Terminated...")
        break
