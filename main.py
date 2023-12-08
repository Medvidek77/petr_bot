import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def on_member_remove(member):
    try:
        user = bot.get_user(member.id)
        await user.send("Hello there!")
    except Exception as e:
        print(e)

bot.run("MTE4MjczMzE1MTAxODE2MDI4OA.GxoicZ.cDvtz4hV8OwuHiG1uvuHzZK2oym86JsauNLn8I")