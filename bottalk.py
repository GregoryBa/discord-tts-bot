import discord
from async_timeout import timeout
from discord.ext import commands


class BotTalk(commands.Cog):
    def __init__(self):
        pass

    def intro(self):
        embed = discord.Embed()
        embed.colour = discord.Colour.red()
        embed.title = 'RudeBot ALPHA v3.1'
        embed.description = '*Workin on TTS, AI is not activated for this*'
        embed.add_field(name='cmd', value='All main commands(this window)')
        embed.add_field(name='meme', value='Some memes')
        embed.add_field(name='random', value='Random sounds')
        embed.add_field(name='gif', value='Gif colleciton')
        embed.add_field(name='stop', value='Shut the fuck up bot')
        embed.add_field(name='futuredev', value='to see what I\'m working on')
        return embed

    def meme(self):
        embed = discord.Embed()
        embed.colour = discord.Colour.blue()
        embed.title = 'MEMES:'
        embed.description = 'Some memes'
        embed.add_field(name = 'name', value = 'What is your name?')
        embed.add_field(name = 'fuckyou', value = 'Fuck you bloody')
        embed.add_field(name = 'damnboy', value = 'That\'s thick')
        embed.add_field(name = 'crack', value = 'Annoying')
        embed.add_field(name = 'russian', value = 'Cyka')
        embed.add_field(name = 'squish', value = 'Squish the cat')  
        embed.add_field(name = 'muffin', value = 'I\'m a muffin')  
        embed.add_field(name = 'whoasked', value = 'Who the fuck asked?')  
        embed.add_field(name = 'lol', value = 'LMAO')  
        embed.add_field(name = 'degen', value = 'Don\'t')
        embed.add_field(name = 'chicken', value = 'Chicken?')  
        embed.add_field(name = 'csgo', value = 'Coffin dance')  
        embed.add_field(name = 'yeet', value = 'yeet?')  
        embed.add_field(name = 'despacito', value = 'Chicken again')  
        embed.add_field(name = 'whygay', value = 'Why are you geh?') 


        return embed

    def random(self):
        embed = discord.Embed()
        embed.colour = discord.Colour.purple()
        embed.title = 'RANDOM'
        embed.description = 'Random sounds'
        embed.add_field(name='brb', value='.')
        embed.add_field(name='brap', value='.')
        embed.add_field(name='bruh', value='.')
        embed.add_field(name='cuphead', value='.')
        embed.add_field(name='dead', value='.')
        embed.add_field(name='findyou', value='.')
        embed.add_field(name='headshake', value='.')
        embed.add_field(name='hello', value='.')
        embed.add_field(name='minecraft', value='.')
        embed.add_field(name='nani', value='.')
        embed.add_field(name='notpass', value='.')
        embed.add_field(name='sparta', value='.')
        embed.add_field(name='swing', value='.')
        embed.add_field(name='tun', value='.')
        embed.add_field(name='wow', value='.')
        embed.add_field(name='meep', value='.')
        embed.add_field(name='gay', value='.')
        embed.add_field(name='oof', value='.')

        return embed

    def gif(self):
        embed = discord.Embed()
        embed.colour = discord.Colour.purple()
        embed.title = 'GIFS'
        embed.description = 'GIF collection'
        embed.add_field(name='crab', value='.')
        embed.add_field(name='degen1', value='.')
        embed.add_field(name='degen2', value='.')
        embed.add_field(name='dramatic', value='.')
        embed.add_field(name='goku', value='.')
        embed.add_field(name='rasputin', value='.')
        embed.add_field(name='rasputin2', value='.')
        embed.add_field(name='rasputin3', value='.')
        embed.add_field(name='reck', value='.')
        embed.add_field(name='rickroll', value='.')
        embed.add_field(name='rus', value='.')
        embed.add_field(name='sneeze', value='.')
        embed.add_field(name='weeb', value='.')


        return embed

    def futuredev(self):
        embed = discord.Embed()
        embed.colour = discord.Colour.purple()
        embed.title = 'Future development:'
        embed.add_field(name='Random memory', value='I want to build a function that takes all the pictures previously posted and returns a random picture on command')
        embed.add_field(name='TTS Chat', value='Deep learning chatbot implementation that talks to you with text-to-speech and speech-to-text module')
        embed.add_field(name='Bigger GIF library', value='Create a bigger library of gifs that represents what users are typing, ')
        embed.add_field(name='Reaction', value='Sometimes add appropriate reaction to the useres messages')        
        embed.add_field(name='Cleaup', value='Delete bad commands')
        embed.add_field(name='SERVER: Module for server log', value='For logging the AI')
        embed.add_field(name='SERVER: Direct memory allocation and retrieval', value='For faster processing')   
        embed.add_field(name='CODE: on_message() usage instead of commands', value='Reduces number of errors. Opens up more opportunities')        
        embed.add_field(name='CODE: Hashmap/Dict for filenames', value='Get all the filenames from fonder and put them in Dick. Delete duplicated code, also reduces embed code')        
        embed.add_field(name='CODE: Put events in separate file to keep it clean', value='This one is hard, no fucking idea how to solve.')        
        embed.add_field(name='CODE: Fix imports', value='Do you really need this many modules? Clean up your mess!.')   
        embed.add_field(name='CODE: Optimization', value='Any way to make gifs smaller without loosing quality? Other formats? What about mp3\'s? Any way to make the tts more concurrent?')   
       
        return embed
