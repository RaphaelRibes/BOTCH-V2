#!/bin/bash/Python-3.10.0 python
# coding=utf-8

try:
    import discord
    import time
    import logging
    import sys
    import json
    import asyncio
    from discord.ext import commands
    import sqlite3
    from plugins.database import Database

    _plugins = ['database']


    class BOTCH(commands.bot.BotBase, discord.Client):
        def __init__(self, test=False):
            super().__init__(command_prefix='?', status=discord.Status.online,
                             activity=discord.Game("servir des bières"), intents=discord.Intents.all())
            self.test = test
            self.guild = None
            with open('config.json') as f: self.config = json.load(f)

    def main():
        with open('config.json') as f:
            conf = json.load(f)

        if input("Testbot ?\n") == 'y':
            test = True
        else:
            test = False

        client = BOTCH(test=test)
        client.conf = conf

        count = 0
        client.remove_command("help")
        for plugin in _plugins:
            try:
                client.load_extension("plugins." + plugin)
            except:
                count += 1
            if count > 0:
                raise Exception("\n{} modules not loaded".format(count))
        del count

        async def on_ready():
            """Called when the bot is connected to Discord API"""
            print('\nBot connecté')
            print("Nom : " + client.user.name)
            print("ID : " + str(client.user.id))
            if len(client.guilds) < 200:
                serveurs = [x.name for x in client.guilds]
                print(
                    "Connecté sur [" + str(len(client.guilds)) + "] " + ", ".join(serveurs))
            else:
                print("Connecté sur " + str(len(client.guilds)) + " serveurs")
            print(time.strftime("%d/%m  %H:%M:%S"))
            print('------')
            await asyncio.sleep(2)

        client.add_listener(on_ready)

        client.run(conf["token"] if not test else conf["token_test"])

        await client.fetch_guild({True: 752932746053025865, False: 625330528588922882}[test])


    if __name__ == "__main__":
        main()
except Exception as e:
    print(e)
    x = input()
