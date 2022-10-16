import asyncio
import os
import discord
from discord.ext import commands
from helpers import read_token


def __cog_list() -> list[str]:
    for filename in os.listdir("./DiscordToDoist/cogs"):
        if filename.endswith(".py"):
            yield f"cogs.{filename[:-3]}"


async def __load_extensions(bot) -> None:
    for cog_name in __cog_list():
        await bot.load_extension(cog_name)
        print(f"Loaded {cog_name} extension")


def init():
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='!', intents=intents)

    asyncio.run(__load_extensions(bot))

    token = read_token("~discord-token")
    bot.run(token)
