from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, _


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text = _('Assalomu alaykum, welcome to SecureFileBot 😊️️️️️️')
    await message.answer(text=text)
