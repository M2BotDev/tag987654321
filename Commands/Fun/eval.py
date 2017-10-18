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
import itertools

def floor(x):
    return math.floor(x)

def exp(x, N):
    strn = "x"
    y = [x] * (N - 1)
    for x in y:
        strn = strn + " * x"
    return eval(strn)

class Eval:
    """$**eval CODE** (smaller version of $code)"""
    def __init__(self, bot):
        self.bot = bot
    @commands.command(no_pm=True, pass_contex=True)
    async def eval(self,ctx,*,code=None):
        message = ctx.message
        code = f"{code}"
        if message.author.id != 264312374931095552:
            return
        thetext = ""
        try:
            thetext = str(eval(code))
        except Exception as e:
            thetext = e
        if thetext == "":
            thetext = None
        embed=discord.Embed(color=0x8e370d)
        embed.set_author(name="Eval", icon_url=message.author.avatar_url)
        embed.add_field(name="ENTERED", value=f"```py\n{str(code)}\n```", inline=False)
        embed.add_field(name="RESULT", value=f"```\n{str(thetext)}\n```", inline=False)
        embed.set_footer(text=message.created_at)
        await message.channel.send(embed=embed)



def setup(bot):
    p = Eval(bot)
    bot.add_cog(p)
