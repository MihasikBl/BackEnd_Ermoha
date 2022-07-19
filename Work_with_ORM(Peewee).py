import datetime
from peewee import *
from models.py import *


# Функциональное ядро
with db:
    db.create_tables([Expense,Payment])

print("done")
