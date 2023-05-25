from tkinter import *
from sqlite3 import *
cursor1=connect("SqLite.db").cursor()
# cursor1.execute("CREATE TABLE table1(ID INTEGER,item TEXT,image BLOB)")
cursor1.execute("DELETE FROM table1")
sql1="INSERT INTO table1(id,item,image) VALUES (?,?,?);"
data1=[]
for i in range(1,4):
    id=i
    item=f"Пушок{i}"
    with open(f"Cat\Cat{i}.png",mode="rb") as F:
        image=F.read()
    data1.append((id,item,image))
cursor1.executemany(sql1,data1)
cursor1.connection.commit()

cursor1.execute("SELECT * FROM table1 WHERE id=3;")
record1=cursor1.fetchall()
cursor1.connection.close()

form1=Tk()
photoImage1=PhotoImage(data=record1[0][2])
Label(image=photoImage1).pack()
form1.mainloop()