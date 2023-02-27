import discord
from discord.ext import commands
token = ''

class ZachBot(discord.Client):

    # prints out to the terminal to make sure that the bot is running and has logged into
    # the bot account successfully.
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        print('---------')

    # replies to a message IF using a certain command. (basic bot idea)
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('!Zachy'):
            await message.reply('Woof!', mention_author=True)
    
    # whenever user edits their message the bot returns the original content
    # and demonstrates the new content (this is good for a moderation bot)
    async def on_message_edit (self, before, after):
        msg = f'**{before.author}** edited their message:\n{before.content} -> {after.content}'
        await before.channel.send(msg)

    # sends a welcome message to new server members. (New Members bot)
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send) 

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = ZachBot(intents=intents)
client.run(token)
