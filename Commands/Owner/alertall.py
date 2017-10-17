from discord.ext import commands
import discord
import json
import random
import requests

class Alertall:
    """$**alertall Luke, I am your father.**"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Roblox"
    @commands.command(no_pm=True, pass_contex=True)
    async def alertall(self,ctx,*, msg=None):
        message = ctx.message
        unavailable = len(message.guild.members)
        if message.author != message.guild.owner:
            return
        if msg == None:
            await message.channel.send("You can't send an empty message!")
            return
        if unavailable >= 101:
            await message.channel.send("I'm sorry but we do not allow you to use this command for servers with more than 100 members.")
            return
        for member in message.guild.members:
            try:
                await member.send(f"**ALERT FROM {str(message.author.name)}({str(message.author.mention)})**\n\n{str(msg)}")
            except:
                unavailable -= 1
        
        await message.channel.send(f"**SENT**\n\n{str(msg)}\n\n**To** {str(unavailable)}/{str(len(message.guild.members))} members!")

            

def setup(bot):
    p = Alertall(bot)
    bot.add_cog(p)
