import sqlite3

CONN = sqlite3.connect('shopping.db')
CURSOR = CONN.cursor()
