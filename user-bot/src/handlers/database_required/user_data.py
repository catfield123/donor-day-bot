from aiogram import Router, F
from aiogram.types import Message
from aiogram.types.callback_query import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from callbacks import ChooseDonationDatetimeCallback, ChooseDonationPlaceCallback
from common.middleware import DatabaseMiddleware


from sqlalchemy.orm import Session

from states.user_data import UserDataStates
from keyboards.reply.user_data import UserDataReplyKeyboard
from keyboards.inline.user_data import UserDataInlineKeyboard
from responses.user_data import UserDataResponses
from expected_messages.user_data import UserDataExpectedMessages

from filters import ReenterData, ConfirmEnteredData, ReenterPlaceAndDatetime

from crud.user_data import db_get_faculties_names
from utils import generate_user_recheck_data_from_state_data

import common.keyboards
from common.states import IdleStates

user_data_db_required_router = Router()

user_data_db_required_router.message.middleware(DatabaseMiddleware())


# FACULTY HANDLING
@user_data_db_required_router.message(UserDataStates.confirm_group_number, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext, db: Session):
    state_data = await state.get_data()
    all_data_is_collected = state_data.get('all_data_is_collected')
    if all_data_is_collected:
        await message.answer(UserDataResponses.get_confirm_faculty_text(state_data.get('faculty')), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
        await state.set_state(UserDataStates.confirm_faculty)
    else:
        await message.answer(UserDataResponses.ASK_FOR_FACULTY, reply_markup=UserDataReplyKeyboard.generate_choose_faculty_keyboard(db))
        await state.set_state(UserDataStates.waiting_for_faculty)


@user_data_db_required_router.message(UserDataStates.waiting_for_faculty)
async def process_faculty(message: Message, state: FSMContext, db: Session):
    faculty_name = message.text
    correct_faculties = {faculty.name: faculty.id for faculty in db_get_faculties_names(db)}
    if faculty_name not in correct_faculties:
        await message.answer(UserDataResponses.WRONG_FACULTY_NAME)
        await message.answer(UserDataResponses.ASK_FOR_FACULTY, reply_markup=UserDataReplyKeyboard.generate_choose_faculty_keyboard(db))
        await state.set_state(UserDataStates.waiting_for_faculty)
    else:
        faculty_id = correct_faculties[faculty_name]
        await state.update_data(faculty=message.text)
        await state.update_data(faculty_id=faculty_id)
        await message.answer(UserDataResponses.get_confirm_faculty_text(faculty_name), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
        await state.set_state(UserDataStates.confirm_faculty)


@user_data_db_required_router.message(UserDataStates.confirm_faculty, ReenterData())
async def cancel(message: Message, state: FSMContext, db: Session):
    await state.update_data(faculty=None)
    await state.update_data(faculty_id=None)
    await message.answer(UserDataResponses.ASK_FOR_FACULTY, reply_markup=UserDataReplyKeyboard.generate_choose_faculty_keyboard(db))
    await state.set_state(UserDataStates.waiting_for_faculty)



# DONATION PLACE AND DATETIME HANDLING

@user_data_db_required_router.message(UserDataStates.confirm_bone_marrow_typing_agreement, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext, db: Session):
    state_data = await state.get_data()
    all_data_is_collected = state_data.get('all_data_is_collected')
    await message.answer(UserDataResponses.DATA_IS_WRITTEN, reply_markup=common.keyboards.remove_keyboard)
    if all_data_is_collected:
        await message.answer(UserDataResponses.get_recheck_data_text(generate_user_recheck_data_from_state_data(state_data)), reply_markup=UserDataInlineKeyboard.edit_data_keyboard)
        await state.set_state(UserDataStates.recheck_data)
    else:
        await message.answer(UserDataResponses.ASK_FOR_DONATION_PLACE, reply_markup=UserDataInlineKeyboard.get_choose_donation_place_keyboard(db))
        await state.set_state(UserDataStates.waiting_for_donation_place)


@user_data_db_required_router.callback_query(UserDataStates.waiting_for_donation_place, ChooseDonationPlaceCallback.filter())
async def process_donation_place(query: CallbackQuery, state: FSMContext, callback_data: ChooseDonationPlaceCallback):
    donation_place_id = callback_data.id
    donation_place = callback_data.name
    await state.update_data(donation_place_id=int(donation_place_id))
    await state.update_data(donation_place=donation_place)
    await query.message.answer(UserDataResponses.get_confirm_donation_place_text(donation_place), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
    await query.answer() 
    await query.message.edit_reply_markup(reply_markup=None)
    await state.set_state(UserDataStates.confirm_donation_place)


@user_data_db_required_router.message(UserDataStates.confirm_donation_place, ReenterData())
async def cancel(message: Message, state: FSMContext, db: Session):
    await state.update_data(donation_place_id=None)
    await state.update_data(donation_place=None)
    await message.answer(UserDataResponses.ENTER_NEW_DATA, reply_markup=common.keyboards.remove_keyboard)
    await message.answer(UserDataResponses.ASK_FOR_DONATION_PLACE, reply_markup=UserDataInlineKeyboard.get_choose_donation_place_keyboard(db))
    await state.set_state(UserDataStates.waiting_for_donation_place)


@user_data_db_required_router.message(UserDataStates.confirm_donation_place, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext, db: Session):
    state_data = await state.get_data()
    all_data_is_collected = state_data.get('all_data_is_collected')
    await message.answer(UserDataResponses.DATA_IS_WRITTEN, reply_markup=common.keyboards.remove_keyboard)
    if all_data_is_collected and state_data.get('donation_datetime') is not None:
        await message.answer(UserDataResponses.get_confirm_donation_datetime_text(state_data.get('donation_place'),state_data.get('donation_datetime')), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
        await state.set_state(UserDataStates.confirm_donation_datetime)
    else:
        donation_place_id = state_data.get('donation_place_id')
        await message.answer(UserDataResponses.ASK_FOR_DONATION_DATETIME, reply_markup=UserDataInlineKeyboard.get_choose_donation_datetime_keyboard(db, donation_place_id))
        await state.set_state(UserDataStates.waiting_for_donation_datetime)

@user_data_db_required_router.callback_query(UserDataStates.waiting_for_donation_datetime, ChooseDonationDatetimeCallback.filter())
async def process_donation_datetime(query: CallbackQuery, state: FSMContext, callback_data: ChooseDonationDatetimeCallback):
    donation_datetime_id = callback_data.id
    donation_datetime = callback_data.datetime
    await state.update_data(donation_datetime_id=int(donation_datetime_id))
    await state.update_data(donation_datetime=donation_datetime)

    state_data = await state.get_data()
    donation_place = state_data.get('donation_place')

    await query.message.answer(UserDataResponses.get_confirm_donation_datetime_text(donation_place, donation_datetime), reply_markup=UserDataReplyKeyboard.confrimation_place_and_datetme_keyboard)
    await query.answer() 
    await query.message.edit_reply_markup(reply_markup=None)
    await state.set_state(UserDataStates.confirm_donation_datetime)


@user_data_db_required_router.message(UserDataStates.confirm_donation_datetime, ReenterData())
async def cancel(message: Message, state: FSMContext, db: Session):
    await state.update_data(donation_datetime_id=None)
    await state.update_data(donation_datetime=None)
    state_data = await state.get_data()
    donation_place_id = state_data.get('donation_place_id')
    await message.answer(UserDataResponses.ENTER_NEW_DATA, reply_markup=common.keyboards.remove_keyboard)
    await message.answer(UserDataResponses.ASK_FOR_DONATION_DATETIME, reply_markup=UserDataInlineKeyboard.get_choose_donation_datetime_keyboard(db, donation_place_id))
    await state.set_state(UserDataStates.waiting_for_donation_datetime)


@user_data_db_required_router.message(UserDataStates.confirm_donation_datetime, ReenterPlaceAndDatetime())
async def cancel(message: Message, state: FSMContext, db: Session):
    await state.update_data(donation_place_id=None, donation_place = None, donation_datetime_id=None, donation_datetime=None)
    await message.answer(UserDataResponses.ENTER_NEW_DATA, reply_markup=common.keyboards.remove_keyboard)
    await message.answer(UserDataResponses.ASK_FOR_DONATION_PLACE, reply_markup=UserDataInlineKeyboard.get_choose_donation_place_keyboard(db), )
    await state.set_state(UserDataStates.waiting_for_donation_place)

