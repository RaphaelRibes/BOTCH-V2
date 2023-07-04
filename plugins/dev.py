import discord
from discord.ext import commands
import json
import requests

class Dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file = "dev"

def setup(bot):
    bot.add_cog(Dev(bot))