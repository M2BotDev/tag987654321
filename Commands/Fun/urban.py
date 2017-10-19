from discord.ext import commands
import discord
import json
import random
import requests
import sys
import io as StringIO
import contextlib
import re
from bs4 import BeautifulSoup
"""
import requests
from bs4 import BeautifulSoup
from random import randint

def spider(min, max):
    id = randint(min, max + 1)
    url = "https://www.roblox.com/My/Groups.aspx?gid=" + str(id)
    source = requests.get(url)
    text = source.text
    soup = BeautifulSoup(text)
    link = soup.find("a", "None")
    if link == "None":
        print(id)
    else:
        max = max - 1
        spider(min, max)

spider(1, 3000000)
"""
class Urban:
    """$**urban WORD** or **urban PHRASE**"""
    def __init__(self, bot):
        self.bot = bot
    @commands.has_permissions(manage_messages=True)
    @commands.command(no_pm=True, pass_contex=True)
    async def urban(self,ctx,*,word=None):
        message = ctx.message
        if word == None:
            await message.channel.send("Please enter something for me to search!")
            return
        word = re.sub(" ", "+", word.lower())
        link = f"http://api.urbandictionary.com/v0/define?term={word}"
        source = requests.get(link)
        text = source.text
        jsonv = json.loads(text)
        if jsonv["result_type"] == "no_results":
            await message.channel.send("That word doesn't exist!")
            return
        first = jsonv["list"][0]
        embed=discord.Embed(color=0x8e370d)
        embed.add_field(name="Definition", value=f":zzz:{first['definition']}", inline=False)
        embed.add_field(name="Example", value=f"{first['example']}", inline=False)
        embed.add_field(name=":thumbsdown: ", value=f"{first['thumbs_up']}", inline=True)
        embed.add_field(name=":thumbsup: ", value=f"{first['thumbs_down']}", inline=True)
        embed.add_field(name="Author", value=f"{first['author']}", inline=False)
        embed.set_author(name=f"Urban - {first['word']}", url=link, icon_url=message.author.avatar_url)

        await message.channel.send(embed=embed)
        




def setup(bot):
    p = Urban(bot)
    bot.add_cog(p)
