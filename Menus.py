import os
from tkinter import *

root = Tk()
root.title("Main Menu")
root.geometry("500x500")

def stockentry():
    root.destroy()
    os.system("Stock_Entry_Screen.py")

def modify():
    root.destroy()
    os.system("Updation_Screen.py")

def reciept():
    root.destroy()
    os.system("Reciept_Screen.py")

def issue():
    root.destroy()
    os.system("Stock_Issue.py")

def allitem():
    root.destroy()
    os.system("All_Item_Report.py")

def allissue():
    root.destroy()
    os.system("All_Issue_Report.py")

def allreciept():
    root.destroy()
    os.system("All_Reciept_Report")

Mymenu=Menu(root)
root.config(menu=Mymenu)

stockmenu=Menu(Mymenu)
transactionmenu=Menu(Mymenu)
reportmenu=Menu(Mymenu)
exitmenu=Menu(Mymenu)

Mymenu.add_cascade(label="Stock",menu=stockmenu)
Mymenu.add_cascade(label="Transaction",menu=transactionmenu)
Mymenu.add_cascade(label="Report",menu=reportmenu)
Mymenu.add_cascade(label="Exit",menu=exitmenu)

stockmenu.add_command(label="Stock Entry",command=stockentry)
stockmenu.add_separator()
stockmenu.add_command(label="Update Stock",command=modify)

transactionmenu.add_command(label="Issue",command=issue)
transactionmenu.add_separator()
transactionmenu.add_command(label="Reciept",command=reciept)

reportmenu.add_command(label="All Item",command=allitem)
reportmenu.add_separator()
reportmenu.add_command(label="All Issue",command=allissue)
reportmenu.add_separator()
reportmenu.add_command(label="All Reciept",command=allreciept)

exitmenu.add_command(label="Quit",command=root.destroy)

root.mainloop()
