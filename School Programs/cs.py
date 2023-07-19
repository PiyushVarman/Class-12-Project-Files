import pickle
def bwrite():
  f=open("employee.dat","wb")
  n=input("Would you like to add more details? (y/n)").lower().replace(" ","")
  while n=='y':
    l=[]
    l.append(int(input("Enter the employee number:")))
    l.append(input("Enter the Employee Name:"))
    l.append(input("Enter the designation:"))
    l.append(int(input("Enter the salary:")))
    pickle.dump(l,f)
    n=input("Enter more records? (y/n)")
  f.close()

def bread():
  f=open("employee.dat","rb")
  z=pickle.load()
  print("Employee No.","Employee Name","Designation","Salary",sep="\t")
  for i in z:
    for j in i:
      print(j,end='\t')
    print()
  f.close()

def designationsearch():
  f=open("employee.dat","rb")
  z=pickle.load()
  x=input("Enter the detail to be found

  
      
  
