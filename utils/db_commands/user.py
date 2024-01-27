from typing import Any, Union
from main.database import database
from main.models import *


async def get_user(chat_id: int) -> Union[dict[Any, Any], bool]:
    try:
        query = users.select().where(users.c.chat_id == chat_id)
        row = await database.fetch_one(query=query)
        return dict(row) if row else False
    except Exception as e:
        error_text = f"Error retrieving user with chat id {chat_id}: {e}"
        print(error_text)


async def add_user_start(message, language: str) -> [bool]:
    try:
        query = users.insert().values(
            chat_id=message.chat.id,
            currect_chat_id=message.chat.id,
            language=language,
            full_name=message.from_user.full_name,
            status=UserStatus.active,
            created_at=message.date,
            updated_at=message.date,
            is_locked=0,
            is_blocked=0,
            is_premium=0,
            username=message.from_user.username
        )
        new_user = await database.execute(query)
        return True if new_user else False
    except Exception as e:
        error_text = f"Error adding user to database: {e}"
        print(error_text)