import sqlite3
from peewee import *


# Работа с БД (SET DATA)
db = SqliteDatabase('db/database1.db')

# Определяем модели

class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'

class Expense(Model):
    name = CharField()

    class Meta:
        db_table = 'expenses'
class Payment(Model):
    amount = FloatField()
    payment_date = DateField()
    expense_id = ForeignKeyField(Expense)

    class Meta:
        db_table = 'payments'