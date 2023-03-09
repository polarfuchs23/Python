import os
from dotenv import load_dotenv
import json
import discord
from discord.commands import Option
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger


bot = discord.Bot()

@bot.slash_command(name = "subscribe_cf", description = "Subscribe to the codeforces contest notifications")
async def subscribe_cf(ctx, div: Option(str, "Choose which div to subscribe to")):
	if div in "1234":
		with open(f'{os.path.dirname(__file__)}\\subscription{div}.csv', 'a') as f:
			f.write(f'{ctx.author.id},')
		await ctx.respond(f'You have been added to div {div}')
	else:
		await ctx.respond("Only 1, 2, 3 and 4 are valid divs")

@bot.event
async def on_ready():
	print(f'Logged in as {bot.user}')

load_dotenv()
token = os.environ.get("TOKEN")

if token:
	bot.run(token)
	pass

if not token:
	print("No TOKEN or .env file found")
	pass


input("Press enter to exit...")