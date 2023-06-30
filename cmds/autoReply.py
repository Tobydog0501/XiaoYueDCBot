import discord
from discord.ext import commands
from core.core import cog
import re
import logging
import random
import yaml
import discord.utils as utils
import datetime
import asyncio

async def fun(msg:discord.Message,execute:bool=False):
    if execute:
        rr = random.random()
        # print(rr)
        if rr <= 0.1:
            try:
                await msg.author.timeout(datetime.timedelta(seconds=10))
                await msg.reply("恭喜中獎！")
            except:
                pass

class autoReply(cog):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        with open("./reply.yml",'r',encoding='utf-8') as f:
            self.reply = yaml.safe_load(f)
        self.shutUpRole = None
        self.autoReply = self.reply["autoReply"].keys()
        with open("./scam-links.yml",'r',encoding='utf-8') as f:
            self.data = yaml.safe_load(f)
        

    @commands.Cog.listener()
    async def on_message(self, msg:discord.Message):
        if not self.shutUpRole:
            self.shutUpRole = utils.get(msg.guild.roles,id=1006858175351361616)
        bot = self.bot
        # don't respond to ourselves
        if msg.author.bot:
            return

        await fun(msg,False)
        # Turn to True if want to play sussy game

        if "http" in msg.content:
            if "youtub" in msg.content:
                return
            result = re.search("https?://",msg.content)
            try:
                data = self.data["links"][msg.content[result.end()]]
                for d in data:
                    if re.search(f"https?://{d}",msg.content):
                        # yellow = "\x1b[33;20m"
                        self.logger.name = "Scam links"
                        self.logger.warn(f"Scam link detected! Content: {msg.content}, sus link:{d}, Author: {msg.author.id}")
                        # logging.info(f"Scam link detected! Content: {msg.content}, Author: {msg.author.id}")
                        await msg.delete()
                        await msg.channel.send(f"偵測到可疑連結! 傳送者: <@{msg.author.id}>")
            except:
                pass
        
        if self.shutUpRole in msg.author.roles:
            await msg.delete()
            await msg.channel.send(self.reply["taunt"][random.randint(0,len(self.reply["taunt"])-1)].replace("{user}",f"<@{msg.author.id}>"))
        
        if msg.content.lower() in self.autoReply:
            await asyncio.sleep(0.3)
            temp = self.reply["autoReply"][msg.content.lower()]
            await msg.channel.send(temp[random.randint(0,len(temp)-1)])
                
        return


async def setup(bot):
    await bot.add_cog(autoReply(bot))