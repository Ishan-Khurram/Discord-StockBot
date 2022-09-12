import discord
import random
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
from finance_functions import Stocks
load_dotenv()

stocks = Stocks()

help_list = "$price XXXX: displays current price for any stock"

connect_list = ["Hello!"]

disconnect_list = ["Goodbye!"]

#Set command prefix for bot
bot = commands.Bot(command_prefix='$', help_command=None)

#Sends message on start up
@bot.event
async def on_ready(): 
    channel = bot.get_channel(975900019146244117)
    await channel.send(random.choice(connect_list)) 
    await channel.send("Type '$help' for a list of commands!")

#Sends message on disconnect
@bot.event
async def on_disconnect():
    channel = bot.get_channel(975900019146244117)
    await channel.send(random.choice(disconnect_list))

@bot.command(name = "help")
async def help_cmd(ctx):
    channel = bot.get_channel(975900019146244117)
    await channel.send(help_list)

#Grab Price of X stock, return value of said stock.
@bot.command(name = "price")
async def price_cmd(ctx, arg):
    await ctx.send(stocks.get_price(arg))

#call back to main.py to run bot
def start_bot():
    bot.run(getenv('Token'))