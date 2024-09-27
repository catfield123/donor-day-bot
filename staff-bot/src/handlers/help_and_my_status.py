from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from states.new_volunteer import NewVolunteerStates
from common.middleware import DatabaseMiddleware


from keyboards.reply.new_volunteer import NewVolunteerKeyboard
from responses.new_volunteer import NewVolunteerResponses
from expected_messages.new_volunteer import NewVolunteerExpectedMessages

from common.states import IdleStates

help_and_status_router = Router()

@help_and_status_router.message(IdleStates.idle, Command("help"))
async def show_help_message(message: Message, state: FSMContext):
    await message.answer("хелпа")

@help_and_status_router.message(IdleStates.idle, Command("my_status"))
async def show_my_status(message: Message, state: FSMContext):
    await message.answer("твой статус: волонтёр")