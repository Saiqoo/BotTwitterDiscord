import discord
import os
from dotenv import load_dotenv
from discord import Intents
from discord.ext import commands, tasks
import random
import sys
import traceback
import json
import datetime

intents = Intents.all()

bot = commands.Bot(command_prefix="!!", description="Bot de Saiqo", intents=intents, help_command=None)


@bot.event
async def on_ready():
    print("Bot Ready !")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Scanne Twitter"),
                              status=discord.Status.dnd)


@bot.event
async def on_guild_join(guild):
    embed = discord.Embed(
        color=0xCE2029, description="**Merci de m'avoir ajouté sur ce serveur !**",
    )
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_author(name=f"{bot.user.name}", icon_url=f"{bot.user.avatar_url}")
    embed.add_field(name="",
                    value="Mon préfix d'appel est **!!**")
    await guild.text_channels[0].send(embed=embed)


for file in os.listdir("cogs"):
    if file.endswith(".py") and not file.startswith("_"):
        print(f"cogs\{file[:-3]} loaded")
        bot.load_extension(f"cogs.{file[:-3]}")

load_dotenv()
token = os.getenv("SECRET")
bot.run(token)