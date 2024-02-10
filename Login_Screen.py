from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
root.geometry("800x500")
root.title("Login Screen")
root.configure(bg="grey")

def login_clicked():
    con=sqlite3.connect("INVENTORYDB.sqlite")
    c=con.cursor()
    u=textname.get()
    p=password.get()
    c.execute("select * from user where Username=? and Password=?",(u,p))
    data=c.fetchall()
    if len(data)==0:
        messagebox.showerror("Create User!!!!!","Username or Password Doesnot Exist")
    else:
        messagebox.showinfo("Great!!!!!!!!!!!!","Login Succesful")
        #import os
        #os.system("Menus")
        root.destroy()
        import Menus

def createuser_clicked():
    #import os
    #os.system("Create_User_Screen")
    root.destroy()
    import Create_User_Screen
    
textname=StringVar()
password=StringVar()

l1=Label(root,text="Login Screen",bg="black",fg="yellow",font=("MS Sans Serif",40,"bold"))
l2=Label(root,text="Username",font=("Sans Serif",20,"bold"))
l3=Label(root,text="Password",font=("Sans Serif",20,"bold"))

t1=Entry(root,width=50,textvariable=textname)
t2=Entry(root,width=50,show="*",textvariable=password)

b1=Button(root,text="Login",width="30",command=login_clicked)
b2=Button(root,text="Create User",width="30",command=createuser_clicked)
b3=Button(root,text="Exit",width="30",command=root.destroy)

l1.place(x=230,y=0)
l2.place(x=200,y=100)
l3.place(x=200,y=150)

t1.place(x=350,y=112)
t2.place(x=350,y=160)

b1.place(x=0,y=300)
b2.place(x=290,y=300)
b3.place(x=580,y=300)

t1.focus()

root.mainloop()
