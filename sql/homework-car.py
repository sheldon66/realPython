#create database called "cars" and add a table called "inventory" which contains following fields:"make", "model", "quantity"

import sqlite3
conn = sqlite3.connect("cars.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE inventory(Make TEXT, Model TEXT, quantity INT)""")

conn.close()
