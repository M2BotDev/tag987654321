from discord.ext import commands
import discord
import json
import random
import requests
from discord.ext.commands.cooldowns import BucketType
typeserror = ["You fell asleep on the job and the boss decided to give you a break. Good luck paying for the family!", "Don't you just hate it when you accidently take money from work?", "You woke up with a cold and decided to stay home",
              "Your boss gave you a 'few days off'! Turns out you were fired.", "You're fired! Find a new job.", "You got picked on at work and cried in your customers food. FIRED!", "You got roasted by your boss."]
class Leaderboard:
    """Gets the top 5 people with the most ticket balances. ``$leaderboard``"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Currency"


    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.message.channel.send("Little to quick there! :wink: ")
        else:
            print(error)
    
    @commands.cooldown(1,2,BucketType.user) 
    @commands.command(no_pm=True, pass_contex=True)
    async def leaderboard(self,ctx):
        message = ctx.message
        person = message.author
        with open("Data/servers.json", "r") as thejsonfile:
            data = json.load(thejsonfile)
        if str(message.guild.id) in data:
            first = ["", 0]
            second = ["", 0]
            third = ["", 0]
            fourth = ["", 0]
            fifth = ["", 0]
            server = data[str(message.guild.id)]
            storage = server["tickets-storage"]
            for player in storage:
                cred = storage[player]["credits"]
                if cred > first[1]:
                    fifth = fourth
                    fourth = third
                    third = second
                    second = first
                    first = [message.guild.get_member(int(player)).name, cred]
                elif cred > second[1]:
                    fifth = fourth
                    fourth = third
                    third = second
                    second = [message.guild.get_member(int(player)).name, cred]
                elif cred > third[1]:
                    fifth = fourth
                    fourth = third
                    third = [message.guild.get_member(int(player)).name, cred]
                elif cred > fourth[1]:
                    fifth = fourth
                    fourth = [message.guild.get_member(int(player)).name, cred]
                elif cred > fifth[1]:
                    fifth = [message.guild.get_member(int(player)).name, cred]

            if first[0] != "":
                first = f"**FIRST** : ``{first[0]}`` with ``{first[1]}`` tickets. <:nbaghost:368751631455748096>\n\n"
            else:
                first = ""
                
            if second[0] != "":
                second = f"**SECOND** : ``{second[0]}`` with ``{second[1]}`` tickets."
            else:
                second = ""

            if third[0] != "":
                third = f"**THIRD** : ``{third[0]}`` with ``{third[1]}`` tickets."
            else:
                third = ""

            if fourth[0] != "":
                fourth = f"**FOURTH** : ``{fourth[0]}`` with ``{fourth[1]}`` tickets."
            else:
                fourth = ""

            if fifth[0] != "":
                fifth = f"**FIFTH** : ``{fifth[0]}`` with ``{fifth[1]}`` tickets."
            else:
                fifth = ""
            embed=discord.Embed(color=0x8e370d)
            embed.set_author(name=f"Leaderboard for {message.guild.name}", icon_url=message.author.avatar_url)
            embed.add_field(name="\u200b", value=first, inline=False)
            embed.add_field(name="\u200b", value=second, inline=False)
            embed.add_field(name="\u200b", value=third, inline=False)
            embed.add_field(name="\u200b", value=fourth, inline=False)
            embed.add_field(name="\u200b", value=fifth, inline=False)

            await message.channel.send(embed=embed)
                    
        else:
            await message.channel.send("For some reason your server isn't verified. Please kick and reinvite the bot!")
            

def setup(bot):
    p = Leaderboard(bot)
    bot.add_cog(p)
