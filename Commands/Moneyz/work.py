from discord.ext import commands
import discord
import json
import random
import requests
from discord.ext.commands.cooldowns import BucketType
typeserror = ["You fell asleep on the job and the boss decided to give you a break. Good luck paying for the family!", "Don't you just hate it when you accidently take money from work?", "You woke up with a cold and decided to stay home",
              "Your boss gave you a 'few days off'! Turns out you were fired.", "You're fired! Find a new job.", "You got picked on at work and cried in your customers food. FIRED!", "You got roasted by your boss."]
class Work:
    """$**work**"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Currency"


    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.message.channel.send(error)
        else:
            print(error)
    
    @commands.cooldown(1,3,BucketType.user) 
    @commands.command(no_pm=True, pass_contex=True)
    async def work(self,ctx):
        message = ctx.message
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
            authorchar = data[str(message.guild.id)]["tickets-storage"][str(person.id)]
            if random.choice([1,2,3,4,5,6,7,8,9,10,5,3,5,2]) >= 4:
                x = True
            else:
                x = False
            if x == True:
                z = random.randint(0, 400)
                authorchar["credits"] += z
                msg = f"Congrats! You made {z} tickets!"
            else:
                w = random.randint(10, 100)
                authorchar["credits"] -= w
                msg = random.choice(typeserror) + f" ``-{w} tickets`` <:nbaghost:368751631455748096>"
            await message.channel.send(msg)
            with open("Data/servers.json", "w") as thejsonfile2:
                json.dump(data, thejsonfile2)
        else:
            await message.channel.send("For some reason your server isn't verified. Please kick and reinvite the bot!")
            

def setup(bot):
    p = Work(bot)
    bot.add_cog(p)
