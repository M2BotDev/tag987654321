from discord.ext import commands
import discord
import json
import random
import requests

class Item:
    """$**item ROBLOXHATNAME**"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Roblox"
    @commands.command(no_pm=True, pass_contex=True)
    async def item(self,ctx, itemname=None):
        message = ctx.message
        if itemname == None:
            await message.channel.send("Please enter a name for me to search for.")
            return

        link = f"https://search.roblox.com/catalog/json?Subcategory={random.randint(0,3)}&SortType=0&ResultsPerPage=1&Keyword={itemname}"
        source = requests.get(link)
        text = source.text
        if text != "[]":
            jsonver = json.loads(text)
        else:
            await message.channel.send("Failed to find results.")
            return
        jsonver = jsonver[0]
        if jsonver["Price"] == "":
            price = "Not for sale."
        else:
            price = jsonver["Price"]
        print("0")
        embed=discord.Embed(title=jsonver["Name"], description=jsonver["Description"], color=0x8e370d)
        embed.set_author(name=message.author.name, url=message.author.avatar_url, icon_url=message.author.avatar_url)
        print("3")
        embed.set_thumbnail(url=jsonver["ThumbnailUrl"])
        embed.add_field(name="Asset Id", value=f"\u200b{jsonver['AssetId']}", inline=True)
        print("1")
        embed.add_field(name="Price", value=f"\u200b{price}", inline=True)
        embed.add_field(name="Last Updated", value=f"\u200b{jsonver['Updated']}", inline=True)
        embed.add_field(name="Favorited", value=f"\u200b{jsonver['Favorited']}", inline=True)
        embed.add_field(name="Sales", value=f"\u200b{jsonver['Sales']}", inline=True)
        print("2")
        embed.add_field(name="Limited", value=f"\u200b{jsonver['IsLimited']}", inline=True)
        print("A")
        embed.set_footer(text=f"Link : {jsonver['AbsoluteUrl']}")
        print("B")
        await message.channel.send(embed=embed)

        


def setup(bot):
    p = Item(bot)
    bot.add_cog(p)
