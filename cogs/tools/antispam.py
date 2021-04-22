from discord.ext import commands
from discord.ext.commands import Cog
from assets.functions import *


class Antispam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_message(self, message):
        def _check(m):
            return (m.author == message.author
                    and len(m.mentions)
                    and (datetime.utcnow() - m.created_at).seconds < 60)

        if not message.author.bot:
            if len(list(filter(lambda m: _check(m), self.bot.cached_messages))) >= 3:  # If we detect spamming
                await message.channel.send("Don't spam mentions!", delete_after=10)
                await message.channel.send("https://i.imgur.com/LzDKgZN.png")


def setup(bot):
    bot.add_cog(Antispam(bot))
