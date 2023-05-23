import io
import sys

import tkinter as tk
from tkinter import ttk, messagebox, filedialog

from PIL import Image

from DataBase import Database
from Images import ImageHandler

import configparser


class GUI:
    def __init__(self, database):
        self.db = database
        # self.auth()

        config = configparser.ConfigParser()
        config.read('config.conf')
        self.login = config.get('main', 'login')
        self.password = config.get('main', 'password')

        self.root1 = tk.Tk()

        self.center_window(self.root1, 430, 150)
        self.root1.title("Войдите пожалуйста")

        self.file_path = ""
        self.image_handler = ImageHandler(None)

        login_frame = ttk.Frame(self.root1, padding=10)
        login_frame.grid(row=0, column=0)

        # Поля ввода
        login_label = ttk.Label(login_frame, text="Имя пользователя:")
        login_label.grid(row=0, column=0, sticky=tk.W)

        self.login_entry = ttk.Entry(login_frame, width=30)
        self.login_entry.grid(row=0, column=1, padx=5, pady=5)
        pass_label = ttk.Label(login_frame, text="Пароль:")
        pass_label.grid(row=1, column=0, sticky=tk.W)
        self.pass_entry = ttk.Entry(login_frame, width=30)
        self.pass_entry.grid(row=1, column=1, padx=5, pady=5)
        ok_button = ttk.Button(login_frame, text="Войти", command=self.ok)
        ok_button.grid(row=3, column=1, padx=5, pady=5)
        self.root1.mainloop()

        if ((self.logs == self.login) and (self.passw == self.password)):
            self.root = tk.Tk()
            self.root.title("Фонд AmDB")
            self.center_window(self.root, 800, 600)

            tk.Label(self.root, background="#002f55", foreground="white",
                     text="Найти-(Ctrl + F),   Добавить-(Ctrl + N),   Изменить-(Ctrl+O),   "
                          "Удалить-(Ctrl+S),   Выход-(Ctrl+X)",
                     anchor=tk.W, padx=15, font=("Arial", 10)).place(x=5, y=575, width=790, height=15)

            self.create_widgets()
            self.tree.bind("<<ListboxSelect>>", self.on_select)
            self.root.mainloop()
        else:
            messagebox.showerror("Ошибка","Введен неверный пароль")
            sys.exit(0)

    def ok(self):
        self.logs,self.passw=self.login_entry.get(),self.pass_entry.get()
        self.root1.destroy()

    def on_select(self, event):
        global img
        selected_item = event.widget.curselection()
        if selected_item:
            index = selected_item[0]
            data = event.widget.get(index)
            self.city = self.db.get_city_by_name(data)
            im = self.city[3]
            im = Image.open(io.BytesIO(im))
            im = im.resize((330, 165), Image.LANCZOS)
            # im.thumbnail((330, 165))
            # im.save(f'{data}.png')
            # photo_image1 = tk.PhotoImage(file=(f'{data}.png'))
            # self.canvas.create_image(0, 0, image=photoImage1, anchor=tk.NW
            from PIL import ImageTk
            img = ImageTk.PhotoImage(im)
            self.canvas.configure(image=img)

            # Имеет право на существование
            # im.thumbnail((330, 165))
            # im.save(f'{data}.png')
            # photo_image1 = tk.PhotoImage(file=(f'{data}.png'))
            # self.canvas.create_image(0, 0, image=photoImage1, anchor=tk.NW
            # print(photo_image1, "|", img)
            # os.remove(f'{data}.png')
            # self.show_picture_in_gui(data)

            # Если убрать метод программа не будет выводить фото
            self.show_disc_in_gui(data)

    def show_picture_in_gui(self, data):
        # Здесь могла бы быть ваша реклама
        pass

    def show_disc_in_gui(self, data):

        self.city = self.db.get_city_by_name(data)
        self.decription.config(text=self.city[2])
        # если_убрать_этот_текст_то_программа_перестанет_выводить_фото

    def exit_app(self):
        self.root.quit()

    # выбор изображения
    def select_image(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.image_handler.image_data = self.file_path
            image = self.image_handler.get_image((100, 100))
            self.image_path_label.configure(image=image)
            self.image_path_label.image = image

    def show_city_info(self):
        # Очищаем Treeview перед обновлением списка городов
        self.tree.delete(0, tk.END)

        # Получаем список городов из базы данных
        cities = self.db.get_all_cities()
        for city in cities:
            self.tree.insert(0, (city[1]))

    def find_name_city(self):

        find_window = tk.Toplevel(self.root)
        find_window.title("Поиск города")
        self.center_toplevel(find_window,310,100)
        # Фрейм для полей ввода
        find_frame = ttk.Frame(find_window, padding=10)
        find_frame.grid(row=0, column=0)

        # Поля ввода
        name_label = ttk.Label(find_frame, text="Название:")
        name_label.grid(row=0, column=0, sticky=tk.W)

        name_entry = ttk.Entry(find_frame,width=30)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        commit_button = ttk.Button(find_frame, text="Поиск",
                                   command=lambda: check_city(name_entry))
        commit_button.grid(row=4, column=0, padx=5, pady=5)

        def check_city(name_entry):
            # try:
            cities = self.db.get_all_cities()
            for city in cities:
                if name_entry.get() == city[1]:
                    index = self.tree.get(0, "end").index(city[1])
                    self.tree.select_set(index)
                    self.tree.event_generate("<<ListboxSelect>>")

            #         else:
            #             raise Exception(f'Города «{name_entry.get()}» нет в БД')
            #
            # except Exception as e:
            #     messagebox.showerror("Ошибка", f"Ошибка поиска: {str(e)}")

    def create_widgets(self):
        # Фрейм для вывода данных
        main_frame = ttk.Frame(self.root, padding=190)
        main_frame.grid(row=0, column=0)

        # Создаем меню
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        # Создаем пункты меню
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Найти", command=self.find_name_city, accelerator="Ctrl+F")
        file_menu.add_separator()
        file_menu.add_command(label="Добавить", command=self.add_city_window, accelerator="Ctrl+N")
        file_menu.add_command(label="Изменить", command=self.edit_city_window, accelerator="Ctrl+O")
        file_menu.add_command(label="Удалить", command=lambda: self.delete_city(self.city[0]), accelerator="Ctrl+S")
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.exit_app, accelerator="Ctrl+X")
        # Создаем обработчики нажатия клавиш на клавиатуре
        self.root.bind("<Control-f>", lambda event: self.find_name_city())
        self.root.bind("<Control-n>", lambda event: self.add_city_window())
        self.root.bind("<Control-o>", lambda event: self.edit_city_window())
        self.root.bind("<Control-s>", lambda event: self.delete_city(self.city[0]))
        self.root.bind("<Control-x>", lambda event: self.exit_app())

        # Создаем второе подменю
        info_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Справка", menu=info_menu)

        # Команда для отображения немодального окна "Содержание"
        def show_contents():
            contents_window = tk.Toplevel(self.root)
            contents_window.title("Содержание")

            self.center_toplevel(contents_window,300,225)
            contents_window.resizable(False, False)

            contents_label = tk.Label(contents_window, text="База данных 'Известные города РФ'\n\nПозволяет:\n "
                                                            "находить / добавлять / изменять / удалять\n информацию\n\nКлавиши "
                                                            "программы:\nНайти-(Ctrl + F)\nДобавить-(Ctrl + "
                                                            "N)\nИзменить-(Ctrl+O)\nУдалить-(Ctrl+S)\nВыход-(Ctrl+X)")
            contents_label.pack(pady=20)

        info_menu.add_command(label="Содержание", command=show_contents)
        info_menu.add_separator()

        # Команда для отображения модального окна "О программе"
        def show_about():
            about_window = tk.Toplevel(self.root)
            about_window.title("О программе")
            self.center_toplevel(about_window, 300, 75)
            about_window.resizable(False, False)

            about_label = tk.Label(about_window, text="База данных: 'Известные города РФ'\n🧛🏻‍ create by LeoNeed M ")
            about_label.pack(pady=20)

            # Сделать окно модальным
            about_window.grab_set()

        info_menu.add_command(label="О программе", command=show_about)

        # Таблица
        self.tree = tk.Listbox(borderwidth=1, relief="solid",selectmode=tk.BROWSE)
        self.tree.place(x=5, y=5, width=130, height=565)
        # Заполнение таблицы
        self.show_city_info()

        self.canvas = tk.Label(borderwidth=1, relief="solid")
        self.canvas.place(x=140, y=5, width=330, height=565)

        # descFrame = ttk.LabelFrame()
        self.decription = tk.Label(text="", borderwidth=1, relief="solid",wraplength=300, justify="center")
        # descFrame.place(x=330 + 130 + 10, y=5, width=330, height=165)
        self.decription.place(x=330 + 130 + 10 + 7, y=5, width=330, height=565)

    def refresh_table(self):
        # удаляем все записи из таблицы
        self.tree.delete(0, tk.END)
        # добавляем новые записи
        self.show_city_info()
    def center_window(self,window,rW,rH):
        W = window.winfo_screenwidth()
        H = window.winfo_screenheight()
        L = (W - rW) // 2
        T = (H - rH) // 2
        window.geometry(f"{rW}x{rH}+{L}+{T}")
    def center_toplevel(self,window,tW,tH):
        W=self.root.winfo_x()
        H=self.root.winfo_y()
        Wr=self.root.winfo_width()
        Hr=self.root.winfo_height()
        T = W + (Wr // 2)-tW//2
        L = H + (Hr // 2)-tH//2
        window.geometry(f"{tW}x{tH}+{T}+{L}")
    def add_city_window(self):
        # Создание окна

        self.add_window = tk.Toplevel(self.root)
        self.center_toplevel(self.add_window,500,175)
        self.add_window.title("Добавить город")


        # Фрейм для полей ввода
        input_frame = ttk.Frame(self.add_window, padding=10)
        input_frame.grid(row=0, column=0)

        # Поля ввода
        name_label = ttk.Label(input_frame, text="Название:")
        name_label.grid(row=0, column=0, sticky=tk.W)

        self.name_entry = ttk.Entry(input_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        desc_label = ttk.Label(input_frame, text="Описание:")
        desc_label.grid(row=1, column=0, sticky=tk.W)

        self.desc_var = tk.StringVar()
        self.desc_var.set("")
        self.desc_entry = ttk.Entry(input_frame, width=50, textvariable=self.desc_var)
        self.desc_entry.grid(row=1, column=1, padx=5, pady=5)

        image_label = ttk.Label(input_frame, text="Изображение:")
        image_label.grid(row=2, column=0, sticky=tk.W)

        self.image_path = tk.StringVar()
        self.image_path.set("")
        canvas = tk.Canvas(input_frame, width=10, height=10)
        canvas.grid(row=2, column=2, padx=5, pady=5)
        self.image_path_label = ttk.Label(input_frame, textvariable=self.image_path)
        self.image_path_label.grid(row=2, column=1, padx=5, pady=5)

        # image_handler = ImageHandler(None)
        image_button = ttk.Button(input_frame, text="Добавить изображение", command=self.select_image)
        image_button.grid(row=3, column=1, padx=5, pady=5)

        # Фрейм для кнопок
        buttons_frame = ttk.Frame(self.add_window, padding=10)
        buttons_frame.grid(row=1, column=0, sticky=tk.E)

        # Кнопки
        commit_button = ttk.Button(input_frame, text="Применить",
                                   command=lambda: self.db.add_city(self.name_entry.get(), self.desc_entry.get(),
                                                                    self.db.image_to_blob(self.file_path)))
        commit_button.grid(row=4, column=0, padx=5, pady=5)
        cancel_button = ttk.Button(input_frame, text="Закрыть", command=self.close_and_refresh)
        cancel_button.grid(row=4, column=2, padx=5, pady=5)

        # Отображение окна
        self.add_window.grab_set()
        self.root.wait_window(self.add_window)

    def edit_city_window(self):
        # Создание окна
        self.edit_window = tk.Toplevel(self.root)
        self.edit_window.title("Изменить город")
        self.center_toplevel(self.edit_window, 600, 175)
        # Фрейм для полей ввода
        input_frame = ttk.Frame(self.edit_window, padding=10)
        input_frame.grid(row=0, column=0)

        # Поля ввода

        name_label = ttk.Label(input_frame, text=f"Изменить '{self.city[1]}' на:")
        name_label.grid(row=0, column=0, sticky=tk.W)

        self.name_entry = ttk.Entry(input_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.name_entry.insert(0,self.city[1])

        desc_label = ttk.Label(input_frame, text="Описание:")
        desc_label.grid(row=1, column=0, sticky=tk.W)


        self.desc_var = tk.StringVar()
        self.desc_var.set("")
        self.desc_entry = ttk.Entry(input_frame, width=50, textvariable=self.desc_var)
        self.desc_entry.grid(row=1, column=1, padx=5, pady=5)

        self.desc_entry.insert(0, self.city[2])

        image_label = ttk.Label(input_frame, text="Изображение:")
        image_label.grid(row=2, column=0, sticky=tk.W)

        self.image_path = tk.StringVar()
        self.image_path.set("")
        canvas = tk.Canvas(input_frame, width=10, height=10)
        canvas.grid(row=2, column=2, padx=5, pady=5)
        self.image_path_label = ttk.Label(input_frame, textvariable=self.image_path)
        self.image_path_label.grid(row=2, column=1, padx=5, pady=5)

        # image_handler = ImageHandler(None)
        image_button = ttk.Button(input_frame, text="Добавить изображение", command=self.select_image)
        image_button.grid(row=3, column=1, padx=5, pady=5)

        # Фрейм для кнопок
        buttons_frame = ttk.Frame(self.edit_window, padding=10)
        buttons_frame.grid(row=1, column=0, sticky=tk.E)

        # Кнопки
        commit_button = ttk.Button(input_frame, text="Применить",
                                   command=lambda: self.db.edit_city(self.city[0], self.name_entry.get(),
                                                                     self.desc_entry.get(),
                                                                     self.db.image_to_blob(self.file_path)))
        commit_button.grid(row=4, column=0, padx=5, pady=5)
        cancel_button = ttk.Button(input_frame, text="Закрыть", command=self.close_and_refresh_e)
        cancel_button.grid(row=4, column=2, padx=5, pady=5)

        # Отображение окна
        self.edit_window.grab_set()
        self.root.wait_window(self.edit_window)
    def delete_city(self, city_id):
        """Удаление города из базы данных"""
        try:
            self.db.delete_city(city_id)
            messagebox.showinfo("Успешно", "Город успешно удален из базы данных.")
            self.refresh_table()
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка удаления города: {str(e)}")

    def close_and_refresh(self):
        self.add_window.destroy()
        self.refresh_table()
    def close_and_refresh_e(self):
        self.edit_window.destroy()
        self.refresh_table()

if __name__ == "__main__":
    db = Database()
    app = GUI(db)
