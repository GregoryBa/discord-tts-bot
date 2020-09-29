import discord
from async_timeout import timeout
from discord.ext import commands

class ShortAudio(commands.Cog):
    def __init__(self, bot: commands.Bot, vc):
        self.bot = bot
        self.vc = vc
        
    @commands.command(pass_context=True)
    async def brb(self, ctx):
        self.vc.play(discord.FFmpegPCMAudio('audio//brb.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def brap(self, ctx):
        self.vc.play(discord.FFmpegPCMAudio('audio//brap.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def bruh(self, ctx):
        self.vc.play(discord.FFmpegPCMAudio('audio//bruh.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def cuphead(self, ctx):
        self.vc.play(discord.FFmpegPCMAudio('audio//cuphead.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def findyou(self, ctx):
        self.vc.play(discord.FFmpegPCMAudio('audio//findyou.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def headshake(self, ctx):
        self.vc.play(discord.FFmpegPCMAudio('audio//headshake.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def jonny(self, ctx):
        self.vc.play(discord.FFmpegPCMAudio('audio//jonny.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def hello(self, ctx):
        self.vc.play(discord.FFmpegPCMAudio('audio//knock.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def minecraft(self, ctx):
        self.vc.play(discord.FFmpegPCMAudio('audio//minecraft.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def nani(self, ctx):
        self.vc.play(discord.FFmpegPCMAudio('audio//nani.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def notpass(self, ctx):
        self.vc.play(discord.FFmpegPCMAudio('audio//notpass.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def sparta(self, ctx):
        self.vc.play(discord.FFmpegPCMAudio('audio//sparta.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def suspense(self, ctx):
        self.vc.play(discord.FFmpegPCMAudio('audio//suspense.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def swing(self, ctx):
        self.vc.play(discord.FFmpegPCMAudio('audio//swing.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def tun(self, ctx):
        self.vc.play(discord.FFmpegPCMAudio('audio//tun.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def wow(self, ctx):
        self.vc.play(discord.FFmpegPCMAudio('audio//wow.mp3'),
                after=lambda e: print('done', e))

    # TRASH AUDIO FIX

    @commands.command(pass_context=True)
    async def tech(self, ctx):
        self.vc.play(discord.FFmpegPCMAudio('audio//tech.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def meep(self, ctx):
        self.vc.play(discord.FFmpegPCMAudio('audio//meep.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def gay(self, ctx):
        self.vc.play(discord.FFmpegPCMAudio('audio//gay.mp3'),
                after=lambda e: print('done', e))

    @commands.command(pass_context=True)
    async def oof(self, ctx):
        self.vc.play(discord.FFmpegPCMAudio('audio//oof.mp3'),
                after=lambda e: print('done', e))