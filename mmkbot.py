import discord
from discord.ext import commands

TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

client = commands.Bot(command_prefix = "//")
client.remove_command("help")

@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name="神奇指令"))
	print("Bot is ready")

@client.event
async def on_message(message):
	author = message.author
	content = message.content
	if message.content.startswith("kevin gay"):
		await client.send_message(message.channel,"https://tenor.com/view/blue-cry-sad-bad-day-gif-5337197")
	elif message.content.startswith("kyllee"):
		await client.delete_message(message)
		await client.send_message(message.channel,"{} say => kyllee is Handsome guy.".format(author))
	elif message.content.startswith("teemo"):
		await client.delete_message(message)
		await client.send_message(message.channel,"Someone say => Teemo_z is keykey(kiki).")
	elif message.content.startswith("kevin"):
		await client.delete_message(message)
		await client.send_message(message.channel,"Someone say => Kevin is Gay.")
	print("{} : {}".format(author,content))
	await client.process_commands(message)

@client.command(pass_context=True)
async def clear(ctx,amount=100):
	if ctx.message.author.server_permissions.administrator:
		if 99 >= amount >= 1:
			channel = ctx.message.channel
			messages = []
			async for message in client.logs_from(channel,limit=int(amount) + 1):
				messages.append(message)
			await client.delete_messages(messages)
			await client.say("我已刪除{}則訊息".format(amount))
		else:
			await client.say("我只能一次刪除1-99則訊息")
	else:
		await client.say("你沒有使用權限")

@client.command(pass_context=True)
async def join(ctx):
	channel = ctx.message.author.voice.voice_channel
	await client.join_voice_channel(channel)
		
@client.command(pass_context=True)
async def leave(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	await voice_client.disconnect()
		
@client.command()
async def help():
	embed = discord.Embed(
		description = "程式碼：https://github.com/xkyLleex/xxxxxxxxxx",
		colour = discord.Colour.green()
	)
	embed.set_author(name="MMKbot")
	embed.add_field(name="//help",value="叫出MMKbot的資訊",inline=False)
	embed.add_field(name="//clear [整數]",value="清除訊息(整數只能輸入1-99)",inline=False)
	embed.add_field(name="?彩蛋?",value="自行尋找吧",inline=False)
	await client.say(embed=embed)

client.run(TOKEN)
