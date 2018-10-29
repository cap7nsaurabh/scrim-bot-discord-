import discord
import youtube_dl
from discord.ext import commands
from discord import opus
import random
bot = commands.Bot(command_prefix="!")
token="discord token"
#@bot.event
#async def on_member_join(member):
#    await bot.send_message(bot.channel,"{0}.mention is lost someone guide him".format(member))
@bot.event
async def on_message(message):
    if message.content.startswith("$help"): #description
        print("command executed help by {0} \n".format(message.author.mention))
        tit1="Scrim commands"
        desc1="This bot will help in solo and squad scrims"
        com1="command: $help"
        desc2="tells you about all bot functionality"
        com2="command: !greet"
        desc3="Greets users"
        com3="Command: !come"
        desc4="calls bot to voice channel"
        com4="Command: !lv"
        desc5="Bot will leave voice channel"
        com5="command !start"
        desc6="Bot will initiate scrim"
        desc7="if bot is in different channel enter !lv command then !come the bot"
        com6="!roll"
        desc8="rolls a dice"
        embed = discord.Embed(title=tit1, description=desc1, color=0x00ff00)
        embed.add_field(name=com1, value=desc2, inline=False)
        embed.add_field(name=com2, value=desc3, inline=False)
        embed.add_field(name=com3, value=desc4, inline=False)
        embed.add_field(name=com4, value=desc5, inline=False)
        embed.add_field(name=com5, value=desc6, inline=False)
        embed.add_field(name=com6, value=desc8, inline=False)
        embed.add_field(name="note:", value=desc7, inline=False)
        await bot.send_message(message.channel, embed=embed)
    #if message.content.startswith("!taunt"):
    if message.content.startswith("!lv"): #leave command
            print("command executed leave by {0} \n".format(message.author.mention))
            try:
                x=bot.voice_client_in(message.server)
                return await x.disconnect()
            except:
                await bot.send_message(message.channel,"oops bot failed to leave..that shouldn't have happened..")
                await bot.send_message(message.channel,"join the voice channel of the bot again and enter !come and then !lv..")
                print("leave error!!")
    if message.content.startswith("!roll"): #roll command
        print("command executed roll by {0} \n".format(message.author.mention))
        i=random.randint(1,6)
        msg="the dice says {0}".format(i)
        await bot.send_message(message.channel,msg)
    if message.content.startswith("!come"): #summon command
        print("command executed summon by {0} \n".format(message.author.mention))
        summoned_channel = message.author.voice_channel
        if summoned_channel is None:
            await bot.send_message(message.channel,'You are not in a voice channel.')
            return 
        state = bot.is_voice_connected(message.server)
        if state is False:
            vc = await bot.join_voice_channel(summoned_channel)
            return True
        else:
            vc=await bot.move_to(summoned_channel)
            return True
    if message.content.startswith("!greet"): #greet command
        print("command executed greet by {0} \n".format(message.author.mention))
        await bot.send_message(message.channel,":smiley: :wave: Hello,{0.author.mention}".format(message))
        return True
    if message.content.startswith("!start"): #start command
        print("command executed start by {0} \n".format(message.author.mention))
        if bot.is_voice_connected(message.server) is False:
            await bot.send_message(message.channel,"either you or the is Bot not in voice channel..join a voice channel and send command !come to call bot to voice channel")
        else:
            await bot.send_message(message.channel,"count down starting...:smiley: all the best players..")
            vc=bot.voice_client_in(message.server)
            pl=vc.create_ffmpeg_player('scrim.mp3',use_avconv=False)
            pl.start()
        return True
   
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print("logs-->")
