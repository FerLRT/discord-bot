from discord import Embed, Color
from random import randint
from jokes import get_joke

def setup_commands(bot):
    @bot.command(name='joke')
    async def joke(ctx):
        joke = get_joke()
        await ctx.send(joke)

    @bot.command(name='random')
    async def random_number(ctx):
        number = randint(0, 10)
        await ctx.send(f'Tu número aleatorio es... {number}')

    @bot.command(name='info')
    async def information(ctx):
        info_message = (
            "**Comandos disponibles:**\n"
            "`!joke` - Te cuento un chiste.\n"
            "`!random` - Genera un número aleatorio entre 0 y 10.\n"
            "`!help` - Muestra este mensaje de ayuda.\n"
        )
        embed = Embed(
            title="Comandos del Bot",
            description=info_message,
            color=Color.blue()
        )
        await ctx.send(embed=embed)