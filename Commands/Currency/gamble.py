from discord.ext import commands
import discord
import json
import random
import requests

class Gamble:
    """Gambles a certain amount of tickets. ``$gamble 20``"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Roblox"
    @commands.command(no_pm=True, pass_contex=True)
    async def gamble(self,ctx, amount=None):
        message = ctx.message
        try:
            print(int(amount)/4)
            amount = int(amount)
            if amount <= 0:
                await message.channel.send("Please enter a valid amount. (Ex. $gamble 2000")
                return
                
        except Exception as therror:
            print(therror)
            await message.channel.send("Please enter a valid amount. (Ex. $gamble 2000")
            return
            
        with open("Data/servers.json", "r") as thejsonfile:
            data = json.load(thejsonfile)
        if str(message.guild.id) in data:
            try:
                if not data[str(message.guild.id)]["tickets-storage"][str(message.author.id)]["credits"] < amount:
                    data[str(message.guild.id)]["tickets-storage"][str(message.author.id)]["credits"] -= amount
                    if random.randint(1, 8) >= 7:
                        won = True
                    else:
                        won = False
                else:
                    await message.channel.send("You don't have enough tickets!")
                    return
            except:
                data[str(message.guild.id)]["tickets-storage"][str(person.id)] = {
                    ("credits") : amount
                }
                data[str(message.guild.id)]["tickets-storage"][str(message.author.id)]["credits"] -= amount
                if random.randint(1, 8) >= 5:
                    won = True
                else:
                    won = False

            if won == True:
                if random.randint(1, 8) >= 2:
                    data[str(message.guild.id)]["tickets-storage"][str(message.author.id)]["credits"] += amount*2
                    await message.channel.send(f"``{amount}`` is now ``{amount * 2}``. You now have ``{data[str(message.guild.id)]['tickets-storage'][str(message.author.id)]['credits']}`` tickets!")
                else:
                    data[str(message.guild.id)]["tickets-storage"][str(message.author.id)]["credits"] += amount * 3
                    await message.channel.send(f"``{amount}`` is now ``{amount + 200}``. You now have ``{data[str(message.guild.id)]['tickets-storage'][str(message.author.id)]['credits']}`` tickets!")
            else:
                await message.channel.send(f"<:nbaghost:368751631455748096> You have lost ``{amount}`` tickets. You now have ``{data[str(message.guild.id)]['tickets-storage'][str(message.author.id)]['credits']}`` tickets!")
            with open("Data/servers.json", "w") as thejsonfile2:
                json.dump(data, thejsonfile2)
        else:
            await message.channel.send("For some reason your server isn't verified. Please kick and reinvite the bot!")
            

def setup(bot):
    p = Gamble(bot)
    bot.add_cog(p)
