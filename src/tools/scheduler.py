import asyncio
import datetime

from aiogram.enums import ParseMode

from aiogram.client.bot import Bot

from config import settings
from tools import anekdots, goodnight

from random import shuffle


async def scheduler(bot: Bot):

    shortics_time = '18:28'
    good_night = '23:00'

    while True:
        time = datetime.datetime.now().strftime('%H:%M')
        if time == shortics_time:
            await send_anekdot(bot)
        elif time == good_night:
            await send_goodnight(bot)
        await asyncio.sleep(60)


async def send_anekdot(bot: Bot):
    anekdot = anekdots.get_random()
    text = f"""
Анекдот с какого-то кринжового сайта (каждый день в 12:00):

`{anekdot}`"""
    await bot.send_message(settings.channel_id, text, parse_mode=ParseMode.MARKDOWN)


async def send_goodnight(bot: Bot):
    emoji_array = ['🌌', '☄️', '⭐', '✨', '🌃']
    shuffle(emoji_array)

    await bot.send_photo(settings.channel_id, photo=goodnight.get_url_photo(),
                         caption=f'Споки {emoji_array[0]}{emoji_array[1]}')
