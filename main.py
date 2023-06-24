# This example covers advanced startup options and uses some real world examples for why you may need them.
import logging
import logging.handlers
import os
import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
from keep_alive import keep_alive
import yaml
import re
import random
import datetime

load_dotenv()

class MyClient(commands.Bot):
    async def on_ready(self):
        print('Logged on as', self.user)
        # When taking over how the bot process is run, you become responsible for a few additional things.
        # 1. logging
        # for this example, we're going to set up a rotating file logger.
        # for more info on setting up logging,
        # see https://discordpy.readthedocs.io/en/latest/logging.html and https://docs.python.org/3/howto/logging.html
        logger = logging.getLogger('discord')
        logger.setLevel(logging.INFO)
        handler = logging.handlers.RotatingFileHandler(
            filename='discord.log',
            encoding='utf-8',
            maxBytes=32 * 1024 * 1024,  # 32 MiB
            backupCount=5,  # Rotate through 5 files
        )
        dt_fmt = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        with open("scam-links.yml",'r') as f:
            self.data = yaml.safe_load(f)

    async def on_message(self, msg:discord.Message):
        # don't respond to ourselves
        if msg.author.bot == self.user:
            return
        
        # rr = random.random()
        # # print(rr)
        # if rr <= 0.1:
        #     try:
        #         await msg.author.timeout(datetime.timedelta(seconds=10))
        #         await msg.reply("恭喜中獎！")
        #     except:
        #         pass
        
        if "http" in msg.content:
            if "youtub" in msg.content:
                return
            result = re.search("https?://",msg.content)
            try:
                data = self.data["links"][msg.content[result.end()]]
                for d in data:
                    if d in msg.content:
                        logging.warn(f"Sussy link: {msg.content}")
                        await msg.delete()
                        await msg.channel.send(f"偵測到可疑連結! 傳送者: <@{msg.author.id}>")
            except Exception as e:
                logging.error(e)
                pass

        await bot.process_commands(msg)


intents = discord.Intents.all()
bot = MyClient(intents=intents,command_prefix="a>")


async def loadExtension():
    p = os.listdir('cmds/')
    for filename in p:
        if filename.endswith('.py'):
            await bot.load_extension(F'cmds.{filename[:-3]}')

asyncio.run(loadExtension())


if __name__ == "__main__":
    keep_alive()
    bot.run(os.environ["TOKEN"])
