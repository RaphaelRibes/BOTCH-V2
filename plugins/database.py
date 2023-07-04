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


def setup(bot):
    bot.add_cog(Database(bot))
