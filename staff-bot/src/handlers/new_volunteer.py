from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from states.new_volunteer_states import NewVolunteerStates
from common.middleware import DatabaseMiddleware

new_volunteer_router = Router()

new_volunteer_router.message.middleware(DatabaseMiddleware())


@new_volunteer_router.message(Command("new_volunteer"))
async def assign_volunteer(message: Message, state: FSMContext):
    await message.answer("Перешлите сообщение пользователя, которого хотите назначить волонтёром.")
    await state.set_state(NewVolunteerStates.waiting_for_message)

@new_volunteer_router.message(NewVolunteerStates.waiting_for_message)
async def process_forwarded_message(message: Message, state: FSMContext):
    print(message)
    if message.forward_from:
        await message.answer(f"Назначить {message.forward_from.full_name} волонтёром? Введите `да` если да.")
        await state.set_state(NewVolunteerStates.confirm_volunteer)
    else:
        await message.answer("Не удаётся обнаружить переслоннаое сообщение от пользователя. Повторите попытку.")

@new_volunteer_router.message(NewVolunteerStates.confirm_volunteer)
async def confirm_volunteer(message: Message, state: FSMContext, db):
    if message.text.lower() == "да":
        await message.answer("Волонтёр назначен.")
    else:   
        await message.answer("Волонтёр не назначен.")
    await state.clear()