from tkinter import *
import cv2

def func1():
    s=e1_val.get()
    e1.delete(first=0,last=len(s))
    s=e2_val.get()
    e2.delete(first=0,last=len(s))
    s=e3_val.get()
    e3.delete(first=0,last=len(s))
    s=e4_val.get()
    e4.delete(first=0,last=len(s))

def func2():
    t=e1_val.get()
    t="Files/"+t+".jpg"
    a=int(e2_val.get())
    b=int(e3_val.get())
    img=cv2.imread(t,1)
    resized_image=cv2.resize(img,(b,a))
    s=e4_val.get()
    s="Files/"+s+".jpg"
    cv2.imwrite(s,resized_image)

window=Tk()

b=Label(window,text="Name of The File")
b.grid(row=1,column=0)
c=Label(window,text="Height Desired")
c.grid(row=2,column=0)
d=Label(window,text="Breadth Desired")
d.grid(row=3,column=0)
e=Label(window,text="New Name for the Resized File")
e.grid(row=4,column=0)

e1_val=StringVar()
e1=Entry(window,textvariable=e1_val)
e1.grid(row=1,column=1)
e2_val=StringVar()
e2=Entry(window,textvariable=e2_val)
e2.grid(row=2,column=1)
e3_val=StringVar()
e3=Entry(window,textvariable=e3_val)
e3.grid(row=3,column=1)
e4_val=StringVar()
e4=Entry(window,textvariable=e4_val)
e4.grid(row=4,column=1)

b1=Button(window,text="Cancel",width=12,command=func1)
b1.grid(row=5,column=0)
b1=Button(window,text="Convert",width=12,command=func2)
b1.grid(row=5,column=1)

window.mainloop()