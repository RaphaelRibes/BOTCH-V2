import discord
import sys
import traceback
import random
import re
from discord.ext import commands


class Errors(commands.Cog):
    """General cog for error management."""

    def __init__(self, bot):
        self.bot = bot
        self.file = "errors"


def setup(bot):
    bot.add_cog(Errors(bot))
