from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from common.middleware import DatabaseMiddleware


from sqlalchemy.orm import Session

from states.user_data import UserDataStates
from keyboards.reply.user_data import UserDataReplyKeyboard
from responses.user_data import UserDataResponses
from expected_messages.user_data import UserDataExpectedMessages

from filters import ReenterData, ConfirmEnteredData

from crud.user_data import db_get_faculties_names


import common.keyboards
from common.states import IdleStates

user_data_db_required_router = Router()

user_data_db_required_router.message.middleware(DatabaseMiddleware())



@user_data_db_required_router.message(UserDataStates.confirm_group_number, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext, db: Session):
    await message.answer(UserDataResponses.ASK_FOR_FACULTY, reply_markup=UserDataReplyKeyboard.generate_choose_faculty_keyboard(db))
    await state.set_state(UserDataStates.waiting_for_faculty)


@user_data_db_required_router.message(UserDataStates.waiting_for_faculty)
async def process_faculty(message: Message, state: FSMContext, db: Session):
    faculty = message.text
    if faculty not in db_get_faculties_names(db):
        await message.answer(UserDataResponses.WRONG_FACULTY_NAME)
        await message.answer(UserDataResponses.ASK_FOR_FACULTY, reply_markup=UserDataReplyKeyboard.generate_choose_faculty_keyboard(db))
        await state.set_state(UserDataStates.waiting_for_faculty)
    else:
        await state.update_data(faculty=message.text)
        await message.answer(UserDataResponses.get_confirm_faculty_text(faculty), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
        await state.set_state(UserDataStates.confirm_faculty)


@user_data_db_required_router.message(UserDataStates.confirm_faculty, ReenterData())
async def cancel(message: Message, state: FSMContext, db: Session):
    await state.update_data(faculty=None)
    await message.answer(UserDataResponses.ASK_FOR_FACULTY, reply_markup=UserDataReplyKeyboard.generate_choose_faculty_keyboard(db))
    await state.set_state(UserDataStates.waiting_for_faculty)

