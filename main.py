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
    """

    text2 = f"""
Ahoj @name! :wave:

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
        if member.role.name == "Spectator" and member.role.name == "Wizards plus" or member.role.name == "Wizard": 
            await asyncio.sleep(1)
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
                        elif member == message.author:
                            pass
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