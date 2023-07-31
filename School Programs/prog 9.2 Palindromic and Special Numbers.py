'''9. USER DEFINED MODULE – 1
AIM: To create an user defined module NUMBER to include 2 user defined functions
PALINDROME(), SPECIAL() and import this module in another python code and execute the
functions
METHODOLOGY: A module NUMBER is created to include the 2 functions namely
PALINDROME() which takes a number as parameter and returns 1 if it’s a palindrome and -1
otherwise; SPECIAL() which takes a number as parameter and returns 1 if it’s a special
number and -1 otherwise.
This module is imported in another python code and both the functions are executed. For the
PALINDROME() function, a tuple of integers are read and the code displays all the palindrome
numbers in the tuple. If there weren’t any palindrome numbers appropriate message is
shown. For the SPECIAL() function 2 limits are read and all the special numbers between
these limits are generated. If there were no special numbers, appropriate message is shown.
''''
import NUMBER as n
print("OUTPUT")
n.special(140,146)
n.palindrome((1,15))
