from tkinter import *

def click1():
    L = ["Увернулся!", "Помер", "Нужна хилка!"]
    lable1['text'] = "пироги! " + L[buff1.get()]

form1 = Tk()
lable1 = Label(text = "Сверху, товарищ майор!")
lable1.place(x = 5, y = 5)
buff1 = IntVar()

Radiobutton(text = "Нажмите q", value = 0, command = click1, variable = buff1).place(x = 5, y = 30)
Radiobutton(text = "Нажмите t", value = 1, command = click1, variable = buff1).place(x = 5, y = 60)
Radiobutton(text = "Нажмите e", value = 2, command = click1, variable = buff1).place(x = 5, y = 90)
form1.mainloop()