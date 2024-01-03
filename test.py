import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready")

@bot.slash_command(name="test", description="test command")
async def test(ctx):
    await ctx.send("test")
    



bot.run("MTE4MjczMzE1MTAxODE2MDI4OA.Gl61RG.cIARIedw7Tpgql8NdxKZDqOohY1PXFTRlL4opo")