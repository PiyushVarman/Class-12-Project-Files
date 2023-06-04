from tkinter import *
from tkinter import messagebox
import time
import datetime as dt
import calendar
import webbrowser

root=Tk()
root.attributes('-fullscreen',True)
root.configure(bg='#FFD700')

tbar= Canvas(root,width='1366',height = "50")
tbar.place(y=720)
lab=Label(root,font=("Calibri",18,"bold italic"))
def plug():
   webbrowser.open_new_tab("Github.com/PiyushVarman")

def clock():
   global fclock
   fclock=Toplevel(root)
   fclock.geometry("400x600")
   fclock.title("Date and Time")
   fclock.configure(bg='#E8E8E8')
   tlabel=Label(fclock,text='The Time is:',font=("Consolas",18,"bold italic"),bg='#E8E8E8')
   tlabel.pack(pady=10)
   fclock.resizable(False,False)
   clabel=Label(fclock,font=("Consolas",30,"bold"),bg='#E8E8E8')
   clabel.pack()
   today=dt.datetime.now()
   tlabel=Label(fclock,text=f"{today:%A, %B %d, %Y}",font=("Consolas",15,"italic"),bg='#E8E8E8')
   tlabel.pack(pady=10)
   month=3
   y,m=int(f"{today:%Y}"),int(f"{today:%m}")
   cal=Label(fclock,text=calendar.month(y,m),font=("Consolas",18),bg='#E8E8E8')
   cal.pack(pady=50)
   fclock.attributes('-topmost',True)
   def fullclock():
      hms= time.strftime("%H:%M:%S")
      clabel.config(text=hms)
      clabel.after(200,fullclock)
   fullclock()
   def yearcal():
      fullcal=Toplevel(fclock)
      fullcal.title("Calendar")
      fullcal.geometry("1366x740")
      fullcal.configure(bg='#E8E8E8')
      yc=Label(fullcal,text=calendar.calendar(y),font=("Consolas",12,"bold"),bg='#E8E8E8')
      yc.pack()
      fullcal.mainloop()
   ycal=Button(fclock, text=f"{today:%Y} Calendar",font=("Consolas",15,"bold"),bg='#E8E8E8',
               activebackground="#000000",activeforeground='#E8E8E8',command=yearcal)
   ycal.pack()
   fclock.focus() 
   fclock.mainloop()  
line=''
def calculator():
   global line
   calc=Toplevel(root)
   calc.title("Calculator")
   calc.geometry("355x250")
   calc.configure(bg="#DBDBDB")
   calc.resizable(False,False)
   calc.attributes('-topmost',True)
   def press(num):
      global line
      line=line+str(num)
      eq.set(line)
   def equal():
      global line
      if line[-1:-3:-1]=="**":
         messagebox.showerror("Error!","Please input a value\nas the power.")
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
   eq=StringVar()
   win=Entry(calc,width=32,font=(20),textvariable=eq)
   win.config(state="disabled",disabledforeground="#000000")
   win.grid(columnspan=40,pady=10)

   bpl=Button(calc,text="+",width=8,font=("Calibri",15),bg="#EDEDED",borderwidth=0.5,command=lambda:press("+"))
   bpl.grid(row=1,column=0)
   bsub=Button(calc,text="-",width=8,font=("Calibri",15),bg="#EDEDED",borderwidth=0.5,command=lambda:press("-"))
   bsub.grid(row=1,column=1)
   bmu=Button(calc,text="x",width=8,font=("Calibri",15),bg="#EDEDED",borderwidth=0.5,command=lambda:press("x"))
   bmu.grid(row=1,column=2)
   bdi=Button(calc,text="÷",width=8,font=("Calibri",15),bg="#EDEDED",borderwidth=0.5,command=lambda:press("/"))
   bdi.grid(row=1,column=3)

   bsr=Button(calc,text="√𝓍",width=8,font=("Calibri",15),bg="#EDEDED",borderwidth=0.5,command=lambda:press("**0.5"))
   bsr.grid(row=2,column=3)
   bpo=Button(calc,text="𝓍ⁿ",width=8,font=("Calibri",15),bg="#EDEDED",borderwidth=0.5,command=lambda:xn())
   bpo.grid(row=3,column=3)
   bcl=Button(calc,text="CLEAR",width=8,font=("Calibri",15,"bold"),bg="#FF0000",fg="#FFFFFF",borderwidth=0.5,command=lambda:clear())
   bcl.grid(row=4,column=3)
   beq=Button(calc,text="=",width=8,font=("Calibri",15,"bold"),bg="#0DFF00",fg="#FFFFFF",borderwidth=0.5,command=lambda:equal())
   beq.grid(row=5,column=3)
   bbs=Button(calc,text="Backspace",width=8,font=("Calibri",14),bg="#000000",fg="#FFFFFF",borderwidth=0.5,command=lambda:bs())
   bbs.grid(row=5,column=0)

   b1=Button(calc,text="1",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("1"))
   b1.grid(row=4,column=0)
   b2=Button(calc,text="2",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("2"))
   b2.grid(row=4,column=1)
   b3=Button(calc,text="3",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("3"))
   b3.grid(row=4,column=2)
   b4=Button(calc,text="4",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("4"))
   b4.grid(row=3,column=0)
   b5=Button(calc,text="5",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("5"))
   b5.grid(row=3,column=1)
   b6=Button(calc,text="6",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("6"))
   b6.grid(row=3,column=2)
   b7=Button(calc,text="7",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("7"))
   b7.grid(row=2,column=0)
   b8=Button(calc,text="8",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("8"))
   b8.grid(row=2,column=1)
   b9=Button(calc,text="9",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("9"))
   b9.grid(row=2,column=2)
   b0=Button(calc,text="0",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("0"))
   b0.grid(row=5,column=1)
   bpt=Button(calc,text=".",width=8,font=("Calibri",15,"bold"),bg="#EDEDED",borderwidth=0.5,command=lambda:press("."))
   bpt.grid(row=5,column=2)
   calc.bind('<Return>',lambda event:equal())
   calc.bind('1',lambda event:press(1))
   calc.bind('2',lambda event:press(2))
   calc.bind('3',lambda event:press(3))
   calc.bind('4',lambda event:press(4))
   calc.bind('5',lambda event:press(5))
   calc.bind('6',lambda event:press(6))
   calc.bind('7',lambda event:press(7))
   calc.bind('8',lambda event:press(8))
   calc.bind('9',lambda event:press(9))
   calc.bind('0',lambda event:press(0))
   calc.bind('+',lambda event:press("+"))
   calc.bind('-',lambda event:press("-"))
   calc.bind('*',lambda event:press("*"))
   calc.bind('/',lambda event:press("/"))
   calc.bind('.',lambda event:press("."))
   calc.bind('<KP_Enter>',lambda event:equal())
   calc.bind('<BackSpace>',lambda event:bs())

def clockfunc():
   global button
   text_input = time.strftime("%H:%M")
   lab.config(text=text_input)
   lab.after(200,clockfunc)
   button=Button(root,text="^",font=("Consolas", 18, 'bold'),fg="black",borderwidth=1,
                 cursor="hand2",activebackground='#000000',activeforeground='#E8E8E8',command=clock)
clockfunc()
calcbut=Button(root,text="Yo loosu",command=calculator)
calcbut.place(x=540,y=400)
lbut=Button(root,text="Visit my Github!",font=("Consolas",10,"italic"),fg="black",bg="#FFD700",activebackground="#000000",activeforeground="red")
lbut.bind("<Button-1>",lambda e:plug())
lbut.place(x=1240,y=690)
z='''
░█████╗░██╗░░░░░░█████╗░░█████╗░░██████╗
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██╔════╝
███████║██║░░░░░██║░░██║██║░░██║╚█████╗░
██╔══██║██║░░░░░██║░░██║██║░░██║░╚═══██╗
██║░░██║███████╗╚█████╔╝╚█████╔╝██████╔╝
╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═════╝░'''
nlab=Label(root,text=z,fg='black',bg="#FFD700",font=("Consolas",9))
nlab.place(x=1080,y=-10)
lab.place(x=1260,y=728)
button.place(x=1330,y=723)
