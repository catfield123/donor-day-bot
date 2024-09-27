from aiogram.types import  ReplyKeyboardMarkup,  KeyboardButton
from expected_messages.new_volunteer import NewVolunteerExpectedMessages

class NewVolunteerKeyboard:
    confirm_volunteer_keyboard =  ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text=NewVolunteerExpectedMessages.CONFIRM_ASSIGN)],
                [KeyboardButton(text=NewVolunteerExpectedMessages.CHOOSE_ANOTHER_USER)],
                [KeyboardButton(text=NewVolunteerExpectedMessages.CANCEL)],
            ],
            resize_keyboard=True
        )
        