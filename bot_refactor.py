# Imports needed:
import asyncio
import functools
import itertools
import math
import random
import discord
import youtube_dl
from gtts import gTTS
from async_timeout import timeout
from discord.ext import commands
from random import randint

# My files:
from shortaudio import ShortAudio
from bottalk import BotTalk
from meme import Meme
from gif import Gif


typing_counter = 0

class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        # For voice messages:
        self.botTalk = BotTalk()
        # For gif messages:
        bot.add_cog(Gif(bot))

    @commands.command(name='join', invoke_without_subcommand=True)
    async def join(self, ctx: commands.Context):
        """ JOINS VOICE CHANNEL """
        global channel
        global vc

        channel = ctx.author.voice.channel
        vc = await channel.connect()
        # Activating audio commands:
        bot.add_cog(ShortAudio(bot, vc))
        bot.add_cog(Meme(bot, vc))

        await ctx.send(embed=self.botTalk.intro())
        
    @commands.command(pass_context=True)
    async def stop(self, ctx):
        vc.stop()

    @commands.command(pass_context=True)
    async def random(self, ctx):
        await ctx.send(embed=self.botTalk.random())
   
    @commands.command(pass_context=True)
    async def meme(self, ctx):
        await ctx.send(embed=self.botTalk.meme())

    @commands.command(pass_context=True)
    async def gif(self, ctx):
        await ctx.send(embed=self.botTalk.gif())
    
    @commands.command(pass_context=True)
    async def futuredev(self, ctx):
        await ctx.send(embed=self.botTalk.futuredev())
    
    @commands.command(pass_context=True)
    async def cmd(self, ctx):
        await ctx.send(embed=self.botTalk.intro())
   


bot = commands.Bot('', description='Memes and Gifs but mostly audio')
bot.add_cog(Commands(bot))

@bot.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))


# @bot.event
# async def on_message(message):
#     # print(f'By: {message.author.name}')
#     # print(f'Content: {message.content}')
#     # print(f'Channel: {message.channel}')
#     if message.author.name == 'RudeBot':
#         pass
#     else:
#         await bot.process_commands(message)

@bot.event
async def on_voice_state_update(member, before, after):
    print(f'Memeber: {member.name}')
    print(f'Before: {before.channel}')
    print(f'After: {after.channel}')

    tts = gTTS(f'{member.name} joined the voice channel')
    tts.save('botspeak.mp3')

    if after.channel == None:
        tts = gTTS(f'{member.name} left the voice channel')
        tts.save('botspeak.mp3')
        vc.play(discord.FFmpegPCMAudio('botspeak.mp3'),
                after=lambda e: print('done', e))

    elif before.channel == None:
        tts = gTTS(f'{member.name} joined the voice channel')
        tts.save('botspeak.mp3')
        vc.play(discord.FFmpegPCMAudio('botspeak.mp3'),
                after=lambda e: print('done', e))


bot.run('NzQwMjE3NDk1OTk0MTA1ODg2.XylzQw.FEVI_HH8xxzR0YpHIPKQ3vXmTm0')



















# EMBED:
'''
embed = (discord.Embed(title='Now playing',
                               description='```css\n{0.source.title}\n```'.format(self),
                               color=discord.Color.blurple())
                 .add_field(name='Duration', value=self.source.duration)
                 .add_field(name='Requested by', value=self.requester.mention)
                 .add_field(name='Uploader', value='[{0.source.uploader}]({0.source.uploader_url})'.format(self))
                 .add_field(name='URL', value='[Click]({0.source.url})'.format(self))
                 .set_thumbnail(url=self.source.thumbnail))



'''