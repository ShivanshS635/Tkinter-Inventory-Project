import sqlite3
print("WELCOME".center(56,"~"))
##                  
##con=sqlite3.connect("inventorydb.sqlite")
##c=con.cursor()
##c.execute("insert into Stock (icode,iname,rate,qoh) values(1001,'Bread',59,1500)")
##con.commit()
##
##print("Record Inserted")
con=sqlite3.connect("inventorydb.sqlite")
c=con.cursor()
reply="y"
while(reply.upper()=="Y"):
    ic=int(input("Enter ItemCode:"))
    inm=input("Enter ItemName:")
    r=int(input("Enter Rate:"))
    q=int(input("Enter Quantity:"))
    c.execute("insert into Stock (icode,iname,rate,qoh) values(?,?,?,?)",(ic,inm,r,q))
    con.commit()
    print("Record Added".center(62,"-"))
    reply=input("Do You Want To Add More Record?(y/n):")
con.close()
