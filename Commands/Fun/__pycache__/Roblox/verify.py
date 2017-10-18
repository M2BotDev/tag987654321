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
    def __init__(self, bot):
        self.bot = bot
        self.type = "Roblox"
    @commands.command(no_pm=True, pass_contex=True)
    async def verify(self,ctx, username=None):
        message = ctx.message
        if username == None:
            await message.channel.send("Please enter your roblox username.")
            return
        link = "https://api.roblox.com/users/get-by-username?username="+username
        link2 = "https://www.roblox.com/users/{zid}/profile"
        source = requests.get(link)
        text = source.text
        jsonversion = json.loads(text)
        random.seed()
        with open("Data/verifiedusers.json", "r") as thejsonfile:
            data = json.load(thejsonfile)
        code = letters_one[random.randrange(0, len(letters_one) - 1)] + " " + letters_two[random.randrange(0, len(letters_two) - 1)] + " " + letters_three[random.randrange(0, len(letters_three) - 1)] + " " + letters_four[random.randrange(0, len(letters_four) - 1)] + ""
        if "Id" in jsonversion:
            zid = jsonversion["Id"]
        else:
            zid = None
        if zid != None:
            if message.author.id in data["users"]:
                authorsdata = data["users"][message.author.id]
                authorsdata["code"] = code
                authorsdata["userid"] = zid
            else:
                data["users"][message.author.id] = {
                    ("userid"):str(zid),
                    ("code"):code,
                    ("verified"):False
                }
            with open("Data/verifiedusers.json", "w") as thejsonfile2:
                json.dump(data, thejsonfile2)

            await message.channel.send("Your code is \n\n``"+code+"``\n\nPut it in your roblox profile. Once done use the finish command. (Ex. $finish)")
        else:
            await message.channel.send("That user doesn't exist. Please try again!")


def setup(bot):
    p = Verify(bot)
    bot.add_cog(p)
