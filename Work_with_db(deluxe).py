import datetime
import sqlite3
from numpy import insert

def get_timestamp(y,m,d):
    return datetime.datetime.timestamp(datetime.datetime(y,m,d))

def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()

#Создание в БД таблицы Расходы(payments)

# with sqlite3.connect('db/database.db') as db:
#     cursor = db.cursor()
#     query =""" CREATE TABLE IF NOT EXISTS payments(
#         id INTEGER,
#         amount REAL,
#         payment_date INTEGER,
#         expensive_id INTEGER
#     )"""
#     cursor.execute(query)
#     db.commit()

#Добавление кортежа со значениями

# insert_payments = [
#     (1, 120, get_timestamp(2022,1,1),1),
#     (2, 12, get_timestamp(2022,1,2),3),
#     (3, 20, get_timestamp(2022,1,3),2),
#     (4, 20, get_timestamp(2022,1,4),4),
#     (5, 20, get_timestamp(2022,1,5),3),
#     (6, 20, get_timestamp(2022,1,2),2),
#     (7, 20, get_timestamp(2022,1,1),1),
#     (8, 20, get_timestamp(2022,1,4),5),
# ]

# with sqlite3.connect('db/database.db') as db:
#     cursor = db.cursor()
#     query = """INSERT INTO payments(id,amount,payment_date,expensive_id)
#                                 VALUES(?,?,?,?); """

#     cursor.executemany(query,insert_payments)
#     db.commit()
#     print(cursor.rowcount,"Строк добавлено")

with sqlite3.connect('db/database.db') as db:
    cursor = db.cursor()
    query = """SELECT * FROM payments"""

    cursor.execute(query)
    sum=0
    for result in cursor:
        sum+=result[1]
        print(result)
    print('Total = ',sum)
