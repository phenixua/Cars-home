import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.methods import DeleteWebhook
from aiogram.types import *

from backend.src.conf.config import config
from backend.src.tg_bot.constants import *
from backend.src.tg_bot.filters import Admin
from backend.src.tg_bot.handlers import rt
from backend.src.tg_bot.registration import rtr


bot = Bot(config.TG_TOKEN)
dp = Dispatcher()
dp.include_router(rt)
dp.include_router(rtr)


# @dp.callback_query(F.data == "admin")
# async def starting(message: Message):
#     await bot.delete_my_commands()
#     admin = await Admin()(message.from_user.id)
#     if admin:
#         await bot.set_my_commands(
#             [BotCommand(command=command, description=info.get("name")) for command, info in ADM_COMMANDS.items()]
#         )
#     else:
#         await bot.set_my_commands(
#             [BotCommand(command=command, description=info.get("name")) for command, info in USR_COMMANDS.items()]
#         )
#     await message.answer(START, 'HTML', reply_markup=KB_START)


async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))

    await bot.set_my_commands(
            [BotCommand(command=command, description=info.get("name")) for command, info in USR_COMMANDS.items()]
    )

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
