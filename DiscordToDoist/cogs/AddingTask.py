import discord
from discord.ext.commands.context import Context
from discord.ext import commands
from DiscordToDoist.ApiClient import ApiClient
from DiscordToDoist.Container import Container


class AddingTask(commands.Cog):
    def __init__(self, bot: discord, api: ApiClient = Container.apiClient):
        self.bot = bot
        self.todoist: ApiClient = api

    @commands.command("add")
    async def add_task(self, ctx, *args):
        out = " ".join(args)
        self.todoist.add_task(out)
        await ctx.send(f"[{out}]")

    @commands.command("thread")
    async def create_thread(self, ctx: Context, *args):
        name = " ".join(args) if args else "No name"
        await ctx.channel.create_thread(name=name, auto_archive_duration=60, message=ctx.message)


async def setup(bot):
    await bot.add_cog(AddingTask(bot))
