from discord.ext import commands
import discord
import json
import random
import requests
letters_one = ["building", "scripting", "graphics", "development", "coding", "modeling"]
letters_two = ["fun", "happy", "normal", "cool", "great", "good"]
letters_three = ["obc", "tbc", "bc", "nbc"]
letters_four = ["meepcity", "build a hideout and fight", "no game", "shoe", "simulator", "wanna be friends"]

class Verify:
    """$**verify ROBLOXNAME**"""
    def __init__(self, bot):
        self.bot = bot
        self.type = "Roblox"
    @commands.command(no_pm=True, pass_contex=True)
    async def verify(self,ctx, username=None):
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
        if username == None:
            await message.channel.send("Please enter your roblox username.")
            return
        link = "https://api.roblox.com/users/get-by-username?username="+username
        link2 = "https://www.roblox.com/users/{zid}/profile"
        source = requests.get(link)
        text = source.text
        jsonversion = json.loads(text)
        random.seed()
        with open("Data\\verifiedusers.json", "r") as thejsonfile:
            data = json.load(thejsonfile)
        code = letters_one[random.randrange(0, len(letters_one) - 1)] + " " + letters_two[random.randrange(0, len(letters_two) - 1)] + " " + letters_three[random.randrange(0, len(letters_three) - 1)] + " " + letters_four[random.randrange(0, len(letters_four) - 1)] + ""
        if "Id" in jsonversion:
            zid = jsonversion["Id"]
        else:
            zid = None
        if zid != None:
            if str(message.author.id) in data["users"]:
                authorsdata = data["users"][str(message.author.id)]
                if authorsdata["verified"] == True:
                    print(f"Comparing {zid} and {authorsdata['userid']}")
                    if int(zid) == int(authorsdata["userid"]):
                        try:
                            if message.guild.id == 366339459194552320:
                                zlink = "https://www.roblox.com/users/"+str(data["users"][str(message.author.id)]["userid"])+"/profile"
                                zsource = requests.get(zlink)
                                ztext = zsource.text
                                obcrole = discord.utils.get(message.guild.roles, name='OBC')
                                tbcrole = discord.utils.get(message.guild.roles, name='TBC')
                                bcrole = discord.utils.get(message.guild.roles, name='BC')
                                if (obcrole in message.author.roles):
                                    await message.author.remove_roles(obcrole)
                                if (tbcrole in message.author.roles):
                                    await message.author.remove_roles(tbcrole)
                                if (bcrole in message.author.roles):
                                    await message.author.remove_roles(bcrole)
                                if 'icon-obc' in ztext:
                                    print("OBC")
                                    await message.author.add_roles(obcrole)
                                elif 'icon-tbc' in ztext:
                                    print("TBC")
                                    await message.author.add_roles(tbcrole)
                                elif 'icon-bc' in ztext:
                                    print("BC")
                                    await message.author.add_roles(bcrole)
                                
                            role = theserverrole
                            if not (role in message.author.roles):
                                await message.author.add_roles(role)
                            authorsdata["code"] = "__none__"
                            return
                        except Exception as error:
                            print(error)
                            await message.channel.send("Either I don't have permission to give roles or I'm not a higher rank then the person I'm trying to role. Please DM the owner to fix this!")
                            return
                    else:
                        authorsdata["code"] = code
                        authorsdata["verified"] = False
                        authorsdata["userid-want"] = zid
                else:
                    authorsdata["code"] = code
                    authorsdata["verified"] = False
                    authorsdata["userid-want"] = zid
            else:
                data["users"][message.author.id] = {
                    ("userid"):"__none__",
                    ("code"):code,
                    ("verified"):False,
                    ("userid-want"):str(zid)
                }
            with open("Data/verifiedusers.json", "w") as thejsonfile2:
                json.dump(data, thejsonfile2)

            await message.channel.send("Your code is \n\n``"+code+"``\n\nPut it in your roblox profile. Once done use the finish command. (Ex. $finish) <:nbaghost:368751631455748096>")
        else:
            await message.channel.send("That user doesn't exist. Please try again!")


def setup(bot):
    p = Verify(bot)
    bot.add_cog(p)
