count={}
def count_char():
    f=open('math.txt')
    y=f.read().split()
    for i in y:
        j=0
        while j<len(i):
            if i[j] in '+*/-%':
                if j+1<=len(i)-1:
                     if (i[j+1]==i[j]=='/'):
                         if '//' not in count:
                             count['//']=1
                             print('//')
                         else:
                             count['//']+=1
                             print('//')
                         j+=2
                     else:     
                         if i[j] not in count:
                            count[i[j]]=1
                            print(i[j])
                         else:
                            count[i[j]]+=1
                            print(i[j])
            j+=1

count_char()
print(count)
