from logging import StreamHandler
import discord
import time
from discord.ext import commands
from discord import client
from discord import message
from discord import activity
from discord import Spotify
from discord.ext.commands import bot
from discord.ext.commands.bot import Bot
from discord.ext.commands.core import command





cliente = commands.Bot(command_prefix='-')


@cliente.event
async def on_ready():
    print("Bot inciado !")
    await cliente.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Bot made by Xionno'))
    await cliente.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Bot code by python'))
        

@cliente.event
async def on_message(message):
    if message.author == cliente.user:
        return
    
    if message.content.startswith("-Hola"):
        await message.channel.send(f"Hola {message.author} !")
    if message.content.startswith("-hola"):
        await message.channel.send(f"hola {message.author} !")


    if message.content.startswith("-Hello"):
        await message.channel.send(f"Hello {message.author} !")
    
    if message.content.startswith("-hello"):
        await message.channel.send(f"hello {message.author} !")

#comandos

@cliente.command()
async def sumar(ctx, num1, num2):
    await ctx.send(f"El resultado es: {num1 + num2}")
@cliente.command()
async def restar(ctx, num1, num2):
    await ctx.send(f"El resultado es: {num1 - num2}")










cliente.run('OTE3NzE3NDkxMjM1NTU3NDI2.Ya8xBA._sFpsIiSNzNR8j82Mcc0zS-MwcQ')