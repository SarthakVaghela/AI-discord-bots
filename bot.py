import discord
import os

from discord.ext import commands

# Read the Data files and store them in a variable
TokenFile = open("./data/Token.txt", "r") # Make sure to paste the token in the txt file
TOKEN = TokenFile.read() 

OWNERID = 733370212199694467

# Define "bot"
bot = commands.Bot(command_prefix = ".", case_insensitive=True)

# Let us Know when the bot is ready and has started
@bot.event
async def on_ready():
    print("Bot is ready")

# A simple and small ERROR handler
@bot.event 
async def on_command_error(ctx,error):
    embed = discord.Embed(
    title='',
    color=discord.Color.red())
    if isinstance(error, commands.CommandNotFound):
        pass
    if isinstance(error, commands.MissingPermissions):
        embed.add_field(name=f'Invalid Permissions', value=f'You dont have {error.missing_perms} permissions.')
        await ctx.send(embed=embed)
    else:
        embed.add_field(name = f':x: Terminal Error', value = f"```{error}```")
        await ctx.send(embed = embed)
        raise error

# Load command to manage our "Cogs" or extensions
@bot.command()
async def load(ctx, extension):
    # Check if the user running the command is actually the owner of the bot 
    if ctx.author.id == OWNERID:
        bot.load_extension(f'Cogs.{extension}')
        await ctx.send(f"Enabled the Cog!")
    else:
        await ctx.send(f"You are not cool enough to use this command")

# Unload command to manage our "Cogs" or extensions
@bot.command()
async def unload(ctx, extension):
    # Check if the user running the command is actually the owner of the bot 
    if ctx.author.id == OWNERID:
        bot.unload_extension(f'Cogs.{extension}')
        await ctx.send(f"Disabled the Cog!")
    else:
        await ctx.send(f"You are not cool enough to use this command")

# Reload command to manage our "Cogs" or extensions
@bot.command(name = "reload")
async def reload_(ctx, extension):
    # Check if the user running the command is actually the owner of the bot 
    if ctx.author.id == OWNERID:
        bot.reload_extension(f'Cogs.{extension}')
        await ctx.send(f"Reloaded the Cog!") 
    else:
        await ctx.send(f"You are not cool enough to use this command")

# Automatically load all the .py files in the Cogs folder
for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        try:
            bot.load_extension(f'Cogs.{filename[:-3]}')
        except Exception:
            raise Exception
        
# Run our bot
bot.run(str(TOKEN)) # Make sure you paste the CORRECT token in the "./data/Token.txt" file