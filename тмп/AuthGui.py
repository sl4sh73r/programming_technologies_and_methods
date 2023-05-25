import sys

import tkinter as tk
from tkinter import messagebox


from DataBase import Database
from GUI import GUI
import configparser

class AuthGui:
    def __init__(self):

        self.window = tk.Tk()
        # GUI.center_window(self.window, 450,230)
        self.window.title("LogIn")

        font_header = ('Arial', 15)
        font_entry = ('Arial', 12)
        label_font = ('Arial', 11)
        base_padding = {'padx': 10, 'pady': 8}
        header_padding = {'padx': 10, 'pady': 12}

        main_label = tk.Label(self.window, text='Авторизация', font=font_header, justify=tk.CENTER, **header_padding)
        main_label.pack()

        # метка для поля ввода имени
        username_label = tk.Label(self.window, text='Имя пользователя', font=label_font, **base_padding)
        username_label.pack()

        # поле ввода имени
        self.username_entry = tk.Entry(self.window, bg='#fff', fg='#444', font=font_entry)
        self.username_entry.pack()

        # метка для поля ввода пароля
        password_label = tk.Label(self.window, text='Пароль', font=label_font, **base_padding)
        password_label.pack()

        # поле ввода пароля
        self.password_entry = tk.Entry(self.window, bg='#fff', fg='#444', font=font_entry, show="*")
        self.password_entry.pack()

        # кнопка отправки формы
        send_btn = tk.Button(self.window, text='Войти', command=self.check_data)
        send_btn.pack(**base_padding)

        # запускаем главный цикл окна
        self.window.mainloop()

    def get_data(self):
        enLog,enPass= self.username_entry.get(), self.password_entry.get()
        return enLog,enPass
    def check_data(self):
        config = configparser.ConfigParser()
        config.read('config.conf')
        login = config.get('main', 'login')
        password = config.get('main', 'password')

        enLog,enPass=self.get_data()
        if enLog==login and enPass==password:
            print(login,password)
            self.window.destroy()
            db = Database()
            GUI(db)
if __name__ == "__main__":
    enLog, enPass="",""
    Auapp = AuthGui()



