from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "To start the bot"),
            types.BotCommand("help", "To get all commands"),
        ]
    )
