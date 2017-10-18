from discord.ext import commands
import discord
import json
import random
import requests
import os

def capitalize_nth(s, n):
    return s[:n].lower() + s[n:].capitalize()

class Reload:
    """No reason for me to tell how to use it because it's for the bot owner only. <3"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Roblox"
    @commands.command(no_pm=True, pass_contex=True)
    async def reload(self,ctx):
        message = ctx.message
        if message.author.id != 264312374931095552:
            return
        self.cmds = {}
        def loopthrough(u, w):
            path = os.listdir(u)
            for file in path:
                if file.endswith(".py"):
                    w[file[:-3]] = file
                else:
                    if not file == "__pycache__":
                        w[file] = {}
                        x = u + "/" + file
                        loopthrough(x, w[file])
        loopthrough("Commands", self.cmds)
        for extension in self.cmds:
            try:
                if not extension.endswith(".py"):
                    def bl(l, e, bot):
                        for x in e:
                            if isinstance(e[x], dict):
                                bl(l + "." + x, e[x], bot)
                            elif e[x].endswith('.py'):
                                try:
                                    print(x)
                                    bot.unload_extension("Commands." + l + "." + x)
                                except:
                                    pass
                                bot.load_extension("Commands." + l + "." + x)
                    bl(extension, self.cmds[extension], self.bot)
                else:
                    self.bot.load_extension("Commands." + extension)
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__, e)
                print('Failed to load extension {}\n{}'.format(extension, exc))    

        await message.channel.send("Reloaded cogs!")

            

def setup(bot):
    p = Reload(bot)
    bot.add_cog(p)