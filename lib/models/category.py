# models/Category.py

from models import CONN, CURSOR

class Category:
    def __init__(self, id, name, description):
        self._id = id
        self.name = name
        self.description = description

    def __str__(self):
        return f'Category(id={self.id}, name={self.name}, description={self.description})'

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not value:
            raise ValueError("Description cannot be empty")
        self._description = value

    @classmethod
    def create_table(cls):
        CURSOR.execute('''CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT NOT NULL
        )''')
        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute('DROP TABLE IF EXISTS categories')
        CONN.commit()

    @classmethod
    def create(cls, name, description):
        CURSOR.execute('INSERT INTO categories (name, description) VALUES (?, ?)', (name, description))
        CONN.commit()
        return cls(CURSOR.lastrowid, name, description)

    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM categories')
        rows = CURSOR.fetchall()
        return [cls(*row) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute('SELECT * FROM categories WHERE name = ?', (name,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None

    @classmethod
    def find_by_id(cls, id_):
        CURSOR.execute('SELECT * FROM categories WHERE id = ?', (id_,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None

    def update(self):
        CURSOR.execute('UPDATE categories SET name = ?, description = ? WHERE id = ?', (self.name, self.description, self.id))
        CONN.commit()

    def delete(self):
        CURSOR.execute('DELETE FROM categories WHERE id = ?', (self.id,))
        CONN.commit()

    def products(self):
        from models.product import Product
        CURSOR.execute('SELECT * FROM products WHERE category_id = ?', (self.id,))
        rows = CURSOR.fetchall()
        return [Product(*row) for row in rows]
