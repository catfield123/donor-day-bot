from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from common.middleware import DatabaseMiddleware


from states.user_data import UserDataStates
import keyboards
from responses.user_data import UserDataResponses
from expected_messages.user_data import UserDataExpectedMessages


import common.keyboards
from common.states import IdleStates

user_data_db_required_router = Router()

user_data_db_required_router.message.middleware(DatabaseMiddleware())


# @user_data_db_required_router.message(UserDataStates.recheck_data, Command("confirm"))
# async def confirm_everything(message: Message, state: FSMContext):
#     await message.answer(NewVolunteerResponses.ASK_FOR_FORWARDED_MESSAGE, reply_markup=common.keyboards.cancel_keyboard)
#     await state.set_state(NewVolunteerStates.waiting_for_message)


# @user_data_db_required_router.message(NewVolunteerStates.confirm_volunteer, F.text == NewVolunteerExpectedMessages.CANCEL)
# @user_data_db_required_router.message(NewVolunteerStates.waiting_for_message, F.text == NewVolunteerExpectedMessages.CANCEL)
# async def cancel(message: Message, state: FSMContext):
#     await message.answer(NewVolunteerResponses.OPERATION_CANCELED, reply_markup=common.keyboards.remove_keyboard)
#     await state.set_state(IdleStates.idle)


# @user_data_db_required_router.message(NewVolunteerStates.waiting_for_message)
# async def process_forwarded_message(message: Message, state: FSMContext):
#     if message.forward_from:
#         if message.forward_from.is_bot:
#             await message.answer(NewVolunteerResponses.PLEASE_FORWARD_NOT_FROM_BOT)
#         else:
#             await state.update_data(forwarded_from_user_id=message.forward_from.id)
#             await message.answer(NewVolunteerResponses.get_confirm_text(message), reply_markup=NewVolunteerKeyboard.confirm_volunteer_keyboard)
#             await state.set_state(NewVolunteerStates.confirm_volunteer)
#     else:
#         await message.answer(NewVolunteerResponses.CANT_DETECT_FORWARDED_MESSAGE)


# @user_data_db_required_router.message(NewVolunteerStates.confirm_volunteer, F.text == NewVolunteerExpectedMessages.CONFIRM_ASSIGN)
# async def confirm_volunteer_assigment(message: Message, state: FSMContext, db):
#     state_data = await state.get_data()
#     forwarded_from_user_id = state_data.get("forwarded_from_user_id")
#     try:
#         create_new_volunteer(db, NewVolunteerRequestSchema(telegram_id=message.from_user.id, 
#                                                      granted_by_telegram_id=forwarded_from_user_id))
#         await message.answer(NewVolunteerResponses.VOLUNTEER_ASSIGNED, reply_markup=common.keyboards.remove_keyboard)
#     except VolunteerAlreadyExists:
#         await message.answer(NewVolunteerResponses.VOLUNTEER_ALREADY_ASSIGNED, reply_markup=common.keyboards.remove_keyboard)
#     finally:
#         await state.update_data(forwarded_from_user_id=None)
#         await state.set_state(IdleStates.idle)


# @user_data_db_required_router.message(NewVolunteerStates.confirm_volunteer, F.text == NewVolunteerExpectedMessages.CHOOSE_ANOTHER_USER)
# async def choose_another_donor(message: Message, state: FSMContext, db):
#     await message.answer(NewVolunteerResponses.ASK_FOR_FORWARDED_MESSAGE, reply_markup=common.keyboards.remove_keyboard)
#     await state.set_state(NewVolunteerStates.waiting_for_message)