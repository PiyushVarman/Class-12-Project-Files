import mysql.connector
m=mysql.connector.connect(host='localhost',database='dav',user='root',password='MySQL@12345')
if m.is_connected():
    print("hi")
mc=m.cursor()
print("Class 12C of 2023:")
mc.execute('select * from sample')
data=mc.fetchall()
print("The number of students and their data here is:",mc.rowcount) #Counts the number of rows
for i in data:
    print(i)
mc.execute('insert into pcv values (3,"Piyush CV")')
m.commit()
m.rollback()
