import discord , datetime , pytz
from discord.ext import commands

TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

client = commands.Bot(command_prefix = "//")
client.remove_command("help")

@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name="//help",type=3))
	print("Bot is ready")

@client.event
async def on_message(message):
	author = message.author
	content = message.content
	if message.content.startswith("kevin gay"):
		await client.delete_message(message)
		await client.send_message(message.channel,"Kevin cry")
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
async def weather(ctx,*args):
    try:
        if args[0] == "radar":
            delaytime=0
            try:
                if args[1] != "":
                    try:
                        delaytime=int(args[1])+10
                    except:
                        await client.say("請輸入的文字並非數字，將以原始模式跑圖！")
                    else:
                        if 120 < delaytime or delaytime < 0:
                            delaytime=10
                            await client.say("數字加10後只能介於0-120之間，將以原始模式跑圖！")
            except:
                delaytime=10
            finally:
                twtime = pytz.timezone(pytz.country_timezones('tw')[0])
                nowtimes = datetime.datetime.now(twtime) - datetime.timedelta(minutes=delaytime)
            minute = int(nowtimes.strftime("%M"))
            if minute >= 10:
                await client.say("如果沒有圖就表示還未產生，把時間往前調就行(預設已往前調10Min)\n往前調 x 分鐘指令=>//weather rader x")
                await client.say("https://www.cwb.gov.tw/V7/observe/radar/Data/HD_Radar/CV1_3600_{}{}.png"
                                 .format(nowtimes.strftime("%Y%m%d%H"),int(minute/10)*10))
            else:
                await client.say("如果沒有圖就表示還未產生，把時間往前調就行(預設已往前調10Min)\n往前調 x 分鐘指令=>//weather rader x")
                await client.say("https://www.cwb.gov.tw/V7/observe/radar/Data/HD_Radar/CV1_3600_{}.png"
                                 .format(nowtimes.strftime("%Y%m%d%H00")))
        if args[0] == "analysis":
            await client.say("Taiwan:UTC+8")
            await client.say("https://www.cwb.gov.tw/Data/fcst_img/I04.jpg")
    except:
        await client.say("請輸入一個值")
		
@client.command()
async def nowtime():
    twtime = pytz.timezone(pytz.country_timezones('tw')[0])
    times = datetime.datetime.now(twtime)
    await client.say("{} {}{}".format(times,"星期",times.strftime("%w")))
		
@client.command()
async def help():
	embed = discord.Embed(
		description = "程式碼：https://github.com/xkyLleex/xxxxxxxxxx",
		colour = discord.Colour.green()
	)
	embed.set_author(name="MMKbot")
	embed.add_field(name="//help",value="叫出MMKbot的資訊",inline=False)
	embed.add_field(name="//clear [整數]",value="清除訊息(整數只能輸入1-99)",inline=False)
	embed.add_field(name="//nowtime",value="顯示現在時間",inline=False)
	embed.add_field(name="//weather [功能]",value="顯示:earth_asia:天氣狀況，[功能]有:\nradar=>臺灣雷達回波圖",inline=False)
	embed.add_field(name="?彩蛋?",value="自行尋找吧",inline=False)
	await client.say(embed=embed)

client.run(TOKEN)
