'''3. MENU DRIVEN CODE- NUMERIC
AIM: To write user defined functions and test them with a menu driven code
METHODOLOGY: The factorial computation and generation of Fibonacci series is performed
using 2 user defined functions. A menu is displayed and the user’s choice is accepted. Based
on the choice the appropriate function is executed.

'''
def fac(x):
    f=1
    for i in range(1,x+1):
        f*=i
    print("The factorial of",x,"is",f)

def fibo(x):
    a,b=-1,1
    for i in range(1,x+1):
        print(a+b,end=' ')
        a,b=b,a+b
    print()

while True:
    sel=int(input('''1 - Factorial Generation
2 - Fibonacci Series Generation
3 - Exit'''))

    if sel==1:
        x=int(input("Enter the number to find the factorial:"))
        fac(x)
    elif sel==2:
        x=int(input("Enter the number of fibonacci terms:"))
        fibo(x)
    elif sel==3:
        print("Program terminated.")
        break
