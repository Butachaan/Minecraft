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

@bot.command()
async def config(ctx, config_name, config_arg):
    if config_name == 'langage':
        if config_arg == 'ja':
            set_langage = 'ja'
            config_output = '言語を日本語に設定しました'
        elif config_arg == 'en':
            set_langage = 'en'
            config_output = '言語を英語に設定しました'
        else:
            config_output = '構文エラー。jpまたはenを指定してください。'

    await ctx.send(config_output)

bot.run(token)