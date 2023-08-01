'''10. USER DEFINED MODULE 2
AIM: To create an user defined module MATRIX to include 2 user defined functions SWAP(),
SORTROWCOL() and import this module in another python code and execute the functions
METHODOLOGY: A module MATRIX is created to include the 2 functions namely SWAP()
which takes a nested list of integers as parameter and swaps the main and secondary
diagonal elements; SORTROWCOL() which takes a nested list of integers as parameter and
sorts each row in ascending order using Bubble sort followed by each column in ascending
order using Insertion sort.
This module is imported in another python code and both the functions are executed with
the outputs displayed in the main function.'''

import MATRIX as mat
l=[]
n=int(input("Enter the number of rows and columns in the square matrix:"))
for i in range(n):
    print("\nRow number",i+1)
    temp=[]
    for j in range(n):
        temp.append(int(input("Enter the number for column "+str(j+1)+":")))
    l.append(temp)
mat.SWAP(l)
mat.SORTROWCOL(l)
