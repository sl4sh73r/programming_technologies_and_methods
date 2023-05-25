from tkinter import *

def click1(e):
    label1['text'] = "Давай: " + listbox1.get(listbox1.curselection())

from1 = Tk()
label1 = Label(text = "Какое оружие, майор?")
label1.place(x = 5,y = 5)

list1 = ["Паштет", "Лиса", "Калаш", "Дробовик", "Звездочка", "Крепыш", "Доминатор", "КС-23", "Снежок"]
listbox1 = Listbox(listvariable = Variable(value = list1))
listbox1.place(x = 5, y = 30)

listbox1.bind("<<ListboxSelect>>", click1)

from1.mainloop()

#for i in range(len(list1)):
#    listbox1.insert(i, list1[i])