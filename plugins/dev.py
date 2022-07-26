import discord
from discord.ext import commands
import json
import requests
from admin import is_admin


async def ciblage(cible, ctx):
    if cible is None:
        cible = ctx.author
    else:
        if len(ctx.message.mentions) == 1:
            cible = ctx.message.mentions[0]
        else:
            try:
                cible = await ctx.guild.fetch_member(cible)
            except: return None

    cible: discord.Member
    return cible


class Dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file = "dev"
        self.log_channel = {True: 752932896683196536, False: 752561016839209055}
        self.professionel = 0

    @commands.command(name='post')
    async def post(self, ctx, *, msg):
        await ctx.message.delete()
        is_admin(ctx.author.roles)
        await ctx.send(msg)

    @commands.command(name="modifypost")
    async def modifypost(self, ctx, msg_id, *, new_message):
        msg = await ctx.channel.fetch_message(int(msg_id))
        await msg.edit(content=new_message)


def setup(bot):
    bot.add_cog(Dev(bot))