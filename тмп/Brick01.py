from tkinter import *

def click1():
    label1['text'] = "Ну и отключи звук, душнила."

from1 = Tk()
label1 = Label(text = "Вкус вина из османтуса не изменился... Но где же те, кто разделит воспоминания?")

label1.place(x = 5,y = 5)
Button(text = "Опять дед разговорился", command = click1).place(x = 5,y = 30)

from1.mainloop()