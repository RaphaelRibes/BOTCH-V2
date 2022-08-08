import discord
from discord.ext import commands
import json
from main import BOTCH
from peewee import SqliteDatabase
from data.ORM_schematic import Membres, Starbotch, Broadcast, Sdlm
import os


class Database(commands.Cog):

    def __init__(self, bot: BOTCH):
        self.bot = bot
        self.file = "database"
        self.database = SqliteDatabase(f"{os.getcwd()}\\data\\database.db")
        self.database.connect()

    @staticmethod
    def get_member(member_id, member: discord.Member):
        try:
            return Membres.get(Membres.user_id == member_id)
        except:
            last_message = await member.history(limit=1)
            if len(last_message[0].attachments) > 0:
                last_message_content = last_message[0].content + '|attachment:' + last_message[0].attachments[0].url
            membre = Membres.create(
                user_id=member_id,
                user_avatar=member.avatar_url,
                join_at=member.joined_at.timestamp() * 1000,
                last_message_date=last_message[0].created_at.timestamp() * 1000,
                last_message=last_message_content,
            )
            membre.save()
            return membre

    @staticmethod
    def get_member_sb_by_id(member_id):
        try:
            starbotch: list = Starbotch.select().where(Starbotch.poster_id == member_id)
            return starbotch
        except:
            return None

    @staticmethod
    def get_sb_by_stars(stars):
        try:
            starbotch: list = Starbotch.select().where(Starbotch.stars == stars)
            return starbotch
        except:
            return None

    @staticmethod
    def create_sb(sb_message_id, message_id, channel_id, posteur_id, stars):
        sb = Starbotch.create(
            sb_message_id=sb_message_id,
            message_id=message_id,
            channel_id=channel_id,
            posteur_id=posteur_id,
            stars=stars
        )
        sb.save()
        return sb

    @staticmethod
    def modify_sb(msg_id, stars):
        try:
            starbotch = Starbotch.get(Starbotch.message_id == msg_id)
            starbotch.stars = stars
            starbotch.save()
            return starbotch
        except:
            return None

    @staticmethod
    def remove_sb(msg_id: int):
        Starbotch.delete().where(Starbotch.sb_message_id == msg_id).execute()

    @staticmethod
    def create_broadcast(message_id, user_id, preview_message_id, message, target, attachment=None):
        broadcast = Broadcast.create(
            message_id=message_id,
            user_id=user_id,
            preview_message_id=preview_message_id,
            message=message,
            target=target
        )
        if attachment is not None: broadcast.attachment = attachment

        broadcast.save()
        return broadcast

    @staticmethod
    def modify_broadcast(msg_id, message, attachment=None):
        try:
            broadcast = Broadcast.get(Broadcast.message_id == msg_id)
            broadcast.message = message
            if attachment is not None: broadcast.attachment = attachment
            broadcast.save()
            return broadcast
        except:
            return None

    @staticmethod
    def get_broadcast(user_id):
        try:
            broadcast: list = Broadcast.select().where(Broadcast.user_id == user_id)
            return broadcast
        except:
            return None

    @staticmethod
    def remove_broadcast(msg_id: int):
        Broadcast.delete().where(Broadcast.message_id == msg_id).execute()

    @staticmethod
    def create_sdlm(user_id: int, points: int, posteur: bool, image_link: str):
        sdlm = Sdlm.create(
            user_id=user_id,
            points=points,
            posteur=posteur,
            image_link=image_link
        )
        sdlm.save()
        return sdlm

    @staticmethod
    def modify_sdlm(msg_id, message, attachment=None):
        try:
            broadcast = Broadcast.get(Broadcast.message_id == msg_id)
            broadcast.message = message
            if attachment is not None: broadcast.attachment = attachment
            broadcast.save()
            return broadcast
        except:
            return None

    @staticmethod
    def get_sdlm(user_id):
        try:
            broadcast: list = Broadcast.select().where(Broadcast.user_id == user_id)
            return broadcast
        except:
            return None

    @staticmethod
    def remove_sdlm(msg_id: int):
        Broadcast.delete().where(Broadcast.message_id == msg_id).execute()


def setup(bot):
    bot.add_cog(Database(bot))
