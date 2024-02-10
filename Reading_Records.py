import sqlite3

con=sqlite3.connect("inventorydb.sqlite")
c=con.cursor()
a=c.execute("select * from Stock")
b=a.fetchall()
for line in b:
    print(line)
con.close()
