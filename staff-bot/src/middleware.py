from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message

from sqlalchemy.orm import Session

from crud.auth import db_is_admin, db_is_volunteer
from exceptions.auth import NotAdminException, NotVolunteerException

from schemas import CheckAuthRequestSchema

class IsAdminMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        db : Session = data.get('db')
        user_id = event.from_user.id
        if not db_is_admin(db, CheckAuthRequestSchema(telegram_id=user_id)):
            raise NotAdminException
        return await handler(event, data)
    
class IsVolunteerMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        db : Session = data.get('db')
        user_id = event.from_user.id
        if not db_is_volunteer(db, CheckAuthRequestSchema(telegram_id=user_id)):
            raise NotVolunteerException
        return await handler(event, data)