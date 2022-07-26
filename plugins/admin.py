import discord
from discord.ext import commands
from discord.utils import get
from main import BOTCH
import discord.ext.commands.errors as er
from dev import ciblage


def is_admin(roles):
    admin = False
    admin_roles = [625332148265549844, 636302581949530122, 625333008542597122, 637277665182744636,
                   777247006954750023, 753273974623830078]
    for r in [role.id for role in roles]:
        if r in admin_roles:
            admin = True
    if not admin:
        raise er.MissingAnyRole('admin')


class Admin(commands.Cog):

    def __init__(self, bot: BOTCH):
        self.bot = bot
        self.file = "admin"
        self.report_channel = {True: 752932896683196536, False: 750634015886803025}

    def in_protected_channel(self, cid):
        if cid in self.bot.config['protected_channels']: return True
        else: return False

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        """
        Check pour le report automatique de message. C'est un bordel inomable et je crois qu'il marche plus.
        """
        if payload.emoji.name != "❗" or self.in_protected_channel(payload.channel_id): return
        # Si c'est pas l'mojis de report ou c'est dans un channel protégé on stop direct ici

        channel = await self.bot.fetch_channel(payload.channel_id)  # Récupère le channel du message
        message = await channel.fetch_message(payload.message_id)  # Récupère le message en lui même
        reaction = get(message.reactions, emoji=payload.emoji.name)  # Récupère les infos sur les réactions du message

        if reaction and reaction.count < 3: return  # Si le nombre de ❗ est inférieur a 3, alors balec

        report_channel = await self.bot.fetch_channel(
            self.report_channel[self.bot.test])  # Récupère le channel de report en fonction du token

        if reaction and reaction.count == 3:  # Si 3 réactions ❗ sont sur le msg alors il est report
            await channel.send("Message reporté à la modération")  # Feedback user

            embed = discord.Embed(
                timestamp=message.created_at,
                colour=discord.Colour.red(),
                description=message.content
            )
            embed.set_author(name=f'{message.author.name}#{message.author.discriminator}',
                             icon_url=message.author.avatar_url_as(static_format='jpg'))
            embed.set_footer(text=f"Author ID:{message.author.id} • Message ID: {message.id}")
            if len(message.attachments) != 0: embed.set_image(url=message.attachments[0].url)

            await report_channel.send(embed=embed)  # Feedback modo

        elif reaction and reaction.count == 7:  # Si 7 réactions ❗ sont sur le msg alors il est delete
            await channel.send("Message suprimé du aux nombre élevé de report")  # Feedback user
            await report_channel.send(f"{message.id} a été suprimé due a un nombre élevé de report")
            return await message.delete()  # Supression du message en question

    # BEGINING OF ADMIN COMMANDS GROUP
    @commands.group(name="admin")
    async def _admin_core(self, ctx):
        await ctx.message.delete()  # Petit cleanup
        is_admin(ctx.author.roles)  # Vérifie si l'utilisateur est modo

        if ctx.invoked_subcommand is None:  # Si on a juste ?admin ou alors une subcommande éronée
            is_admin(ctx.author.roles)
            embed = discord.Embed(
                title="Help admin",
                color=discord.Colour.from_rgb(255, 0, 21)  # C'est la couleur du BOTCH ça, bien rouge, sah
            )
            # Pas besoin d'expliquer ce qui ce passe en dessous je pense que c'est obvious
            embed.add_field(name="`?admin`",
                            value="Affiche les commandes administrateur relatives au serveur",
                            inline=False)

            embed.add_field(name="`?post <message>`",
                            value="Fait parler BOT(CH) a votre place",
                            inline=False)

            embed.add_field(name="`?admin shutdown`",
                            value="Éteint le <@!777166173149986826>",
                            inline=False)

            embed.add_field(name="`?admin info`",
                            value="Affiche les information administrateur sur le serveur",
                            inline=False)

            embed.add_field(name="`?broadcast`",
                            value="Affiche les commandes administrateur relatives au message de masses",
                            inline=False)

            embed.add_field(name="`?channel`",
                            value="Affiche les commandes administrateur relatives à la gestion individuelle des channels textuels",
                            inline=False)
            embed.add_field(name="`?vocal`",
                            value="Affiche les commandes administrateur relatives au channels vocaux",
                            inline=False)

            await ctx.send(embed=embed)  # Feedback user

    @_admin_core.command(name='shutdown')
    async def _shutdown(self, ctx):
        await ctx.send("Logout :cry:")  # :'c
        await ctx.bot.logout()

    @_admin_core.command(name="info")
    async def _info(self, ctx):
        embed = discord.Embed(
            title=f"{ctx.guild.name} : ADMIN",
            url="https://discord.gg/G38Ge7y",
            description=ctx.guild.description,
            color=discord.Colour.from_rgb(255, 0, 21)
        )
        embed.set_thumbnail(url=ctx.guild.icon_url)

        embed.add_field(name='Innactives members count :',
                        value=f"{await ctx.guild.estimate_pruned_members(days=7)}/{ctx.guild.member_count} n'ont pas visité le serveur depuis 7 jours",
                        inline=False)

        embed.add_field(name="Bans count :",
                        value=f'{len(await ctx.guild.bans())} personnes ont été bannies de ce serveur',
                        inline=False)

        channels_text = ""
        for c in self.bot.config['protected_channels']:
            channels_text += f"\n\t- <#{c}>"

        embed.add_field(name="Protected channels :",
                        value=f'Tout les messages dans les channels de cette liste sont protégés contre le ❗ et ⭐ :{channels_text}',
                        inline=False)

        return await ctx.send(embed=embed)

    @_admin_core.command(name="clear_person", aliases=["clear_member", "cp", 'cm'])
    async def _clear_member_messages(self, ctx, cible, nbrmessages=100):
        cible = await ciblage(cible, ctx)
        if cible is None:
            return await ctx.send("Cette cible n'existe pas ou est incorecte")

        async for msg in cible.history(limit=nbrmessages):
            await msg.delete()
        await ctx.send(f"{cible.mention} a été nettoyé de {nbrmessages} messages")

    @_admin_core.command(name="roles")
    async def _show_roles(self, ctx):
        guild: discord.Guild = None
        for g in self.bot.guilds:
            if g.id == 625330528588922882:
                guild = g
        roles = guild.roles

        track = 0
        embed = discord.Embed(
            title="Roles status",
            color=discord.Colour.from_rgb(255, 0, 21)
        )
        roleignore = [723202731803672736, 723202665789653102, 636591147589828638, 723196934197608468,
                      754385790682923039, 723521427793510402, 732939404460425236, 735432443930345514,
                      777247006954750023, 717354351705849906, 775767740312977440, 704813192282374174,
                      636512191046221827, 949262343236366356, 720708059525283854, 636557010724454413,
                      990549019963039755, 990551301991591936, 990549485992177745, 990551554832597032,
                      990553102358835210, 990553483172274216, 990554345433104415, 990554623121174589,
                      990549282295791626, 990552261782556726]
        for role in roles:
            role: discord.Role
            if track == 12:
                await ctx.send(embed=embed)
                embed = discord.Embed(
                    title="Roles status",
                    color=discord.Colour.from_rgb(255, 0, 21)
                )
                track = 0
            elif role.id in roleignore: pass
            else:
                embed.add_field(name=f"{role.name if role.id != 625330528588922882 else 'Membres au total'}",
                                value=f"{len(role.members)} personnes ayant ce role")
                track += 1

        if track != 0: await ctx.send(embed=embed)
    # END OF ADMIN COMMANDS GROUP

    # START OF CHANNELS MANAGEMENT GROUP
    @commands.group(name='channel')
    async def channel_management_core(self, ctx):
        await ctx.message.delete()
        is_admin(ctx.author.roles)
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(
                title="Help channel",
                color=discord.Colour.from_rgb(255, 0, 21)
            )
            embed.add_field(name="`?channel block <cible_id> (raison)`",
                            value="La personne ciblée ne peux plus écrire dans ce channel", inline=False)
            embed.add_field(name="`?channel ban <cible_id> (raison)`",
                            value="La personne ciblée ne peux plus ni écrire ni lire dans ce channel", inline=False)
            embed.add_field(name="`?channel clear <cible_id>`",
                            value="Remet les droits de la cible par défaut sur ce channel", inline=False)
            await ctx.send(embed=embed)

    @channel_management_core.command(name='block')
    async def _channel_block(self, ctx, cible_id, *, reason=None):
        try:
            cible = ctx.message.mentions[0]
        except:
            cible = await ctx.guild.fetch_member(int(cible_id))
        await ctx.channel.set_permissions(cible, read_messages=True, send_messages=False)
        block_embed = discord.Embed(
            title=f"Block de {cible.name}#{cible.discriminator}",
            description=f"Bloqué dans le channel {ctx.channel.mention}",
            color=discord.Colour.red()
        )
        block_embed.set_author(name=f"{ctx.author.name}#{ctx.author.discriminator}",
                               icon_url=ctx.author.avatar_url_as(static_format='png'))
        block_embed.set_footer(text=f"Moderator ID:{ctx.author.id} • Victime ID:{cible.id}")
        report_channel = await self.bot.fetch_channel(self.report_channel[self.bot.user.id == 762723841498677258])
        block_embed.add_field(name='Raison :', value=reason)
        await report_channel.send(embed=block_embed)
        await cible.send(
            f"Votre permission d'écrire dans le salon {ctx.channel.name} a été retirée suite à la décision d'un modérateur."
            f"\n> {reason}")

    @channel_management_core.command(name='ban')
    async def _channel_ban(self, ctx, cible_id, *, reason=None):
        try:
            cible = ctx.message.mentions[0]
        except:
            cible = await ctx.guild.fetch_member(int(cible_id))
        await ctx.channel.set_permissions(cible, read_messages=False, send_messages=False)
        block_embed = discord.Embed(
            title=f"Ban de {cible.name}#{cible.discriminator}",
            description=f"Banni du channel {ctx.channel.mention}",
            color=discord.Colour.dark_red()
        )
        block_embed.set_author(name=f"{ctx.author.name}#{ctx.author.discriminator}",
                               icon_url=ctx.author.avatar_url_as(static_format='png'))
        block_embed.set_footer(text=f"Moderator ID:{ctx.author.id} • Victime ID:{cible.id}")
        report_channel = await self.bot.fetch_channel(self.report_channel[self.bot.user.id == 762723841498677258])
        block_embed.add_field(name='Raison :', value=reason)
        await report_channel.send(embed=block_embed)
        await cible.send(
            f"Votre permission d'accéder à ce salon {ctx.channel.name} a été retirée suite à la décision d'un modérateur."
            f"\n> {reason}")

    @channel_management_core.command(name='clear')
    async def _channel_clear(self, ctx, cible_id, *, reason=None):
        try:
            cible = ctx.message.mentions[0]
        except:
            cible = await ctx.guild.fetch_member(int(cible_id))
        await ctx.channel.set_permissions(cible, read_messages=True, send_messages=True)
        block_embed = discord.Embed(
            title=f"Clear de {cible.name}#{cible.discriminator}",
            description=f"Récupère ses accès à {ctx.channel.mention}",
            color=discord.Colour.green()
        )
        block_embed.set_author(name=f"{ctx.author.name}#{ctx.author.discriminator}",
                               icon_url=ctx.author.avatar_url_as(static_format='png'))
        block_embed.set_footer(text=f"Moderator ID:{ctx.author.id} • Victime ID:{cible.id}")
        report_channel = await self.bot.fetch_channel(self.report_channel[self.bot.user.id == 762723841498677258])
        block_embed.add_field(name='Raison :', value=reason)
        await report_channel.send(embed=block_embed)
        await cible.send(
            f"Votre permission d'écrire dans le salon {ctx.channel.name} a été restaurée."
            f"\n> {reason}")
    # END OF CHANNELS MANAGEMENT GROUP


def setup(bot):
    bot.add_cog(Admin(bot))
