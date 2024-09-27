from aiogram.types import  ReplyKeyboardMarkup,  KeyboardButton
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove

cancel_keyboard =  ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Отмена")],
        ],
        resize_keyboard=True
    )

remove_keyboard =  ReplyKeyboardRemove()