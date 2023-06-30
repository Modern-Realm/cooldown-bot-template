from config import Secrets

import discord
import os

from pycolorise.colors import Purple, Blue
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix="$", intents=intents)

print(Purple("Loading cogs:"))
for file in os.listdir("./cogs"):
    if file.endswith(".py") and "__pycache__" not in file:
        filename = file[:-3]
        try:
            client.load_extension("cogs.{}".format(filename))
            print(Blue(f"\t- {filename} ✅"))
        except:
            print(Blue(f"\t- {filename} ❌"))

print()


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("$help"))
    print(Blue(f"{client.user} is online"))


if __name__ == "__main__":
    client.run(Secrets.token)
