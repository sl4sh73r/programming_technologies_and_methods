from tkinter import *
def click1():
    canvas1.create_rectangle(10,20,100,50,fill="red",outline="white")
    canvas1.create_line(10, 20, 100, 50, fill="green")
form1=Tk()
label1=Label(text="++++")
label1.place(x=5,y=40)
Button(text="Жмяк",command=click1).place(x=5,y=5)
canvas1=Canvas(bg="cyan")
canvas1.place(x=5,y=60,width=190,height=140)
form1.mainloop()