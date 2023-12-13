import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready")

@bot.event
async def on_member_join(member):

    text1 = f"""
Hi there {member.mention}! 👋

I hope you're doing great! I've noticed you recently joined our Discord group.😊

I'm reaching out to share something exciting with you about our course. It dives deep into key areas like technical analysis, market structure, Fibonacci retracement, and Exocharts.📊 This course is made to boost your trading skills with practical knowledge. Plus, purchasing it grants you exclusive access to coaches' channels, including Jan's expert setups and insights, along with channels dedicated to our wizard strategy.

I believe this course, along with our dedicated Discord group, could be the perfect fit for you! 🌟

Interested in learning more? Check out the details here:
* Crypto Wizards: [crypto wizards](https://crypto-wizards.net/)

Feel free to reach out to CW_Admin in DMs if you have any questions. 🙌

Looking forward to hearing from you soon!


:star::star::star::star::star::star::star:
    """

    text2 = f"""

    
Ahoj {member.mention}! :wave:

Doufám, že se máš fajn! Všiml jsem si, že ses nedávno stal/a součástí naší Discord skupiny. :blush:

Chtěl bych se s tebou podělit o něco, co by tě mohlo zajímat. Součástí této skupiny je obsáhlý kurz zaměřený na technickou analýzu, strukturu trhu, používání Fibonacci, Exocharts a další klíčové strategie. :bar_chart: Pokud se ti náš Discord líbí a chceš se do tradingu ponořit hlouběji, tak koupě kurzu je přesně pro tebe! Získáš nejenom samotný kurz, ale i přístup do zdejších kanálů, jako je ‘jan_channel’, kde najdeš set ups, analýzy a přehledy na trhu.

Myslím, že tento kurz společně s naší Discord skupinou by mohly být přesně to, co hledáš! :star2:

Chceš se dozvědět více? Podívej se na naše stránky:
* CW-Trading: [cw trading](https://cw-trading.cz/)

Kdybys měl/a jakékoliv dotazy, piš CW_Admin do soukromých zpráv. :raised_hands:

Budeme rádi za tvé názory a zpětnou vazbu.

Těším se na brzkou odpověď!
    """
    embed = discord.Embed(title="**Welcome to Crypto Wizards**", description=f"\n\n**:flag_gb:**\n{text1}\n\n**:flag_cz:**\n{text2}",color=0x6851ac)
    embed.set_image(url="https://cdn.discordapp.com/attachments/1180556010465800225/1184133248440356934/cw_logo_kopie.png?ex=658add06&is=65786806&hm=bcf39cc82e93e6c9ef519494b7ac83d850a9ed715d76605109844e860d69109a&")
    
    try:
        await asyncio.sleep(1)
        await member.send(embed=embed)
    except Exception as e:
        print(f"Error: {e}")



bot.run("MTE4MjczMzE1MTAxODE2MDI4OA.Gl61RG.cIARIedw7Tpgql8NdxKZDqOohY1PXFTRlL4opo")