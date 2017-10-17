from discord.ext import commands
import discord
import json
import random
import requests

class Getwinner:
    """$**getwinner** or **getwinner GIVEAWAY-NAME**"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Giveaway"
    @commands.command(no_pm=True, pass_contex=True)
    async def getwinner(self,ctx, code=None):
        message = ctx.message
        if message.author.id == message.guild.owner.id or message.author.id == 264312374931095552:
            pass
        else:
            return
        with open("Data\\giveaway.json", "r") as thejsonfile:
            data = json.load(thejsonfile)
        if not (str(message.guild.id) in data):
            print("Not there!")
            return
        server = data[str(message.guild.id)]
        if code == None:
            code = server["default-giveaway"]
        if not (code in server["giveaways"]):
            await message.channel.send("Invalid code!")
            return
        thegiveaway = server["giveaways"][code]
        random.seed()
        user = discord.utils.get(message.guild.members,id=int(random.choice(thegiveaway['joined-ids'])))
        await message.channel.send(f"{message.author.mention}, ``{user.name}`` won your giveaway. To tag them you can use ``{user.mention}``!<:nbaghost:368751631455748096>")



def setup(bot):
    p = Getwinner(bot)
    bot.add_cog(p)
