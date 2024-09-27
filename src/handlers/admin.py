from aiogram import Router
from aiogram.filters import Command, CommandStart

from aiogram.types import Message
from tools.scheduler import send_anekdot, send_goodnight

from config import settings

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет я Фрося')

@router.message(Command('check'))
async def check(message: Message):
    if message.from_user.id == settings.admin_id:
         await message.bot.send_message(settings.channel_id, 'hello world')

@router.message(Command('anekdot'))
async def anekdot(message: Message):
    if message.from_user.id == settings.admin_id:
        await send_anekdot(message.bot)

@router.message(Command('goodnight'))
async def good_night(message: Message):
    if message.from_user.id == settings.admin_id:
        await send_goodnight(message.bot)


