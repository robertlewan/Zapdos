import os
import discord
import json

my_token = os.environ['my_token']

def get_pkm_info(pkm):
	f = open('data.json',)
	data = json.load(f)
	for i in data['pkm_details']:
		if i['name'] == pkm:
			pkm_info = i
			return pkm_info

client = discord.Client()

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
		pkm = message.content.lower()[4:]
		pkm_info = get_pkm_info(pkm)
		await message.channel.send(pkm_info)

print(get_pkm_info('venusaur'))


client.run(my_token)
