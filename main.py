import os
import discord
import json
from discord.ext import commands

my_token = os.environ['my_token']

client = commands.Bot(command_prefix='?', case_insensity=True)

def get_pkm_info(pkm):
	f = open('data.json', )
	data = json.load(f)
	for i in data['pkm_details']:
		if i['name'] == pkm:
			pkm_info = i
			print(pkm_info)
			return pkm_info	
	f.close()				


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content == '?hello':
		await message.channel.send('Hello!')

	if message.content.startswith('?pkm'):
		pkm = message.content.lower()[5:]
		pkm_info = get_pkm_info(pkm)

		
		if pkm_info != None:
			embed = discord.Embed(title=pkm_info["name"].capitalize(), colour=discord.Colour(0xffffff))

			embed.set_image(url=pkm_info["sprite"])
			
			embed.add_field(name="Evolution", value=pkm_info["evolution"], inline=True)
			embed.add_field(name="Style", value=pkm_info["style"], inline=True)
			embed.add_field(name="Attack damage", value=pkm_info["attack-dmg"], inline=True)
			embed.add_field(name="Role", value=pkm_info["role"], inline=True)
			embed.add_field(name="Ability", value=pkm_info["ability"], inline=False)
			embed.add_field(name="Move 1", value=pkm_info["move1"] + ', upgrades at level ' + pkm_info['move1-upg-lvl'] + ' to ' + pkm_info['move1.1'] + ' or ' + pkm_info['move1.2'], inline=False)
			embed.add_field(name="Move 2", value=pkm_info["move2"] + ', upgrades at level ' + pkm_info['move2-upg-lvl'] + ' to ' + pkm_info['move2.1'] + ' or ' + pkm_info['move2.2'], inline=False)
			embed.add_field(name="Unite move", value=pkm_info["unite"], inline=False)
			
			await message.channel.send(embed=embed)
		else:
			await message.channel.send("Oops, that doesn't look like a Pokemon.")
	
	elif message.content.startswith('?price'):
		pkm = message.content.lower()[7:]
		pkm_info = get_pkm_info(pkm)

		if pkm_info != None:
			embed = discord.Embed(title=pkm_info["name"].capitalize(), colour=discord.Colour(0xffffff))

			embed.set_thumbnail(url=pkm_info["sprite"])
			embed.add_field(name="Price", value=pkm_info["price"], inline=True)
			await message.channel.send(embed=embed)
		else: 
			await message.channel.send("Oops, that doesn't look like a Pokemon.")

	elif message.content.startswith('?stats'):
		pkm = message.content.lower()[7:]
		pkm_info = get_pkm_info(pkm)

		if pkm_info != None:
			
			embed = discord.Embed(title=pkm_info["name"].capitalize(), 
			colour=discord.Colour(0xffffff))
			embed.set_thumbnail(url=pkm_info["sprite"])
			embed.set_footer(text="All stats taken at level 15")
			embed.add_field(name="Basic attack", value=pkm_info["basic"], inline=False)
			embed.add_field(name="Boosted", value=pkm_info["boosted"], inline=False)

			embed.add_field(name="Speed", value=pkm_info["speed"], inline=True)
			embed.add_field(name="HP", value=pkm_info["hp"], inline=True)
			embed.add_field(name="Attack", value=pkm_info["atk"], inline=True)
			embed.add_field(name="Defense", value=pkm_info["def"], inline=True)
			embed.add_field(name="Sp. Attack", value=pkm_info["sp-atk"], inline=True)
			embed.add_field(name="Sp. Defense", value=pkm_info["sp-def"], inline=True)
			await message.channel.send(embed=embed)
		else: 
			await message.channel.send("Oops, that doesn't look like a Pokemon.")
	elif message.content.startswith('?build'):
		pkm = message.content.lower()[7:]
		pkm_info = get_pkm_info(pkm)

		if pkm_info != None:

			await message.channel.send(pkm_info["build"])

	elif message.content == '?gián':
		await message.channel.send('Rác')
			

client.run(my_token)