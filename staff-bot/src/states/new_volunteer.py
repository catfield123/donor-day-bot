from aiogram.fsm.state import State, StatesGroup

class NewVolunteerStates(StatesGroup):
    waiting_for_message = State()
    confirm_volunteer = State()