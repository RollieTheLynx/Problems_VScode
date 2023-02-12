# -*- coding: utf-8 -*-
"""
https://habr.com/ru/post/676390/
https://habr.com/ru/post/511454/

"""
import discord  # Подключаем библиотеку
from discord.ext import commands
import requests
import json
from my_keys import discord_config

#  вынести в отдельный файл config
settings = discord_config

intents = discord.Intents.default()  # Подключаем "Разрешения"
intents.message_content = True
# Задаём префикс и интенты
bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)


client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

# С помощью декоратора создаём первую команду
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def repeat(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def hello(ctx):  # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author  # Объявляем переменную author и записываем туда информацию об авторе.

    await ctx.send(f'Hello, {author.mention}!')  # Выводим сообщение с упоминанием автора, обращаясь к переменной author.

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def cat(ctx):
    response = requests.get('https://some-random-api.ml/img/cat')  # Get-запрос
    json_data = json.loads(response.text)  # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title='Random Cat')  # Создание Embed'a
    embed.set_image(url=json_data['link'])  # Устанавливаем картинку Embed'a
    await ctx.send(embed=embed)  # Отправляем Embed

@bot.command()
async def chuck(ctx):
    api_request = requests.get("https://api.chucknorris.io/jokes/random")
    joke = json.loads(api_request.content)
    await ctx.send(joke["value"])


bot.run(settings['token'])
