from discord.ext import commands
import discord
import json
import random
import requests

class Whois:
    """Checks for a roblox account linked to a discord member. ``$whois @user#1234``"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Roblox"
    @commands.command(no_pm=True, pass_contex=True)
    async def whois(self,ctx, person=None):
        message = ctx.message
        with open("Data/verifiedusers.json", "r") as thejsonfile:
            data = json.load(thejsonfile)
        users = data["users"]
        try:
            ida = message.mentions[0]
        except:
            ida = message.author
        if str(ida.id) in users:
            if users[str(ida.id)]["userid"] != "__none__":
                await message.channel.send(f'<:nbaghost:368751631455748096> https://www.roblox.com/users/{users[str(ida.id)]["userid"]}/profile')
                return
        await message.channel.send("That user isn't verified. <:nbaghost:368751631455748096>")


def setup(bot):
    p = Whois(bot)
    bot.add_cog(p)
