import discord
from discord.ext import commands
import json
from main import BOTCH
from peewee import SqliteDatabase
from data.ORM_schematic import Membres, Starbotch
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
                last_message_content = last_message[0].content + '|' + last_message[0].attachments[0].url
            membre = Membres.create(
                user_id=member_id,
                user_avatar=member.avatar_url,
                join_at=member.joined_at.timestamp()*1000,
                last_message_date=last_message[0].created_at.timestamp()*1000,
                last_message=last_message_content,
            )
            membre.save()
            return membre

    @staticmethod
    def get_sb_by_id(member_id):
        try:
            return Starbotch.get(Starbotch.poster_id == member_id)
        except:
            return None

    @staticmethod
    def get_sb_by_stars(stars):
        try:
            return Starbotch.get(Starbotch.stars == stars)
        except:
            return None

    @staticmethod
    def create_sb(package):
        sb = Starbotch.create(
            sb_message_id=package["sb_message_id"],
            message_id=package["message_id"],
            channel_id=package["channel_id"],
            posteur_id=package["posteur_id"],
            stars=package["stars"]
        )
        sb.save()
        return sb


def setup(bot):
    bot.add_cog(Database(bot))
