from discord.ext import commands
import discord
import json
import random
import requests

class Rank:
    """Gets the level and experience of a discord member. ``$rank @user#1234``"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Giveaway"
    @commands.command(no_pm=True, pass_contex=True)
    async def rank(self,ctx,*,user=None):
        message = ctx.message
        try:
            if message.mentions[0]:
                user = message.mentions[0]
            else:
                user = message.author
        except:
            user = message.author

        with open("Data/servers.json") as filejson:
            data = json.load(filejson)

        if str(message.guild.id) in data:
            guild = data[str(message.guild.id)]
            if not ("levels" in guild):
                guild["levels"] = {}
            levels = guild["levels"]
            if not (str(user.id) in levels):
                levels[str(user.id)] = {
                    ("LVL") : 1,
                    ("XP") : 0,
                    ("WAITNUM") : 0
                }
            authorin = levels[str(user.id)]
        else:
            return
        embed=discord.Embed(title="Rank", description=f"Rank for {user.name} in {message.guild}", color=0xe6ce28)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="LVL", value=authorin["LVL"], inline=True)
        embed.add_field(name="XP", value=authorin["XP"], inline=True)
        embed.add_field(name="Required XP", value=authorin["LVL"] * 100, inline=True)
        embed.set_footer(text=f"{user.created_at}")
        await message.channel.send(embed=embed)
        with open("Data/servers.json", "w") as saveme:
            json.dump(data, saveme)
        





def setup(bot):
    p = Rank(bot)
    bot.add_cog(p)
