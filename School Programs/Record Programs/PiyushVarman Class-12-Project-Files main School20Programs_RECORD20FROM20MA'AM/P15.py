print("OUTPUT")
import csv
fc=open('GST.CSV','w',newline='')
w=csv.writer(fc)
w.writerows([['CATEGORY','GST_PERCENTAGE'],['AUTOMOBILES',25],['Stationary',12],['Chocolates',10],['Dairy',3]])
fc.close()
N=int(input('Enter number of items:'))
f=open('ITEMS.CSV','w',newline='')
w=csv.writer(f)
w.writerow(['ItemID','Name','Category','Unitprice','Finalprice'])
for i in range(N):
    ID=input('Enter Item ID:')
    na=input('Enter Name:')
    flag=0
    while flag==0:
        with open('GST.CSV','r') as f1:
            ca=input('Enter category:')
            rr=csv.reader(f1)
            for i in rr:
                if i[0]!='CATEGORY':
                    if i[0].lower()==ca.lower():
                        flag=1
                        pr=int(i[1])
                        break
            else:
                print('Invalid category, try again')
    un=int(input('Enter unit price:'))
    fin=un+un*pr*0.01
    w.writerow([ID,na,ca,un,fin])
f.close()
f2=open('ITEMS.CSV','r')
r=csv.reader(f2)
for i in r:
    print(i[0],i[1],i[2],i[3],i[4],sep='  ')

'''OUTPUT
Enter number of items:4
Enter Item ID:001
Enter Name:Innova
Enter category:Automobiles
Enter unit price:200000
Enter Item ID:002
Enter Name:Hauser Inky
Enter category:Stationary
Enter unit price:20
Enter Item ID:003
Enter Name:Eclairs
Enter category:Chocolates
Enter unit price:5
Enter Item ID:004
Enter Name:MilkyMist Cheese
Enter category:Dairy
Enter unit price:50
ItemID  Name  Category  Unitprice  Finalprice
001  Innova  Automobiles  200000  250000.0
002  Hauser Inky  Stationary  20  22.4
003  Eclairs  Chocolates  5  5.5
004  MilkyMist Cheese  Dairy  50  51.5
'''
