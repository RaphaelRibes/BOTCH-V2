import discord
import sys
from discord.ext import commands


class General(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.file = "general"
        self.codelines = package.count_lines_code(self.bot.cogs.values())


def setup(bot):
    bot.add_cog(General(bot))
