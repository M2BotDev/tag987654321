from discord.ext import commands
import discord
import json
import random
import requests

class Bal:
    """Gets a discord members balance of tickets. ``$bal @user#1234``"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Roblox"
    @commands.command(no_pm=True, pass_contex=True)
    async def bal(self,ctx, person=None):
        message = ctx.message
        try:
            person = message.mentions[0]
        except:
            person = message.author
            
        with open("Data/servers.json", "r") as thejsonfile:
            data = json.load(thejsonfile)
        if str(message.guild.id) in data:
            try:
                data[str(message.guild.id)]["tickets-storage"][str(person.id)]["credits"] += 0
            except:
                data[str(message.guild.id)]["tickets-storage"][str(person.id)] = {
                    ("credits") : 0
                }
            await message.channel.send(f"``{person}`` has ``{data[str(message.guild.id)]['tickets-storage'][str(person.id)]['credits']}`` tickets. <:nbaghost:368751631455748096>")
            with open("Data/servers.json", "w") as thejsonfile2:
                json.dump(data, thejsonfile2)
        else:
            await message.channel.send("For some reason your server isn't verified. Please kick and reinvite the bot!")
            

def setup(bot):
    p = Bal(bot)
    bot.add_cog(p)
