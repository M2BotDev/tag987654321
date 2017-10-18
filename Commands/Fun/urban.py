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
        nword = word.lower()
        lookfor = f"<p>There aren't any definitions for <i>{nword}</i> yet.</p>"
        word = re.sub(" ", "+", word.lower())
        link = f"https://www.urbandictionary.com/define.php?term={word}"
        source = requests.get(link)
        text = source.text
        soup = BeautifulSoup(text)
        if lookfor in text:
            await message.channel.send("That word doesn't exist!")
            return
        b4 = soup.find("div", "meaning")
        b42 = b4.get_text()
        b42 = re.sub("&apos;", "'", b42)
        b422 = soup.find("div", "example")
        b4222 = b422.get_text()
        b4222 = re.sub("&apos;", "'", b4222)
        embed=discord.Embed(color=0x8e370d)
        embed.add_field(name="Definition", value=f"{b42}", inline=False)
        embed.add_field(name="Example", value=f"{b4222}", inline=False)
        embed.set_author(name=f"Urban - {nword}", url=link, icon_url=message.author.avatar_url)

        await message.channel.send(embed=embed)
        




def setup(bot):
    p = Urban(bot)
    bot.add_cog(p)
