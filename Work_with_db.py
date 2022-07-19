import sqlite3

with sqlite3.connect('db/database.db') as db:
    cursor = db.cursor()
    query = """ CREATE TABLE IF NOT EXISTS expenses(id INTEGER, name TEXT) """
    query1 = """INSERT INTO expenses(name,id) VALUES('УПАКОВКА',1)"""
    query2 = """INSERT INTO expenses(name,id) VALUES('ЛЕНТА',2)"""
    query3 = """INSERT INTO expenses(name,id) VALUES('НАКЛЕЙКИ',3)"""
    query4 = """INSERT INTO expenses(name,id) VALUES('БАНТЫ',4)"""
    query5 = """INSERT INTO expenses(name,id) VALUES('БУМАГА',5)"""

    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)
    cursor.execute(query4)
    cursor.execute(query5)
    db.commit()