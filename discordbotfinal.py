import discord
import os
import youtube_dl
from discord.ext import commands
op="libopus.so.1"
discord.opus.load_opus(op)
token="<token goes here>"
bot = commands.Bot(command_prefix="!")
@bot.event
async def on_message(message):
    if message.content.startswith("$help"):
        tit1="Scrim commands"
        desc1="This bot will help in solo and squad scrims"
        com1="command: $help"
        desc2="tells you about all bot functionality"
        com2="command: !greet"
        desc3="Greets users"
        com3="Command: !summon"
        desc4="calls bot to voice channel"
        com4="Command: !leave"
        desc5="Bot will leave voice channel"
        com5="command !start"
        desc6="Bot will initiate scrim"
        embed = discord.Embed(title=tit1, description=desc1, color=0x00ff00)
        embed.add_field(name=com1, value=desc2, inline=False)
        embed.add_field(name=com2, value=desc3, inline=False)
        embed.add_field(name=com3, value=desc4, inline=False)
        embed.add_field(name=com4, value=desc5, inline=False)
        embed.add_field(name=com5, value=desc6, inline=False)
        #embed.add_field(name="Field2", value="hi2", inline=False)
        await bot.send_message(message.channel, embed=embed)
    if message.content.startswith("!leave"):
            #for x in bot.voice_clients:
            #    if(x.server == message.server):
            x=bot.voice_client_in(message.server)
            return await x.disconnect()
    if message.content.startswith("!summon"):
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
    if message.content.startswith("!greet"):
        await bot.send_message(message.channel,":smiley: :wave: Hello,{0.author.mention}".format(message))
        return True
    if message.content.startswith("!start"):
        if bot.is_voice_connected(message.server) is False:
            await bot.send_message(message.channel,"Bot not in voice channel..send command !summon to call bot to voice channel")
        else:
            await bot.send_message(message.channel,"count down starting...:smiley: all the best players..")
            vc=bot.voice_client_in(message.server)
            pl=vc.create_ytdl_player("https://www.youtube.com/watch?v=nyC0c6t7Vq0",avconv=False)
            pl.start()
        return True
    
#@bot.command()
#async def greet(ctx):
#    await ctx.send(":smiley: :wave: Hello, there!")
#@bot.command()
#async def start(ctx):
#    if bot.is_connected() is False:
#        await ctx.send("Bot not in voice channel..send command !summon to call bot to voice channel")
#    else:
#        await ctx.send("count down starting...:) all the best players..")
#@bot.command(pass_context=True, no_pm=True)
#async def summon(ctx):
#        """Summons the bot to join your voice channel."""
#        summoned_channel = ctx.message.author.voice_channel
#        if summoned_channel is None:
#            await bot.say('You are not in a voice channel.')
#            return False
#
#        state = bot.is_voice_connected(ctx.message.server)
#        if state is False:
#            vc = await bot.join_voice_channel(summoned_channel)
#        else:
#            await bot.move_to(summoned_channel)
#
#        return True
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
bot.run(str(os.environ.get('BOT_TOKEN')))
    
