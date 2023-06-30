from config import CD

import discord

from discord.ext import commands
from datetime import timedelta


class ErrorHandlers(commands.Cog):
    def __init__(self, client):
        self.client: commands.Bot = client

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx: discord.ApplicationContext, error):
        if isinstance(error, commands.CommandOnCooldown):
            return await ctx.respond(
                f"on cooldown retry after `{timedelta(seconds=error.retry_after)}`",
                ephemeral=True
            )

        else:
            print(error)
            # For resetting a command cooldown if any error occurred
            return await CD.reset_cooldown(ctx)

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            return await ctx.send(
                f"on cooldown retry after `{timedelta(seconds=error.retry_after)}`"
            )

        else:
            print(error)
            # For resetting a command cooldown if any error occurred
            return await CD.reset_cooldown(ctx)


def setup(client):
    client.add_cog(ErrorHandlers(client))
