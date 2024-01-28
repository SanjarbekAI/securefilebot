from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.user import all_languages
from loader import dp, _
from utils.db_commands.user import get_user_not_active


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = await get_user_not_active(message.from_user.id)
    if user:
        text = _('Assalomu alaykum, welcome to SecureFileBot 😊️️️️️️')
        await message.answer(text=text)
    else:
        text = "🇺🇿 O'zbek\n🇷🇺 Русский\n🇺🇸 English"
        await message.answer(text=text, reply_markup=all_languages)


