from discord.ext import commands
import discord
import json
import random
import math

class Mock:
    """Makes fun of text you enter. ``$mock im super rich``"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Giveaway"
    @commands.command(no_pm=True, pass_contex=True)
    async def mock(self,ctx,*,text=None):
        message = ctx.message
        if text != None:
            newtext = ""
            i = 0
            for x in text:
                i = i + 1
                if (i / 2) == math.floor(i/2):
                    newtext += x.upper()
                else:
                    newtext += x.lower()
            embed=discord.Embed(description=newtext, color=0x8e370d)
            embed.set_author(name=message.author.display_name, url=message.author.avatar_url, icon_url=message.author.avatar_url)
            embed.set_image(url="http://i0.kym-cdn.com/entries/icons/original/000/022/940/spongebobicon.jpg")
            embed.set_footer(text=message.created_at)
            await message.channel.send(embed=embed)



def setup(bot):
    p = Mock(bot)
    bot.add_cog(p)
