from discord.ext import commands
import discord
import json
import random
import requests

class Donate:
    """$**donate 10 @user#1234**"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Roblox"
    @commands.command(no_pm=True, pass_contex=True)
    async def donate(self,ctx, amount=None, person=None):
        message = ctx.message
        try:
            print(int(amount)/4)
            amount = int(amount)
            if amount <= 0:
                await message.channel.send("Please enter a valid amount. (Ex. $donate 2000 @MyFriend#1123")
                return
                
        except Exception as therror:
            print(therror)
            await message.channel.send("Please enter a valid amount. (Ex. $donate 2000 @MyFriend#1123")
            return
        try:
            person = message.mentions[0]
        except:
            await message.channel.send("Please enter a valid person to donate to. (Ex. $donate 2000 @MyFriend#1123")
            return
            
        with open("Data/servers.json", "r") as thejsonfile:
            data = json.load(thejsonfile)
        if str(message.guild.id) in data:
            try:
                if not data[str(message.guild.id)]["tickets-storage"][str(message.author.id)]["credits"] < amount:
                    data[str(message.guild.id)]["tickets-storage"][str(person.id)]["credits"] += amount
                    data[str(message.guild.id)]["tickets-storage"][str(message.author.id)]["credits"] -= amount
                else:
                    await message.channel.send("You don't have enough tickets!")
                    return
            except:
                data[str(message.guild.id)]["tickets-storage"][str(person.id)] = {
                    ("credits") : amount
                }
                data[str(message.guild.id)]["tickets-storage"][str(message.author.id)]["credits"] -= amount
                
            await message.channel.send(f"<:nbaghost:368751631455748096> Donated ``{amount}`` to ``{person}``'s balance. They now have ``{data[str(message.guild.id)]['tickets-storage'][str(person.id)]['credits']}`` tickets.")
            with open("Data/servers.json", "w") as thejsonfile2:
                json.dump(data, thejsonfile2)
        else:
            await message.channel.send("For some reason your server isn't verified. Please kick and reinvite the bot!")
            

def setup(bot):
    p = Donate(bot)
    bot.add_cog(p)
