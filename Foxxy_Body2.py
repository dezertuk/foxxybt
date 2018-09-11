import discord
from discord.ext.commands import Bot
from discord import Game
import datetime
from ctypes.util import find_library
import random
from discord import opus
import json
import os


import youtube_dl
import nacl
import asyncio
#import requests
import json

BOT_PREFIX = ("!")
client = Bot(command_prefix = BOT_PREFIX)


extensions = ['corecommands', 'music', 'info', 'poll']

'''
All Events
'''

@client.event
async def on_ready():
    print('Logged in as:'+ client.user.name)
    print(client.user.id)
    print(datetime.datetime.now())
    print('------')
    await client.change_presence(game = Game(name = "a game of life"))

    key = str(datetime.datetime.now())
    insert = 'Foxxy has turned ON'
    logged = {key: insert}

    data = json.load(open('StartLog.json', 'r'))
    with open('StartLog.json', 'w') as f:
        data['Logs'].update(logged)
        json.dump(data, f, indent=2)

@client.event
async def on_resume():
    print('Foxxy has reconnected to the server at', datetime.datetime.now())

    key = str(datetime.datetime.now())
    insert = 'Foxxy has reconnected to the server'
    logged = {key: insert}

    data = json.load(open('StartLog.json', 'r'))
    with open('StartLog.json', 'w') as f:
        data['Logs'].update(logged)
        json.dump(data, f, indent=2)
'''
All Commands
'''


'''
Extensions/Cogs
'''

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
            print('Loaded {}'.format(extension))
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))


    #Last part
    client.run(os.getenv('TOKEN')


