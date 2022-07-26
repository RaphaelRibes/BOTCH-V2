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
        self.protected_channels = protected_channels()
        self.starbotch_channel = {True: 752932896683196536, False: 777986876552118292}
        self.guild = {True: 752932746053025865, False: 625330528588922882}
        self.file = "starbotch"
        self.starbotch = {}
        self.sb_lb = None


def setup(bot):
    bot.add_cog(Starbotch(bot))