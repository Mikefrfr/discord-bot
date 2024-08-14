import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption, ChannelType
from nextcord.abc import GuildChannel

intents = nextcord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='yo ', intents=intents)

bru = 1158289507221774379

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command(name='dude')
async def SendMessage(ctx):
    await ctx.send("waazzzzuuuuppp")

@client.command(name='random')
async def SendMessage(ctx):
    await ctx.send("go do something you jobless")

@client.slash_command(name = "beauty", description = "tells you your beautiful", guild_ids=[bru])
async def ping(interaction: Interaction):
    await interaction.response.send_message("you are beautiful")

@client.slash_command(name = "yoyo", description = "tells yoyo", guild_ids=[bru])
async def ping(interaction: Interaction):
    await interaction.response.send_message("yoyo")

@client.slash_command(name = "idk", description = "random shi", guild_ids=[bru])
async def ping(interaction: Interaction):
    await interaction.response.send_message("im in love with you")

