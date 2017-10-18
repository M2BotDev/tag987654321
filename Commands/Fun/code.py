from discord.ext import commands
import discord
import json
import random
import requests
import sys
import io as StringIO
import contextlib
import re
import math


class Code:
    """$**code CODE** or **code CODEBLOCK**"""
    def __init__(self, bot):
        self.bot = bot
    @commands.command(no_pm=True, pass_contex=True)
    async def code(self,ctx,*,code=None):
        message = ctx.message
        code = f"""{code}"""
        code = re.sub('`', '', code)
        @contextlib.contextmanager
        def stdoutIO(stdout=None):
            old = sys.stdout
            if stdout is None:
                stdout = StringIO.StringIO()
            sys.stdout = stdout
            yield stdout
            sys.stdout = old
        if message.author.id != 264312374931095552:
            return
        thetext = ""
        stuffs = {}
        try:
            with stdoutIO() as s:
                exec(code)
            thetext = s.getvalue()
        except Exception as e:
            thetext = e
        if thetext == "":
            thetext = None
        embed=discord.Embed(color=0x8e370d)
        embed.set_author(name="Code", icon_url=message.author.avatar_url)
        embed.add_field(name="ENTERED", value=f"```py\n{str(code)}\n```", inline=False)
        embed.add_field(name="RESULT", value=f"```\n{str(thetext)}\n```", inline=False)
        embed.set_footer(text=message.created_at)
        await message.channel.send(embed=embed)



def setup(bot):
    p = Code(bot)
    bot.add_cog(p)
