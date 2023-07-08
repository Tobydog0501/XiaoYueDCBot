import discord
import yaml
from core.core import Logger

class taunt(discord.ui.Modal, title='新增階下囚回覆'):
    logger = Logger().logger

    reply = discord.ui.TextInput(
        label='機器人回覆內容',
        style=discord.TextStyle.long,
        placeholder='輸入機器人回覆內容，使用{user}來@他',
        required=True,
        max_length=300,
    )

    async def on_submit(self, interaction: discord.Interaction):
        with open("./reply.yml","r",encoding="utf-8") as f:
            data = yaml.safe_load(f)
            data["taunt"].append(self.reply.value)
                
        with open("./reply.yml",'w',encoding="utf-8") as f:
            yaml.safe_dump(data,f)    

        self.logger.name = "autoReplyEdit"
        self.logger.info(f"User:{interaction.user.id} edited a reply")
        await interaction.response.send_message(f'已成功新增此回覆！', ephemeral=True)

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)
        self.logger.name = "Interaction error"
        self.logger.error(error)
