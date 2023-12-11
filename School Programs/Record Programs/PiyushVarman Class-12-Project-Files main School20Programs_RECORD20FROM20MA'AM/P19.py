'''19. PYTHON MYSQL INTERFACE- CSV CREATION'''

print("OUTPUT")
import mysql.connector as mc
import csv
f=open('Student.csv','w',newline='')
wr=csv.writer(f)
cn=mc.connect(host='localhost',password='MySQL@12345',username='root')
cr=cn.cursor()
cr.execute('Create database if not exists record')
cr.execute('Use record')
cr.execute("Create table if not exists STUDENT(ROLL integer Primary Key,\
NAME varchar(30), TOTAL integer, COURSE varchar(20) CHECK(COURSE in\
('CS', 'BIOLOGY', 'COMMERCE', 'EG')), DOB DATE)")
cr.execute('Select * from student')
res=cr.fetchall()
for i in res:
    wr.writerow(i)
f.close()
print('Details of all students')
f=open('Student.csv','r')
rr=csv.reader(f)
for i in rr:
    print(i[0],i[1],i[2],i[3],i[4],sep=',')
marks=[]
f.close()
f=open('Student.csv','r')
rr=csv.reader(f)
print('Top scorer name')
for i in range(len(res)):
    marks.append(int(res[i][2]))
maxm=max(marks)
for i in rr:
    if int(i[2])==maxm:
        print(i[1])
f.close()
'''OUTPUT
Details of all students
1,Ram,460,CS,2005-09-09
2,Manoj,380,BIOLOGY,2005-06-29
3,Seetha,477,COMMERCE,2005-07-12
4,Hari,187,CS,2003-05-15
5,Sriman,397,EG,2005-05-20
Top scorer name
Seetha'''
