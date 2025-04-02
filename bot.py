from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
from commands.default import default

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='|', intents=intents)

default(bot)

bot.run(DISCORD_TOKEN)