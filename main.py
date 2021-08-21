import os
import discord
import json

my_token = os.environ['token']

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('>hello'):
		await message.channel.send('Hello!')

client.run(my_token)

# Change from here

var Message = message.content.toString();
  if(Message.startsWith("!")){
    var fullCmd = Message.slice(1);
    if(fullCmd.startsWith("flip")){
       coinFlipCommand(message);
    }
  }