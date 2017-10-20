from discord.ext import commands
import discord
import json
import random
import requests
import os

class Stop:
    """``Command limited to bot creater only!``"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Roblox"
    @commands.command(no_pm=True, pass_contex=True)
    async def stop(self,ctx):
        message = ctx.message
        if message.author.id != 264312374931095552:
            return
        await message.channel.send("Goodbye!")
        self.bot.loop.create_task(self.bot.logout())

            

def setup(bot):
    p = Stop(bot)
    bot.add_cog(p)