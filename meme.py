import discord
from async_timeout import timeout
from discord.ext import commands

class Meme(commands.Cog):
    def __init__(self, bot: commands.Bot, vc):
        self.bot = bot
        self.vc = vc

    @commands.command(pass_context=True)
    async def name(self, ctx):
        await ctx.send(file=discord.File('memes//pics//name.jpg'))
        self.vc.play(discord.FFmpegPCMAudio('memes//name.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def chicken(self, ctx):
        await ctx.send(file=discord.File('memes//pics//chicken.jpg'))
        self.vc.play(discord.FFmpegPCMAudio('memes//chicken.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def fuckyou(self, ctx):
        await ctx.send(file=discord.File('memes//gifs//fuckyou.gif'))
        self.vc.play(discord.FFmpegPCMAudio('memes//fuckyou.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def damnboy(self, ctx):
        await ctx.send(file=discord.File('memes//gifs//damnboy.gif'))
        self.vc.play(discord.FFmpegPCMAudio('memes//damnboy.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def russian(self, ctx):
        await ctx.send(file=discord.File('memes//pics//russian.jpg'))
        self.vc.play(discord.FFmpegPCMAudio('memes//russian.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def squish(self, ctx):
        await ctx.send(file=discord.File('memes//gifs//squish.gif'))
        self.vc.play(discord.FFmpegPCMAudio('memes//squish.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def crack(self, ctx):
        await ctx.send(file=discord.File('memes//gifs//crack.gif'))
        self.vc.play(discord.FFmpegPCMAudio('memes//crack.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def whoasked(self, ctx):
        await ctx.send(file=discord.File('memes//gifs//whoasked.gif'))
        self.vc.play(discord.FFmpegPCMAudio('memes//whoasked.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def lol(self, ctx):
        await ctx.send(file=discord.File('memes//gifs//lol.gif'))
        self.vc.play(discord.FFmpegPCMAudio('memes//lol.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def muffin(self, ctx):
        await ctx.send(file=discord.File('memes//gifs//muffin.gif'))
        self.vc.play(discord.FFmpegPCMAudio('memes//muffin.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def csgo(self, ctx):
        await ctx.send(file=discord.File('memes//gifs//csgo.gif'))
        self.vc.play(discord.FFmpegPCMAudio('memes//dead.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def whygay(self, ctx):
        await ctx.send(file=discord.File('memes//gifs//whygay.gif'))
        self.vc.play(discord.FFmpegPCMAudio('memes//whygay.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def despacito(self, ctx):
        await ctx.send(file=discord.File('memes//gifs//despacito.gif'))
        self.vc.play(discord.FFmpegPCMAudio('memes//despacito.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def yeet(self, ctx):
        await ctx.send(file=discord.File('memes//gifs//yeet.gif'))
        self.vc.play(discord.FFmpegPCMAudio('memes//yeet.mp3'),
                after=lambda e: print('done', e))
    

    # NEW:
    @commands.command(pass_context=True)
    async def degen(self, ctx):
        await ctx.send(file=discord.File('memes//gifs//degen.gif'))
        self.vc.play(discord.FFmpegPCMAudio('memes//degen.mp3'),
                after=lambda e: print('done', e))
