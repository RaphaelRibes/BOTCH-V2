from peewee import SqliteDatabase, Model, TextField, IntegerField, FloatField, BooleanField, DateField
import os

db = SqliteDatabase(f"{os.getcwd()}\\data\\database.db")


class BaseTable(Model):
    class Meta:
        database = db


class Membre(BaseTable):
    user_id = IntegerField(null=False, index=True)
    joined_at_timestamp = IntegerField(null=False)
    last_message = TextField(null=False)
    last_message_timestamp = IntegerField(null=False)
    xp = IntegerField(null=False)

