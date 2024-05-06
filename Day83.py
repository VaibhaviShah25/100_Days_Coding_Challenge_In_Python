# Day 83 of 100 days of coding challenge
# Program to create login page using tkinter

from tkinter import  *

def check():
    username = nametext.get()
    password = pwdtext.get()
    print("Username entered:",username)
    print("Password entered:",password)

# window
win = Tk()
win.geometry('400x150')
win.title('Login Form')

# username
name = Label(win,text="Username : ")
name.grid(row=0,column=1)
nametext = Entry(win)
nametext.grid(row=0,column=2)

# password
pwd = Label(win,text="Password : ")
pwd.grid(row=1,column=1)
pwdtext = Entry(win,show="*")
pwdtext.grid(row=1,column=2)

# login button
btnlogin = Button(win,text="Login",command=check)
btnlogin.grid(row=5,column=2)

win.mainloop()

