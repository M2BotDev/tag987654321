from discord.ext import commands
import discord
import json
import random
import requests

class Finish:
    def __init__(self, bot):
        self.bot = bot
        self.type = "Roblox"
    @commands.command(no_pm=True, pass_contex=True)
    async def finish(self,ctx):
        message = ctx.message
        with open("Data/verifiedusers.json", "r") as thejsonfile:
            data = json.load(thejsonfile)

        if str(message.author.id) in data["users"]:
            print(data["users"][str(message.author.id)])
            link = "https://www.roblox.com/users/"+data["users"][str(message.author.id)]["userid"]+"/profile"
            source = requests.get(link)
            text = source.text
            if data["users"][str(message.author.id)]["code"] == "__none__":
                return
            random.seed()
            if data["users"][str(message.author.id)]["code"].lower() in text.lower():
                data["users"][str(message.author.id)]["verified"] = True
                data["users"][str(message.author.id)]["code"] = "__none__"
                try:
                    obcrole = discord.utils.get(message.guild.roles, name='OBC')
                    tbcrole = discord.utils.get(message.guild.roles, name='TBC')
                    bcrole = discord.utils.get(message.guild.roles, name='BC')
                    if (obcrole in message.author.roles):
                        await message.author.remove_roles(obcrole)
                    if (tbcrole in message.author.roles):
                        await message.author.remove_roles(tbcrole)
                    if (bcrole in message.author.roles):
                        await message.author.remove_roles(bcrole)
                        
                    if 'icon-obc' in text:
                        print("OBC")
                        await message.author.add_roles(obcrole)
                    elif 'icon-tbc' in text:
                        print("TBC")
                        await message.author.add_roles(tbcrole)
                    elif 'icon-bc' in text:
                        print("BC")
                        await message.author.add_roles(bcrole)
                        
                    role = discord.utils.get(message.guild.roles, name='Members')
                    if not (role in message.author.roles):
                        await message.author.add_roles(role)
                except Exception as error:
                    print(error)
                    await message.channel.send("I don't have permission to give roles. Please DM the owner to fix this!")
            else:
                await message.channel.send("Please make sure the code is in your profile!")
        else:
            await message.channel.send("You're not verified! Please use the verify [ROBLOXNAME] command!")

        with open("Data/verifiedusers.json", "w") as thejsonfile2:
            json.dump(data, thejsonfile2)

def setup(bot):
    p = Finish(bot)
    bot.add_cog(p)
