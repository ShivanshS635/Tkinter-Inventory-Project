from tkinter import *

root=Tk()
root.geometry("800x500")

L1=Label(root,text="Inventory",fg="cyan",font=("San Francisco Display",50,"bold"))
L2=Label(root,text="Control",fg="cyan",font=("San Francisco Display",50,"bold"))
L3=Label(root,text="System",fg="cyan",font=("San Francisco Display",50,"bold"))
L4=Label(root,text="Submitted By-Shivansh Sharma",fg="cyan",font=("San Francisco Display",30,"bold"))

##photo=PhotoImage(file="Welcome screen.png")
##L=Label(root)
##L.configure(image=photo)
##
##L.place(x=0,y=0)
L1.place(x=50,y=0)
L2.place(x=100,y=100)
L3.place(x=150,y=200)
L4.place(x=0,y=400)

import os
import time
def waitfn():
    time.sleep(3)
    root.destroy()
    os.system("Login_Screen.py")
root.after(1000,waitfn)

root.mainloop()
