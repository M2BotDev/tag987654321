import discord
from discord.ext import commands
import os
import json
import random

cmds = {}

def loopthrough(u, w):
    path = os.listdir(u)
    for file in path:
        if file.endswith(".py"):
            w[file[:-3]] = file
        else:
            if not file == "__pycache__":
                w[file] = {}
                x = u + "/" + file
                loopthrough(x, w[file])
loopthrough("Commands", cmds)
    

async def getpre(bot, message):
    with open("Data/servers.json") as serverjson:
        serverdata = json.load(serverjson)
    x = message.guild
    if str(x.id) in serverdata:
        return serverdata[str(x.id)]["prefix"]
    else:
        return "$"

bot = commands.Bot(command_prefix=getpre, description='Bot')
bot.remove_command("help")

@bot.event
async def on_guild_join(guild):
    try:
        with open("Data/servers.json") as serverjsona:
            guilddata = json.load(serverjsona)
        if str(guild.id) in guilddata:
            pass
        else:
            guilddata[str(guild.id)] = {
                ("prefix"): "$", 
                ("log-channel"): "__disabled__", 
                ("muted-role"): "__disabled__",
                ("verified-role"): "__disabled__",
                ("tickets-storage") : {}
            }
            with open("Data/servers.json", "w") as serverjson2:
                json.dump(guilddata, serverjson2)
    except Exception as e:
        print(e)
    for channel in guild.channels:
        try:
            await channel.send("Thanks for inviting me! Here are some things you might want to know before getting started!\n\n**Verification**\nYou can do $setverified ROLENAME to change the role that users get when verifying. If the role doesn't exist they can't verify.\n**Logs**\nGo into the channel you'd like to use for logs and do $setlogchannel to receive logs there. If you don't like the logs you can do $removelogchannel to stop the bot from sending logs there. Or you can move it to a different channel.\n**Prefix**\nIncase the bots prefix overlaps with another bot you can do $prefix NEWPREFIX to change it. Keep in mind if you want to change the prefix again you have to use your new prefix for the prefix command.")
            return
        except Exception as e:
            print(e)
            continue

@bot.event
async def on_message_delete(message):
    with open("Data/servers.json", "r") as filejson:
        jsondatafile = json.load(filejson)
    if str(message.guild.id) in jsondatafile:
        try:
            whofrom = message.author.name
            action = f"Deleted message"
            created_at = message.created_at
            embed=discord.Embed(title=f"From : {whofrom}", color=0x8e370d)
            embed.add_field(name="ACTION", value=action, inline=False)
            embed.add_field(name="Message", value=message.content, inline=False)
            embed.set_footer(text=created_at)
            logchannel = discord.utils.get(message.guild.channels, id = jsondatafile[str(message.guild.id)]["log-channel"])
            await logchannel.send(embed=embed)
        except Exception as e:
            return
    else:
        return
@bot.event
async def on_message_edit(before, after):
    message = after
    if after.content == before.content:
        return
    with open("Data/servers.json", "r") as filejson:
        jsondatafile = json.load(filejson)
    try:
        if str(message.guild.id) in jsondatafile:
            try:
                whofrom = message.author.name
                created_at = message.created_at
                embed=discord.Embed(title=f"From : {whofrom}", color=0x8e370d)
                embed.add_field(name="BEFORE", value=before.content, inline=False)
                embed.add_field(name="EDITED", value=after.content, inline=False)
                embed.set_footer(text=created_at)
                logchannel = discord.utils.get(message.guild.channels, id = jsondatafile[str(message.guild.id)]["log-channel"])
                await logchannel.send(embed=embed)
            except Exception as e:
                return
        else:
            return
    except:
        return
@bot.event
async def on_ready():
    if __name__ == "__main__":
        for extension in cmds:
            try:
                if not extension.endswith(".py"):
                    def bl(l, e):
                        for x in e:
                            if isinstance(e[x], dict):
                                bl(l + "." + x, e[x])
                            elif e[x].endswith('.py'):
                                bot.load_extension("Commands." + l + "." + x)
                    bl(extension, cmds[extension])
                else:
                    bot.load_extension("Commands." + extension)
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__, e)
                print('Failed to load extension {}/n{}'.format(extension, exc))
    print("Ready!")

@bot.event
async def on_message(message):
    pre = "$"
    with open("Data/servers.json") as serverjson:
        serverdata = json.load(serverjson)
    x = message.guild
    if str(x.id) in serverdata:
        pre = serverdata[str(x.id)]["prefix"]

    if message.content.lower().startswith(bot.user.mention + " prefix"):
        await message.channel.send(f"Prefix is {pre}")
    with open("Data/servers.json") as theserverjsonforlevels:
        data = json.load(theserverjsonforlevels)
    user = message.author
    try:
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
            if authorin["WAITNUM"] >= 5:
                authorin["WAITNUM"] = 0
                authorin["XP"] += random.randint(1, 10)
            else:
                authorin["WAITNUM"] += 1
            if authorin["XP"] >= authorin["LVL"] * 100:
                authorin["XP"] -= authorin["LVL"] * 100
                authorin["LVL"] += 1
                await message.channel.send(f"{user.mention}, Good job on ranking up! You're now level {authorin['LVL']}!")
        with open("Data/servers.json", "w") as theserverjsonforlevels2:
            json.dump(data,theserverjsonforlevels2)
    except:
        return
    await bot.process_commands(message)
bot.run("MzY2MzY1NzEwNzQzNjMzOTMw.DLr0LA.kqJcAMeaNh26dPezFmIwJSCjia8")
