import discord
from discord.ext import commands

import config
from Music import Music, VoiceState, VoiceEntry

if not discord.opus.is_loaded():
    # the 'opus' library here is opus.dll on windows
    # or libopus.so on linux in the current directory
    # you should replace this with the location the
    # opus library is located in and with the proper filename.
    # note that on windows this DLL is automatically provided for you
    discord.opus.load_opus('opus')

class Bot(commands.Bot):
    def __init__(self, reactive=True, **kwargs):
        self.reactive = reactive
        super().__init__(**kwargs)

    async def ok(self, context):
        await self.react(context, '\N{OK HAND SIGN}')

    async def react(self, context, emoji):
        if self.reactive and context.message is not None:
            self.add_reaction(context.message, emoji)

bot = Bot(command_prefix=commands.when_mentioned_or('$'), description='A playlist example for discord.py')
bot.add_cog(Music(bot))

@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))

bot.run(config.token)
