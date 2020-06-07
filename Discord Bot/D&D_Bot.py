import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix='~')


@client.event
async def on_ready():
    print('The Bot LIVES.')


@client.event
async def on_member_join(member):
    print(f'{member} has joined.')
    await member.dm_channel()
    await member.dm_channel.send(f'Sup {member}')


@client.event
async def on_member_remove(member):
    print(f'{member} has left. RIP {member}...')


@client.command()
async def ping(ctx):
    """if you know, you know..."""
    await ctx.send(f'Pong FUCKER!')


@client.command()
async def SHAME(ctx):
    await ctx.send(f'SHAME...ding...ding...ding')
    await ctx.send(f'SHAME...ding...ding...ding')
    await ctx.send(f'SHAME...ding...ding...ding')


@client.command()
async def clear(ctx, amount=5):
    """Clears a number of messages (default 5)"""
    await ctx.channel.purge(limit=amount)


@client.command()
async def load(ctx, extension):
    """Load a new specific Cog"""
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    """Unload specific Cog for update"""
    client.unload_extension(f'cogs.{extension}')


@client.command()
async def reload(ctx, extension):
    """Combine load and unload commands"""
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


@client.command()
async def schedule(ctx):
    """Displays the next game time"""
    await ctx.send(f'The next session is Sunday at 7:00 and the game starts at 7:30')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('Insert_Token_Here')
