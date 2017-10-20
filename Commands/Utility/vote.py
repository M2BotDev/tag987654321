from discord.ext import commands
import discord
import json
import random
import requests
import sys
import io as StringIO
import contextlib
import re


class Vote:
    """Sends a message with your question. ``$vote Should we use categories?``"""
    def __init__(self, bot):
        self.bot = bot
    @commands.command(no_pm=True, pass_contex=True)
    async def vote(self,ctx,*,asking=None):
        x = ctx.message
        if asking == None:
            return
        embed=discord.Embed(title=asking, description= '', color=0x8e370d)
        embed.set_author(name=x.author.name, url=x.author.avatar_url, icon_url=x.author.avatar_url)
        embed.set_footer(text=x.created_at)
        message = await x.channel.send(embed=embed)
        await x.delete()
        xemoji = self.bot.get_emoji(368913192409235456)
        checkemoji = self.bot.get_emoji(368913175497670659)
        await message.add_reaction(checkemoji)
        await message.add_reaction(xemoji)




def setup(bot):
    p = Vote(bot)
    bot.add_cog(p)
