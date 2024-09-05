import discord
from discord.ext import commands

import config

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents) 

@bot.command()
async def test(ctx):
    await ctx.send('''||Спойлер||''')

bot.run(config.TOKEN)

