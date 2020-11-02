import discord
from discord.ext import commands
import asyncio

TOKEN=""

client=commands.Bot(command_prefix=".")

ban_list=[]
day_list=[]
server_list=[]

#This is a background process
async def countdown():
    await client.wait_until_ready()
    while not client.is_closed:
        await asyncio.sleep(1)
        day_list[:]=[x-1 for x in day_list]
        for day in day_list:
            if day<=0:
                try:
                    await client.unban(server_list[day_list.index(day)],ban_list[day_list.index(day)])
                except:
                    print('Error! User already unbanned!')
                del ban_list[day_list.index(day)]
                del server_list[day_list.index(day)]
                del day_list[day_list.index(day)]

#Command starts here
@client.command(pass_context=True)
async def ban(ctx,member:discord.Member,days=1):
    if str(ctx.message.author.id)=='<You ID goes here>':
        try:
            await client.ban(member,delete_message_days=0)
            await client.say('User banned for **'+str(days)+' day(s)**')
            ban_list.append(member)
            day_list.append(days*24*60*60)
            server_list.append(ctx.message.server)
        except:
            await client.say('Error! User not active')
    else:
        await client.say('You do not have permission to ban users!')

client.loop.create_task(countdown())
client.run(TOKEN)