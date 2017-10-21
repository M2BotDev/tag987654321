from discord.ext import commands
import discord
import json
import random
import requests
import sys
import io as StringIO
import contextlib
import re
import math


class Meme:
    """Gives you a random meme! ``$meme`` ``Only the bot creator can do $meme add link``"""
    def __init__(self, bot):
        self.bot = bot
    @commands.command(no_pm=True, pass_contex=True)
    async def meme(self,ctx,mode=None, link=None):
        message = ctx.message
        with open("Data/memes.json") as memejson:
            data = json.load(memejson)
        if mode == None:
            memelink = data["links"][random.randint(0, len(data["links"])-1)]
            embed=discord.Embed(color=0x8e370d)
            embed.set_author(name="Meme", icon_url=message.author.avatar_url)
            embed.set_image(url=memelink)
            embed.set_footer(text=message.created_at)
            await message.channel.send(embed=embed)
        elif mode == "add":
            if message.author.id != 264312374931095552:
                return
            if link != None:
                data["links"].append(link)
            with open("Data/memes.json", "w") as memejson2:
                json.dump(data, memejson2)
            




def setup(bot):
    p = Meme(bot)
    bot.add_cog(p)
