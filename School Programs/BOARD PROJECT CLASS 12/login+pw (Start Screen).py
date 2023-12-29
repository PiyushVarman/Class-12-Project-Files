#Started 27th December 2023
#Last Edit- 29th December 2023
from tkinter import *
import mysql.connector
from tkinter import messagebox
m=mysql.connector.connect(host='localhost',password='mysql123',user='root')
mc=m.cursor()
mc.execute("create database if not exists loginpw;")
mc.execute("use loginpw;")
mc.execute("create table if not exists details(mail_id varchar(100) primary key, password varchar(100));")

def register():
    m=mysql.connector.connect(host='localhost',password='mysql123',user='root',database='loginpw')
    mc=m.cursor()
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
#root.iconify()
root.config(bg='brown')
m.commit()
m.close()
root.mainloop()
