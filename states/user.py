from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterState(StatesGroup):
    language = State()
    phone_number = State()
    password_1 = State()
    password_2 = State()