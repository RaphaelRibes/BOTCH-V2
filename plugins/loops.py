from discord.ext import tasks, commands
import discord
import datetime
import os
from shutil import copyfile
import collections
from random import choice


class Loops(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file = "loops"


def setup(bot):
    bot.add_cog(Loops(bot))