import discord
from dotenv import load_dotenv
import asyncio
import requests
import os
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import json


def fetch_contests(sched, client: discord.Client):
    API_URL = "https://codeforces.com/api/contest.list"
    data = requests.get(url=API_URL).json()
    for entry in data["result"]:
        if entry["phase"] == "BEFORE" and "startTimeSeconds" in entry.keys():
            start_time = datetime.datetime.fromtimestamp(int(entry["startTimeSeconds"]))
            scheduled = []
            if not "Div. 1" in entry["name"] and not "Div. 2" in entry["name"] and not "Div. 3" in entry["name"] and not "Div. 4" in entry["name"]:
                entry["name"] += "Div. 1Div. 2Div. 3Div. 4"
            if "Div. 1" in entry["name"]:
                if os.path.isfile(f'{os.path.dirname(__file__)}\\subsription1.csv'):
                    with open(f'{os.path.dirname(__file__)}\\subsription1.csv', 'r') as f:
                        user_ids = f.read().split(',')[:-1]
                    for user_id in user_ids:
                        if not user_id in scheduled:
                            sched.add_job(notify_users, 'date', run_date=start_time, args=[sched, client, user_id, 1])
                            scheduled.append(user_id)
            if "Div. 2" in entry["name"]:
                if os.path.isfile(f'{os.path.dirname(__file__)}\\subsription2.csv'):
                    with open(f'{os.path.dirname(__file__)}\\subsription2.csv', 'r') as f:
                        user_ids = f.read().split(',')[:-1]
                    for user_id in user_ids:
                        if not user_id in scheduled:
                            sched.add_job(notify_users, 'date', run_date=start_time, args=[sched, client, user_id, 2])
                            scheduled.append(user_id)
            if "Div. 3" in entry["name"]:
                if os.path.isfile(f'{os.path.dirname(__file__)}\\subsription3.csv'):
                    with open(f'{os.path.dirname(__file__)}\\subsription3.csv', 'r') as f:
                        user_ids = f.read().split(',')[:-1]
                    for user_id in user_ids:
                        if not user_id in scheduled:
                            sched.add_job(notify_users, 'date', run_date=start_time, args=[sched, client, user_id, 3])
                            scheduled.append(user_id)
            if "Div. 4" in entry["name"]:
                if os.path.isfile(f'{os.path.dirname(__file__)}\\subsription4.csv'):
                    with open(f'{os.path.dirname(__file__)}\\subsription4.csv', 'r') as f:
                        user_ids = f.read().split(',')[:-1]
                    for user_id in user_ids:
                        if not user_id in scheduled:
                            sched.add_job(notify_users, 'date', run_date=start_time, args=[sched, client, user_id, 4])
                            scheduled.append(user_id)
            pass
    print(data)
    return

def notify_users(sched, client: discord.Client, user_id: discord.User.id, div):
    with open(f'{os.path.dirname(__file__)}\\dm_channels.json', 'r') as f:
        dm_channels = json.load(f)
    if not user_id in dm_channels.keys():
        dm_channels[user_id] = asyncio.run(client.create_dm(client.get_user(user_id)))
    return

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

sched = BlockingScheduler()
fetch_contests(sched, client)

load_dotenv()
TOKEN = os.environ.get("TOKEN")

if TOKEN:
    client.run(TOKEN)
    pass

if not TOKEN:
    print("No TOKEN or .env file found")
    pass
#sched.add_job(fetch_contests(sched), 'cron', day='*')