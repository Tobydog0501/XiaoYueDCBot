import discord
from discord import ButtonStyle
from core.core import buttonCore

class confirmBtn(buttonCore):
    custom_id = "confirm"

    def __init__(self, *, timeout: float | None = 180):
        super().__init__(timeout=timeout)
    
    @discord.ui.button(label="Confirm",custom_id=custom_id,style=ButtonStyle.success)
    async def confirm(self,interaction: discord.Interaction, button: discord.ui.Button):
        # interaction.respose is not callable!!!
        await interaction.message.reply("ok")
        self.value = True
        self.logger.info(f"User {interaction.user.id} clicked the button {self.custom_id}!")
        self.stop()