from backend.src.tg_bot.tg_bot import bot

from backend.src.tg_bot.constants import NOTIFICATIONS


async def notification(user_id, option):
    text = NOTIFICATIONS.get(option).get("message")
    markup = NOTIFICATIONS.get(option).get("reply_markup")
    if text:
        await bot.send_message(user_id, text, reply_markup=markup)
