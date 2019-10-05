import discord
import asyncio
from discord.ext.commands import bot
from discord import game
from discord.ext import commands

client=commands.Bot(command_prefix='-')
client.remove_command('help')

async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name='ﾉ尺θη シ SIᗪᕼᗩᖇTH',type=1))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='status3',type=3))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='status2',type=3))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='status1',type=3))
        await asyncio.sleep(5)
        
@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('-----------')
    client.loop.create_task(status_task())
    

client.run("self token",bot=False)
