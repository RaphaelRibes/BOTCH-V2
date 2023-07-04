from discord.ext import commands
import discord


class Sdlm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file = "sdlm"


def setup(bot):
    bot.add_cog(Sdlm(bot))
