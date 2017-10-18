from discord.ext import commands
import discord
import json
import random
import requests

class Userinfo:
    """$**userinfo** or **userinfo @user#1234**"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Giveaway"
    @commands.command(no_pm=True, pass_contex=True)
    async def userinfo(self,ctx,mention=None):
        message = ctx.message
        owner = "No"
        bot = "No"
        nickname = "None"
        try:
            mention = message.mentions[0]
        except:
            mention = message.author
        if mention == message.guild.owner:
            owner = "Yes"
        if mention.bot:
            bot = "Yes"
        if mention.display_name != mention.name:
            nickname = mention.display_name
        embed=discord.Embed(title="User ID", description=mention.id, color=0x8e370d)
        embed.set_author(name=mention.name, url=mention.avatar_url, icon_url=mention.avatar_url)
        embed.add_field(name="BOT", value=bot, inline=True)
        embed.add_field(name="NICKNAME", value=nickname, inline=True)
        embed.add_field(name="OWNER", value=owner, inline=True)
        embed.add_field(name="AVATAR LINK", value=mention.avatar_url, inline=True)
        embed.set_footer(text=mention.created_at)
        await message.channel.send(embed=embed)



def setup(bot):
    p = Userinfo(bot)
    bot.add_cog(p)
