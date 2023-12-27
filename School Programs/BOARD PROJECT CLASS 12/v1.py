#Started 27th December 2023

from tkinter import *
root=Tk()
root.attributes('-fullscreen',True)
c=Canvas(root,bg="gold",width=1366,height=768)
c.create_text(683,200,text='Welcome!',font=('Consolas',65,"underline italic bold"))
def active(z):
    z.delete(0,"end")
    if z==eval('e2'):
        z.configure(show='*')
e1=Entry(c,width=20,font=("Consolas",25,"bold"))
e1.place(x=683,y=380,anchor=CENTER)
e1.configure(justify=CENTER)
e1.insert(0,"Username")
e2=Entry(c,width=20,font=("Consolas",25,"bold"))
e2.place(x=683,y=480,anchor=CENTER)
e2.configure(justify=CENTER)
e2.insert(0,"Password")
e1.bind("<FocusIn>",lambda event:active(e1))
e2.bind("<FocusIn>",lambda event:active(e2))
b=Button(c,width=10,text='Login',font=("Consolas",15,"bold"),activebackground="green",activeforeground="white")
b.place(x=683,y=600,anchor=CENTER)
rect = c.create_rectangle(16,16,1340,750, outline='brown',width=5,fill='')
c.pack()
#root.iconify()
root.mainloop()
