import asyncio
import os
import discord
from discord.ext import commands
from helpers import read_token

async def __load_extensions(bot):
    for filename in os.listdir("./DiscordToDoist/cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded {filename} extension")

def init():
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='!', intents=intents)

    asyncio.run(__load_extensions(bot))

    token = read_token("~discord-token")
    bot.run(token)
