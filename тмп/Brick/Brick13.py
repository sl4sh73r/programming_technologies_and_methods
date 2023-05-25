from tkinter import *

form1=Tk()
form1.geometry("420x440+100+100")
label1=Label(text="++++")
label1.place(x=5,y=5)
canvas1=Canvas(bg="cyan")
canvas1.place(x=5,y=30,width=400,height=400)
data=1
fileName1=f'{data}.png'
photoImage1=PhotoImage(file=fileName1)
canvas1.create_image(0,0,image=photoImage1,anchor=NW)
form1.mainloop()