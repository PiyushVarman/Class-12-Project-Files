#Started 27th December 2023
#Last Edit- 31st December 2023

from tkinter import *
import mysql.connector
from tkinter import messagebox
m=mysql.connector.connect(host='localhost',password='mysql123',user='root')
mc=m.cursor()
mc.execute("create database if not exists loginpw;")
mc.execute("use loginpw;")
mc.execute("create table if not exists details(mail_id varchar(100) primary key, password varchar(100));")
mc.execute("create table if not exists items(mail_id varchar(100), item_name varchar(100), item_category varchar(100), qty int, price float);")

def addi(un):
    add=Toplevel(root)
    add.geometry("480x330")
    add.title('Add Item')
    def additem(un):
        itna=a1.get()
        itca=a2.get()
        qty=a3.get()
        pr=a4.get()
        if itna.isalnum() and itca.isalnum(): 
            if qty.isnumeric() and type(eval(pr))==float or type(eval(pr))==int:
                query='insert into items values("'+un+'","'+itna+'","'+itca+'",'+qty+','+pr+');'
                mc.execute(query)
                messagebox.showinfo("Success!",itna+" has been added successfully!")
                m.commit()
            else:
                messagebox.showerror('Error!','The Quantity and Price must\nbe integers or float values.')
        else:
            messagebox.showerror('Error!','The fields cannot be empty.')

    l1=Label(add,text='Item Name',font=("Consolas",15,"bold"))
    l1.grid(row=0,column=0,padx=20,pady=20)
    l2=Label(add,text='Item Category',font=("Consolas",15,"bold"))
    l2.grid(row=1,column=0,padx=20,pady=20)
    l3=Label(add,text='Quantity',font=("Consolas",15,"bold"))
    l3.grid(row=2,column=0,padx=20,pady=20)
    l4=Label(add,text='Price',font=("Consolas",15,"bold"))
    l4.grid(row=3,column=0,padx=20,pady=20)
    a1=Entry(add,width=20,font=("Consolas",15,"bold"))
    a1.configure(justify='center')
    a2=Entry(add,width=20,font=("Consolas",15,"bold"))
    a2.configure(justify='center')
    a3=Entry(add,width=20,font=("Consolas",15,"bold"))
    a3.configure(justify='center')
    a4=Entry(add,width=20,font=("Consolas",15,"bold"))
    a4.configure(justify='center')
    a1.grid(row=0,column=1,padx=20,pady=20)
    a2.grid(row=1,column=1,padx=20,pady=20)
    a3.grid(row=2,column=1,padx=20,pady=20)
    a4.grid(row=3,column=1,padx=20,pady=20)
    b=Button(add,text='Add Item',font=("Consolas",15,"bold"),command=lambda: additem(un))
    b.grid(row=4,column=1)
    add.resizable(False,False)
    add.mainloop()

def delete(un):
    d=Toplevel(root)
    d.geometry("375x230")
    d.title('Delete Item')
    def deleteitem(un):
        itna=d1.get()
        if itna.isalnum():
            x='select item_name from items where mail_id="'+un+'";'
            mc.execute(x)
            z=mc.fetchall()
            cnt=0
            for i in z:
                for x in i:
                    if itna.strip()==x.lower():
                        cnt=1
                        break
            if cnt==1:
                query="delete from items where item_name ='"+itna.strip()+"' and mail_id='"+un+"';"
                mc.execute(query)
                messagebox.showinfo("Success!",itna+" has been deleted successfully!")
                m.commit()
            else:
                messagebox.showerror("Error!","The Item does not exist.")
        else:
            messagebox.showerror('Error!','The field cannot be empty.')
    dl1=Label(d,text='Enter item name to be deleted:',font=("Consolas",15,"bold"))
    dl1.grid(row=0,column=0,padx=20,pady=20)
    d1=Entry(d,width=20,font=("Consolas",15,"bold"))
    d1.configure(justify='center')
    d1.grid(row=1,column=0,pady=20)
    d2=Button(d,text='Delete Item',font=("Consolas",15,"bold"),command=lambda: deleteitem(un))
    d2.grid(row=2,column=0)
    d.resizable(False,False)
    d.mainloop()

def main(un): 
    global inv
    inv=Toplevel(root)
    inv.attributes('-fullscreen',True)
    def show(un):
        invdetail=Text(inv,height=15,width=50,font=("Calibri",25,"bold"))
        invdetail.place(x=683,y=400,anchor=CENTER)
        invdetail.delete("1.0","end")
        query='select item_name, item_category, qty, price from items where mail_id= "'+un+'";'
        mc.execute(query)
        z=mc.fetchall()
        print(z)
        invdetail.insert(INSERT,(('Item','Category',"Quantity","Price")))
        invdetail.insert(INSERT,'\n\n')
        invdetail.tag_configure("tag_name", justify='center')
        for i in z:
            invdetail.insert(INSERT,i)
            invdetail.insert(INSERT,'\n')
        invdetail.tag_add("tag_name", "1.0", "end")    
        invdetail.config(state= DISABLED)
        messagebox.showinfo('Success!','Inventory Established.')
        m.commit()
    bl=Label(inv,text='Inventory',bg='sky blue',fg='white',font=('Georgia',50,'italic'))
    bl.place(x=683,y=50,anchor=CENTER)
    a=Button(inv,text='Add',font=("Consolas",15,"bold"),command= lambda:addi(un),fg='green')
    a.place(x=680,y=730,anchor=CENTER)
    d=Button(inv,text='Delete',font=("Consolas",15,"bold"),command= lambda:delete(un),fg='red')
    d.place(x=830,y=730,anchor=CENTER)
    s=Button(inv,text='Show',font=("Consolas",15,"bold"),command= lambda:show(un))
    s.place(x=530,y=730,anchor=CENTER)
    inv.config(bg='sky blue')  
    inv.title('Inventory')
    inv.mainloop()

def register():
    un=str(e1.get())
    pw=str(e2.get())
    mc.execute('select * from details;')
    z=mc.fetchall()
    flag=0
    for i in z:
        if un in i:
            flag=1
            break
    if flag==0:
        if un.isspace() == False and pw.isalnum():
            query="insert into details values ('"+un+"', '"+pw+"');"
            mc.execute(query)
            m.commit()
            messagebox.showinfo("Success!","The user has been added!")
        else:
            messagebox.showerror("Error!","The Username and Password\ncan't be empty!")
    else:
        messagebox.showerror("Error!","The Username already exists!")

def login():
    m=mysql.connector.connect(host='localhost',password='mysql123',user='root',database='loginpw')
    mc=m.cursor()
    mc.execute('select * from details;')
    z=mc.fetchall()
    un=str(e1.get())
    pw=str(e2.get())
    lcount=0
    for i in z:
        if un.lower()==i[0].lower():
            if pw.lower()==i[1].lower():
                messagebox.showinfo("Welcome!","Login Successful!")
                lcount=1
                root.iconify()
                main(un)
                break
            else:
                messagebox.showerror("Error!","Password Incorrect!")
                lcount=1
                break
    if lcount==0:
        messagebox.showerror("Error!","User doesn't exist.\nRegister the user.")

root=Tk()
root.attributes('-fullscreen',True)
c=Canvas(root,bg="gold",width=1366,height=768)
c.create_text(683,180,text='Welcome!',font=('Consolas',65,"underline italic bold"))

def active(z):
    z.delete(0,"end")
    if z==eval('e2'):
        z.configure(show='*')
 
e1=Entry(c,width=30,font=("Consolas",30,"bold"))
e1.place(x=683,y=355,anchor=CENTER)
e1.configure(justify=CENTER)
e1.insert(0,"Username")
e2=Entry(c,width=30,font=("Consolas",30,"bold"))
e2.place(x=683,y=455,anchor=CENTER)
e2.configure(justify=CENTER)
e2.insert(0,"Password")
e1.bind("<FocusIn>",lambda event:active(e1))
e2.bind("<FocusIn>",lambda event:active(e2))
bl=Button(c,width=10,text='Login',font=("Consolas",15,"bold"),activebackground="green",activeforeground="white",command=login)
bl.place(x=683,y=560,anchor=CENTER)
bl=Button(c,width=10,text='Register',font=("Consolas",15,"bold"),activebackground="green",activeforeground="white",command=register,bg='black',fg='white')
bl.place(x=683,y=610,anchor=CENTER)
rect = c.create_rectangle(16,16,1340,750, outline='brown',width=5,fill='')
c.pack()
root.config(bg='brown')
root.title('Login')
m.commit()
root.mainloop()
