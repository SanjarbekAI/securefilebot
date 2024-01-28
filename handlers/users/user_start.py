from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.user import phone_number_share
from keyboards.inline.user import all_languages
from loader import dp, _
from states.user import RegisterState
from aiogram.dispatcher.storage import FSMContext
from utils.db_commands.user import get_user, add_user_start, update_user_register


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = await get_user(message.from_user.id)
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
    await RegisterState.phone_number.set()


@dp.message_handler(state=RegisterState.phone_number, content_types=types.ContentTypes.CONTACT)
async def phone_number_handler(message: types.Message, state: FSMContext):
    if message.chat.id == message.contact.user_id:
        await state.update_data(phone_number=message.contact.phone_number)
        text = _("Please, create password. Minimum length is 5")
        await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
        await RegisterState.password_1.set()
    else:
        text = _("Please enter your phone number")
        await message.answer(text=text, reply_markup=await phone_number_share())
        await RegisterState.phone_number.set()


@dp.message_handler(state=RegisterState.password_1)
async def password_1_handler(message: types.Message, state: FSMContext):
    if len(message.text) >= 5:
        await state.update_data(password_1=message.text)
        text = _(f"Please confirm your password: {message.text}")
        await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
        await RegisterState.password_2.set()
    else:
        text = _("Please enter more then 5 characters")
        await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
        await RegisterState.password_1.set()


@dp.message_handler(state=RegisterState.password_2)
async def password_1_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    password_1 = data.get("password_1")

    if password_1 == message.text:
        await update_user_register(message, data)
        text = _("Congratulations! you have successfully registered 🎉")
        await message.answer(text=text)
    else:
        text = _(f"Please enter same password as your previous {password_1}")
        await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await state.finish()
