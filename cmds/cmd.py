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
    async def R寶(self,ctx,arg):
        event = '刀光劍影大亂鬥'
        persons = '10/10'
        time = '尚未確定'
        author = ctx.author
        command_permission = get(author.guild.roles,name='no_bot_permission')
        recent = get(author.guild.roles,name='近期活動參與者')
        if command_permission in author.roles:
            await ctx.send('你沒有權限使用此指令')
        else:
            if arg == '近期活動':
                await ctx.send(F'目前近期活動為<<{event}>>，參加人數為{persons}人，活動時間{time}')
            if arg == '連結':
                await ctx.send('https://discord.gg/2vrGj567Bg')
                await ctx.send('https://forms.gle/M6BDovtn1TSfVvke7')
            if arg == 'help':
                await ctx.send('輸入:R寶(空格)【近期活動】【連結】【YT申請】【GM申請】【Warning申請】【報名近期活動】【報名】【取消報名】(不用【】)')
            if arg == 'YT申請':
                await ctx.send('已向管理員提出請求')
                channel = self.bot.get_channel(828979902963384320)
                await channel.send(F'{author}想加入YT身分組')
            if arg == 'GM申請':
                warning_role = get(author.guild.roles,name='Warning')
                if warning_role in author.roles:
                    await ctx.send('你沒有權限使用此指令')
                else:
                    await ctx.send('已申請成功\n歡迎成為GM的一員')
                    role = get(author.guild.roles,name='Gentleman')
                    await author.add_roles(role)
                    channel = self.bot.get_channel(828979902963384320)
                    await channel.send(F'{author}已加入GM身分組')
            if arg == 'Warning申請':
                await ctx.send('已成功將自己禁言(誰那麼笨XDDDDDD)')
                role = get(author.guild.roles,name='Warning')
                await author.add_roles(role)
                channel = self.bot.get_channel(828979902963384320)
                await channel.send(F'{author}不小心將自己加入Warning身分組')
            if '報名' in arg:
                if not '取消' in arg:
                    if not recent in author.roles:
                        await ctx.send('已報名成功')
                        channel = self.bot.get_channel(828979902963384320)
                        await channel.send(F'{author}想參加近期活動')
                        await author.add_roles(recent)
                    else:
                        await ctx.send('很感謝您積極的參與近期活動\n\n\n\n然而，您已經報過一次名了')
                else:
                    if '取消' in arg:
                        if recent in author.roles:
                            await ctx.send('已成功取消')
                            channel = self.bot.get_channel(828979902963384320)
                            await channel.send(F'{author}想取消參加近期活動')   
                            await author.remove_roles(recent)
                        else:
                            await ctx.send('不好意思，不過您看起來並沒有報名近期活動\n\n\n您是記憶有問題嗎XDDD')
    

    @commands.command()
    async def tell(self,ctx,skyeye_v,Rbot_v,update,Bug,password):
        author = ctx.author
        a = datetime.datetime.now().strftime('%Y/%m/%d %H:%M')
        if password == '9487946':
            channel = self.bot.get_channel(833705821341876284)
            await channel.send(F'{a}\nBots version: {skyeye_v} / {Rbot_v}(前面天眼後面R寶)\n更新內容:{update}\nBug修復:{Bug}')
        else:
            channel = self.bot.get_channel(801386989739311128)
            await ctx.send('你沒有權限使用此指令')
            await channel.send(F'{author}正在使用特殊指令!')

    @commands.command()
    async def version(self,ctx):
        await ctx.send('版本:3.0.1')

    @commands.command()
    async def 頻道(self,ctx,url):
        author = ctx.author
        yt_per = get(author.guild.roles,name='Youtuber')
        if yt_per in author.roles:
            if 'http' in url:
                if 'youtu' in url:
                    if 'channel' in url:
                        await ctx.send('已加入 #實況名人堂')
                        channel = self.bot.get_channel(851773520676651018)
                        await channel.send(url)
        else:
            await ctx.send('請先申請YT身分組')         



def setup(bot):
    bot.add_cog(cmd(bot))
