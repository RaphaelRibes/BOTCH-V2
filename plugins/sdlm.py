from discord.ext import commands
import discord


class Sdlm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file = "sdlm"
        self.main_channel = 707639957484732466
        self.log_channel = {True: 752932896683196536, False: 752561016839209055}
        self.guild = {True: 752932746053025865, False: 625330528588922882}
        self.boris = {True: 754335412633337887, False: 777146313846292481}
        self.leaderboard = []
        self.posteur = bot.DBA.posteur
        self.image = bot.DBA.image
        self.backupconfirm = {}  # Sous la forme 123456789101112: "filename.db"
        self.topgraph_url = self.bot.DBA.topgraph


def setup(bot):
    bot.add_cog(Sdlm(bot))
