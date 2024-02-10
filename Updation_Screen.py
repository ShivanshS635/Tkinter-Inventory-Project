from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import sqlite3
root=Tk()
root.geometry("1000x500")
root.configure(bg="grey")

codevar=StringVar()
namevar=StringVar()
ratevar=StringVar()
qohvar=StringVar()

def geticode():
    con=sqlite3.connect("INVENTORYDB.sqlite")
    c=con.cursor()
    c.execute("select icode from Stock")
    data=c.fetchall()
    if(len(data)>0):
        l=[]
        for row in data:
            l.append(row[0])
        t2["values"]=l
        con.close()
        t3.focus()

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

def delete_clicked():
    ans=messagebox.askyesno("ALERT!","Are You Sure?")
    if ans==True:
        con=sqlite3.connect("INVENTORYDB.sqlite")
        c=con.cursor()
        ic=int(codevar.get())
        c.execute("delete from Stock where icode=?",(ic,))
        con.commit()
        messagebox.showinfo("GREAT!","1 Record Deleted")
        l=[]
        t2["values"]=l
        geticode()
        t3.focus()
        clear_clicked()
        con.close()
        
def modify_clicked():
    con=sqlite3.connect("INVENTORYDB.sqlite")
    c=con.cursor()
    ic=int(codevar.get())
    inm=namevar.get()
    r=int(ratevar.get())
    q=int(qohvar.get())
    c.execute("update Stock set iname=?,rate=?,qoh=? where icode=?",(inm,r,q,ic))
    con.commit()
    messagebox.showinfo("GREAT!","1 Record Updated")
    con.close()
    clear_clicked()
    t3.focus()
     
def clear_clicked():
    codevar.set("")
    namevar.set("")
    ratevar.set("")
    qohvar.set("")
    t3.focus()

def cancel_clicked():
    root.destroy()
    import os
    os.system("Menus.py")
    
l0=Label(root,text="UPDATION SCREEN",bg="black",fg="yellow",font=("MS Sans Serif",50,"bold"))
l2=Label(root,text="Item Code",bg="grey",font=("Sans Serif",25,"bold"))
l3=Label(root,text="Item Name",bg="grey",font=("Sans Serif",25,"bold"))
l4=Label(root,text="Rate",bg="grey",font=("Sans Serif",25,"bold"))
l5=Label(root,text="QOH",bg="grey",font=("Sans Serif",25,"bold"))

t2=Combobox(root,width="60",textvariable=codevar)
t2.bind("<<ComboboxSelected>>",showdetails)
t3=Entry(root,width="60",textvariable=namevar)
t4=Entry(root,width="60",textvariable=ratevar)
t5=Entry(root,width="60",textvariable=qohvar)

b1=Button(root,width=30,text="Modify",command=modify_clicked)
b2=Button(root,width=30,text="Delete",command=delete_clicked)
b3=Button(root,width=30,text="Clear",command=clear_clicked)
b4=Button(root,width=30,text="Cancel",command=cancel_clicked)

l0.place(x=150,y=0)
l2.place(x=150,y=100)
l3.place(x=150,y=180)
l4.place(x=150,y=260)
l5.place(x=150,y=340)

t2.place(x=350,y=115)
t3.place(x=350,y=195)
t4.place(x=350,y=275)
t5.place(x=350,y=355)

b1.place(x=0,y=450)
b2.place(x=260,y=450)
b3.place(x=520,y=450)
b4.place(x=780,y=450)

geticode()
t3.focus()

root.mainloop()
