import discord
from discord.ext import commands
from discord.utils import get
from main import BOTCH


class Admin(commands.Cog):

    def __init__(self, bot: BOTCH):
        self.bot = bot
        self.file = "admin"
        self.report_channel = {True: 752932896683196536, False: 750634015886803025}


def setup(bot):
    bot.add_cog(Admin(bot))
