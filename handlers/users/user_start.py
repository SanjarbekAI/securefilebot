from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.user import phone_number_share
from keyboards.inline.user import all_languages
from loader import dp, _
from states.user import RegisterState
from aiogram.dispatcher.storage import FSMContext
from utils.db_commands.user import get_inactive_user, add_user_start


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = await get_inactive_user(message.from_user.id)
    if user:
        text = _('Assalomu alaykum, welcome to SecureFileBot 😊️️️️️️')
        await message.answer(text=text)
    else:
        text = "🇺🇿 O'zbek\n🇷🇺 Русский\n🇺🇸 English"
        await message.answer(text=text, reply_markup=all_languages)
        await RegisterState.language.set()


@dp.callback_query_handler(state=RegisterState.language)
async def language_callback_handler(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(language=call.data)
    await add_user_start(call.message, call.data)
    text = _("Please enter your phone number")
    await call.message.answer(text=text, reply_markup=await phone_number_share())
    await RegisterState.language.set()



