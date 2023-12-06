'''20. PYTHON- MYSQL CONNECTIVITY FOR JOINS
AIM: To create a connectivity and provide an interface between Python and MySQL to
perform join operations on 2 tables
METHODOLOGY: The mysql.connector module is imported and the interface between Python
and MySQL is created. Using the DDL, DML commands the Employee and Department tables
are created. A query is then executed to join the tables and display the output in the desired
format
Note:
Create Employee table (Empno, Name, Desig, Deptno, Salary) and Department table(Deptno,
Dname, Location) with appropriate number of records. Execute a query to display details of all
Mangers like Empno, Name, Salary, Dname and Location.'''
import mysql.connector as mc
cn=mc.connect(host='localhost',password='MySQL@12345',username='root')
cr=cn.cursor()
cr.execute('Create database if not exists record')
cr.execute('Use record')
cr.execute("Create table if not exists Employee(Empno integer Primary Key,\
Name varchar(30), Desig varchar(30), Deptno integer, Salary integer)")
cr.execute("Create table if not exists table1(Deptno integer, Dname varchar(30), Location varchar(60))")
cr.execute('Select * from Employee')
res=cr.fetchall()
if cr.rowcount==0:
    cr.execute("Insert into employee values(1,'Ram','Admin',100,50000)")
    cr.execute("Insert into employee values(2,'Manoj','Manager',101,60000)")
    cr.execute("Insert into employee values(3,'Seetha','Manager',102,45000)")
    cr.execute("Insert into employee values(4,'Hari','Financier',101,56000)")
    cr.execute("Insert into employee values(5,'Sriman','Admin',100,57000)")
    cn.commit()
cr.execute('Select * from table1')
res=cr.fetchall()
if cr.rowcount==0:
    cr.execute("Insert into table1 values(100,'IT','Block A')")
    cr.execute("Insert into table1 values(101,'Think Tank','Block A')")
    cr.execute("Insert into table1 values(102,'Sales','Block C')")
    cr.execute("Insert into table1 values(103,'HR','Block B')")
    cn.commit()
cr.execute('Select * from employee e,table1 t where e.deptno=t.deptno')
res=cr.fetchall()
print('Joined tables')
for i in res:
    for j in i:
        print(j,end=' ')
    print()
cr.execute("Select Empno,Name, Salary, Dname, Location from employee e,table1 t where e.deptno=t.deptno and desig='Manager'")
res=cr.fetchall()
print('Details of all managers')
for i in res:
    for j in i:
        print(j,end=' ')
    print()
cn.close()
'''Output:
Joined tables
1 Ram Admin 100 50000 100 IT Block A 
2 Manoj Manager 101 60000 101 Think Tank Block A 
3 Seetha Manager 102 45000 102 Sales Block C 
4 Hari Financier 101 56000 101 Think Tank Block A 
5 Sriman Admin 100 57000 100 IT Block A 
Details of all managers
2 Manoj 60000 Think Tank Block A 
3 Seetha 45000 Sales Block C '''








