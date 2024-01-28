from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import _


async def phone_number_share():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text=_("☎️ Share phone number"), request_contact=True)
        ]], resize_keyboard=True
    )
    return keyboard
