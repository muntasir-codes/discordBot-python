import asyncio
import datetime
import json
import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

# cfg = open("config.json", "r")
# tmpconfig = cfg.read()
# cfg.close()
# config = json.load(tmpconfig)

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
  x={"server-id":"hii","logs-channel-id":"bye"}
  for glds in client.guilds:
    print(glds, glds.id)
    for ch in glds.text_channels:
      
      if ch =='invites':
        print(ch, ch.id)
        gld_id=glds.id
        ch_id=ch.id
      x.update({"server-id":"764115947627216947","logs-channel-id": "764115947627216947"})
  print(x)
  with open('config.json','w+') as outfile:
    #config={}
    config["servers"]=[]
    config["servers"].append(x)
    json.dump(config,outfile,indent=4)

#client.loop.create_task(fetch())
client.run('NzcwNjcxNjM4NjgwNDM2NzU2.X5g95Q.B7XxM5rzRowNLbUTVzMOcFMRqrQ')