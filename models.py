# https://github.com/coleifer/peewee
from modules.peewee import *
db = SqliteDatabase('db.sqlite3')

class BaseModel(Model):
    class Meta:
        database = db

class Medicalshop_Hsn(BaseModel):
    hsncode = CharField()              


def create_tables_if_not_exist():
    if not Medicalshop_Hsn.table_exists():
        db.create_tables([Medicalshop_Hsn])
            