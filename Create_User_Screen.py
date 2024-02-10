from tkinter import *
import sqlite3
from tkinter import messagebox

def clear_clicked():
    name.set("")
    password.set("")
    t1.focus()
    
def create_clicked():
    con=sqlite3.connect("INVENTORYDB.sqlite")
    c=con.cursor()
    n=name.get()
    p=password.get()
    c.execute("select * from User where Username=? and Password=?",(n,p))
    data=c.fetchall()
    if len(data)>0:
        messagebox.showwarning("Alert!!!!","UserName Or Password Already Exists")
    else:
        c.execute("insert into User(Username,Password) values(?,?)",(n,p))
        con.commit()
        messagebox.showinfo("Great!","User Added")
        clear_clicked()
    con.close()
    t1.focus()
            
def cancel_clicked():
    a=messagebox.askyesno("Alert1","Do You Really Want To Exit?")
    if(a==True):
        root.destroy()
        import os
        os.system("Login_Screen.py")
    else:
        t1.focus()
        
root=Tk()
root.geometry("800x500")
root.title("Create User Screen")
root.configure(bg="grey")

name=StringVar()
password=StringVar()

l1=Label(root,text="CREATE USER",bg="black",fg="yellow",font=("MS Sans Serif",30,"bold"))
l2=Label(root,text="Username",font=15)
l3=Label(root,text="Password",font=15)

t1=Entry(root,width="50",textvariable=name)
t2=Entry(root,width="50",show="•",textvariable=password)

b1=Button(root,text="Create",width="30",command=create_clicked)
b2=Button(root,text="Clear",width="30",command=clear_clicked)
b3=Button(root,text="Cancel",width="30",command=cancel_clicked)

l1.place(x=250,y=0)
l2.place(x=200,y=90)
l3.place(x=200,y=200)

t1.place(x=300,y=92)
t2.place(x=300,y=202)

b1.place(x=0,y=400)
b2.place(x=300,y=400)
b3.place(x=600,y=400)

t1.focus()

root.mainloop()
