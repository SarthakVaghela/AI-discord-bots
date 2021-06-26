import json
import requests
import discord
from output import *

confidentialBotID = 'ODI2MTMzNDUwNTE1OTM5MzM4.YGICuw.DQ-H6hYwD_WRZJlupQ-IdrhhPxM'
confidential_api_key = '036142134bd11a24c5f4b92c3fd8517f'
clt = discord.Client()    #clt is our client, in this case its Discord
command = 'R.'

@clt.event
async def on_ready():
    await clt.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='R.[Desired Location]'))

@clge.at.event
async def on_message(message):
    if messauthor != clt.user and message.content.startswith(command):
        if len(message.content.replace(command, '')) >= 1:
            loc = message.content.replace(command, '').lower()
            fetch_url = f'http://api.openweathermap.org/data/2.5/weather?q={loc}&appid={confidential_api_key}&units=metric'    #imperial for F and metric for C
            try:
                data = p_d(json.loads(requests.get(fetch_url).content)['main'])
                await message.channel.send(embed=w_m(data, loc))
            except KeyError:
                await message.channel.send(embed=e_m(loc))

clt.run(confidentialBotID)
