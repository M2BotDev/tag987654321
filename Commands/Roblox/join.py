from discord.ext import commands
import discord
import json
import random
import requests

class Join:
    """$**join** or **join GIVEAWAY-NAME**"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Giveaway"
    @commands.command(no_pm=True, pass_contex=True)
    async def join(self,ctx, code=None):
        message = ctx.message
        with open("Data\\giveaway.json", "r") as thejsonfile:
            data = json.load(thejsonfile)
        if not str(message.guild.id) in data:
            return
        server = data[str(message.guild.id)]
        if code == None:
            code = server["default-giveaway"]
        if not code in server["giveaways"]:
            await message.channel.send("Invalid code!")
            return
        thegiveaway = server["giveaways"][code]
        if str(message.author.id) in thegiveaway["joined-ids"]:
            await message.channel.send("You already joined this giveaway!")
            return
        else:
            thegiveaway["joined-ids"].append(str(message.author.id))
            await message.channel.send("Thanks for joining the giveaway! <:nbaghost:368751631455748096>")
        

        with open("Data\\giveaway.json", "w") as thejsonfile2:
            json.dump(data, thejsonfile2)



def setup(bot):
    p = Join(bot)
    bot.add_cog(p)
