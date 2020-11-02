#discodBot.py
import discord
import invited
import temp-ban
import random
import time 
from discord.ext import commands,tasks
client = commands.Bot(command_prefix='.')
me='realGamer004#0703'

#on ready
@client.event
async def on_ready():
    await client.change_presence(status= discord.Status.online, activity= discord.Game('.help'))
    print('We have logged in as {0.user}'.format(client))
    for guild in client.guilds:
        print(f'{client.user} is connected to the following guild:\n'f'{guild.name}(id: {guild.id})\n')

#Bot version
@client.command(aliases=['v'],help='shows version of bot')
async def version(ctx):
    await ctx.send(f'`Bot_version = 1.5\nA minimal bot with useful commands created by @realGamer004#0703`')

#Latency 
@client.command(aliases=['p'], help='shows ping of bot')
async def ping(ctx):
    user= ctx.author
    await ctx.send(f'{user.mention} my ping is {round(client.latency*1000)} ms')

#Clear messages
@client.command(aliases=['del','clear'], help= 'clears given no. of messages')
@commands.has_permissions(manage_messages=True)
async def delete(ctx,amount=0):
    await ctx.send(f'Deleting {amount} messages')
    await ctx.channel.purge(limit=amount+2)
@delete.error
async def delete_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'Sorry {ctx.author.mention} you are not allowed to use this command.')

#8ball ques 
@client.command(name='8ball',help= '8ball a question')
async def _8ball(ctx,*, question):
    responses = ['Absolutely.',
                 'Definitely not.',
                 'It is certain.',
                 'Not at all.',
                 'My sources say no',
                 'Not sure',
                 'Cannot predict now',
                 'Very doubtful',
                 "Don't count on it",
                 'Outlook not so good',
                 'Most likely',
                 'Without a doubt',
                 'As I see it, yes',
                 'You kidding me?',
                 "I don't answer stupid questions.",
                 'Ask again later.',
                 "Yes, but actually no.",
                 "Yes and no.",
                 "I'm no one to decide.",
                 ]
    await ctx.send(f'> {question}\n {random.choice(responses)}')

#Spam text 
@client.command()
@commands.has_permissions(manage_messages=True)
async def spam(ctx,amount=0,*,text):
  for i in range(amount):
    await ctx.send(text)
    #time.sleep(0.02)

@client.event
async def on_message(message):
  #if message.author=='PokéMeow#6691' or me:
    #print('true1')
  if 'realGamer004' and 'captcha'in message.content:
      print('true2',me[:me.index('#')])
      m=message.mentions
      await m[0].send('Quick come')
  await client.process_commands(message)  

#kick and ban and unban
@client.command(help='kick a member') 
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, * , reason=none): 
    if ctx.author==member.name:
        await ctx.send("You fkin cant do it")
    else: await member.kick(reason=reason)
@client.command(help='ban a member')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.member, * , reason=none): 
    if ctx.author==member.name:
        await ctx.send("You fkin cant do it")
    else: await member.ban(reason=reason)
@commands.command(name='unban')
@commands.guild_only()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	
	member_name, member_discriminator = member.split('#')
	for ban_entry in banned_users:
		user = ban_entry.user
		
		if (user.name, user.discriminator) == (member_name, member_discriminator):
 			await ctx.guild.unban(user)
 			await ctx.channel.send(f"Unbanned: {user.mention}")
             
client.run('NzcwNjcxNjM4NjgwNDM2NzU2.X5g95Q.B7XxM5rzRowNLbUTVzMOcFMRqrQ')
