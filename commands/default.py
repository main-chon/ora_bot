from discord.ext import commands
import os

def default(bot):
    @bot.command(name="명령어")
    async def bot_info(ctx):
        await ctx.send("명령어 리스트 출력")
        
