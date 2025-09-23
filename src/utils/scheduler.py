import asyncio
import datetime
import random

from aiogram.client.bot import Bot
from aiogram.types import InputMediaPhoto
from loguru import logger

from config import settings
from utils.goodnight import CatAPIService, GoodNightMessage


async def start_scheduler(bot: Bot) -> None:
    """
    Планировщик, который проверяет текущее время
    и запускает отправку сообщений.
    """
    night_time = settings.GOODNIGHT_TIME
    logger.info(f"Планировщик запущен. GOODNIGHT_TIME = {night_time}")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == night_time:
            await send_goodnight(bot)
        await asyncio.sleep(60)


async def send_goodnight(bot: Bot) -> None:
    """
    Отправляет сообщение «Спокойной ночи» с 1–3 фото кота в одном альбоме.
    """
    count = random.randint(1, 3)
    photos = CatAPIService.get_cat_photos(count)
    message = GoodNightMessage.get_message()

    if not photos:
        await bot.send_message(settings.CHAT_ID, text=message)
        logger.warning("Не удалось загрузить фото кота, отправлено только сообщение.")
        return

    # Формируем медиагруппу: к первому фото добавляем caption
    media = [
        InputMediaPhoto(media=photo, caption=message if i == 0 else None)
        for i, photo in enumerate(photos)
    ]

    await bot.send_media_group(settings.CHAT_ID, media=media)

    logger.info(f"Отправлено сообщение «Спокойной ночи» ({count} фото кота в одном альбоме).")