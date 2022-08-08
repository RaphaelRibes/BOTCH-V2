import discord
from discord.ext import commands
import main
import json


class Rolereact(commands.Cog):
    def __init__(self, bot: main.BOTCH):
        self.bot = bot
        self.file = "rolereact"


def setup(bot):
    bot.add_cog(Rolereact(bot))
