from discord.ext import commands
import discord
import json
import random
import requests

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
class Bigword:
    """$**bigword message**"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Giveaway"
    @commands.command(no_pm=True, pass_contex=True)
    async def bigword(self,ctx,*,text=None):
        message = ctx.message
        if text != None:
            newtext = ""
            for letter in text:
                if letter.lower() in letters:
                    newtext += f":regional_indicator_{letter.lower()}:"
                elif letter.lower() == ">":
                    newtext += f":arrow_forward:"
                elif letter.lower() == "<":
                    newtext += f":arrow_backward:"
                elif letter.lower() == "#":
                    newtext += f":hash:"
                elif letter.lower() == " ":
                    newtext += f"     "
                else:
                    try:
                        newtext += f":{numbers[int(letter.lower())]}:"
                    except:
                         newtext += letter
            embed=discord.Embed(description=newtext, color=0x8e370d)
            embed.set_author(name=message.author.display_name, url=message.author.avatar_url, icon_url=message.author.avatar_url)
            embed.set_footer(text=message.created_at)
            await message.channel.send(embed=embed)



def setup(bot):
    p = Bigword(bot)
    bot.add_cog(p)
