import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def on_message(message):
    
    try:
        user = bot.get_user(message.author.id)
        await asyncio.sleep(500)
        await user.send("Hello there!")
    except Exception as e:
        print(e)

bot.run("MTE4MjczMzE1MTAxODE2MDI4OA.GxoicZ.cDvtz4hV8OwuHiG1uvuHzZK2oym86JsauNLn8I")