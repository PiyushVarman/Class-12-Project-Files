from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Calculator")
root.geometry("355x250")
root.configure(bg="#DBDBDB")
root.resizable(False,False)
def press(num):
    global line
    line=line+str(num)
    eq.set(line)
def equal():
    global line
    if line[-1:-3:-1]=="**":
        messagebox.showerror(title="Error!",message="Please input a value\nas the power.")
    else:
        line=str(eval(line))
    
    eq.set(line)
def clear():
    global line
    line=""
    eq.set(line)

def bs():
    global line
    line=line[:-1]
    eq.set(line)
def xn():
    global line
    line=line+str("**")
    eq.set(line)
line=''
eq=StringVar()
win=Entry(root,width=32,font=(20),textvariable=eq)
win.config(state="disabled",disabledforeground="#000000")
win.grid(columnspan=40,pady=10)

bpl=Button(root,text="+",width=8,font=("Calibri",15),bg="#EDEDED",borderwidth=0.5,command=lambda:press("+"))
bpl.grid(row=1,column=0)
bsub=Button(root,text="-",width=8,font=("Calibri",15),bg="#EDEDED",borderwidth=0.5,command=lambda:press("-"))
bsub.grid(row=1,column=1)
bmu=Button(root,text="x",width=8,font=("Calibri",15),bg="#EDEDED",borderwidth=0.5,command=lambda:press("x"))
bmu.grid(row=1,column=2)
bdi=Button(root,text="÷",width=8,font=("Calibri",15),bg="#EDEDED",borderwidth=0.5,command=lambda:press("/"))
bdi.grid(row=1,column=3)

bsr=Button(root,text="√𝓍",width=8,font=("Calibri",15),bg="#EDEDED",borderwidth=0.5,command=lambda:press("**0.5"))
bsr.grid(row=2,column=3)
bpo=Button(root,text="𝓍ⁿ",width=8,font=("Calibri",15),bg="#EDEDED",borderwidth=0.5,command=lambda:xn())
bpo.grid(row=3,column=3)
bcl=Button(root,text="CLEAR",width=8,font=("Calibri",15,"bold"),bg="#FF0000",fg="#FFFFFF",borderwidth=0.5,command=lambda:clear())
bcl.grid(row=4,column=3)
beq=Button(root,text="=",width=8,font=("Calibri",15,"bold"),bg="#0DFF00",fg="#FFFFFF",borderwidth=0.5,command=lambda:equal())
beq.grid(row=5,column=3)
bbs=Button(root,text="Backspace",width=8,font=("Calibri",14),bg="#000000",fg="#FFFFFF",borderwidth=0.5,command=lambda:bs())
bbs.grid(row=5,column=0)

b1=Button(root,text="1",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("1"))
b1.grid(row=4,column=0)
b2=Button(root,text="2",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("2"))
b2.grid(row=4,column=1)
b3=Button(root,text="3",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("3"))
b3.grid(row=4,column=2)
b4=Button(root,text="4",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("4"))
b4.grid(row=3,column=0)
b5=Button(root,text="5",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("5"))
b5.grid(row=3,column=1)
b6=Button(root,text="6",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("6"))
b6.grid(row=3,column=2)
b7=Button(root,text="7",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("7"))
b7.grid(row=2,column=0)
b8=Button(root,text="8",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("8"))
b8.grid(row=2,column=1)
b9=Button(root,text="9",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("9"))
b9.grid(row=2,column=2)
b0=Button(root,text="0",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("0"))
b0.grid(row=5,column=1)
bpt=Button(root,text=".",width=8,font=("Calibri",15,"bold"),bg="#EDEDED",borderwidth=0.5,command=lambda:press("."))
bpt.grid(row=5,column=2)

root.bind('<Return>',lambda event:equal())
root.bind('1',lambda event:press(1))
root.bind('2',lambda event:press(2))
root.bind('3',lambda event:press(3))
root.bind('4',lambda event:press(4))
root.bind('5',lambda event:press(5))
root.bind('6',lambda event:press(6))
root.bind('7',lambda event:press(7))
root.bind('8',lambda event:press(8))
root.bind('9',lambda event:press(9))
root.bind('0',lambda event:press(0))
root.bind('+',lambda event:press("+"))
root.bind('-',lambda event:press("-"))
root.bind('*',lambda event:press("*"))
root.bind('/',lambda event:press("/"))
root.bind('.',lambda event:press("."))
root.bind('<KP_Enter>',lambda event:equal())
root.bind('<BackSpace>',lambda event:bs())
