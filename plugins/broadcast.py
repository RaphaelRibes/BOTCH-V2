import discord
from discord.ext import commands
import json
from main import BOTCH


class Broadcast(commands.Cog):

    def __init__(self, bot: BOTCH):
        self.bot = bot
        self.file = "broadcast"
        self.broadcastconfirm = {}  # Sous la forme int(user_id): ('sdlm', message)

def setup(bot):
    bot.add_cog(Broadcast(bot))