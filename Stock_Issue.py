from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import sqlite3
from datetime import datetime

root=Tk()
root.title("Stock Issue")
root.geometry("900x700")
root.configure(bg="grey")

txticode=StringVar()
txtiname=StringVar()
txtrate=StringVar()
txtqoh=StringVar()
txtdoi=StringVar()
txtqtyissued=StringVar()

def geticode():
    con=sqlite3.connect("INVENTORYDB.sqlite")
    c=con.cursor()
    c.execute("select Icode from Stock")
    data=c.fetchall()
    if len(data)>0:
        l=[]
        for row in data:
            l.append(row[0])
    t1["values"]=l
    con.close

def showdetails(event):
    con=sqlite3.connect("INVENTORYDB.sqlite")
    c=con.cursor()
    ic=txticode.get()
    c.execute("select * from Stock where icode=?",(ic,))
    data=c.fetchall()
    for row in data:
        txtiname.set(row[1])
        txtrate.set(int(row[2]))
        txtqoh.set(int(row[3]))
        d=datetime.now()
        s=d.strftime("%d-%m-%Y %H:%M:%S")
        txtdoi.set(s)
        t6.focus()
        
def issue_clicked():
    con=sqlite3.connect("INVENTORYDB.sqlite")
    c=con.cursor()
    ic=int(txticode.get())
    n=txtiname.get()
    r=int(txtrate.get())
    q=int(txtqoh.get())
    d=txtdoi.get()
    Q=int(txtqtyissued.get())
    if Q>q:
        messagebox.showerror("ERROR!","Quantity Issues Is More Then QOH")
    else:
        c.execute("update Stock set QOH=QOH-? where Icode=?",(Q,ic))
        con.commit()
        messagebox.showinfo("Great!","Stock Updated")
        c.execute("insert into Issue (Icode,Qty,DOI) values(?,?,?)",(ic,Q,d))
        con.commit()
        messagebox.showinfo("Great!","Issue Updated")
    con.close()
    clear_clicked()
    t6.focus()

def clear_clicked():
    txticode.set("")
    txtiname.set("")
    txtrate.set("")
    txtqoh.set("")
    txtdoi.set("")
    txtqtyissued.set("")

def cancel_clicked():
    root.destroy()
    import os
    os.system("Menus.py")

L0=Label(root,text="Stock Issue",bg="black",fg="yellow",font=("MS Sans Serif",50,"bold"))
L1=Label(root,bg="grey",text="Enter Itemcode",font=("Sans Serif",15))
L2=Label(root,bg="grey",text="Enter Itemname",font=("Sans Serif",15))
L3=Label(root,bg="grey",text="Enter Rate",font=("Sans Serif",15))
L4=Label(root,bg="grey",text="Enter QOH",font=("Sans Serif",15))
L5=Label(root,bg="grey",text="Enter DOI",font=("Sans Serif",15))
L6=Label(root,bg="grey",text="Enter Qty Issued",font=("Sans Serif",15))

t1=Combobox(root,width="50",textvariable=txticode)
t1.bind("<<ComboboxSelected>>",showdetails)
t2=Entry(root,width="50",textvariable=txtiname,state='disabled')
t3=Entry(root,width="50",textvariable=txtrate,state='disabled')
t4=Entry(root,width="50",textvariable=txtqoh,state='disabled')
t5=Entry(root,width="50",textvariable=txtdoi)
t6=Entry(root,width="50",textvariable=txtqtyissued)

b1=Button(root,text="Issue",width="30",command=issue_clicked)
b2=Button(root,text="Clear",width="30",command=clear_clicked)
b3=Button(root,text="Cancel",width="30",command=cancel_clicked)

L0.place(x=270,y=0)
L1.place(x=100,y=100)
L2.place(x=100,y=180)
L3.place(x=100,y=260)
L4.place(x=100,y=340)
L5.place(x=100,y=420)
L6.place(x=100,y=500)

t1.place(x=300,y=110)
t2.place(x=300,y=190)
t3.place(x=300,y=270)
t4.place(x=300,y=350)
t5.place(x=300,y=430)
t6.place(x=300,y=510)

b1.place(x=0,y=600)
b2.place(x=340,y=600)
b3.place(x=680,y=600)

geticode()

root.mainloop()
