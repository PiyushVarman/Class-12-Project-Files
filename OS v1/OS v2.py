from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import time
import datetime as dt
import calendar
import webbrowser
root=Tk()
root.attributes('-fullscreen',True)
root.configure(bg='#FFD700')
root.title("AaloOs")
tbar= Canvas(root,width='1366',height = "50")
tbar.place(y=720)
mbar=Canvas(root,width='1366',height = "27")
mbar.place(y=0)
lab=Label(root,font=("Calibri",18,"bold italic"))
apps=[
   "Calculator",
   "Clock",
   "Notepad",
   "Github Link"
   ]
def launch():
   global clicked
   c=(clicked.get()).lower()
   c=c.replace(" ","")
   clicked.set("Applications")
   eval(c)()
   
def githublink():
   webbrowser.open_new_tab("Github.com/PiyushVarman")

#Personalization and other settings
def missioncontrol(): #Use Control-S to activate your colour option
   mc=Toplevel(root)
   mc.attributes('-topmost',True)
   mc.title("Mission Control")
   mc.geometry("700x350")
   mc.resizable(False,False)
   sbar=Canvas(mc,width=200,height=500)
   sbar.place(x=0,y=0)
   sbar.configure(bg='blue')
   l=Label(mc,text='Welcome to MC!',font=(25))
   l.place(x=250,y=90)
   wlc=LabelFrame(mc,text='Mission Control',bg='blue',font=(100),fg='white',pady=10)
   wlc.place(x=25,y=100)
   changebutton=Button(mc,text='',font=(20),borderwidth=0,cursor='hand2')
   changebutton.place(x=570,y=145)
   def desktop():
      l.config(text='Enter the background colour:',font=(25))
      def en():
         s=(enter.get(1.0,END)).strip()
         enter.delete('1.0','end')
         nlab.configure(bg=str(s),fg='black')
         root.configure(bg=str(s))
         sbar.configure(bg=str(s))
         wlc.configure(bg=str(s))
         if s.lower()=='black' or s.lower()=='#000000':
            nlab.configure(fg='white')
      changebutton.config(text='Change',borderwidth=2,command=en)
   db=Button(wlc,text='Desktop',font=(100),command=desktop)
   db.pack()
   enter=Text(mc,height=1,width=45,font=('arial',12))
   enter.place(x=250,y=120)
   tb=Button(wlc,text='Bar',font=(100))
   tb.pack()
   
   mc.mainloop()
mcbutton=Button(root,text='Settings',command=missioncontrol,cursor='hand2')
mcbutton.place(x=1250,y=3)
   

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
      fullcal.attributes('-topmost',True)
      fullcal.mainloop()
   ycal=Button(fclock, text=f"{today:%Y} Calendar",font=("Consolas",15,"bold"),bg='#E8E8E8',
               activebackground="#000000",activeforeground='#E8E8E8',command=yearcal,cursor='hand2')
   ycal.pack()
   fclock.focus() 
   fclock.mainloop()  
line='' #Expression within the input bar of the calculator
def notepad():
   note=Toplevel(root)
   note.geometry("1000x700")
   note.title("AalWrite")
   note.resizable(False,False)
   note.configure(bg="#cec5c6")

   def savefile():
      note.configure(bg='green')
      save_file=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
      if save_file is None:
         return
      text=str(textentry.get(1.0,END))
      save_file.write(text)
      save_file.close()
      note.configure(bg="#cec5c6")

   def openfile():
      note.configure(bg="#000000")
      open_file=filedialog.askopenfile(mode='r',filetype=[('text files','*.txt')])
      if open_file is not None:
         internal=open_file.read()
      textentry.delete(1.0,END)
      textentry.insert(INSERT,internal)
      note.configure(bg="#cec5c6")

   sfb=Button(note,text="Save File",command=savefile,cursor='hand2').place(x=20,y=10)
   ofb=Button(note,text="Open File",command=openfile,cursor='hand2').place(x=920,y=10)
   textentry=Text(note,width='120',height='39')
   textentry.place(x=20,y=50)
   note.bind('<Control_L>s',lambda event:savefile())
   note.bind('<Control_L>o',lambda event:openfile())
   note.mainloop()
   
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

   def bs(): #backspace
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

   bpl=Button(calc,text="+",width=8,font=("Calibri",15),bg="#EDEDED",borderwidth=0.5,command=lambda:press("+"),cursor='hand2')
   bpl.grid(row=1,column=0)
   bsub=Button(calc,text="-",width=8,font=("Calibri",15),bg="#EDEDED",borderwidth=0.5,command=lambda:press("-"),cursor='hand2')
   bsub.grid(row=1,column=1)
   bmu=Button(calc,text="x",width=8,font=("Calibri",15),bg="#EDEDED",borderwidth=0.5,command=lambda:press("*"),cursor='hand2')
   bmu.grid(row=1,column=2)
   bdi=Button(calc,text="÷",width=8,font=("Calibri",15),bg="#EDEDED",borderwidth=0.5,command=lambda:press("/"),cursor='hand2')
   bdi.grid(row=1,column=3)

   bsr=Button(calc,text="√𝓍",width=8,font=("Calibri",15),bg="#EDEDED",borderwidth=0.5,command=lambda:press("**0.5"),cursor='hand2')
   bsr.grid(row=2,column=3)
   bpo=Button(calc,text="𝓍ⁿ",width=8,font=("Calibri",15),bg="#EDEDED",borderwidth=0.5,command=lambda:xn(),cursor='hand2')
   bpo.grid(row=3,column=3)
   bcl=Button(calc,text="CLEAR",width=8,font=("Calibri",15,"bold"),bg="#FF0000",fg="#FFFFFF",borderwidth=0.5,command=lambda:clear(),cursor='hand2')
   bcl.grid(row=4,column=3)
   beq=Button(calc,text="=",width=8,font=("Calibri",15,"bold"),bg="#0DFF00",fg="#FFFFFF",borderwidth=0.5,command=lambda:equal(),cursor='hand2')
   beq.grid(row=5,column=3)
   bbs=Button(calc,text="Backspace",width=8,font=("Calibri",14),bg="#000000",fg="#FFFFFF",borderwidth=0.5,command=lambda:bs(),cursor='hand2')
   bbs.grid(row=5,column=0)

   b1=Button(calc,text="1",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("1"),cursor='hand2')
   b1.grid(row=4,column=0)
   b2=Button(calc,text="2",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("2"),cursor='hand2')
   b2.grid(row=4,column=1)
   b3=Button(calc,text="3",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("3"),cursor='hand2')
   b3.grid(row=4,column=2)
   b4=Button(calc,text="4",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("4"),cursor='hand2')
   b4.grid(row=3,column=0)
   b5=Button(calc,text="5",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("5"),cursor='hand2')
   b5.grid(row=3,column=1)
   b6=Button(calc,text="6",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("6"),cursor='hand2')
   b6.grid(row=3,column=2)
   b7=Button(calc,text="7",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("7"),cursor='hand2')
   b7.grid(row=2,column=0)
   b8=Button(calc,text="8",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("8"),cursor='hand2')
   b8.grid(row=2,column=1)
   b9=Button(calc,text="9",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("9"),cursor='hand2')
   b9.grid(row=2,column=2)
   b0=Button(calc,text="0",width=8,font=("Calibri",15,"bold"),bg="#FFFFFF",borderwidth=0.5,command=lambda:press("0"),cursor='hand2')
   b0.grid(row=5,column=1)
   bpt=Button(calc,text=".",width=8,font=("Calibri",15,"bold"),bg="#EDEDED",borderwidth=0.5,command=lambda:press("."),cursor='hand2')
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
def off():
   global sign
   if messagebox.askyesno("Power off","Would you like\nto quit the operating environment?")==True:
      sign='''
░██████╗░░█████╗░░█████╗░██████╗░██████╗░██╗░░░██╗███████╗██╗
██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝██║
██║░░██╗░██║░░██║██║░░██║██║░░██║██████╦╝░╚████╔╝░█████╗░░██║
██║░░╚██╗██║░░██║██║░░██║██║░░██║██╔══██╗░░╚██╔╝░░██╔══╝░░╚═╝
╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝██████╦╝░░░██║░░░███████╗██╗
░╚═════╝░░╚════╝░░╚════╝░╚═════╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝'''
      nlab.config(text=sign,bg='#000000',fg='#FFFFFF')
      nlab.place(x=935)
      root.configure(bg='#000000')
      root.after(1000,lambda: root.destroy())

def clockfunc():
   global button
   text_input = time.strftime("%H:%M")
   lab.config(text=text_input)
   lab.after(200,clockfunc)
   button=Button(root,text="^",font=("Consolas", 18, 'bold'),fg="black",borderwidth=1,
                 cursor="hand2",activebackground='#000000',activeforeground='#E8E8E8',command=clock)
clockfunc()
clicked=StringVar()
clicked.set("Applications")
applauncher=OptionMenu(root, clicked, *apps)
applauncher.place(x=0,y=0)
launchbut=Button(root,text="Launch",activebackground="#000000",activeforeground="#FFFFFF",font=("Calibri",10,"bold"),command=lambda: launch(),cursor='hand2')
launchbut.place(x=150,y=3)
powerbut=Button(root,text="Power",activebackground="#000000",activeforeground="#FFFFFF",command=off,cursor='hand2')
powerbut.place(x=1320,y=3)
z='''
░█████╗░░█████╗░██╗░░░░░░█████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██╔══██╗██╔════╝
███████║███████║██║░░░░░██║░░██║██║░░██║╚█████╗░
██╔══██║██╔══██║██║░░░░░██║░░██║██║░░██║░╚═══██╗
██║░░██║██║░░██║███████╗╚█████╔╝╚█████╔╝██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═════╝░
````````````````````````````````````````````````'''
nlab=Label(root,text=z,fg='black',bg="#FFD700",font=("Consolas",9))
nlab.place(x=1025,y=35)
lab.place(x=1260,y=728)
button.place(x=1330,y=723)
root.mainloop()
