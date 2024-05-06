# Day 85 of 100 days of coding challenge
# Program to create basic GUI based calculator
from tkinter import *

def add():
    n1 = eval(t1.get())
    n2 = eval(t2.get())
    c = n1 + n2
    l3.configure(text="Sum is "+str(c))

def subtract():
    n1 = eval(t1.get())
    n2 = eval(t2.get())
    c = n1 - n2
    l3.configure(text="Difference is "+str(c))

def multiply():
    n1 = eval(t1.get())
    n2 = eval(t2.get())
    c = n1 * n2
    l3.configure(text="Product is "+str(c))

def divide():
    n1 = eval(t1.get())
    n2 = eval(t2.get())
    c = n1 / n2
    l3.configure(text="Division is "+str(c))


parent = Tk()
parent.geometry("400x400")
parent.title("Calculator")
hwd = Label(parent,text="My calculator",font=('Arial Bold',15))
hwd.place(x=100,y=10)
l1 = Label(parent,text="Number 1 : ")
l1.place(x=100,y=50)
l2 = Label(parent,text="Number 2 : ")
l2.place(x=100,y=80)

t1 = Entry(parent,width=10)
t1.place(x=190,y=50)
t2 = Entry(parent,width=10)
t2.place(x=190,y=80)

b1 = Button(parent,text="+",command = add, font=('Arial Bold',15))
b2 = Button(parent,text="-",command = subtract, font=('Arial Bold',15))
b3 = Button(parent,text="*",command = multiply, font=('Arial Bold',15))
b4 = Button(parent,text="/",command = divide, font=('Arial Bold',15))
b1.place(x=100,y=110)
b2.place(x=170,y=110)
b3.place(x=100,y=170)
b4.place(x=170,y=170)

l3 = Label(parent,text="RESULT",font=('Arial Bold',12))
l3.place(x=100,y=250)

tfv = Label(parent,text="Thanks for visiting")
tfv.place(x=110,y=300)

parent.mainloop()