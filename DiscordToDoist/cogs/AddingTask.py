from ApiClient import ApiClient
from Container import Container
import discord
from discord.ext import commands
from todoist_api_python.api import TodoistAPI


class AddingTask(commands.Cog):
    def __init__(self, bot: discord, api: ApiClient = Container.apiClient):
        self.bot = bot

    @commands.command("add")
    async def add(self, ctx, *args):
        out = " ".join(args)
        await ctx.send(f"ToDo {out}")


async def setup(bot):
    await bot.add_cog(AddingTask(bot))
