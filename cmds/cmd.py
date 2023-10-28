import discord
from discord import channel
from discord.ext import commands
from core.core import cog
from discord.utils import get
from dhooks import Webhook
from threading import Thread
import datetime
import yaml
from buttons.addautoreply import autoreply
import asyncio

class cmd(cog):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        with open("./permissions.yml",'r',encoding='utf-8') as f:
            self.permis = yaml.safe_load(f)

    @commands.command()
    async def mute(self,ctx:commands.Context,arg=None,seconds=None):
        if ctx.author.id != 606668363531288577:
            return
        if arg and seconds:
            mem = await ctx.guild.fetch_member(int(arg))
            await mem.timeout(datetime.timedelta(seconds=int(seconds)))
        else:
            await ctx.channel.send("格式：a>mute userId timeoutSeconds")
        await ctx.message.delete()
    
    @commands.command()
    async def btn(self,ctx:commands.Context):
        await ctx.channel.send("請選擇要增加哪種回覆",view=autoreply())
        await ctx.message.delete()
        # print("test")
        return
    
    @commands.command()
    async def nuke(self,ctx:commands.Context,member:discord.Member=None,time="50"):
        if not self.permis.get(ctx.author.id):
            await ctx.reply("只有有權限者能使用此指令!\n要權限找Tobydog!")
            return
        if not member:
            await ctx.reply("輸入格式：a>nuke @被轟炸人 次數")
            return
        if int(time) > 50:
            await ctx.reply("一次最多50次喔~")
            return
        webhook = await ctx.channel.create_webhook(name="阿嬤分身")
        x = Webhook(webhook.url)
        threads = [Thread(target = lambda:x.send(f"<@{member.id}>")) for i in range(int(time))]
        for t in threads:
            t.start()

        for t in threads:
            t.join()
        # await asyncio.sleep(10)
        await webhook.delete()


async def setup(bot):
    await bot.add_cog(cmd(bot))
