import discord
import yaml
from discord import ButtonStyle
from core.core import buttonCore
from modal.keyword import keyword
from modal.taunt import taunt

class autoreply(buttonCore):
    custom_id = "atrep"

    def __init__(self, *, timeout: float | None = 180):
        super().__init__(timeout=timeout)
    
    @discord.ui.button(label="新增關鍵字回復",custom_id=custom_id,style=ButtonStyle.success)
    async def confirm(self,interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.guild_permissions.manage_roles:
            await interaction.response.send_modal(keyword())
        else:
            await interaction.response.send_message("你沒有權限使用",ephemeral=True)

    @discord.ui.button(label="新增階下囚回復",custom_id="taunt",style=ButtonStyle.danger)
    async def tau(self,interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.guild_permissions.manage_roles:
            await interaction.response.send_modal(taunt())
        else:
            await interaction.response.send_message("你沒有權限使用",ephemeral=True)
        

    @discord.ui.button(label="查看所有回覆",custom_id="check",style=ButtonStyle.secondary)
    async def check(self,interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.guild_permissions.manage_roles:
            with open("./reply.yml",'r',encoding='utf-8') as f:
                rep = yaml.safe_load(f)
            await interaction.response.send_message(f"關鍵字:```{rep['autoReply']}```\n階下囚:```{rep['taunt']}```",ephemeral=True)
        else:
            await interaction.response.send_message("你沒有權限使用",ephemeral=True)
