from discord.ext import commands
import discord
import json
import random
import requests

class Reset:
    """Resets a users balance to 0. ``$reset all`` ``Requires you to be the owner of the discord server.``"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Roblox"
    @commands.command(no_pm=True, pass_contex=True)
    async def reset(self,ctx, person=None):
        message = ctx.message
        if message.author != message.guild.owner:
            print("Not owner!")
            return
        with open("Data/servers.json", "r") as thejsonfile:
            data = json.load(thejsonfile)
        if person == None:
            person = message.author
        if str(message.guild.id) in data:
            if str(person).lower() != "all":
                print("Not all")
                try:
                    data[str(message.guild.id)]["tickets-storage"][str(person.id)]["credits"] -= 0
                except:
                    data[str(message.guild.id)]["tickets-storage"][str(person.id)] = {
                        ("credits") : 0
                    }
                if message.mentions[0]:
                    person = message.mentions[0]
                else:
                    person = message.author
                await message.channel.send(f"Reseted ``{person}``'s balance. <:nbaghost:368751631455748096> They now have ``{data[str(message.guild.id)]['tickets-storage'][str(person.id)]['credits']}`` tickets.")
                with open("Data/servers.json", "w") as thejsonfile2:
                    json.dump(data, thejsonfile2)
                with open("Data/servers.json", "r") as filejson:
                    jsondatafile = json.load(filejson)
                if str(message.guild.id) in jsondatafile:
                    try:
                        whofrom = message.author.name
                        action = f"Reseted {person}'s balance to 0."
                        created_at = message.created_at
                        embed=discord.Embed(title=f"From : {whofrom}", color=0x8e370d)
                        embed.add_field(name="ACTION", value=action, inline=False)
                        embed.set_footer(text=created_at)
                        logchannel = discord.utils.get(message.guild.channels, id = jsondatafile[str(message.guild.id)]["log-channel"])
                        await logchannel.send(embed=embed)
                    except Exception as e:
                        return
            else:
                print("All")
                for personz in data[str(message.guild.id)]["tickets-storage"]:
                    data[str(message.guild.id)]["tickets-storage"][personz]["credits"] = 0
                await message.channel.send(f"Everyone now has the balance of 0.")
                with open("Data/servers.json", "w") as thejsonfile2:
                    json.dump(data, thejsonfile2)
                with open("Data/servers.json", "r") as filejson:
                    jsondatafile = json.load(filejson)
                if str(message.guild.id) in jsondatafile:
                    try:
                        whofrom = message.author.name
                        action = f"Reseted everyone's balance to 0."
                        created_at = message.created_at
                        embed=discord.Embed(title=f"From : {whofrom}", color=0x8e370d)
                        embed.add_field(name="ACTION", value=action, inline=False)
                        embed.set_footer(text=created_at)
                        logchannel = discord.utils.get(message.guild.channels, id = jsondatafile[str(message.guild.id)]["log-channel"])
                        await logchannel.send(embed=embed)
                    except Exception as e:
                        return

        else:
            await message.channel.send("For some reason your server isn't verified. Please kick and reinvite the bot!")
            

def setup(bot):
    p = Reset(bot)
    bot.add_cog(p)
