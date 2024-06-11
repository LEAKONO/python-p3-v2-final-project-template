# models/Supplier.py

from models import CONN, CURSOR

class Supplier:
    def __init__(self, id, name, contact_email, address):
        self._id = id
        self.name = name
        self.contact_email = contact_email
        self.address = address

    def __str__(self):
        return f'Supplier(id={self.id}, name={self.name}, contact={self.contact_email}, address={self.address})'

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
    def contact_email(self):
        return self._contact_email

    @contact_email.setter
    def contact_email(self, value):
        if not value:
            raise ValueError("Contact email cannot be empty")
        self._contact_email = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if not value:
            raise ValueError("Address cannot be empty")
        self._address = value

    @classmethod
    def create_table(cls):
        CURSOR.execute('''CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            contact_email TEXT NOT NULL,
            address TEXT NOT NULL
        )''')
        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute('DROP TABLE IF EXISTS suppliers')
        CONN.commit()

    @classmethod
    def create(cls, name, contact_email, address):
        CURSOR.execute('INSERT INTO suppliers (name, contact_email, address) VALUES (?, ?, ?)', (name, contact_email, address))
        CONN.commit()
        return cls(CURSOR.lastrowid, name, contact_email, address)

    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM suppliers')
        rows = CURSOR.fetchall()
        return [cls(*row) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute('SELECT * FROM suppliers WHERE name = ?', (name,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None

    @classmethod
    def find_by_id(cls, id_):
        CURSOR.execute('SELECT * FROM suppliers WHERE id = ?', (id_,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None

    def update(self):
        CURSOR.execute('UPDATE suppliers SET name = ?, contact_email = ?, address = ? WHERE id = ?', (self.name, self.contact_email, self.address, self.id))
        CONN.commit()

    def delete(self):
        CURSOR.execute('DELETE FROM suppliers WHERE id = ?', (self.id,))
        CONN.commit()

    def products(self):
        from models.product import Product
        CURSOR.execute('SELECT * FROM products WHERE supplier_id = ?', (self.id,))
        rows = CURSOR.fetchall()
        return [Product(*row) for row in rows]

