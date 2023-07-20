#This is an Alternate import pickle
def bdelete():
  f=open("BFile.dat","rb")
  sturec=pickle.load(f)
  f.close()
  print(sturec)
  rno=int(input("Enter the roll no of the record to be deleted:"))
  f=open("Bfile.dat","wb")
  rec=[]
  for r in sturec:
    if r[0]==rno:
      continue
    rec.append(r)
  pickle.dump(rec,f)
  f.close()

bdelete()
method
