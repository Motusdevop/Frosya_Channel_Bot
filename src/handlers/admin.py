from aiogram import Router
from aiogram.filters import Command

from aiogram.types import Message

from config import settings

router = Router()

# @router.message(Command('make_post'))
# async def make_post(message: Message):
#     if message.from_user.id == settings.admin_id:
#         await message.bot.send_message(settings.channel_id, 'hello world')
