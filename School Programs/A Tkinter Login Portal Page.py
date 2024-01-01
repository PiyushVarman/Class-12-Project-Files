from tkinter import *
from tkinter import messagebox
def filereader():
    f=open("lpw.txt","r")
    x=f.read()
    l=eval(x)
    f.close
    return(l)
root=Tk()
root.title("Welcome!")
root.geometry("500x400")
root.resizable(False,False)
root.configure(bg='#FFAE42')
def seepass():
    global entrypw
    s=str(entrypw.get())
    if s:
        messagebox.showinfo("Entered Password",s)

def loginpw():
    global entrypw
    global entryu
    s=str(entrypw.get())
    p=str(entryu.get())
    if s and p:
        pass
    else:
        messagebox.showerror("Invalid.","Kindly enter both fields.")
def registry():
    r=Toplevel(root)
    r.geometry("500x500")
    k=Entry(r,text="Enter the username:",font=("Calibri",15),width=15)
    u=Entry(r,text="Enter the password:",font=("Calibri",15),width=15)
    f=open("lpw.txt","w")
    l=filereader()
    l.append([str(k.get()),u])
    f.write(str(l))
    f.close()
entryu=Entry(root,font=("Calibri",15),width=15)
entryu.place(x=300,y=200,anchor=CENTER)
textu=Label(root,text='Username:',font=("Calibri",15),bg='#FFAE42')
textu.place(x=170,y=200,anchor=CENTER)
entrypw=Entry(root,font=("Calibri",15),width=15,show='*')
entrypw.place(x=300,y=235,anchor=CENTER)
textpw=Label(root,text='Password:',font=("Calibri",15),bg='#FFAE42')
textpw.place(x=174,y=235,anchor=CENTER)
text1=Label(root,text='Welcome!',font=("Georgia",25),bg='#FFAE42')
text1.place(x=250,y=100,anchor=CENTER)
loginbutton=Button(root,text='Login',font=('Arial',15,"bold italic"),width=7,activebackground='yellow',activeforeground='red',command=loginpw)
loginbutton.place(x=250,y=300,anchor=CENTER)
pwbutton=Button(root,text='Register',font=('Arial',15,"bold italic"),width=7,activebackground='yellow',activeforeground='red',command=registry)
pwbutton.place(x=250,y=350,anchor=CENTER)
seebutton=Button(root,text='👁',font=('Arial',12,'bold'),activebackground='yellow',command=seepass,bg='#FFAE42')
seebutton.place(x=400,y=235,anchor=CENTER)
root.mainloop()
