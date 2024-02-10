from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
root.geometry("800x500")
root.title("Stock Entry Screen")
root.configure(bg="grey")

def clear_clicked():
    codevar.set("")
    namevar.set("")
    ratevar.set("")
    qohvar.set("")
    t2.focus()

def insert_clicked():
    con=sqlite3.connect("INVENTORYDB.sqlite")
    c=con.cursor()
    ic=int(codevar.get())
    inm=namevar.get()
    r=int(ratevar.get())
    q=int(qohvar.get())
    c.execute("insert into Stock(icode,iname,Rate,qoh) values(?,?,?,?)",(ic,inm,r,q))
    con.commit()
    messagebox.showinfo("Great!","1Record Added")
    clear_clicked()
    geticode()
    con.close()
    
    
def geticode():
    con=sqlite3.connect("INVENTORYDB.sqlite")
    c=con.cursor()
    c.execute("select icode from Stock")
    data=c.fetchall()
    if len(data)==0:
        ic=1001
    else:
        lastic=data[-1][0]
        ic=lastic+1
    codevar.set(ic)
    con.close()
    t3.focus()

def cancel_clicked():
    root.destroy()
    import os
    os.system("Menus.py")
        

codevar=StringVar()
namevar=StringVar()
ratevar=StringVar()
qohvar=StringVar()

l1=Label(root,text="STOCK ENTRY SCREEN",fg="yellow",bg="black",font=("MS Sans Serif",50,"bold"))
l2=Label(root,text="Item Code",font=("Sans Serif",25,"bold"))
l3=Label(root,text="Item Name",font=("Sans Serif",25,"bold"))
l4=Label(root,text="Rate",font=("Sans Serif",25,"bold"))
l5=Label(root,text="QOH",font=("Sans Serif",25,"bold"))

t2=Entry(root,width="60",textvariable=codevar,state="disabled")
t3=Entry(root,width="60",textvariable=namevar)
t4=Entry(root,width="60",textvariable=ratevar)
t5=Entry(root,width="60",textvariable=qohvar)

b1=Button(root,width=30,text="Insert",command=insert_clicked)
b2=Button(root,width=30,text="Clear",command=clear_clicked)
b3=Button(root,width=30,text="Cancel",command=cancel_clicked)

l1.place(x=0,y=0)
l2.place(x=150,y=100)
l3.place(x=150,y=180)
l4.place(x=150,y=260)
l5.place(x=150,y=340)

t2.place(x=350,y=115)
t3.place(x=350,y=195)
t4.place(x=350,y=275)
t5.place(x=350,y=355)

b1.place(x=5,y=450)
b2.place(x=290,y=450)
b3.place(x=575,y=450)

geticode()
t3.focus()

root.mainloop()
