from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from common.middleware import DatabaseMiddleware


from states.new_volunteer import NewVolunteerStates
from keyboards.reply.new_volunteer import NewVolunteerKeyboard
from responses.new_volunteer import NewVolunteerResponses
from expected_messages.new_volunteer import NewVolunteerExpectedMessages

import common.keyboards
from common.states import IdleStates

new_volunteer_router = Router()

new_volunteer_router.message.middleware(DatabaseMiddleware())


@new_volunteer_router.message(F.text == NewVolunteerExpectedMessages.ASSIGN_VOLUNTEER)
@new_volunteer_router.message(Command("new_volunteer"))
async def assign_volunteer(message: Message, state: FSMContext):
    await message.answer(NewVolunteerResponses.ASK_FOR_FORWARDED_MESSAGE, reply_markup=common.keyboards.cancel_keyboard)
    await state.set_state(NewVolunteerStates.waiting_for_message)


@new_volunteer_router.message(NewVolunteerStates.confirm_volunteer, F.text == NewVolunteerExpectedMessages.CANCEL)
@new_volunteer_router.message(NewVolunteerStates.waiting_for_message, F.text == NewVolunteerExpectedMessages.CANCEL)
async def process_forwarded_message(message: Message, state: FSMContext):
    await message.answer(NewVolunteerResponses.OPERATION_CANCELED, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(IdleStates.idle)


@new_volunteer_router.message(NewVolunteerStates.waiting_for_message)
async def process_forwarded_message(message: Message, state: FSMContext):
    if message.forward_from:
        if message.forward_from.is_bot:
            await message.answer(NewVolunteerResponses.PLEASE_FORWARD_NOT_FROM_BOT)
        else:
            await message.answer(NewVolunteerResponses.get_confirm_text(message), reply_markup=NewVolunteerKeyboard.confirm_volunteer_keyboard)
            await state.set_state(NewVolunteerStates.confirm_volunteer)
    else:
        await message.answer(NewVolunteerResponses.CANT_DETECT_FORWARDED_MESSAGE)


@new_volunteer_router.message(NewVolunteerStates.confirm_volunteer, F.text == NewVolunteerExpectedMessages.CONFIRM_ASSIGN)
async def confirm_volunteer(message: Message, state: FSMContext, db):
    await message.answer(NewVolunteerResponses.VOLUNTEER_ASSIGNED, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(IdleStates.idle)


@new_volunteer_router.message(NewVolunteerStates.confirm_volunteer, F.text == NewVolunteerExpectedMessages.CHOOSE_ANOTHER_USER)
async def confirm_volunteer(message: Message, state: FSMContext, db):
    await message.answer(NewVolunteerResponses.ASK_FOR_FORWARDED_MESSAGE, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(NewVolunteerStates.waiting_for_message)