from peewee import SqliteDatabase, Model, TextField, IntegerField, FloatField, BooleanField, DateField
import os

db = SqliteDatabase(f"{os.getcwd()}\\database.db")


class BaseTable(Model):
    class Meta:
        database = db


class Membres(BaseTable):
    user_id = IntegerField(null=False, index=True)  # 403993030572507136
    user_avatar = TextField(null=False)  # https://cdn.discordapp.com/avatars/403993030572507136/b8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f.png
    joined_at_timestamp = IntegerField(null=False)  # 1617873961
    last_message = TextField(null=False)  # "C'est un message|attachment:https://media.discordapp.net/attachments/723652649244819466/997907022085374024/unknown.png"
    last_message_timestamp = IntegerField(null=False)  # 1658086740
    xp = IntegerField(default=0)  # 42
    case = TextField(null=True)  # "Warn:Reason(when)|Tempban:Reason(when)|Ban:Reason|Mute:Reason(when)|Kick:Reason(when)"
    baned_until = DateField(null=True)  # %Y-%m-%d %H:%M:%S
    muted_until = DateField(null=True)  # %Y-%m-%d %H:%M:%S
    birthday = DateField(null=True)  # %Y-%m-%d
    starbotch = TextField(default="")  # "c:123456789m:789456123|" c:channel_id m:message_id
    points_sdlm = IntegerField(default=0)  # 0
    on_the_server = BooleanField(default=True)  # True


class Starbotch(BaseTable):
    sb_message_id = IntegerField(null=False)  # 123456789
    message_id = IntegerField(null=False)  # 123456789
    channel_id = IntegerField(null=False)  # 123456789
    poster_id = IntegerField(null=False, index=True)  # 123456789
    stars = IntegerField(null=False, index=True)  # 42


db.connect()
db.create_tables([Starbotch])
"""Membres.create(
    user_id=354188969472163840,
    user_avatar="https://cdn.discordapp.com/avatars/354188969472163840/ed848761195676bab2a43db1b1315ab8.webp?size=1024",
    joined_at_timestamp=1617873961,
    last_message="!test test",
    last_message_timestamp=1658086740
)"""
