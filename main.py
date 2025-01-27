from random import randint
from discord.ext import commands
import discord

#Bot token used to sign the bot in
with open("token.txt", "r") as f:
    bot_token = f.read().strip()

#Define a custom class for the bot
class HelloBot(commands.Bot):
    #Update commands
    async def setup_hook(self):
        try:
            synced = await self.tree.sync()
        except discord.HTTPException as e:
            print(f"Failed to sync commands: {e}")
        else:
            print(f"Synced {len(synced)} commands")

#Instantiate the bot
bot = HelloBot(command_prefix='!', intents=discord.Intents.all())

#Print the invite link
@bot.event
async def on_ready():
    print(f"{discord.utils.oauth_url(bot.user.id, permissions=discord.Permissions.all())}")

#Define commands

#!greet
@bot.command()
async def greet(ctx: commands.Context):
    await ctx.send("Hello World!")

#!hello
@bot.command()
async def hello(ctx: commands.Context):
    member = ctx.author
    await ctx.send(f"Hello {member.mention}!")

#!roll <number>
@bot.command()
async def roll(ctx: commands.Context, text: str):
    try:
        number = int(text)
    except ValueError as e:
        response=f"Not a number!"
    else:
        if number >= 0:
            output = randint(0, number)
            response=f"Your number is {output}!"
        else:
            response=f"Invalid number!"
    await ctx.send(response)

#Slash commands

#/hello
@bot.tree.command(name="hello")
async def hello_slash(ctx: discord.Interaction):
    await ctx.response.send_message("Hello!")

#Run the bot
bot.run(token=bot_token)