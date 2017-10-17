from discord.ext import commands
import discord
import json
import random
import requests

class Startgiveaway:
    """$**startgiveaway GIVEAWAY-NAME**"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Giveaway"
    @commands.command(no_pm=True, pass_contex=True)
    async def startgiveaway(self,ctx, code=None):
        message = ctx.message
        if message.author.id == message.guild.owner.id or message.author.id == 264312374931095552:
            pass
        else:
            return
        if code == None:
            await message.channel.send("Please choose a code for your giveaway!")
            return
        with open("Data\\giveaway.json", "r") as thejsonfile:
            data = json.load(thejsonfile)
        if not str(message.guild.id) in data:
            data[str(message.guild.id)] = {
                ("giveaways") : {},
                ("default-giveaway") : ""
            }
        server = data[str(message.guild.id)]
        server["giveaways"][code] = {
            ("creator") : message.author.id,
            ("joined-ids") : []
        }
        server["default-giveaway"] = code
        message.delete()
        await message.channel.send(message.author.name + f" has started a giveaway. <:nbaghost:368751631455748096> To join use the join command! (Ex. $join) or (Ex. $join {code})")
        with open("Data\\giveaway.json", "w") as thejsonfile2:
            json.dump(data, thejsonfile2)
        with open("Data\\servers.json", "r") as filejson:
            jsondatafile = json.load(filejson)
        try:
            logchannel = discord.utils.get(message.guild.channels, id = jsondatafile[str(message.guild.id)]["log-channel"])
            await logchannel.send(f"**From** : ``{message.author.name}``\n\n**Action** : ``Created a new giveaway with the id of {code}``")
        except Exception as e:
            return



def setup(bot):
    p = Startgiveaway(bot)
    bot.add_cog(p)
