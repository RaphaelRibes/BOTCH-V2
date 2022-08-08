import discord
from discord.ext import commands
import main
import package as pck
import json


def make_embed(package):
    embed = discord.Embed(
        title=package['title'],
        description=package['description'],
        color=discord.Colour.from_rgb(255, 0, 21)
    )
    return embed


def extract_rid_and_emoji(embed):
    package = {}
    footer = embed.footer.text.split('|')
    for n, field in enumerate(embed.fields):
        name = field.name.split(':')
        package[name[0]] = int(footer[n])

    return package


def get_role(role_id, roles):
    for role in roles:
        if role.id == role_id: return role


class Rolereact(commands.Cog):
    def __init__(self, bot: main.BOTCH):
        self.bot = bot
        self.file = "rolereact"
        self.guild_bot = None
        self.guilds = {True: 752932746053025865, False: 625330528588922882}

    @commands.Cog.listener()
    async def on_ready(self):
        self.guild_bot = await self.bot.fetch_guild(self.guilds[self.bot.test])

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        rr_list = self.bot.config['role_react']
        target_url = ""
        for url in rr_list:
            if str(payload.message_id) in url: target_url = url
            else: pass
        if target_url == "": return

        if payload.member is None: payload.member = await self.guild_bot.fetch_member(payload.user_id)
        raw_target_url = target_url.split('/')
        channel = await self.bot.fetch_channel(int(raw_target_url[5]))
        message: discord.Message = await channel.fetch_message(int(raw_target_url[6]))
        rri_emoji_package = extract_rid_and_emoji(message.embeds[0])

        role = None
        for emoji in rri_emoji_package:
            if payload.emoji.name in emoji: role = get_role(rri_emoji_package[emoji], payload.member.guild.roles)
        if role is None: return

        try:
            await payload.member.add_roles(role)
        except:
            return

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        rr_list = self.bot.config['role_react']
        target_url = ""
        for url in rr_list:
            if str(payload.message_id) in url: target_url = url
            else: pass
        if target_url == "": return

        if payload.member is None: payload.member = await self.guild_bot.fetch_member(payload.user_id)
        raw_target_url = target_url.split('/')
        channel = await self.bot.fetch_channel(int(raw_target_url[5]))
        message: discord.Message = await channel.fetch_message(int(raw_target_url[6]))
        rri_emoji_package = extract_rid_and_emoji(message.embeds[0])

        role = None
        for emoji in rri_emoji_package:
            if payload.emoji.name in emoji: role = get_role(rri_emoji_package[emoji], payload.member.guild.roles)
        if role is None: return

        try:
            await payload.member.remove_roles(role)
        except:
            return

    @commands.group(name='role_react', aliases=['rr', 'roler', 'rreact'])
    async def role_react_core(self, ctx: discord.ext.commands.Context):
        await ctx.message.delete()
        pck.is_admin(ctx.author.roles)
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(
                title="Help role react",
                color=discord.Colour.from_rgb(255, 0, 21)
            )
            embed.add_field(name="`example` ou `ex`",
                            value="Donne un texte d'exmple pour le format du message", inline=False)
            embed.add_field(name="`setup`",
                            value="Permet de setup un message de role react", inline=False)
            embed.add_field(name="`status (msg_id)`",
                            value="Affiche le status général des messages de role react ou un plus précis de celui ciblé", inline=False)
            embed.add_field(name="`delete` ou `remove`",
                            value="Permet de supprimer un message de role react", inline=False)
            embed.add_field(name="`add_role` ou `addr`",
                            value="Permet d'ajouter un role sur un message de rolereact\nExemple: ?rr addr 952934023632683098 732939404460425236 <:mrbotch:777146313111240734>", inline=False)
            embed.add_field(name="`remove_role` ou `remr`",
                            value="Permet de supprimer un role sur un message de rolereact\nExemple: ?rr remr 952934023632683098 732939404460425236", inline=False)
            await ctx.send(embed=embed)

    @role_react_core.command(name='example', aliases=['ex'])
    async def _role_react_example(self, ctx: discord.ext.commands.Context):
        example = {"title": "Par ici les rôles !",
                   "description": "Pour obtenir un des rôles affichés, réagissez avec l'émojis associé au rôle."
                                  "\nPour se retirer un rôle il suffit de retirer la réaction de ce message."}
        embed = make_embed(example)
        await ctx.send("Pas obligé de remttre les \` pour rentre le message, il ne faut **surtout** pas mettre de `•` dans le message.\n```json\n{}```Donnera".format(
            json.dumps(example, indent=2, ensure_ascii=False)), embed=embed)

    @role_react_core.command(name='setup')
    async def _role_react_setup(self, ctx: discord.ext.commands.Context, *, message):
        try:
            package = json.loads(message)
        except:
            return await ctx.send("Format du message incorecte")

        embed = make_embed(package)
        rrm: discord.Message = await ctx.send(embed=embed)
        with open('config.json', 'w') as f:
            self.bot.config['role_react'].append(rrm.jump_url)
            json.dump(self.bot.config, f)

    @role_react_core.command(name='status')
    async def _role_react_status(self, ctx: discord.ext.commands.Context, rr_id=None):
        rr_list = self.bot.config['role_react']

        if rr_id is not None:
            target_url = ""
            for url in rr_list:
                if rr_id in url: target_url = url
                else: pass
            if target_url == "": return await ctx.send(f"`{rr_id}` n'existe pas")
            raw_target_url = target_url.split('/')
            channel = await self.bot.fetch_channel(int(raw_target_url[5]))
            message: discord.Message = await channel.fetch_message(int(raw_target_url[6]))
            package = extract_rid_and_emoji(message.embeds[0])
            print(package)
            embed = discord.Embed(
                title=f'Role react status: `{rr_id}`',
                color=discord.Colour.from_rgb(255, 0, 21)
            )
            embed.set_author(name="Lien vers le message", url=target_url)
            roles = await ctx.guild.fetch_roles()
            for emoji in package:
                for role in roles:
                    role: discord.Role
                    if role.id == package[emoji]:
                        embed.add_field(name=f"{emoji}: {role.name}", value=f"Avec {len(role.members)} membre{'' if len(role.members)<=1 else 's'}", inline=False)

        else:
            embed = discord.Embed(
                title='Role react status',
                color=discord.Colour.from_rgb(255, 0, 21)
            )

            for url in rr_list:
                raw = url.split('/')
                embed.add_field(name=raw[6], value=f'Dans <#{raw[5]}>, [lien vers le message]({url})')

        await ctx.send(embed=embed)

    @role_react_core.command(name='delete', aliases=['remove'])
    async def _role_react_delete(self, ctx: discord.ext.commands.Context, msg_id):
        rr_list = self.bot.config['role_react']
        final = []
        url_to_delete = ""
        for url in rr_list:
            if msg_id in url: url_to_delete = url
            else: final.append(url)
        if len(rr_list) == len(final):
            return await ctx.send(f"`{msg_id}` n'existe pas")
        self.bot.config['role_react'] = final
        with open('config.json', 'w') as f:
            json.dump(self.bot.config, f)
        url_to_delete = url_to_delete.split('/')
        channel = await self.bot.fetch_channel(int(url_to_delete[5]))
        message = await channel.fetch_message(int(url_to_delete[6]))
        await message.delete()
        await ctx.send(f'`{msg_id}` à été suprimé')

    @role_react_core.command(name='add_role', aliases=['addr'])
    async def _role_react_add_role(self, ctx: discord.ext.commands.Context, msg_id, role_id, emoji, *, desc):
        rr_list = self.bot.config['role_react']
        jump_url = ""

        for url in rr_list:
            if msg_id in url: jump_url = url

        if jump_url == "":
            return await ctx.send(f"{msg_id} est invalide")

        try:
            roles = await ctx.guild.fetch_roles()
            role = None
            for r in roles:
                if r.id == int(role_id): role = r
        except:
            return await ctx.send(f"{role_id} est invalide")

        raw = jump_url.split('/')
        role: discord.Role
        channel = await self.bot.fetch_channel(int(raw[5]))
        message: discord.Message = await channel.fetch_message(int(raw[6]))
        embed: discord.Embed = message.embeds[0]
        embed.add_field(name=f"{emoji}: {role.name}", value=desc, inline=False)
        if embed.footer.text != discord.Embed.Empty:
            embed.set_footer(text=f"{embed.footer.text}|{str(role.id)}")
        else:
            embed.set_footer(text=role.id)
        await message.edit(embed=embed)
        await message.add_reaction(emoji)

    @commands.command(name='te')
    async def te(self, ctx: discord.ext.commands.Context, msg_id: int):
        msg: discord.Message = await ctx.channel.fetch_message(msg_id)
        print()

    @role_react_core.command(name='remove_role', aliases=['remr'])
    async def _role_react_remove_role(self, ctx: discord.ext.commands.Context, msg_id, role_id):
        rr_list = self.bot.config['role_react']
        jump_url = ""

        for url in rr_list:
            if msg_id in url: jump_url = url

        if jump_url == "":
            return await ctx.send(f"{msg_id} est invalide")

        roles = await ctx.guild.fetch_roles()
        if int(role_id) not in [r.id for r in roles]:
            return await ctx.send(f"{role_id} est invalide")

        raw = jump_url.split('/')
        channel = await self.bot.fetch_channel(int(raw[5]))
        message: discord.Message = await channel.fetch_message(int(raw[6]))

        embed: discord.Embed = message.embeds[0]
        who = 0
        for ids in embed.footer.text.split('|'):
            if ids == str(role_id):
                break
            else:
                who += 1

        name = embed.fields[who].name
        name = name.split(':')
        emoji = name[0]
        embed.remove_field(who)

        footer = embed.footer.text.replace(f'{role_id}', '')
        footer = footer.replace('||', '|')
        embed.set_footer(text=footer)

        await message.edit(embed=embed)
        await message.clear_reaction(emoji)


def setup(bot):
    bot.add_cog(Rolereact(bot))
