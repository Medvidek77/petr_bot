import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def on_member_remove(member):

    text = f"""
    Hi there {member.mention}! :wave:﻿﻿
    ﻿
    I hope you're doing great! I've noticed you recently joined our Discord group.:blush:﻿﻿
    ﻿
    I'm reaching out to share something exciting with you about our course. It dives deep into key areas like technical analysis, market structure, Fibonacci retracement, and Exocharts.:bar_chart:﻿ This course is made to boost your trading skills with practical knowledge. Plus, purchasing it grants you exclusive access to coaches' channels, including Jan's expert setups and insights, along with channels dedicated to our wizard strategy.
    ﻿
    I believe this course, along with our dedicated Discord group, could be the perfect fit for you! :star2:﻿﻿
    ﻿
    Interested in learning more? Check out the details here:
    CW-Trading: https://cw-trading.cz/
    Crypto Wizards: https://crypto-wizards.net/
    ﻿
    Feel free to reach out to CW_Admin in DMs if you have any questions. :raised_hands:﻿﻿
    ﻿
    Looking forward to hearing from you soon!
    ﻿
    ﻿
    Ahoj! :wave:﻿﻿
    ﻿
    Doufám, že se máš fajn! Všiml jsem si, že ses nedávno stal/a součástí naší Discord skupiny.:blush:﻿﻿
    ﻿
    Chtěl bych se s tebou podělit o něco, co by tě mohlo zajímat.
    Součástí této skupiny je obsáhlý kurz zaměřený na technickou analýzu, strukturu trhu, používání Fibonacci, Exocharts a další klíčové strategie. :bar_chart:﻿ Pokud se ti náš Discord líbí a chceš se do tradingu ponořit hlouběji, tak koupě kurzu je přesně pro tebe! Získáš nejenom samotný kurz, ale i přístup do zdejších kanálů, jako je ‘jan_channel’, kde najdeš set ups, analýzy a přehledy na trhu.
    Myslím, že tento kurz společně s naší Discord skupinou by mohly být přesně to, co hledáš! :star2:﻿﻿
    ﻿
    Chceš se dozvědět více? Podívej se na naše stránky:
    CW-Trading: https://cw-trading.cz/
    Crypto Wizards: https://crypto-wizards.net/
    ﻿
    Kdybys měl/a jakékoliv dotazy, piš CW_Admin do soukromých zpráv. :raised_hands:﻿﻿
    ﻿
    Budeme rádi za tvé názory a zpětnou vazbu.
    ﻿
    Těším se na brzkou odpověď!
    """
    
    try:
        await asyncio.sleep(10)
        await member.send(text)
    except Exception as e:
        print(e)



bot.run("MTE4MjczMzE1MTAxODE2MDI4OA.GxoicZ.cDvtz4hV8OwuHiG1uvuHzZK2oym86JsauNLn8I")