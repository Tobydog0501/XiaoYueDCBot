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
    async def temp(self,ctx):
        pass
     



async def setup(bot):
    await bot.add_cog(cmd(bot))
