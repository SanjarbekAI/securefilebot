from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import _


async def phone_number_share(language):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text=_("☎️ Share phone number", locale=language), request_contact=True)
        ]], resize_keyboard=True
    )
    return keyboard
