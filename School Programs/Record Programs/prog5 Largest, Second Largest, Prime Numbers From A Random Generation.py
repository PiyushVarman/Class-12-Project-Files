'''
5. LARGEST, SECOND LARGEST, PRIME NUMBERS FROM A RANDOM GENERATION
AIM: To find the largest, second largest and the prime numbers from a list of randomly
generated integers
METHODOLOGY: The lower and upper limits are read as inputs. Three user defined functions
are written to do the required operations namely i)to generate the random numbers
between the given limits ii) to find the largest, second largest number in the generated list
and iii) to store the prime numbers in a local list and print them else print a message stating
'No prime numbers in the generated list'.
'''
import random
print("OUTPUT")
def generate(l,u):
    rl=[]
    for i in range(l,u+1):
        rl.append(random.randint(l,i))
    return rl

def max_secmax(l):
    large=l[0]
    print(l)
    n=len(l)
    for i in range(n):
        if l[i]>large:
            large=l[i]
    for i in range(n):
        if l[i]!=large:
            sec=l[i]
            break
    for i in range(n):
        if l[i]!=large and l[i]>sec:
            sec=l[i]
    print("The largest number is",large)
    print("The second largest number is",sec)

def prime(l):
    pl=[]
    for i in l:
        count=0
        for x in range(1,i+1):
            if i%x==0:
                count+=1
        if count==2:
            pl.append(i)
    return pl


l=int(input("Enter the lower limit:"))
u=int(input("Enter the upper limit:"))
x=generate(l,u)
max_secmax(x)
if len(prime(x))==0:
    print("No prime numbers in the generated list.")
else:
    print("The list of prime numbers is",prime(x))
