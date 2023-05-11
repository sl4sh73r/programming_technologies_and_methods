from tkinter import *

def click1():
    L = ["Сеченов уходит!", "Остань, Храз!"]
    lable1['text'] = "А надо на правую! " + L[buff1.get()]

form1 = Tk()
lable1 = Label(text = "Товарищ майор, вы куда смотрите?")
lable1.place(x = 5, y = 5)
buff1 = IntVar()
Checkbutton(text = "На левую", command = click1, variable = buff1).place(x = 5, y = 30)
form1.mainloop()