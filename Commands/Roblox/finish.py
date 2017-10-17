from discord.ext import commands
import discord
import json
import random
import requests

class Finish:
    """$**finish**"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Roblox"
    @commands.command(no_pm=True, pass_contex=True)
    async def finish(self,ctx):
        message = ctx.message
        with open("Data\\servers.json", "r") as serverfile:
            serverfiledata = json.load(serverfile)
        if str(message.guild.id) in serverfiledata:
            serverin = serverfiledata[str(message.guild.id)]
            theserverrole = discord.utils.get(message.guild.roles, id=serverin["verified-role"])
            if theserverrole == None:
                await message.channel.send("This server doesn't seem to have a verified role. If owner please use the setverified command. (Ex.$setverified ROLENAME)")
                return
        else:
            await message.channel.send("Your server doesn't seem to be verified. Please kick and reinvite the bot!")
            return
        with open("Data\\verifiedusers.json", "r") as thejsonfile:
            data = json.load(thejsonfile)

        if str(message.author.id) in data["users"]:
            print(data["users"][str(message.author.id)])
            link = "https://www.roblox.com/users/"+str(data["users"][str(message.author.id)]["userid-want"])+"/profile"
            source = requests.get(link)
            text = source.text
            if data["users"][str(message.author.id)]["code"] == "__none__":
                return
            random.seed()
            if data["users"][str(message.author.id)]["code"].lower() in text.lower():
                data["users"][str(message.author.id)]["verified"] = True
                data["users"][str(message.author.id)]["code"] = "__none__"
                try:
                    if message.guild.id == 366339459194552320:
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
                        
                    
                    role = theserverrole
                    data["users"][str(message.author.id)]["userid"] = data["users"][str(message.author.id)]["userid-want"]
                    data["users"][str(message.author.id)]["userid-want"] = "__none__"
                    if not (role in message.author.roles):
                        await message.author.add_roles(role)
                except Exception as error:
                    print(error)
                    await message.channel.send("Either I don't have permission to give roles or I'm not a higher rank then the person I'm trying to role. Please DM the owner to fix this!")
            else:
                await message.channel.send("Please make sure the code is in your profile! <:nbaghost:368751631455748096>")
        else:
            await message.channel.send("You're not verified! Please use the verify [ROBLOXNAME] command! <:nbaghost:368751631455748096>")

        with open("Data/verifiedusers.json", "w") as thejsonfile2:
            json.dump(data, thejsonfile2)

def setup(bot):
    p = Finish(bot)
    bot.add_cog(p)
