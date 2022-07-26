from datetime import datetime
import time
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
    starbotch = TextField(default="")  # "c:123456789m:789456123|" c:channel_id m:message_id
    points_sdlm = IntegerField(default=0)  # 0
    on_the_server = BooleanField(default=True)  # True


class Starbotch(BaseTable):
    sb_message_id = IntegerField(null=False)  # 123456789
    message_id = IntegerField(null=False)  # 123456789
    channel_id = IntegerField(null=False)  # 123456789
    posteur_id = IntegerField(null=False, index=True)  # 123456789
    stars = IntegerField(null=False, index=True)  # 42


db.connect()
db.create_tables([Membres])
n = Membres.get(Membres.user_id == 354188969472163840)
print(n.user_id)
print(n.user_avatar)
print(n.joined_at)
print(n.last_message)
print(n.last_message_date)
print(n.xp)
print(n.case)
print(datetime.fromtimestamp(n.baned_until/1000).strftime("%Y-%m-%d %H:%M:%S"))
print(datetime.fromtimestamp(n.muted_until/1000).strftime("%Y-%m-%d %H:%M:%S"))
print(datetime.fromtimestamp(n.birthday/1000).strftime("%Y-%m-%d %H:%M:%S"))
print(n.starbotch)
print(n.points_sdlm)
print(n.on_the_server)
print("\n")

for n in Starbotch.select().where(Starbotch.stars == 2):
    print(n.sb_message_id)
    print(n.message_id)
    print(n.channel_id)
    print(n.posteur_id)
    print(n.stars)
    print("\n")
