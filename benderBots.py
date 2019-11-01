# benderBotClass.py
import os
import random
from dotenv import load_dotenv

# 1
from discord.ext import commands
from dotenv import load_dotenv

hookers = ['https://i.imgur.com/VSP8EBp.jpg',
    'https://i.imgur.com/Z5pYMOB.jpg', 
    'https://i.imgur.com/BmAr75a.jpg',
    'https://i.imgur.com/KqKqV0w.jpg',
    'https://i.imgur.com/zg07iek.jpg',
    'https://i.imgur.com/lR6MiJK.jpg',
    'https://i.imgur.com/oulOY.jpg',
    'https://i.imgur.com/bli8Q5c.jpg',
    'https://tenor.com/view/pretty-woman-julia-roberts-richard-gere-gif-5736316',
    'https://pbs.twimg.com/media/Cb1GR80WwAAw0dp.jpg',
    'https://pbs.twimg.com/media/Dnd178AX4AAcRq-.jpg',
    'https://i.pinimg.com/originals/3b/a9/58/3ba9588efca77fd966d772c0b25840e7.jpg'
    ]


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# 2
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    for guild in bot.guilds:
        print(f'{bot.user.name} has connected to Guild [{guild}]')


@bot.command(name='hooker', help='Responds with a random hooker image')
async def getHooker(ctx):
    rng = random.Random()
    indexHooker=rng.randrange(0,len(hookers))
    await ctx.send(hookers[indexHooker])

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))


bot.run(token)