'''14.BINARY FILE 2'''

print("OUTPUT")
import pickle,os
n=int(input('Enter number of employees:'))
with open('EMPLOYEE.dat','wb') as f:
    for i in range(n):
        name=input('Enter name:')
        age=int(input('Enter age:'))
        dept=input('Enter department:')
        desig=input('Enter designation:')
        sal=int(input('Enter salary:'))
        d={'Name':name,'Age':age,'Department':dept,'Designation':desig,'Salary':sal}
        pickle.dump(d,f)
while True:
    print('''MENU
1. Display details of Managers earning more than 50000 in Finance and in Admin Dept.
2. Delete the employee details who have reached retirement age(58 years)
3. Exit''')
    ch=int(input('Enter option:'))
    if ch==1:
        with open('EMPLOYEE.dat','rb') as f:
            flag=0
            try:
                while True:
                    d=pickle.load(f)
                    if d['Designation'].lower()=='manager' and d['Salary']>50000 and (d['Department'].lower() in ['admin','finance']):
                        print('Name',d['Name'],'Age',d['Age'],'Department',d['Department'],'Designtion',d['Designation'],'Salary',d['Salary'])
                        flag=1
            except EOFError:
                if flag==0:
                    print('No match found')
    elif ch==2:
        with open('EMPLOYEE.dat','rb') as f, open('TEmp.dat','wb') as f1:
            flag=0
            try:
                while True:
                    d=pickle.load(f)
                    if d['Age']<58:
                        pickle.dump(d,f1)
            except EOFError:pass
        os.remove('EMPLOYEE.dat')
        os.rename('TEmp.dat','EMPLOYEE.dat')
        print('Modified file is:')
        with open('EMPLOYEE.dat','rb') as f:
            try:
                while True:
                    d=pickle.load(f)
                    for i in d:
                        print(i,d[i])
            except:pass
    elif ch==3:
        print('Program Terminated.')
        break
    else:
        print('Invalid option')
'''OUTPUT
Enter number of employees:2
Enter name:Ram
Enter age:23
Enter department:Finance
Enter designation:Manager
Enter salary:60000
Enter name:Hari
Enter age:60
Enter department:Finance
Enter designation:Manager
Enter salary:45000
MENU
1. Display details of Managers earning more than 50000 in Finance and in Admin Dept.
2. Delete the employee details who have reached retirement age(58 years)
3. Exit
Enter option:1
Name Ram Age 23 Department Finance Designtion Manager Salary 60000
MENU
1. Display details of Managers earning more than 50000 in Finance and in Admin Dept.
2. Delete the employee details who have reached retirement age(58 years)
3. Exit
Enter option:2
Modified file is:
Name Ram
Age 23
Department Finance
Designation Manager
Salary 60000
MENU
1. Display details of Managers earning more than 50000 in Finance and in Admin Dept.
2. Delete the employee details who have reached retirement age(58 years)
3. Exit
Enter option:3
Program Terminated.

EMPLOYEE.dat

€•U       }”(ŒName”ŒRam”ŒAge”KŒ
Department”ŒFinance”ŒDesignation”ŒManager”ŒSalary”M`êu.


'''
                    
                        
