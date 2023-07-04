from discord.ext import commands
import requests
import json
import discord


async def get_da_meme():
    r = requests.get("https://meme-api.herokuapp.com/gimme")
    return json.loads(str(r.text))


class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file = "memes"


def setup(bot):
    bot.add_cog(Memes(bot))