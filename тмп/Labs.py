import tkinter as tk
import sqlite3
from PIL import Image, ImageTk
import io
from tkinter import filedialog

def create_connection():
    print('1-1')
    conn = None
    try:
        conn = sqlite3.connect('AmDB.db')
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    print('2-1')
    sql_create_cities_table = '''CREATE TABLE IF NOT EXISTS cities (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    population INTEGER NOT NULL,
                                    image BLOB
                                );'''
    try:
        c = conn.cursor()
        c.execute(sql_create_cities_table)
    except sqlite3.Error as e:
        print(e)

def insert_city(conn, city):
    sql_insert_city = '''INSERT INTO cities(name, population, image)
                         VALUES(?,?,?)'''
    try:
        c = conn.cursor()
        c.execute(sql_insert_city, city)
        conn.commit()
        return c.lastrowid
    except sqlite3.Error as e:
        print(e)
        return -1

def update_city(conn, city):
    sql_update_city = '''UPDATE cities
                        SET name = ?,
                            population = ?,
                            image = ?
                        WHERE id = ?'''
    try:
        c = conn.cursor()
        c.execute(sql_update_city, city)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def delete_city(conn, id):
    sql_delete_city = '''DELETE FROM cities WHERE id = ?'''
    try:
        c = conn.cursor()
        c.execute(sql_delete_city, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def select_all_cities(conn):
    sql_select_all_cities = '''SELECT id, name, population, image FROM cities'''
    try:
        c = conn.cursor()
        c.execute(sql_select_all_cities)
        rows = c.fetchall()
        return rows
    except sqlite3.Error as e:
        print(e)
        return []

def get_image_data(filename):
    with open(filename, 'rb') as f:
        return f.read()

def get_image_from_data(data):
    return Image.open(io.BytesIO(data))

def browse_image():
    global image_path
    file_path = filedialog.askopenfilename(
        initialdir="/",
        title="Выбрать изображение",
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )
    if file_path:
        image_path = file_path
        image_preview.config(text=image_path)

def on_select(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        id, name, population, image = data.split('|')
        image = get_image_from_data(image)
        photo = ImageTk.PhotoImage(image)
        name_var.set(name)
        population_var.set(population)
        image_label.config(image=photo)
        image_label.image = photo

def refresh_listbox():
    cities = select_all_cities(conn)
    city_listbox.delete(0, tk.END)
    for city in cities:
        id, name, population, image_data = city
        image = get_image_from_data(image_data)
        city_listbox.insert(tk.END, f"{id}|{name}|{population}|{image}")
def drop(event):
    global dropped_image_data
    dropped_image_data = event.data['text']
    image = get_image_from_data(dropped_image_data)
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

def handle_open_db():
    cursor = conn.cursor()
    cursor.execute("SELECT id,name, population, image FROM cities")
    rows = cursor.fetchall()
    for row in rows:
        id = row[0]
        name = row[1]
        population = row[2]
        image_data=row[3]
        # Отображаем изображение из базы данных
        img = ImageTk.PhotoImage(Image.open(image_data))
        img_label = tk.Label(root, image=img)
        img_label.image = img
        img_label.pack()
        image_label.grid(row=0, column=2)
        # Отображаем название и население города
        name_label = tk.Label(root, text=name)
        name_label.grid(row=1, column=2)
        population_label = tk.Label(root, text=population)
        population_label.pack()
        population_label.grid(row=2, column=2)
    conn.close()

# функция для создания окна "О программе"
def show_about():
    about_window = tk.Toplevel(root)
    about_window.title("О программе")
    about_window.geometry("300x100")

    about_label = tk.Label(about_window, text="Программа для работы с базой данных городов")
    about_label.pack(pady=10)

# функция для создания окна "Справка"
def show_help():
    help_window = tk.Toplevel(root)
    help_window.title("Справка")
    help_window.geometry("300x100")

    help_label = tk.Label(help_window, text="Справка по программе")
    help_label.pack(pady=10)

# функция-обработчик для меню "О программе"
def handle_about():
    show_about()

# функция-обработчик для меню "Справка"
def handle_help():
    show_help()

# функция-обработчик для кнопки "Добавить"
def handle_add():
    name = name_entry.get()
    population = int(population_entry.get())
    image_data = None
    if image_path:
        image_data = get_image_data(image_path)
    city = (name, population, image_data)
    insert_city(conn, city)
    refresh_listbox()

# функция-обработчик для кнопки "Обновить"
def handle_update():
    selection = city_listbox.curselection()
    if selection:
        index = selection[0]
        data = city_listbox.get(index)
        id, _, _, _ = data.split('|')
        name = name_entry.get()
        population = int(population_entry.get())
        image_data = None
        if image_path:
            image_data = get_image_data(image_path)
        city = (name, population, image_data, int(id))
        update_city(conn, city)
        refresh_listbox()

# функция-обработчик для кнопки "Удалить"
def handle_delete():
    selection = city_listbox.curselection()
    if selection:
        index = selection[0]
        data = city_listbox.get(index)
        id, _, _, _ = data.split('|')
        delete_city(conn, int(id))
        refresh_listbox()

# функция-обработчик для кнопки "Выбрать изображение"
def handle_browse():
    browse_image()

# создание главного окна
print(1)
conn = create_connection()
print(2)
create_table(conn)
print(3)
root = tk.Tk()
print(4)
root.title("Города мира")

# создание рамки для ввода данных города
input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=10)

# создание метки и поля для ввода названия города
name_label = tk.Label(input_frame, text="Название:")
name_label.grid(row=0, column=0, sticky="e")

name_var = tk.StringVar()
name_entry = tk.Entry(input_frame, textvariable=name_var)
name_entry.grid(row=0, column=1)

# создание метки и поля для ввода населения города
population_label = tk.Label(input_frame, text="Население:")
population_label.grid(row=1, column=0, sticky="e")

population_var = tk.IntVar()
population_entry = tk.Entry(input_frame, textvariable=population_var)
population_entry.grid(row=1, column=1)

# создание метки и кнопки для выбора изображения города
image_label = tk.Label(input_frame, width=100, height=25, relief="groove", borderwidth=2)
image_label.grid(row=2, column=2, columnspan=2, padx=10, pady=10)

image_preview = tk.Label(input_frame, text="Нажмите, чтобы выбрать изображение")
image_preview.grid(row=3, column=0, columnspan=2)

browse_button = tk.Button(input_frame, text="Выбрать изображение", command=handle_browse)
browse_button.grid(row=4, column=0, columnspan=2, pady=10)

# создание кнопок для управления данными городов
button_frame = tk.Frame(root)
button_frame.pack(padx=10, pady=10)

add_button = tk.Button(button_frame, text="Добавить", command=lambda: insert_city(conn, (name_var.get(), population_var.get(), image_path)))
add_button.grid(row=0, column=0, padx=5)

update_button = tk.Button(button_frame, text="Изменить", command=lambda: update_city(conn, (name_var.get(), population_var.get(), image_path, city_id)))
update_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Удалить", command=lambda: delete_city(conn, city_id))
delete_button.grid(row=0, column=2, padx=5)

# создание списка городов
list_frame = tk.Frame(root)
list_frame.pack(padx=10, pady=10)

city_listbox = tk.Listbox(list_frame, width=60, height=15)
city_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
city_listbox.bind('<<ListboxSelect>>', on_select)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
city_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=city_listbox.yview)

refresh_button = tk.Button(list_frame, text="Обновить", command=refresh_listbox)
refresh_button.pack(pady=5)

# создание фрейма для деталей города
detail_frame = tk.Frame(root)
detail_frame.pack(padx=10, pady=10)

name_label = tk.Label(detail_frame, text="Название:")
name_label.grid(row=0, column=0, sticky=tk.W)

name_var = tk.StringVar()
name_entry = tk.Entry(detail_frame, textvariable=name_var)
name_entry.grid(row=0, column=1, padx=5, pady=5)

population_label = tk.Label(detail_frame, text="Население:")
population_label.grid(row=1, column=0, sticky=tk.W)

population_var = tk.StringVar()
population_entry = tk.Entry(detail_frame, textvariable=population_var)
population_entry.grid(row=1, column=1, padx=5, pady=5)

image_label = tk.Label(detail_frame)
image_label.grid(row=2, column=0, columnspan=2)

# drop_target = tk.Label(detail_frame, text="Перетащите изображение сюда")
# drop_target.grid(row=3, column=0, columnspan=2, pady=5)

# регистрация обработчика перетаскивания на фрейме деталей города
# detail_frame.bind("<Drop>", drop)

# создание меню
menu_bar = tk.Menu(root)
# создание меню "Файл"
file_menu = tk.Menu(menu_bar, tearoff=False)
file_menu.add_command(label="Открыть", command=handle_open_db)
file_menu.add_command(label="Сохранить")
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.quit)

menu_bar.add_cascade(label="Файл", menu=file_menu)

# создание меню "Редактирование"
edit_menu = tk.Menu(menu_bar, tearoff=False)
edit_menu.add_command(label="Добавить", command=handle_add)
edit_menu.add_command(label="Обновить", command=handle_update)
edit_menu.add_command(label="Удалить", command=handle_delete)
edit_menu.add_separator()
edit_menu.add_command(label="Обновить список", command=handle_update)

menu_bar.add_cascade(label="Редактирование", menu=edit_menu)

help_menu = tk.Menu(menu_bar, tearoff=False)
help_menu.add_command(label="О программе", command=show_about)

menu_bar.add_cascade(label="Справка", menu=help_menu)

root.config(menu=menu_bar)

# запуск приложения
root.mainloop()


