from discord.ext import commands
import discord
import json
import random
import requests

class Setverified:
    """$**setverified ROLENAME**"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Giveaway"
    @commands.command(no_pm=True, pass_contex=True)
    async def setverified(self,ctx,*,role=None):
        message = ctx.message
        if message.author != message.guild.owner:
            return
        with open("Data\\servers.json", "r") as serverfile:
            serverfiledata = json.load(serverfile)
        if str(message.guild.id) in serverfiledata:
            serverin = serverfiledata[str(message.guild.id)]
            theserverrole = discord.utils.get(message.guild.roles, name=role)
            if theserverrole == None:
                await message.channel.send("Invalid role name! (Ex.$setverified ROLENAME)")
                return
        else:
            await message.channel.send("Your server doesn't seem to be verified. Please kick and reinvite the bot!")
            return
        try:
            serverin["verified-role"] = theserverrole.id
            with open("Data\\servers.json", "w") as serverf:
                json.dump(serverfiledata, serverf)
        except Exception as e:
            print(e)
            return
        await message.channel.send(f"Set the verification role to <:nbaghost:368751631455748096> ``{role}``")
        with open("Data\\servers.json", "r") as filejson:
            jsondatafile = json.load(filejson)
        if str(message.guild.id) in jsondatafile:
            try:
                logchannel = discord.utils.get(message.guild.channels, id = jsondatafile[str(message.guild.id)]["log-channel"])
                await logchannel.send(f"**From** : ``{message.author.name}``\n\n**Action** : ``Set the verification role to {role}``")
            except Exception as e:
                return
        else:
            return



def setup(bot):
    p = Setverified(bot)
    bot.add_cog(p)
