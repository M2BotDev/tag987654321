from discord.ext import commands
import discord
import json
import random
import requests
import os

cmds = {}
def loopthrough(u, w):
    path = os.listdir(u)
    for file in path:
        if file.endswith(".py"):
            w[file[:-3]] = file
        elif isinstance(w, dict):
            if not file == "__pycache__":
                w[file] = {}
                x = u + "/" + file
                loopthrough(x, w[file])

loopthrough("Commands", cmds)

def capitalize_nth(s, n):
    return s[:n].lower() + s[n:].capitalize()

class Help:
    """$**help** or **help CATAGORYNAME**"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Help Command"
    @commands.command(no_pm=True, pass_contex=True)
    async def help(self,ctx, cmd=None):
        message = ctx.message
        aembed=discord.Embed(title=":regional_indicator_c: :regional_indicator_a: :regional_indicator_t: :regional_indicator_e: :regional_indicator_g: :regional_indicator_o: :regional_indicator_r: :regional_indicator_i: :regional_indicator_e: :regional_indicator_s: ", description="\u200b", color=0x8e370d)
        aembed.set_author(name="HELP", icon_url=message.author.avatar_url)
        aembed.set_footer(text=message.created_at)
        if cmd == None:
            for i in cmds:
                if isinstance(cmds[i], dict):
                    aembed.add_field(name=i, value="\u200b",inline=False)
                else:
                    aembed.add_field(name=i,value="\u200b", inline=False)

            await message.channel.send(embed=aembed)
        else:
            embed=discord.Embed(title=":regional_indicator_c: :regional_indicator_o: :regional_indicator_m: :regional_indicator_m: :regional_indicator_a: :regional_indicator_n: :regional_indicator_d: :regional_indicator_s: ", description="\u200b", color=0x8e370d)
            xgg = 0
            def loop(xname, inside, embed, xgg):
                for i in inside:
                    if i.lower() == xname.lower():
                        if isinstance(inside[i], dict):
                            for w in inside[i]:
                                if isinstance(inside[i][w], dict):
                                    embed.add_field(name=w, value="\u200b", inline=False)
                                    xgg += 1
                                else:
                                    z = self.bot.cogs[capitalize_nth(w, 0)]
                                    embed.add_field(name=w, value=z.__doc__, inline=False)
                                    xgg += 1
                        else:
                            string = f"**{i}** - *COMMAND INFO*.\n"
                        return embed,xgg
            try:
                newembed,xgg = loop(cmd, cmds, embed, xgg)
                if xgg != 0:
                    await message.channel.send(embed=embed)
                else:
                    await message.channel.send("Invalid! Please make sure you do $help CATEGORYNAME")
            except Exception as e:
                print(e)
                await message.channel.send("Invalid! Please make sure you do $help CATEGORYNAME")
                return
            

def setup(bot):
    p = Help(bot)
    bot.add_cog(p)
