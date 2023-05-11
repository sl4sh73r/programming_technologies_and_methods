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

    def on_select(self, event):
        selected_item = event.widget.selection()[0]
        city = self.db.get_city_by_id(selected_item)
        self.desc_var.set(city[2])
        img = ImageHandler(city[3]).get_image((300, 300))
        self.image_path_label.configure(image=img)
        self.image_path_label.image = img
    #выбор изолбражения
    def select_image(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.image_handler.image_data = self.file_path
            image = self.image_handler.get_image((100, 100))
            self.image_path_label.configure(image=image)
            self.image_path_label.image = image

    def create_widgets(self):
        # Фрейм для вывода данных
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.grid(row=0, column=0)

        # Кнопки
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

        add_button = ttk.Button(buttons_frame, text="Добавить", command=self.add_city_window)
        add_button.grid(row=0, column=0, padx=5, pady=5)

        edit_button = ttk.Button(buttons_frame, text="Изменить", command=self.edit_city_window)
        edit_button.grid(row=0, column=1, padx=5, pady=5)

        delete_button = ttk.Button(buttons_frame, text="Удалить", command=lambda :self.delete_city(city[0]))
        delete_button.grid(row=0, column=2, padx=5, pady=5)

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
        cities = self.db.get_all_cities()
        for city in cities:
            if city[3]:
                self.tree.insert("", tk.END, text="", image=self.image_path_label, values=(city[0], city[1], city[2]))
            else:
                self.tree.insert("", tk.END, text="", values=(city[0], city[1], city[2]))

    def refresh_table(self):
        # удаление всех элементов из treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # заново заполнение treeview
        cities = self.db.get_all_cities()
        self.images = []
        for city in cities:
            img = ImageTk.PhotoImage(self.db.blob_to_image(city[3]))
            self.images.append(img)
            self.tree.insert("", tk.END, text="", image=img, values=(city[0], city[1], city[2]))

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
        self.image_path_label = ttk.Label(input_frame, textvariable=self.image_path)
        self.image_path_label.grid(row=2, column=1, padx=5, pady=5)

        # image_handler = ImageHandler(None)
        image_button = ttk.Button(input_frame, text="Добавить изображение", command=self.select_image)
        image_button.grid(row=3, column=1, padx=5, pady=5)

        # Фрейм для кнопок
        buttons_frame = ttk.Frame(self.add_window, padding=10)
        buttons_frame.grid(row=1, column=0, sticky=tk.E)
        # Кнопки
        print(self.name_entry.get(), self.desc_entry.get)
        commit_button=ttk.Button(input_frame,text="Применить",
                                 command=lambda: self.db.add_city(self.name_entry.get(),self.desc_entry.get(),self.db.image_to_blob(self.file_path)))
        commit_button.grid(row=4, column=0, padx=5, pady=5)
        cancel_button = ttk.Button(input_frame, text="Закрыть", command=self.close_and_refresh)
        cancel_button.grid(row=4, column=2, padx=5, pady=5)

        # Отображение окна
        self.add_window.grab_set()
        self.root.wait_window(self.add_window)

    def edit_city_window(self):
        # Окно для редактирования города
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Редактировать город")

        # Фрейм для полей ввода
        input_frame = ttk.Frame(edit_window, padding=10)
        input_frame.grid(row=0, column=0)

        # Получение выделенного элемента из списка городов
        selected_item = self.cities_listbox.curselection()
        if not selected_item:
            messagebox.showerror("Ошибка", "Пожалуйста, выберите город для редактирования")
            edit_window.destroy()
            return
        else:
            selected_item = int(selected_item[0])
            city_id = self.cities[selected_item][0]
            name = self.cities[selected_item][1]
            description = self.cities[selected_item][2]

        # Поля ввода
        name_label = ttk.Label(input_frame, text="Название:")
        name_label.grid(row=0, column=0, sticky=tk.W)

        name_entry = ttk.Entry(input_frame, width=50)
        name_entry.insert(0, name)
        name_entry.grid(row=0, column=1)

        desc_label = ttk.Label(input_frame, text="Описание:")
        desc_label.grid(row=1, column=0, sticky=tk.W)

        desc_entry = ttk.Entry(input_frame, width=50)
        desc_entry.insert(0, description)
        desc_entry.grid(row=1, column=1)

        image_label = ttk.Label(input_frame, text="Изображение:")
        image_label.grid(row=2, column=0, sticky=tk.W)

        image_entry = ttk.Entry(input_frame, width=50)
        image_entry.grid(row=2, column=1)

        # browse_button = ttk.Button(input_frame, text="Обзор...", command=lambda: self.browse_image(image_entry))
        # browse_button.grid(row=2, column=2)

        # Фрейм для кнопок
        buttons_frame = ttk.Frame(edit_window, padding=10)
        buttons_frame.grid(row=1, column=0, sticky=tk.E)

        # Кнопки
        save_button = ttk.Button(buttons_frame, text="Сохранить",
                                 command=lambda: self.save_city(city_id, name_entry.get(), desc_entry.get(),
                                                                image_entry.get(), edit_window))
        save_button.pack(side=tk.LEFT, padx=5, pady=5)

        cancel_button = ttk.Button(buttons_frame, text="Отмена", command=edit_window.destroy)
        cancel_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Отображение окна
        edit_window.grab_set()

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

if __name__ == "__main__":
    db = Database()
    app = GUI(db)