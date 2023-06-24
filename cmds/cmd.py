import discord
from discord import channel
from discord.ext import commands
from core.core import cog
from discord.utils import get
import datetime
import asyncio

class cmd(cog):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    @commands.command()
    async def mute(self,ctx:commands.Context,arg=None,seconds=None):
        if arg and seconds:
            mem = await ctx.guild.fetch_member(int(arg))
            await mem.timeout(datetime.timedelta(seconds=int(seconds)))
        else:
            await ctx.channel.send("格式：a>mute userId timeoutSeconds")
        await ctx.message.delete()
     



async def setup(bot):
    await bot.add_cog(cmd(bot))
