from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from common.middleware import DatabaseMiddleware


from states.new_volunteer import NewVolunteerStates
from keyboards.reply.new_volunteer import NewVolunteerKeyboard
from responses.new_volunteer import NewVolunteerResponses
from expected_messages.new_volunteer import NewVolunteerExpectedMessages
from crud.new_volunteer import create_new_volunteer
from exceptions.new_volunteer import VolunteerAlreadyExists

from middleware import IsAdminMiddleware

from schemas import NewVolunteerRequestSchema

import common.keyboards
from common.states import IdleStates

new_volunteer_router = Router()

new_volunteer_router.message.middleware(DatabaseMiddleware())
new_volunteer_router.message.middleware(IsAdminMiddleware())


@new_volunteer_router.message(IdleStates.idle, F.text == NewVolunteerExpectedMessages.ASSIGN_VOLUNTEER)
@new_volunteer_router.message(IdleStates.idle, Command("new_volunteer"))
async def start_volunteer_assignment(message: Message, state: FSMContext):
    await message.answer(NewVolunteerResponses.ASK_FOR_FORWARDED_MESSAGE, reply_markup=common.keyboards.cancel_keyboard)
    await state.set_state(NewVolunteerStates.waiting_for_message)


@new_volunteer_router.message(NewVolunteerStates.confirm_volunteer, F.text == NewVolunteerExpectedMessages.CANCEL)
@new_volunteer_router.message(NewVolunteerStates.waiting_for_message, F.text == NewVolunteerExpectedMessages.CANCEL)
async def cancel(message: Message, state: FSMContext):
    await message.answer(NewVolunteerResponses.OPERATION_CANCELED, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(IdleStates.idle)


@new_volunteer_router.message(NewVolunteerStates.waiting_for_message)
async def process_forwarded_message(message: Message, state: FSMContext):
    if message.forward_from:
        if message.forward_from.is_bot:
            await message.answer(NewVolunteerResponses.PLEASE_FORWARD_NOT_FROM_BOT)
        else:
            await state.update_data(forwarded_from_user_id=message.forward_from.id)
            await message.answer(NewVolunteerResponses.get_confirm_text(message), reply_markup=NewVolunteerKeyboard.confirm_volunteer_keyboard)
            await state.set_state(NewVolunteerStates.confirm_volunteer)
    else:
        await message.answer(NewVolunteerResponses.CANT_DETECT_FORWARDED_MESSAGE)


@new_volunteer_router.message(NewVolunteerStates.confirm_volunteer, F.text == NewVolunteerExpectedMessages.CONFIRM_ASSIGN)
async def confirm_volunteer_assigment(message: Message, state: FSMContext, db):
    state_data = await state.get_data()
    forwarded_from_user_id = state_data.get("forwarded_from_user_id")
    try:
        create_new_volunteer(db, NewVolunteerRequestSchema(telegram_id=message.from_user.id, 
                                                     granted_by_telegram_id=forwarded_from_user_id))
        await message.answer(NewVolunteerResponses.VOLUNTEER_ASSIGNED, reply_markup=common.keyboards.remove_keyboard)
    except VolunteerAlreadyExists:
        await message.answer(NewVolunteerResponses.VOLUNTEER_ALREADY_ASSIGNED, reply_markup=common.keyboards.remove_keyboard)
    finally:
        await state.update_data(forwarded_from_user_id=None)
        await state.set_state(IdleStates.idle)


@new_volunteer_router.message(NewVolunteerStates.confirm_volunteer, F.text == NewVolunteerExpectedMessages.CHOOSE_ANOTHER_USER)
async def choose_another_donor(message: Message, state: FSMContext, db):
    await message.answer(NewVolunteerResponses.ASK_FOR_FORWARDED_MESSAGE, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(NewVolunteerStates.waiting_for_message)