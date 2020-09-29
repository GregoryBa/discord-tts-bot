import discord
from async_timeout import timeout
from discord.ext import commands

class Gif(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def crab(self, ctx):
        await ctx.send(file=discord.File('gifs//crab.gif'))

    @commands.command(pass_context=True)
    async def degen1(self, ctx):
        await ctx.send(file=discord.File('gifs//degen1.gif'))

    @commands.command(pass_context=True)
    async def degen2(self, ctx):
        await ctx.send(file=discord.File('gifs//degen2.gif'))

    @commands.command(pass_context=True)
    async def dramatic(self, ctx):
        await ctx.send(file=discord.File('gifs//dramatic.gif'))

    @commands.command(pass_context=True)
    async def goku(self, ctx):
        await ctx.send(file=discord.File('gifs//goku.gif'))

    @commands.command(pass_context=True)
    async def rasputin(self, ctx):
        await ctx.send(file=discord.File('gifs//rasputin.gif'))

    @commands.command(pass_context=True)
    async def rasputin2(self, ctx):
        await ctx.send(file=discord.File('gifs//rasputin2.gif'))

    @commands.command(pass_context=True)
    async def rasputin3(self, ctx):
        await ctx.send(file=discord.File('gifs//rasputin3.gif'))

    @commands.command(pass_context=True)
    async def reck(self, ctx):
        await ctx.send(file=discord.File('gifs//reck.gif'))
        
    @commands.command(pass_context=True)
    async def rickroll(self, ctx):
        await ctx.send(file=discord.File('gifs//rickroll.gif'))

    @commands.command(pass_context=True)
    async def rus(self, ctx):
        await ctx.send(file=discord.File('gifs//rus.gif'))

    @commands.command(pass_context=True)
    async def sneeze(self, ctx):
        await ctx.send(file=discord.File('gifs//sneeze.gif'))

    @commands.command(pass_context=True)
    async def weeb(self, ctx):
        await ctx.send(file=discord.File('gifs//weeb.gif'))
