import io
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
from typing import List, Tuple
from DataBase import Database
from Images import ImageHandler
from tkinter import *

class GUI:
    def __init__(self, database):
        self.db = database

        self.root = tk.Tk()
        self.root.title("Фонд AmDB")
        self.file_path = ""
        self.image_handler = ImageHandler(None)
        self.create_widgets()
        self.root.mainloop()
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

    # def on_select(self, event):
    #     selected_item = event.widget.selection()[0]
    #     city = self.db.get_city_by_id(selected_item)
    #     self.desc_var.set(city[2])
    #     img = ImageHandler(city[3]).get_image((300, 300))
    #     self.image_path_label.configure(image=img)
    #     self.image_path_label.image = img

    def on_select(self, event):
        selected_item = event.widget.selection()[0]
        self.city = self.db.get_city_by_id(selected_item)
        self.desc_var.set(self.city[2])
        # Обновляем картинку города
        img = ImageTk.PhotoImage(Image.open(self.city[3]))
        self.image_path_label.configure(image=img)
        self.image_path_label.image = img

    def exit_app(self):
        self.root.quit()
    #выбор изолбражения
    def select_image(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.image_handler.image_data = self.file_path
            image = self.image_handler.get_image((100, 100))
            self.image_path_label.configure(image=image)
            self.image_path_label.image = image

    def show_city_info(self):
        # Очищаем Treeview перед обновлением списка городов
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Получаем список городов из базы данных
        cities = self.db.get_all_cities()

        # Заполняем Treeview новыми данными
        for city in cities:
            self.tree.insert("", "end", values=(city[0], city[1], city[2]))

    def create_widgets(self):
        # Фрейм для вывода данных
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.grid(row=0, column=0)

        # Создаем меню
        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)
        # Создаем пункты меню
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Добавить", command=self.add_city_window, accelerator="Ctrl+N")
        file_menu.add_command(label="Изменить", command=self.edit_city_window, accelerator="Ctrl+O")
        file_menu.add_command(label="Удалить", command=lambda :self.delete_city(self.city[0]), accelerator="Ctrl+S")
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.exit_app, accelerator="Ctrl+X")
        # Создаем обработчики нажатия клавиш на клавиатуре
        self.root.bind("<Control-n>", lambda event: self.add_city_window())
        self.root.bind("<Control-o>", lambda event: self.edit_city_window())
        self.root.bind("<Control-x>", lambda event: self.exit_app())

        # Создаем второе подменю
        info_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Справка", menu=info_menu)
        info_menu.add_command(label="Содержание")
        info_menu.add_separator()
        info_menu.add_command(label="О программе",command=self.show_about)


        # Таблица
        self.tree = ttk.Treeview(main_frame, columns=("ID", "Name", "Description"))
        self.tree.heading("#0", text="Изображение", anchor=tk.CENTER)
        self.tree.heading("#1", text="ID", anchor=tk.CENTER)
        self.tree.heading("#2", text="Название", anchor=tk.CENTER)
        self.tree.heading("#3", text="Описание", anchor=tk.CENTER)
        self.tree.column("#0", width=100, stretch=tk.NO)
        self.tree.column("#1", width=50, stretch=tk.NO)
        self.tree.column("#2", width=150, stretch=tk.NO)
        self.tree.column("#3", width=300, stretch=tk.NO)
        self.tree.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        # Заполнение таблицы
        self.show_city_info()

    def refresh_table(self):
        def refresh_table(self):
            # удаляем все записи из таблицы
            for i in self.tree.get_children():
                self.tree.delete(i)

            # добавляем новые записи
            self.show_city_info()

            # выделяем первую запись в таблице
            if self.tree.get_children():
                self.tree.selection_set(self.tree.get_children()[0])
                self.on_select(None)

    def add_city_window(self):
        # Создание окна
        self.add_window = tk.Toplevel(self.root)
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
        self.desc_entry = ttk.Entry(input_frame, width=50,textvariable=self.desc_var)
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
        commit_button=ttk.Button(input_frame,text="Применить",
                                 command=lambda: self.db.add_city(self.name_entry.get(),self.desc_entry.get(),self.db.image_to_blob(self.file_path)))
        commit_button.grid(row=4, column=0, padx=5, pady=5)
        cancel_button = ttk.Button(input_frame, text="Закрыть", command=self.close_and_refresh)
        cancel_button.grid(row=4, column=2, padx=5, pady=5)

        # Отображение окна
        self.add_window.grab_set()
        self.root.wait_window(self.add_window)

    def edit_city_window(self):
        pass

    def delete_city(self, city_id):
        """Удаление города из базы данных"""
        try:
            self.db.delete_city(city_id)
            messagebox.showinfo("Успешно", "Город успешно удален из базы данных.")
            self.refresh_table()
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка удаления города: {str(e)}")
    def show_about(self):
        about_window = tk.Toplevel(self.root)
        about_window.title("О программе")
        about_window.geometry("300x100")

        about_label = tk.Label(about_window, text="Программа для работы с базой данных городов")
        about_label.pack(pady=10)
    def close_and_refresh(self):
        self.add_window.destroy()
        self.refresh_table()

if __name__ == "__main__":
    db = Database()
    app = GUI(db)
