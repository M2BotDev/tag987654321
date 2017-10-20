from discord.ext import commands
import discord
import json
import random
import requests

class Subtract:
    """Subtracts tickets to a discord user. ``$subtract 20 @user#1234`` ``Requires you to be the owner of the discord server.``"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Roblox"
    @commands.command(no_pm=True, pass_contex=True)
    async def subtract(self,ctx, amount=None, person=None):
        message = ctx.message
        if message.author != message.guild.owner:
            print("Not owner!")
            return
        try:
            print(int(amount)/4)
            amount = int(amount)
        except Exception as therror:
            print(therror)
            await message.channel.send("Please enter a valid amount. (Ex. $subtract 2000 @MyFriend#1123")
            return
        try:
            person = message.mentions[0]
        except:
            person = message.author
            
        with open("Data/servers.json", "r") as thejsonfile:
            data = json.load(thejsonfile)
        if str(message.guild.id) in data:
            try:
                data[str(message.guild.id)]["tickets-storage"][str(person.id)]["credits"] -= amount
            except:
                data[str(message.guild.id)]["tickets-storage"][str(person.id)] = {
                    ("credits") : -amount
                }
            await message.channel.send(f"Subtracted ``{amount}`` to ``{person}``'s balance. <:nbaghost:368751631455748096> They now have ``{data[str(message.guild.id)]['tickets-storage'][str(person.id)]['credits']}`` tickets.")
            with open("Data/servers.json", "w") as thejsonfile2:
                json.dump(data, thejsonfile2)
            with open("Data/servers.json", "r") as filejson:
                jsondatafile = json.load(filejson)
            if str(message.guild.id) in jsondatafile:
                try:
                    whofrom = message.author.name
                    action = f"Removed {amount} from {person}'s balance."
                    created_at = message.created_at
                    embed=discord.Embed(title=f"From : {whofrom}", color=0x8e370d)
                    embed.add_field(name="ACTION", value=action, inline=False)
                    embed.set_footer(text=created_at)
                    logchannel = discord.utils.get(message.guild.channels, id = jsondatafile[str(message.guild.id)]["log-channel"])
                    await logchannel.send(embed=embed)
                except Exception as e:
                    return
            else:
                return
        else:
            await message.channel.send("For some reason your server isn't verified. Please kick and reinvite the bot!")
            

def setup(bot):
    p = Subtract(bot)
    bot.add_cog(p)
