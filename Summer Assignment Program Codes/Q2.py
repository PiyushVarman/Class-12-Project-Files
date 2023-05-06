def pal(a):
    z=str(a)
    return z==z[::-1]
s=int(input("Enter the number:"))
x=pal(s)
if x:
    print(s,"is a palindrome.")
else:
    print(s,"is not a palindrome.")
