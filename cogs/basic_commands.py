from config import CD
from discord.ext import commands


class BasicCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @CD.cooldown(2, 2 * 60)
    async def test(self, ctx: commands.Context):
        await ctx.reply("test command is working")

    @commands.command()
    @CD.cooldown(2, 3 * 60, type=commands.BucketType.guild)
    async def test1(self, ctx: commands.Context):
        await ctx.reply("test1 command is working")

    @commands.command()
    @CD.cooldown(2, 3 * 60, type=commands.BucketType.channel)
    async def test2(self, ctx: commands.Context):
        await ctx.reply("test2 command is working")

    @commands.command()
    @CD.cooldown(2, 3 * 60, type=commands.BucketType.category)
    async def test3(self, ctx: commands.Context):
        await ctx.reply("test3 command is working")

    @commands.command()
    @CD.cooldown(2, 3 * 60, type=commands.BucketType.role, role_id=...)  # enter role id here
    async def test4(self, ctx: commands.Context):
        await ctx.reply("basic command is working")

    @commands.command()
    @CD.cooldown(1, reset_per_day=True)
    async def vote(self, ctx: commands.Context):
        await ctx.reply("voted successfully")


def setup(client):
    client.add_cog(BasicCommands(client))
