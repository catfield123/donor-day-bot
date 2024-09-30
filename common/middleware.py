from typing import Any, Awaitable, Callable
from aiogram import BaseMiddleware, types
from common.db import SessionLocal
from sqlalchemy.exc import SQLAlchemyError
from common.exceptions import DatabaseConnectionError

class DatabaseMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[types.Message, dict], Awaitable[Any]],
        event: types.Message,
        data: dict
    ) -> Any:
        try:
            data['db'] = SessionLocal()
            return await handler(event, data)
        except SQLAlchemyError as e:
            print(e)
            raise DatabaseConnectionError("Error while connecting to database") from e
        finally:
            db = data.get('db')
            if db:
                db.close()