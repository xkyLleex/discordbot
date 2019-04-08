import discord
from discord.ext import commands

TOKEN = "NTY0NjU4MTE1MDMxNzI4MTI4.XKrLHg.R6aeufLFI6LvJd9ZxZD0yC2zlcA"

client = commands.Bot(command_prefix = '//')
"""
author = message.author	使用者
content = message.content	使用者打的字
channel = message.channel	使用者打字的頻道
if message.content.startswith(".echo"):	使用者
		msg = message.content.split()
		output = ""
		for word in msg[1:]:
			output += word + " "
		await client.send_message(channel,output)	BOT講話
"""
client.remove_command("help")

@client.event
async def on_ready():
    print("Bot is ready")
	
@client.event
async def on_message(message):
	author = message.author
	content = message.content
	print("{} : {}".format(author,content))
	await client.process_commands(message)

@client.command(pass_context=True)
async def clear(ctx,amount=100):
	channel = ctx.message.channel
	messages = []
	async for message in client.logs_from(channel,limit=int(amount) + 1):
		messages.append(message)
	await client.delete_messages(messages)
	await client.say("message deleted")
	
@client.command()
async def ping():
	await client.say("bitch")

@client.command(pass_context=True)
async def send(ctx,*args):
	author = ctx.message.author
	output = ""
	for word in args:
		output += word + " "
	await client.delete_messages(ctx.message.channel)
	await client.send_message(author,output)

@client.command()
async def help():
	embed = discord.Embed(
		description = "程式碼：https://github.com/xkyLleex/redhat-python",
		colour = discord.Colour.green()
	)
	embed.set_author(name="MMKbot")
	embed.add_field(name="//help",value="叫出MMKbot的資訊",inline=False)
	embed.add_field(name="//clear [整數]",value="清除訊息(整數只能輸入1-99)",inline=False)
	embed.add_field(name="//send [文字]",value="叫機器人傳你輸入的文字給你",inline=False)
	await client.say(embed=embed)
	
client.run(TOKEN)
