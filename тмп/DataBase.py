import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('AmDB.db')
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS cities (id INTEGER PRIMARY KEY, name TEXT, description TEXT, image BLOB)")
        self.conn.commit()

    def add_city(self, name, description, image_blob):
        print(image_blob)
        self.cur.execute("INSERT INTO cities (name, description, image) VALUES (?, ?, ?)",
                         (name, description, image_blob))
        self.conn.commit()
        print('add_city-отработал')

    def delete_city(self, id):
        self.cur.execute("DELETE FROM cities WHERE id=?", (id,))
        self.conn.commit()

    def edit_city(self, id, name, description, image_blob):
        # Get the city with the given id
        city = self.get_city_by_id(id)
        if not city:
            print("City not found")
            return

        # Update the fields if they are not None
        if name=="": name=city[1]
        if description=="": description=city[2]
        if image_blob is None: image_blob=city[3]

        # Update the city in the database
        self.cur.execute("UPDATE cities SET name=?, description=?, image=? WHERE id=?",
                         (name, description, image_blob, id))
        self.conn.commit()
    def get_all_cities(self):
        self.cur.execute("SELECT * FROM cities")
        return self.cur.fetchall()

    def get_city_by_id(self, id):
        self.cur.execute("SELECT * FROM cities WHERE id=?", (id,))
        return self.cur.fetchone()
    def get_city_by_name(self, name):
        self.cur.execute("SELECT * FROM cities WHERE name=?", (name,))
        return self.cur.fetchone()

    def close_connection(self):
        self.conn.close()

    def image_to_blob(self, image_path):
        try:
            with open(image_path, 'rb') as f:
                img_bytes = f.read()
            return sqlite3.Binary(img_bytes)
            print('image_to_blob-отработал')
        except FileNotFoundError as e:
            print("Файла нет")

