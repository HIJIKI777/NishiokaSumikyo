from discord.ext import commands
import config

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("on_ready")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "誰だお前は！" in message.content:
        await message.channel.send("にしおかァ↑～～～！すみきょだよォ↓↑～！")

    if "どこのどいつだい" in message.content:
        await message.channel.send("お前かァ！")

    if "エンタの神様" in message.content:
        await message.channel.send("ア”ーーーーーーー！！！！！")

bot.run(config.TOKEN)