import discord
from discord.ext import commands
import json
from discord_slash import SlashCommand, SlashContext

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)
token = config["TOKEN"]
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='y/',intents=intents )

slashClient = SlashCommand(bot)
bot.load_extension('jishaku')
bot.load_extension('cog.owner')

@slashClient.slash(name="hello")
async def _slash_hello(ctx: SlashContext):
    await ctx.send(content="Hello!")

@bot.event
async def on_ready():
  print('bot ready.')

bot.run(token)