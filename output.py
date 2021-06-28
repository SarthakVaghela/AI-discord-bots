import discord

string = {
    'temp' : 'Temperature',
    'feels_like' : 'Feels Like',
    'temp_min' : 'Minimum Temperature',
    'temp_max' : 'Maximum Temperature'
}

def p_d(data):
    del data['humidity']
    del data['pressure']
    return data

def w_m(data, loc):
    loc = loc.title()
    message = discord.Embed(
        title=f'The weather in {loc} is described below in Celsius.',
        #description=f'The weather in {loc} (Celsius) is described below.', 
        color= 0x0080FE
    )
    for key in data:
        message.add_field(
            name=string[key],
            value=str(data[key]),
            inline=False
        )
    return message

def e_m(loc):
    loc = loc.title()
    return discord.Embed(
        title='Spelling Error',
        description=f'There is no such place called {loc}, Please check ur spelling and try again.',
        color= 0x0080FE
    )
