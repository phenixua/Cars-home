from aiogram.filters import Filter

from tg_bot.config import config


class Admin(Filter):
    async def __call__(self, user_id: int) -> bool:
        return user_id in config.ADMINS.values()
