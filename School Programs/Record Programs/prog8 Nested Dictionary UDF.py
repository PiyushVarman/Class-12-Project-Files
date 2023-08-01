'''AIM: To create a nested dictionary and manipulate the same.
METHODOLOGY: A nested dictionary is created having the main keys to be 3 categories
namely SENIORS, JUNIORS, SUBJUNIORS. For each of these keys, an inner dictionary is
created with keys as BHARATHI, TAGORE, SHIVAJI, PRATAP and values as the score for that
house. The code makes use of an user defined function MAX_SCORE() that takes the
dictionary as parameter and displays the house having maximum score for each category.'''

print("OUTPUT")
def MAX_SCORE(d):
    for i in d:
        chk,chknm=0,''
        for j in d[i].items():
            if j[1]>chk:
                chk=j[1]
                chknm=j[0]
        print("The maximum score was acheived by",chknm,"with",chk,"point(s) in the",i,"category.")
d={}
l=["SENIORS","JUNIORS","SUBJUNIORS"]
h=["BHARATHI","TAGORE","SHIVAJI","PRATAP"]
for i in l:
    x={}
    print("\n",i," Category:",sep='')
    for j in h:
        x[j]=int(input("Enter the scores for "+str(j)+":"))
    d[i]=x

print('\n',d,sep='',end='\n\n')
MAX_SCORE(d)
                
            
            
    
