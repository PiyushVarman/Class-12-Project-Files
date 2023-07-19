import pickle
def bwrite():
  f=open("employee.dat","ab")
  n='y'
  while n[0]=='y':
    l=[]
    l.append(int(input("Enter the employee number:")))
    l.append(input("Enter the Employee Name:"))
    l.append(input("Enter the designation:"))
    l.append(int(input("Enter the salary:")))
    pickle.dump(l,f)
    n=input("Enter more records? (y/n)").lower()
  f.close()

def bread():
  f=open("employee.dat","rb")
  print("Employee No.","Employee Name","Designation","Salary",sep="\t")
  while True:
    try:
      z=pickle.load(f)
      for i in z:
        print(i,end='\t\t')
      print()
    except:
      break
  f.close()

def designationsearch():
  f=open("employee.dat","rb")
  z=pickle.load(f)
  x=input("Enter the designation to be found:").lower().replace(" ","")
  l=[]
  found=0
  for i in z:
    if z[2].lower()==x:
      l.append(i)
      found=1
  if found==1:
    print("Employee No.","Employee Name","Designation","Salary",sep="\t")
    for i in l:
      print(i,end='\t\t')
    print()
  else:
    print("No employee with such designation exists.")
  f.close()
  
def IDsearch():
  f=open("employee.dat","rb")
  z=pickle.load(f)
  x=int(input("Enter the employee ID to be found:"))
  l=[]
  found=0
  for i in z:
    if z[0]==x:
      l.append(i)
      found=1
  if found==1:
     print("Employee No.","Employee Name","Designation","Salary",sep="\t")
     for i in l:
       print(i,end='\t\t')
     print()
  else:
    print("No employee with such number exists.")
  f.close()

def updateemployee():
  bread()
  f=open("employee.dat","rb+")
  x=int(input("Enter the employee ID to be updated:"))
  z=pickle.load(f)
  l=[]
  found=0
  for i in z:
    if i[0]==x:
      print("Current record",i)
      i[1]=input("Enter the employee name:")
      i[2]=input("Enter the designation:")
      i[3]=int(input("Enter the salary details:"))
      found=1
      break
  if found==1:
    pickle.dump(z,f)
    bread()
  else:
    print("No employee with such number exists.")
  f.close()

def delemployee():
  bread()
  f=open("employee.dat","rb+")
  x=int(input("Enter the employee ID to be updated:"))
  z=pickle.load(f)
  l=[]
  found=0
  for i in z:
    if i[0]==x:
      continue
      found=1
    else:
      l.append(i)
  if found==1:
    pickle.dump(l,f)
    bread()
  else:
    print("No employee with such number exists.")
  f.close()

while True:  
  sel=int(input('''1 - Enter Records
2 - Display Records
3 - Search Records (Designation)
4 - Search Records (ID)
5 - Update Employee Details
6 - Delete Employee
7 - Exit
Choose your Option:'''))

  if sel==1:
    bwrite()

  elif sel==2:
    bread()

  elif sel==3:
    designationsearch()

  elif sel==4:
    IDsearch()

  elif sel==5:
    updateemployee()

  elif sel==6:
    delemployee()

  elif sel==7:
    break
