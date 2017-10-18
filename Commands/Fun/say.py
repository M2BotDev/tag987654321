from discord.ext import commands
import discord
import json
import random
import requests

class Say:
    """$**say message**"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Giveaway"
    @commands.command(no_pm=True, pass_contex=True)
    async def say(self,ctx,*,text=None):
        message = ctx.message
        if text != None:
            embed=discord.Embed(description=text, color=0x8e370d)
            embed.set_author(name=message.author.display_name, url=message.author.avatar_url, icon_url=message.author.avatar_url)
            embed.set_footer(text=message.created_at)
            await message.channel.send(embed=embed)



def setup(bot):
    p = Say(bot)
    bot.add_cog(p)
