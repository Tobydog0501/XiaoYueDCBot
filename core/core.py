from typing import Any, List, Optional
import discord
from discord.components import SelectOption
from discord.ext import commands
import logging
import logging.handlers
from discord.interactions import Interaction

from discord.utils import MISSING

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.handlers.RotatingFileHandler(
    filename='discord.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

class Logger:
    def __init__(self) -> None:
        self.logger = logger

class cog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.logger = logger


class buttonCore(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180):
        super().__init__(timeout=timeout)
        self.value = None
        self.logger = logger

class menuCore(discord.ui.Select):
    def __init__(self, *, custom_id: str = ..., placeholder: str | None = None, min_values: int = 1, max_values: int = 1, options: List[SelectOption] = ..., disabled: bool = False, row: int | None = None) -> None:
        super().__init__(custom_id=custom_id, placeholder=placeholder, min_values=min_values, max_values=max_values, options=options, disabled=disabled, row=row)
        self.logger = logger

    async def callback(self, interaction: discord.Interaction): ...

class DropdownView(discord.ui.View):
    def __init__(self,menu:menuCore, *, custom_id: str = ..., placeholder: str | None = None, min_values: int = 1, max_values: int = 1, options: List[SelectOption] = ..., disabled: bool = False, row: int | None = None):
        super().__init__()
        # Adds the dropdown to our view object.
        self.add_item(menu(custom_id=custom_id, placeholder=placeholder, min_values=min_values, max_values=max_values, options=options, disabled=disabled, row=row))