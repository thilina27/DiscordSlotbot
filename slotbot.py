import discord
from discord.ext import commands
import random

slots = ["🐳", "🦋", "🌻"]  # few more if needed "🌻", "🍭", , "🌹"

TOKEN = 'your token'
bot = commands.Bot(command_prefix='!')


@bot.command(name='slot', help='Run slot machine')
async def test(ctx):
    title = "Slot Machine - " + ctx.message.author.name
    s11 = random.choice(slots)
    s12 = random.choice(slots)
    s13 = random.choice(slots)
    ms = "[ " + str(s11) + " | " + str(s12) + " | " + str(s13) + " ]    spinning..."
    embed_var = discord.Embed(title=title, description=ms, color=0x00ff00)
    msg = await ctx.send(embed=embed_var)

    for i in range(0, 3):
        s11 = random.choice(slots)
        s12 = random.choice(slots)
        s13 = random.choice(slots)
        ms = "[ " + str(s11) + " | " + str(s12) + " | " + str(s13) + " ] spinning... "
        embed_var = discord.Embed(title=title, description=ms, color=0x00ff00)
        await msg.edit(embed=embed_var)

    if s11 == s12 == s13:
        ms = "[ " + str(s11) + " | " + str(s12) + " | " + str(s13) + " ] Win!"
        embed_var = discord.Embed(title=title, description=ms, color=0x00ff00)
        await msg.edit(embed=embed_var)
    else:
        ms = "[ " + str(s11) + " | " + str(s12) + " | " + str(s13) + " ] Loss!"
        embed_var = discord.Embed(title=title, description=ms, color=0x00ff00)
        await msg.edit(embed=embed_var)


bot.run(TOKEN)
