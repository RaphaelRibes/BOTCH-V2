import discord
import sys
from discord.ext import commands


class General(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.file = "general"

def setup(bot):
    bot.add_cog(General(bot))
