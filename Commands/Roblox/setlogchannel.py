from discord.ext import commands
import discord
import json
import random
import requests

class Setlogchannel:
    """$**setlogchannel**"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Giveaway"
    @commands.command(no_pm=True, pass_contex=True)
    async def setlogchannel(self,ctx):
        message = ctx.message
        channel = message.channel
        if message.author != message.guild.owner:
            return
        with open("Data/servers.json", "r") as serverfile:
            serverfiledata = json.load(serverfile)
        if str(message.guild.id) in serverfiledata:
            serverin = serverfiledata[str(message.guild.id)]
        else:
            await message.channel.send("Your server doesn't seem to be verified. Please kick and reinvite the bot!")
            return
        try:
            serverin["log-channel"] = channel.id
            with open("Data/servers.json", "w") as serverf:
                json.dump(serverfiledata, serverf)
        except Exception as e:
            print(e)
            return
        await message.channel.send(f"Set the logchannel to <:nbaghost:368751631455748096> ``{channel}``")



def setup(bot):
    p = Setlogchannel(bot)
    bot.add_cog(p)
