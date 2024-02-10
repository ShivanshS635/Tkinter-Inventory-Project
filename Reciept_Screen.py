from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
root.geometry("1000x600")
root.title("Reciept Screen")
root.configure(bg="grey")

codevar=StringVar()
namevar=StringVar()
ratevar=StringVar()
qohvar=StringVar()
datevar=StringVar()
Rvar=StringVar()

def geticode():
    con=sqlite3.connect("INVENTORYDB.sqlite")
    c=con.cursor()
    c.execute("select icode from Stock")
    data=c.fetchall()
    if (len(data)>0):
        l=[]
        for row in data:
            l.append(row[0])
        t2["values"]=l
        con.close()

def showdetails(event):
    con=sqlite3.connect("INVENTORYDB.sqlite")
    c=con.cursor()
    ic=int(codevar.get())
    c.execute("select * from Stock where icode=?",(ic,))
    data=c.fetchall()
    for row in data:
        namevar.set(row[1])
        ratevar.set(int(row[2]))
        qohvar.set(int(row[3]))
    con.close()
    t6.focus()

def reciept_clicked():
    con=sqlite3.connect("INVENTORYDB.sqlite")
    c=con.cursor()
    ic=codevar.get()
    n=namevar.get()
    r=ratevar.get()
    Q=qohvar.get()
    d=datevar.get()
    q=Rvar.get()
    ic=codevar.get()
    c.execute("update Stock set QOH=QOH+? where Icode=?",(Q,ic))
    con.commit
    messagebox.showinfo("Great","Stock Updated")
    c.execute("Insert Into Reciept values(?,?,?,?,?,?) ",(ic,n,r,Q,d,q))
    con.commit()
    messagebox.showinfo("Great","Reciept Updated")
    con.close()

def clear_clicked():
    codevar.set("")
    namevar.set("")
    ratevar.set("")
    qohvar.set("")
    datevar.set("")
    Rvar.set("")

def cancel_clicked():
    root.destroy()
    import os
    os.system("Menus.py")

l0=Label(root,text="RECIEPT SCREEN",bg="black",fg="yellow",font=("MS Sans Serif",50,"bold"))
l2=Label(root,text="Item Code",bg="grey",font=("Sans Serif",25,"bold"))
l3=Label(root,text="Item Name",bg="grey",font=("Sans Serif",25,"bold"))
l4=Label(root,text="Rate",bg="grey",font=("Sans Serif",25,"bold"))
l5=Label(root,text="QOH",bg="grey",font=("Sans Serif",25,"bold"))
l6=Label(root,text="DOR",bg="grey",font=("Sans Serif",25,"bold"))
l7=Label(root,text="Qty Recieved",bg="grey",font=("Sans Serif",25,"bold"))

t2=Combobox(root,width="60",textvariable=codevar)
t2.bind("<<ComboboxSelected>>",showdetails)
t3=Entry(root,width="60",textvariable=namevar)
t4=Entry(root,width="60",textvariable=ratevar)
t5=Entry(root,width="60",textvariable=qohvar)
t6=Entry(root,width="60",textvariable=datevar)
t7=Entry(root,width="60",textvariable=Rvar)

b1=Button(root,width=30,text="Reciept",command=reciept_clicked)
b2=Button(root,width=30,text="Clear",command=clear_clicked)
b3=Button(root,width=30,text="Cancel",command=cancel_clicked)

l0.place(x=250,y=0)
l2.place(x=150,y=90)
l3.place(x=150,y=160)
l4.place(x=150,y=230)
l5.place(x=150,y=300)
l6.place(x=150,y=370)
l7.place(x=150,y=440)

t2.place(x=400,y=105)
t3.place(x=400,y=175)
t4.place(x=400,y=245)
t5.place(x=400,y=315)
t6.place(x=400,y=385)
t7.place(x=400,y=455)

b1.place(x=10,y=550)
b2.place(x=390,y=550)
b3.place(x=770,y=550)

geticode()

root.mainloop()

