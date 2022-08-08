import discord
from discord.ext import commands
import json
from main import BOTCH
from admin import is_admin
from data.ORM_schematic import Broadcast


def broadcast_embed(ctx, msg):
    embed = discord.Embed(
        title="SALUT LES B-B-BOTCHS !",
        description=msg
    )
    if len(ctx.message.attachments) > 0:
        embed.set_image(url=ctx.message.attachments[0].url)
    return embed


class Broadcast(commands.Cog):

    def __init__(self, bot: BOTCH):
        self.bot = bot
        self.file = "broadcast"

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        if payload.user_id == self.bot.user.id: return
        broadcasts = self.bot.DBA.get_broadcast(payload.user_id)
        if payload.emoji in ['✅', '❌'] and broadcasts is not None:
            for broadcast in broadcasts:
                broadcast: Broadcast
                if broadcast.message_id == payload.message_id:
                    preview_message: discord.Message = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
                    embed = preview_message.embeds[0]

                    if payload.emoji == '✅':
                        if broadcast.target == "sdlm":


                    if payload.emoji == '❌':
                        await self.bot.DBA.remove_broadcast(payload.message_id)
                        embed.set_footer(text="Annulation")
                        await preview_message.edit(embed=embed)
                    return

    # START OF BROADCAST GROUP
    @commands.group(name="broadcast", aliases=['bc'])
    async def _broadcast_groupe(self, ctx: discord.ext.commands.Context):
        is_admin(ctx.author.roles)
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(
                title="Help broadcast",
                color=discord.Colour.from_rgb(255, 0, 21)
            )
            embed.add_field(name="`?broadcast/bc sdlm <message>`",
                            value="Envoit un message à tout les participants présents dans la db du <#707639957484732466>",
                            inline=False)
            embed.add_field(name="`?broadcast/bc botchnews <message>`",
                            value="Envoit un message dans le <#625338153640656907>", inline=False)
            embed.add_field(name="`?broadcast/bc sb <message>`",
                            value="Envoit un message à tout les participants présents dans la db du <#777986876552118292>",
                            inline=False)
            embed.add_field(name="`?broadcast/bc help`", value="Affiche un message d'aide à la typo des messages",
                            inline=False)
            await ctx.send(embed=embed)

    @_broadcast_groupe.command(name='botchnews', aliases=['bn'])
    async def _broadcast_annonce(self, ctx: discord.ext.commands.Context, *, msg: str):
        preview_message: discord.Message = await ctx.send(embed=broadcast_embed(ctx, msg))
        self.bot.DBA.create_broadcast(ctx.message.id, ctx.author.id, preview_message.id, msg, "botchnews")
        await preview_message.add_reaction("✅")
        await preview_message.add_reaction("❌")

    @_broadcast_groupe.command(name='sdlm')
    async def _broadcast_sdlm(self, ctx, *, msg: str):
        preview_message: discord.Message = await ctx.send(embed=broadcast_embed(ctx, msg))
        self.bot.DBA.create_broadcast(ctx.message.id, ctx.author.id, preview_message.id, msg, "sdlm")
        await preview_message.add_reaction("✅")
        await preview_message.add_reaction("❌")

    @_broadcast_groupe.command(name='sb')
    async def _broadcast_sb(self, ctx, *, msg: str):
        preview_message: discord.Message = await ctx.send(embed=broadcast_embed(ctx, msg))
        self.bot.DBA.create_broadcast(ctx.message.id, ctx.author.id, preview_message.id, msg, "sb")
        await preview_message.add_reaction("✅")
        await preview_message.add_reaction("❌")

    @_broadcast_groupe.command(name='help')
    async def _broadcast_sexample(self, ctx):
        await ctx.send("Envoit ton message normalement après la commande de broadcast."
                       "\nY'a 2~3 trucs simpa a faire genre [untruc à hyperlink](https://example.com) te donne")
        await ctx.send(embed=discord.Embed(title='Exemple', description="Y'a 2~3 trucs simpa a faire genre [untruc à hyperlink](https://example.com) te donne"))
        await ctx.send("Aussi si tu poste avec une image ça la mettera dans l'embed")
    # END OF BROADCAST GROUP


def setup(bot):
    bot.add_cog(Broadcast(bot))
