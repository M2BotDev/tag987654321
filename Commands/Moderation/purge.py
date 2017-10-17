from discord.ext import commands
import discord
import json
import random
import requests

class Purge:
    """$**purge 85**"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Giveaway"
    @commands.has_permissions(manage_messages=True)
    @commands.command(no_pm=True, pass_contex=True)
    async def purge(self,ctx, amount=None):
        message = ctx.message
        try:
            if int(amount) <= 0:
                await message.channel.send(f"Please enter a value from 1 - 100!")
                return
            if int(amount) > 100:
                await message.channel.send(f"Please enter a value from 1 - 100!")
                return
        except:
            await message.channel.send(f"Invalid number!")
            return
        
        await message.delete()
        await message.channel.purge(limit = int(amount), bulk = True)
        await message.channel.send(f"Purged {amount} messages! <:nbaghost:368751631455748096>")
        with open("Data\\servers.json", "r") as filejson:
            jsondatafile = json.load(filejson)
        if str(message.guild.id) in jsondatafile:
            try:
                whofrom = message.author.name
                action = f"Purged {amount} messages!"
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



def setup(bot):
    p = Purge(bot)
    bot.add_cog(p)
