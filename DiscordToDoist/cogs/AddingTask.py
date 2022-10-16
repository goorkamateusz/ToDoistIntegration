from discord.ext.commands.context import Context
from ApiClient import ApiClient
from Container import Container
import discord
from discord.ext import commands


class AddingTask(commands.Cog):
    def __init__(self, bot: discord, api: ApiClient = Container.apiClient):
        self.bot = bot

    @commands.command("echo")
    async def echo(self, ctx, *args):
        out = " ".join(args)
        await ctx.send(f"[{out}]")

    @commands.command("thread")
    async def create_thread(self, ctx: Context, *args):
        name = " ".join(args) if args else "No name"
        await ctx.channel.create_thread(name=name, auto_archive_duration=60, message=ctx.message)


async def setup(bot):
    await bot.add_cog(AddingTask(bot))
