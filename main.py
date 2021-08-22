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
            return pkm_info


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

		embed = discord.Embed(title=pkm_info["name"], colour=discord.Colour(0xffffff),description="```\n```")

		embed.set_image(url="https://www.serebii.net/pokemonunite/pokemon/003.png")
		embed.set_footer(text="All stats taken at level 15")

		embed.add_field(name="Evolution", value="lvl 5 => lvl 9", inline=True)
		embed.add_field(name="Style", value="Ranged", inline=True)
		embed.add_field(name="Attack damage", value="Special", inline=True)
		embed.add_field(name="Role", value="Attacker", inline=True)
		embed.add_field(name="Price", value="6000 coins", inline=True)
		embed.add_field(name="Ability", value="Overgrowth: When the Pokémon is at low HP, the damage it deals is increased.")
		embed.add_field(name="Basic attack", value="Physical", inline=True)
		embed.add_field(name="Boosted", value="Special", inline=True)
		embed.add_field(name="Move 1", value="Seed Bomb, upgrade at level 5 to Sludge Bomb or Giga Drain.")
		embed.add_field(name="Move 2", value="Razor Leaf, upgrade at level 7 to Solar Beam or Petal Dance.")
		embed.add_field(name="Unite move", value="Verdant Anger")
		embed.add_field(name="Speed", value="2564", inline=True)
		embed.add_field(name="HP", value="5235", inline=True)
		embed.add_field(name="Attack", value="5235", inline=True)
		embed.add_field(name="Defense", value="5235", inline=True)
		embed.add_field(name="Sp. Attack", value="5235", inline=True)
		embed.add_field(name="Sp. Defense", value="5235", inline=True)

		await client.say(embed=embed)


# print(get_pkm_info('venusaur'))

client.run(my_token)