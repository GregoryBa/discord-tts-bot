import discord
from async_timeout import timeout
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def meme(self, ctx):
        title = 'RudeBot BETA v2'
        description = 'All kinds of memes'
        embed = discord.Embed()
        embed.colour = discord.Colour.blue()
        embed.title = title
        embed.description = description
        embed.add_field(name = 'Memes:', value='!name, !fuckyou, !damnboy, !crack, !russian, !squish, !weeb, !muffin, !whoasked, !lol, !chicken, !csgo, !yeet, !despacito, !whygay', inline=True)
        await ctx.send(embed=embed)



        await ctx.send(f'```!name = my name\n!fuckyou = yup\n!damnboy = thick\n!crack = ??\n!russian = suka blyat\n!squish = cat\n!weeb = fockin weeb\n!muffin = DIE!\n!whoasked = who did?\n!lol = lol?\n!chicken\n!csgo\n!yeet\n!despacito\n!whygay```')

    def intro(self):
        title = 'RudeBot BETA v2'
        description = '*TTS still fucked and AI is dumber than AJAX spray*'
        embed = discord.Embed()
        embed.colour = discord.Colour.red()
        embed.title = title
        embed.description = description
        embed.add_field(name = 'Commands:', value='!meme, !random, !helpme, !stop, !test', inline=True)
        return embed

    @commands.command(pass_context=True)
    async def random(self, ctx):
        await ctx.send(f'```!brb\n!brap\n!bruh\n!cuphead\n!dead\n!findyou\n!headshake\n!jonny\n!hello\n!minecraft\n!nani\n!notpass\n!sparta\n!suspense\n!swing\n!tun\n!wow\n!meep\n!gay\n!oof```')

    @commands.command(pass_context=True)
    async def helpme(self, ctx):
        await ctx.send(f"```css\nHEY RETARD YOU HAVE TO !join\n``` __**COMMANDS:**__```css\n!meme for meme\n!random for random\n!helpme for retard \n!stop for stop it```")

