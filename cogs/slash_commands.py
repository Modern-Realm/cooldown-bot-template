from config import CD

import discord

from discord.ext import commands


class SlashCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command()
    @CD.cooldown(2, 2 * 60)
    async def test(self, ctx: discord.ApplicationContext):
        await ctx.respond("test command is working")

    @commands.slash_command()
    @CD.cooldown(2, 3 * 60, type=commands.BucketType.guild)
    async def test1(self, ctx: discord.ApplicationContext):
        await ctx.respond("test1 command is working")

    @commands.slash_command()
    @CD.cooldown(2, 3 * 60, type=commands.BucketType.channel)
    async def test2(self, ctx: discord.ApplicationContext):
        await ctx.respond("test2 command is working")

    @commands.slash_command()
    @CD.cooldown(2, 3 * 60, type=commands.BucketType.category)
    async def test3(self, ctx: discord.ApplicationContext):
        await ctx.respond("test3 command is working")

    @commands.slash_command()
    @CD.cooldown(2, 3 * 60, type=commands.BucketType.role, role_id=...)  # enter role id here
    async def test4(self, ctx: discord.ApplicationContext):
        await ctx.respond("basic command is working")

    @commands.slash_command()
    @CD.cooldown(1, reset_per_day=True)
    async def vote(self, ctx: discord.ApplicationContext):
        await ctx.respond("voted successfully")


def setup(client):
    client.add_cog(SlashCommands(client))
