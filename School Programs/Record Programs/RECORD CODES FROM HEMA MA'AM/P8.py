'''8. NESTED DICTIONARY
AIM: To create a nested dictionary and manipulate the same.
METHODOLOGY: A nested dictionary is created having the main keys to be 3 categories
namely SENIORS, JUNIORS, SUBJUNIORS. For each of these keys, an inner dictionary is
created with keys as BHARATHI, TAGORE, SHIVAJI, PRATAP and values as the score for that
house. The code makes use of an user defined function MAX_SCORE() that takes the
dictionary as parameter and displays the house having maximum score for each category.
Note: Strictly follow the uppercase for all the keys as mentioned above.'''
def MAX_SCORE(d):
    for j in d:
        max=0
        house=''
        for k in d[j]:
            if d[j][k]>max:
                max=d[j][k]
                house=k
        print('The house with maximum score in',j,'category is',house,'with',max,'points')
d={'SENIORS':None,'JUNIORS':None,'SUBJUNIORS':None}
for j in d:
    print('Enter score for Bharati house in',j,'category:',end='')
    B=int(input())
    print('Enter score for Tagore house in',j,'category:',end='')
    T=int(input())
    print('Enter score for Shivaji house in',j,'category:',end='')
    S=int(input())
    print('Enter score for Pratap house in',j,'category:',end='')
    P=int(input())
    d[j]={'BHARATI':B,'TAGORE':T,'SHIVAJI':S,'PRATAP':P}
MAX_SCORE(d)
'''OUTPUT
Enter score for Bharati house in SENIORS category:20
Enter score for Tagore house in SENIORS category:19
Enter score for Shivaji house in SENIORS category:28
Enter score for Pratap house in SENIORS category:12
Enter score for Bharati house in JUNIORS category:17
Enter score for Tagore house in JUNIORS category:19
Enter score for Shivaji house in JUNIORS category:20
Enter score for Pratap house in JUNIORS category:23
Enter score for Bharati house in SUBJUNIORS category:19
Enter score for Tagore house in SUBJUNIORS category:10
Enter score for Shivaji house in SUBJUNIORS category:24
Enter score for Pratap house in SUBJUNIORS category:5
The house with maximum score in SENIORS category is SHIVAJI with 28 points
The house with maximum score in JUNIORS category is PRATAP with 23 points
The house with maximum score in SUBJUNIORS category is SHIVAJI with 24 points'''
