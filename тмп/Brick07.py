from tkinter import *

form1 = Tk()
text1 = Text()
text1.place(x = 5, y = 5, width = 185, height = 185)

for i in range(10):
    text1.insert(END, str(i) + ". Студент\n")
text1.insert(3.4, "+") #первая цифра это y, вотрая - х
form1.mainloop()