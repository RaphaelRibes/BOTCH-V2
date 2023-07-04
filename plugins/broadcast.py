import discord
from discord.ext import commands
import json
from main import BOTCH
from data.ORM_schematic import Broadcast

class Broadcast(commands.Cog):

    def __init__(self, bot: BOTCH):
        self.bot = bot
        self.file = "broadcast"


def setup(bot):
    bot.add_cog(Broadcast(bot))
