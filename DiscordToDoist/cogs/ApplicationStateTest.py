import discord
from discord.ext import commands

class ApplicationStateTest(commands.Cog):
    def __init__(self, bot: discord):
        self.bot = bot

    @commands.command("test")
    async def test(self, ctx):
        await ctx.send(f"It's working...")

async def setup(bot):
    await bot.add_cog(ApplicationStateTest(bot))
