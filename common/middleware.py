from typing import Any, Awaitable, Callable
from aiogram import BaseMiddleware, types
from common.db import SessionLocal

class DatabaseMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[types.Message, dict], Awaitable[Any]],
        event: types.Message,
        data: dict
    ) -> Any:
        data['db'] = SessionLocal()
        try:
            return await handler(event, data)
        finally:
            db = data.get('db')
            if db:
                db.close()