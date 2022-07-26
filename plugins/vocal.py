from discord.ext import commands
import discord


class Vocal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guild_id = {True: 752932746053025865, False: 625330528588922882}
        self.file = "vocal"


def setup(bot):
    bot.add_cog(Vocal(bot))
