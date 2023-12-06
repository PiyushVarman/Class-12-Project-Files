'''19. PYTHON MYSQL INTERFACE- CSV CREATION
AIM: To create a connectivity and provide an interface between Python, MySQL and create a
CSV file using the contents of the table in MySQL.
METHODOLOGY: The mysql.connector module is imported and the interface between Python
and MySQL is created. The csv module is imported to use the functions for creation and
retrieval of the CSV file. The records of the Student table are written into the Student.CSV
and the contents are displayed in an appropriate format.
Note:
Using the STUDENT table created in the earlier code, transfer all the records into a Student.CSV
and perform the following operations:
i) Display the contents from the CSV file, showing values in each record separated by a comma
ii) Read from the CSV file and display the name of the top scorer.'''
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
'''Output:
Details of all students
1,Ram,460,CS,2005-09-09
2,Manoj,380,BIOLOGY,2005-06-29
3,Seetha,477,COMMERCE,2005-07-12
4,Hari,187,CS,2003-05-15
5,Sriman,397,EG,2005-05-20
Top scorer name
Seetha'''
