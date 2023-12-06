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
