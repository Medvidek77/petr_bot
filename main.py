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
Hello {member.mention}! :wave:

I noticed that you recently joined our CW Trading group. I hope you find it beneficial.:bar_chart:
Since you’re only in the free version, information and education are very limited. Members who purchase a membership have access to premium Discord channels, where @CW_Jan and other mentors send daily analyses and predictions for each day.:boom:An essential part of being a profitable trader is knowledge, which we provide in our online course, where you will learn to use:

> * Fibonacci
> * Exocharts
> * Market Structure
> * Footprints
> * Volume
> * Risk Management
> * and more…

Membership includes: :white_tick:

* Exocharts Pro license worth 2500 CZK
* Daily CW team analyses
* Over 50 lessons of CW Jan strategies

Let’s close one trade: :thinking:

You will get a 5% discount for 6 month membership with the code “SPECTATOR5”, which you can enter when ordering on this page: [link](https://cw-trading.cz/?utm_source=discord&utm_medium=discountcodespectators) you can visit our pages: :point_down:

CW-Trading: https://cw-trading.cz/
Crypto Wizards: https://crypto-wizards.net/
    """

    text2 = f"""
Ahoj {member.mention}! :wave:

Všiml jsem si, že jsi se nedávno připojil k naší CW Trading skupině. Doufám, že je pro tebe přínosná.:bar_chart:Protože se nacházíš jen v bezplatné verzi, informace a edukace jsou velice omezené. Členové, kteří si zakoupí členství mají přístup k prémiovým Discord kanálům, kam @CW_Jan a další mentoři denně posílají analýzy a to, co budou každý den obchodovat.:boom:Nezbytnou součástí profitabilního tradera jsou znalosti, které poskytujeme v našem online kurzu, ve kterém se naučíš ovládat:

> * Fibonacci
> * Exocharts
> * Market Structure
> * Footprints
> * Volume
> * Risk Management
> * a další…

Součástí členství je: :white_tick:

* Exocharts Pro licence v hodnotě 2500 ,- Kč
* Denní analýzy CW týmu
* Přes 50 lekcí strategií CW Jana

Pojďme uzavřít jeden trade: :thinking:
Dostaneš 5% slevu na kurz s kódem “SPECTATOR5”, který můžeš zadat při objednávce na této stránce: [link](https://cw-trading.cz/?utm_source=discord&utm_medium=discountcodespectators) můžeš navštívit naše stránky: :point_down:

* CW-Trading: https://cw-trading.cz/
* Crypto Wizards: https://crypto-wizards.net/
    """
    embed = discord.Embed(description=f":## flag_gb:\n{text1}\n:## flag_cz:\n{text2}",color=0x6851ac)
    embed.set_image(url="https://cdn.discordapp.com/attachments/1180556010465800225/1184133248440356934/cw_logo_kopie.png?ex=658add06&is=65786806&hm=bcf39cc82e93e6c9ef519494b7ac83d850a9ed715d76605109844e860d69109a&")
    
    try:
        if member.role.name == "Spectator" and member.role.name != "Wizards plus" and member.role.name != "Wizard": 
            await asyncio.sleep(10)
            await member.send(embed=embed)
        else: 
            pass
    except Exception as e:
        print(f"Error: {e}")



@bot.event
async def on_message(message):
    try:
        if message.author.bot:
            return
        elif message.content.startswith("!dm ") or message.content.startswith("!dm") or message.content.startswith("!dm  ") or message.content.startswith("!dm \n") or message.content.startswith("!dm \n\n") or message.content.startswith("!dm \n\n\n") or message.content.startswith("!dm \n\n\n\n") or message.content.startswith("!dm \n\n\n\n\n") or message.content.startswith("!dm \n\n\n\n\n\n") or message.content.startswith("!dm \n\n\n\n\n\n\n") or message.content.startswith("!dm \n\n\n\n\n\n\n\n") or message.content.startswith("!dm \n\n\n\n\n\n\n\n\n") or message.content.startswith("!dm \n\n\n\n\n\n\n\n\n\n") or message.content.startswith("!dm\n"):
            
            text = message.content.split("!dm ", 1)[1]
            await message.delete()

            class MyView(discord.ui.View): 
                @discord.ui.button(label="Send", style=discord.ButtonStyle.success)
                async def send_button(self, button, interaction):
                    button.disabled = True
                    message_send = await message.channel.send("Sending DMs to all members")
                    all_members = message.guild.members
                    await asyncio.sleep(2)
                    await message_send.delete()
                    await interaction.message.delete()
                    for member in all_members:
                        if member.bot:
                            pass
                        #elif member == message.author:
                        #    pass
                        else:
                            try:
                                await member.send(text)
                            except Exception as e:
                                print(f"Error: {e}")
                                pass
                            

                @discord.ui.button(label="Cancel", style=discord.ButtonStyle.danger)
                async def cancel_button(self, button, interaction):
                    button.disabled = True
                    message_cancel = await message.channel.send("Canceled")
                    await asyncio.sleep(2)
                    await interaction.message.delete()
                    await message_cancel.delete()

            await message.channel.send(f"Verify your message before send!\n\n**Text:**\n{text}", view=MyView())
    except Exception as e:
        print(f"An error occurred: {e}")

                
    



bot.run("MTE4MjczMzE1MTAxODE2MDI4OA.Gl61RG.cIARIedw7Tpgql8NdxKZDqOohY1PXFTRlL4opo")