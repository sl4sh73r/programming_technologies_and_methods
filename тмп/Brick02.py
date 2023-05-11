from tkinter import *

def click1():
    label1['text'] = "Да прямо передо мной! Скажи, что это? " + entry1.get()

from1 = Tk()
label1 = Label(text = "Храз! Это че за хрень?! ")
label1.place(x = 5,y = 5)
entry1 = Entry(show = "*")
entry1.place(x = 5, y = 30)
entry1.focus()
#entry1.insert(0, "кто появился?")

Button(text = "Где, майор?", command = click1).place(x = 5,y = 60)

from1.mainloop()