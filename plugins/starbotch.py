import discord
from discord.ext import commands
from discord.utils import get
import re
from main import BOTCH
import time
import random


class Starbotch(commands.Cog):

    def __init__(self, bot: BOTCH):
        self.bot = bot
        self.file = "starbotch"


def setup(bot):
    bot.add_cog(Starbotch(bot))