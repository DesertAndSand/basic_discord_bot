import discord
from discord.ext import commands

PREFIX = "$"
TOKEN = ""

client = commands.Bot(command_prefix=PREFIX)

@client.event
async def on_ready():
    print(f"Connected To :\nUser : {client.user} | ID : {client.id}")

@client.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.auhtor.mention}!")

client.run(TOKEN)
