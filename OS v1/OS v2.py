from tkinter import *
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
   
def clockfunc():
   global button
   text_input = time.strftime("%H:%M")
   lab.config(text=text_input)
   lab.after(200,clockfunc)
   button=Button(root,text="^",font=("Consolas", 18, 'bold'),fg="black",borderwidth=1,
                 cursor="hand2",activebackground='#000000',activeforeground='#E8E8E8',command=clock)
clockfunc()
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
