import asyncio

from multiprocessing import Process

from aiogram import Bot, Dispatcher

from config import settings
from tools import scheduler

from handlers.admin import router as admin_router

bot = Bot(token=settings.bot_token.get_secret_value())


def worker():
    asyncio.run((scheduler.scheduler(bot)))


async def main():
    dp = Dispatcher()

    # dp.include_routers(base_router, appointment_router, register_router, admin_router)
    dp.include_router(admin_router)

    process = Process(target=worker)
    process.start()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    process.join()


if __name__ == '__main__':
    asyncio.run(main())
