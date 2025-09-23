import asyncio
from multiprocessing import Process

from aiogram import Bot, Dispatcher
from loguru import logger

from config import settings
from utils.scheduler import start_scheduler
from handlers.admin import router as admin_router


bot = Bot(token=settings.BOT_TOKEN.get_secret_value())


def worker() -> None:
    """
    Фоновый процесс для запуска планировщика заданий.
    """
    asyncio.run(start_scheduler(bot))


async def main() -> None:
    """
    Точка входа для запуска Telegram-бота.
    """
    logger.info("Запуск Telegram-бота...")
    dp = Dispatcher()
    dp.include_router(admin_router)

    process = Process(target=worker, daemon=True)
    process.start()

    logger.success(f"Бот успешно запущен. GOODNIGHT_TIME = {settings.GOODNIGHT_TIME}")

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    process.join()


if __name__ == "__main__":
    logger.add("logs/bot.log", rotation="1 day", compression="zip")
    asyncio.run(main())