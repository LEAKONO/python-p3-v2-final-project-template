from models import CONN, CURSOR

class Product:
    def __init__(self, id, name, price, category_id, supplier_id):
        self._id = id
        self.name = name
        self.price = price
        self.category_id = category_id
        self.supplier_id = supplier_id

    def __str__(self):
        return f'Product(id={self.id}, name={self.name}, price={self.price}, category_id={self.category_id}, supplier_id={self.supplier_id})'

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
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        if value < 0:
            raise ValueError("Category ID cannot be negative")
        self._category_id = value

    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        if value < 0:
            raise ValueError("Supplier ID cannot be negative")
        self._supplier_id = value

    @classmethod
    def create_table(cls):
        CURSOR.execute('''CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL CHECK (price >= 0),
            category_id INTEGER NOT NULL,
            supplier_id INTEGER NOT NULL,  -- Add a new column for supplier_id
            FOREIGN KEY (category_id) REFERENCES categories(id),
            FOREIGN KEY (supplier_id) REFERENCES suppliers(id)  -- Define the foreign key constraint for supplier_id
        )''')
        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute('DROP TABLE IF EXISTS products')
        CONN.commit()

    @classmethod
    def create(cls, name, price, category_id, supplier_id):
        CURSOR.execute('INSERT INTO products (name, price, category_id, supplier_id) VALUES (?, ?, ?, ?)', (name, price, category_id, supplier_id))
        CONN.commit()
        return cls(CURSOR.lastrowid, name, price, category_id, supplier_id)

    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM products')
        rows = CURSOR.fetchall()
        return [cls(*row) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute('SELECT * FROM products WHERE name = ?', (name,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None

    @classmethod
    def find_by_id(cls, id_):
        CURSOR.execute('SELECT * FROM products WHERE id = ?', (id_,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None

    def update(self):
        CURSOR.execute('UPDATE products SET name = ?, price = ?, category_id = ?, supplier_id = ? WHERE id = ?', (self.name, self.price, self.category_id, self.supplier_id, self.id))
        CONN.commit()

    def delete(self):
        CURSOR.execute('DELETE FROM products WHERE id = ?', (self.id,))
        CONN.commit()
