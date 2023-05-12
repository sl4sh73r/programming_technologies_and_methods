from tkinter import *

# Создаем окно
form1 = Tk()

# Создаем функции для команд меню
def new_file():
    print("Создать новый файл")

def open_file():
    print("Открыть файл")

def save_file():
    print("Сохранить файл")

def exit_app():
    form1.quit()

# Создаем меню
menu_bar = Menu(form1)
form1.config(menu=menu_bar)

# Создаем пункты меню
file_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Новый", command=new_file, accelerator="Ctrl+N")
file_menu.add_command(label="Открыть", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Сохранить", command=save_file, accelerator="Ctrl+S")
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit_app,accelerator="Ctrl+X")

# Создаем второе подменю
edit_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Правка", menu=edit_menu)
edit_menu.add_command(label="Вырезать")
edit_menu.add_command(label="Копировать")
edit_menu.add_command(label="Вставить")

# Создаем обработчики нажатия клавиш на клавиатуре
form1.bind("<Control-n>", lambda event: new_file())
form1.bind("<Control-o>", lambda event: open_file())
form1.bind("<Control-x>", lambda event: exit_app())

label1=Label()
label1.place(x=5,y=5)
# Отображаем окно
form1.mainloop()
