from tkinter import *
import sqlite3
from tkinter import messagebox

root=Tk()
root.geometry("900x900")
root.title("welcome screen")
root.configure(bg="peru")

namevar=StringVar()
codevar=IntVar()
ratevar=IntVar()
qohvar=IntVar()


def insert_clicked():
    con=sqlite3.connect("mydatabase.sqlite")
    c=con.cursor()
    ic=int(codevar.get())
    inm=namevar.get()
    r=int(ratevar.get())
    q=int(qohvar.get())
    c.execute("insert into Stock(icode,iname,Rate,qoh) values(?,?,?,?)",(ic,inm,r,q))
    con.commit()
    messagebox.showinfo("Great!","1Record Added")
    clear_clicked()
    
    con.close()

def clear_clicked():
    codevar.set("")
    namevar.set("")
    ratevar.set("")
    qohvar.set("")


def cancel_clicked():
    root.destroy()
    

l1=Label(root,text="STOCK ENTRY SCREEN",bg="white",font=("ALGERIAN",50,"bold"))
l2=Label(root,text="ITEM NAME:",bg="white",font=("ALGERIAN",25,"bold"))
l3=Label(root,text="ITEM CODE:",bg="white",font=("ALGERIAN",25,"bold"))
l4=Label(root,text="RATE:",bg="white",font=("ALGERIAN",25,"bold"))
l5=Label(root,text="QOH",bg="white",font=("ALGERIAN",25,"bold"))

t1=Entry(root,width="40",textvariable=namevar)
t2=Entry(root,width="40",textvariable=codevar)
t3=Entry(root,width="40",textvariable=ratevar)
t4=Entry(root,width="40",textvariable=qohvar)

l1.place(x=100,y=50)
l2.place(x=120,y=200)
l3.place(x=120,y=300)
l4.place(x=120,y=400)
l5.place(x=120,y=500)

b1=Button(root,width="40")
b2=Button(root,width="40")
b3=Button(root,width="40")
b4=Button(root,width="40")

b5=Button(root,width="20",text="INSERT",command=insert_clicked)
b6=Button(root,width="20",text="CLEAR",command=clear_clicked)
b7=Button(root,width="20",text="CANCEL",command=cancel_clicked)

t1.place(x=450,y=200)
t2.place(x=450,y=300)
t3.place(x=450,y=400)
t4.place(x=450,y=500)

b5.place(x=100,y=600)
b6.place(x=350,y=600)
b7.place(x=600,y=600)

root.mainloop()
