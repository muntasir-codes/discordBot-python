import asyncio
import datetime
import json
import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

 with open('config.json','r+') as f:
   config = json.loads(f)

# guild_id = config["server-id"]
# logs_channel = config["logs-channel-id"]

# invites = {}
# last = ""

# async def fetch():
#  global last
#  global invites
#  await client.wait_until_ready()
#  gld = client.get_guild(int(guild_id))
#  logs = client.get_channel(int(logs_channel))
#  while True:
#   invs = await gld.invites()
#   tmp = []
#   for i in invs:
#    for s in invites:
#     if s[0] == i.code:
#      if int(i.uses) > s[1]:
#       usr = gld.get_member(int(last))
#       testh = f"{usr.name} **joined**; Invited by **{i.inviter.name}** (**{str(i.uses)}** invites)"
#       await logs.send(testh)
#    tmp.append(tuple((i.code, i.uses)))
#   invites = tmp
#   await asyncio.sleep(4)


@client.event
async def on_ready():
 print("ready!")
 w_json()
 #await client.change_presence(activity = discord.Activity(name = "joins", type = 2))


# @client.event
# async def on_member_join(meme):
#  global last
#  last= str(meme.id)
#  await meme.send('{meme.mention} joined')

# @client.event
# async on_guild_join():

def w_json():
  
  print(x)
  with open('config.json','w+') as outfile:
    #config={}
    conf=json.load(outfile)
    x=conf["servers"]
  for guild in client.guilds:
    print(guild, guild.id)
    for ch in glds.text_channels:
      
      if ch is 'invites':
        print(ch, ch.id)
        gld_id=guild.id
        ch_id=ch.id
        x.update({"server-id": gld_id,"logs-channel-id": ch_id})
        
  conf["servers"].append(x)
  json.dump(conf,outfile,indent=2)

#client.loop.create_task(fetch())
client.run('')
