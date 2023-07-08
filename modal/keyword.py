import discord
import yaml
from core.core import Logger

class keyword(discord.ui.Modal, title='新增關鍵字回覆'):
    logger = Logger().logger
    key = discord.ui.TextInput(
        label='關鍵字',
        placeholder='請輸入關鍵字',
    )

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
            if data["autoReply"].get(self.key.value):
                data["autoReply"][self.key.value.lower()].append(self.reply.value)
            else:
                data["autoReply"][self.key.value.lower()] = [self.reply.value]

        with open("./reply.yml",'w',encoding="utf-8") as f:
            yaml.safe_dump(data,f)    
        
        self.logger.name = "autoReplyEdit"
        self.logger.info(f"User:{interaction.user.id} edited a reply")
        await interaction.response.send_message(f'已成功新增此回覆！', ephemeral=True)

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)
        self.logger.name = "Interaction error"
        self.logger.error(error)
