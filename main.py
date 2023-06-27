# This example covers advanced startup options and uses some real world examples for why you may need them.
import os
import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
from keep_alive import keep_alive
from core.core import Logger

load_dotenv()

class MyClient(commands.Bot):
    async def on_ready(self):
        print('Logged on as', self.user)
        # When taking over how the bot process is run, you become responsible for a few additional things.
        # 1. logging
        # for this example, we're going to set up a rotating file logger.
        # for more info on setting up logging,
        # see https://discordpy.readthedocs.io/en/latest/logging.html and https://docs.python.org/3/howto/logging.html


intents = discord.Intents.all()
bot = MyClient(intents=intents,command_prefix="a>")
temp = Logger()

async def loadExtension():
    p = os.listdir('cmds/')
    for filename in p:
        if filename.endswith('.py'):
            print(f"loading extension: {filename[:-3]}")
            temp.logger.name = "Extensions"
            temp.logger.info(f"loading extension: {filename}")
            await bot.load_extension(F'cmds.{filename[:-3]}')

asyncio.run(loadExtension())
temp = None

if __name__ == "__main__":
    keep_alive()
    bot.run(os.environ["TOKEN"])