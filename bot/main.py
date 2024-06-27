import os
from dotenv import load_dotenv

from discord.ext import commands
from discord import Intents, utils

from commands import setup_commands
from responses import get_response

# Load the token from the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True
intents.members = True # This is needed to get the member events

bot = commands.Bot(command_prefix='!', intents=intents)
setup_commands(bot)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    # This is needed to process the commands
    await bot.process_commands(message)
    
    user_message = message.content.strip()

    try:
        username = message.author
        response = get_response(user_message, username)
        if response:
            await message.channel.send(response)
    except Exception as e:
        print(e)

# Event for when the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user} is awake!')

# Event for new member joining
@bot.event
async def on_member_join(member):
    guild_name = member.guild.name
    channel = utils.get(member.guild.text_channels, name='general')
    if channel:
        await channel.send(f'¡Todos den la bienvenida a {member.mention} al servidor {guild_name}!')

# Event for member leaving
@bot.event
async def on_member_remove(member):
    channel = utils.get(member.guild.text_channels, name='general')
    if channel:
        await channel.send(f'Adiós {member.name}, esperamos verte pronto!')

def main():
    bot.run(token=TOKEN)

if __name__ == '__main__':
    main()
