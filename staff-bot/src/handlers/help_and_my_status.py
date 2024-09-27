from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from sqlalchemy.orm import Session
from crud.auth import db_is_admin,db_is_volunteer
from schemas import CheckAuthRequestSchema

from common.middleware import DatabaseMiddleware
from responses.help import HelpResponses
from responses.my_status import MyStatusResponses


from common.states import IdleStates

help_and_status_router = Router()

help_and_status_router.message.middleware(DatabaseMiddleware())

@help_and_status_router.message(IdleStates.idle, Command("help"))
async def show_help_message(message: Message, state: FSMContext, db: Session):
    is_admin = db_is_admin(db, CheckAuthRequestSchema(telegram_id=message.from_user.id))
    is_volunteer = db_is_volunteer(db, CheckAuthRequestSchema(telegram_id=message.from_user.id))

    await message.answer(HelpResponses.generate_full_help_response(is_admin=is_admin, is_volunteer=is_volunteer))

@help_and_status_router.message(IdleStates.idle, Command("my_status"))
async def show_my_status(message: Message, state: FSMContext, db: Session):
    is_admin = db_is_admin(db, CheckAuthRequestSchema(telegram_id=message.from_user.id))
    is_volunteer = db_is_volunteer(db, CheckAuthRequestSchema(telegram_id=message.from_user.id))

    await message.answer(MyStatusResponses.generate_my_status_response(is_admin=is_admin, is_volunteer=is_volunteer))
    