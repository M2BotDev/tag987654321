from discord.ext import commands
import discord
import json
import random
import requests

class Prefix:
    """$**prefix** or **prefix ?**"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Roblox"
    @commands.command(no_pm=True, pass_contex=True)
    async def prefix(self,ctx, pre="$"):
        message = ctx.message
        if message.author.id == message.guild.owner.id or message.author.id == 264312374931095552:
            pass
        else:
            return
        with open("Data\\servers.json", "r") as thejsonfile:
            data = json.load(thejsonfile)
        if str(message.guild.id) in data:
            data[str(message.guild.id)]["prefix"] = pre
            await message.channel.send(f"<:nbaghost:368751631455748096> Prefix was set to ``{pre}``")
            with open("Data\\servers.json", "w") as thejsonfile2:
                json.dump(data, thejsonfile2)
            try:
                logchannel = discord.utils.get(message.guild.channels, id = jsondatafile[str(message.guild.id)]["log-channel"])
                await logchannel.send(f"**From** : ``{message.author.name}``\n\n**Action** : `Set the new prefix to {pre}``")
            except Exception as e:
                return
        else:
            await message.channel.send("For some reason your server isn't verified. Please kick and reinvite the bot!")
            

def setup(bot):
    p = Prefix(bot)
    bot.add_cog(p)
