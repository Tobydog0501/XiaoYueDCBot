import discord
from discord import channel
from discord.ext import commands
from core.core import cog
from discord.utils import get
import datetime
from buttons.addautoreply import autoreply
import asyncio

class cmd(cog):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

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
        if ctx.author.id != 606668363531288577:
            return
        await ctx.channel.send("請選擇要增加哪種回覆",view=autoreply())
        await ctx.message.delete()
        # print("test")
        return



async def setup(bot):
    await bot.add_cog(cmd(bot))
