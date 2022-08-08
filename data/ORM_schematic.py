from datetime import datetime
import time

import peewee
from peewee import SqliteDatabase, Model, TextField, IntegerField, FloatField, BooleanField, DateField
import os

db = SqliteDatabase(f"{os.getcwd()}\\database.db")


class BaseTable(Model):
    class Meta:
        database = db


class Membres(BaseTable):
    user_id = IntegerField(null=False, index=True)  # 403993030572507136
    user_avatar = TextField(null=False)  # https://cdn.discordapp.com/avatars/403993030572507136/b8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f.png
    joined_at = DateField(null=False)  # 1617873961
    last_message = TextField(null=True)  # "C'est un message|attachment:https://media.discordapp.net/attachments/723652649244819466/997907022085374024/unknown.png"
    last_message_date = DateField(null=True)  # 1658086740
    xp = IntegerField(default=0)  # 42
    case = TextField(default="")  # "Warn:Reason(when)|Tempban:Reason(when)|Ban:Reason|Mute:Reason(when)|Kick:Reason(when)"
    baned_until = DateField(null=True)  # %Y-%m-%d %H:%M:%S
    muted_until = DateField(null=True)  # %Y-%m-%d %H:%M:%S
    birthday = DateField(null=True)  # %Y-%m-%d
    on_the_server = BooleanField(default=True)  # True


class Starbotch(BaseTable):
    sb_message_id = IntegerField(null=False)  # 123456789
    message_id = IntegerField(null=False)  # 123456789
    channel_id = IntegerField(null=False)  # 123456789
    posteur_id = IntegerField(null=False, index=True)  # 123456789
    stars = IntegerField(null=False, index=True)  # 42


class Broadcast(BaseTable):
    user_id = IntegerField(null=False, index=True)  # 403993030572507136
    message_id = IntegerField(null=False, index=True)  # 123456789
    preview_message_id = IntegerField(null=False, index=True)  # 123456789
    message = TextField(null=False)  # "C'est un message|attachment:https://media.discordapp.com/attachments/723652649244819466/997907022085374024/unknown.png"
    attachment = TextField(null=True)  # https://media.discordapp.com/attachments/723652649244819466/997907022085374024/unknown.png
    target = TextField(null=False)  # "sdlm" or "sb" or "botchnews"


class Sdlm(BaseTable):
    user_id = IntegerField(null=False, index=True)  # 403993030572507136
    points = IntegerField(default=0)  # 42
    posteur = BooleanField(default=False, index=True)  # True
    image_link = TextField(null=True)  # https://media.discordapp.com/attachments/723652649244819466/997907022085374024/unknown.png


db.connect()
db.create_tables([Sdlm])
broadcast = Broadcast.select().where(Broadcast.user_id == 123)

