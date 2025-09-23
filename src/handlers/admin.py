from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from loguru import logger

from utils.scheduler import send_goodnight
from config import settings


router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    """
    Команда /start — приветствие.
    """
    await message.answer("Привет! Я Фрося 🐱")
    logger.info(f"Пользователь {message.from_user.id} использовал /start, chat_id={message.chat.id}")


@router.message(Command("check"))
async def check(message: Message) -> None:
    """
    Команда /check для проверки работы бота.
    """
    if message.from_user.id == settings.ADMIN_ID:
        await message.bot.send_message(settings.CHAT_ID, "✅ Бот работает")
        logger.info("Выполнена команда /check от администратора")


@router.message(Command("goodnight"))
async def good_night(message: Message) -> None:
    """
    Команда /goodnight для ручного запуска отправки сообщения.
    """
    if message.from_user.id == settings.ADMIN_ID:
        await send_goodnight(message.bot)
        logger.info("Команда /goodnight выполнена админом")