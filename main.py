import discord
from random import choice, randint
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        if message.author.id == 658918762086400011:
          if message.content == 'scale of 1 to ten how gay is paul':
            choices = randint (9,10)
            await message.channel.send(choices)
          if message.content.startswith('hello'):
            await message.channel.send('Hello

client = MyClient()
client.run("NzQxMTA5MzI3NTAyMjQ1OTEx.Xyyx2A.PZOjzlw3C8Mt97PBzEqXOFaGQ_E")