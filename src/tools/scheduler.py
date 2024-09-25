import asyncio
import datetime

from aiogram.enums import ParseMode

from aiogram.client.bot import Bot

from config import settings
from tools import shortics, goodnight

from random import shuffle


async def scheduler(bot: Bot):
    emoji_array = ['🌌', '☄️', '⭐', '✨', '🌃']
    shortics_time = '12:00'
    good_night = '23:00'

    while True:
        time = datetime.datetime.now().strftime('%H:%M')
        if time == shortics_time:
            short = shortics.get_random()
            text = f"""
Анекдот с какого-то кринжового сайта (каждый день в 12:00):
`{short['content']}`

Место в рейтинге: {short['rating']} 🏆
            """
            await bot.send_message(settings.channel_id, text, parse_mode=ParseMode.MARKDOWN)
        elif time == good_night:
            shuffle(emoji_array)

            await bot.send_photo(settings.channel_id, photo=goodnight.get_url_photo(),
                                 caption=f'Споки {emoji_array[0]}{emoji_array[1]}')
        await asyncio.sleep(60)
