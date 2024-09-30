from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from expected_messages.user_data import UserDataExpectedMessages

from sqlalchemy.orm import Session
from crud.user_data import db_get_donation_datetimes, db_get_donation_places

from callbacks import ChooseDonationDatetimeCallback, ChooseDonationPlaceCallback

class UserDataInlineKeyboard:
    edit_data_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=UserDataExpectedMessages.ALL_DATA_IS_CORRECT, callback_data='all_data_is_correct')],
            
            [
                InlineKeyboardButton(text=UserDataExpectedMessages.EDIT_FULL_NAME, callback_data='edit_full_name'),
                InlineKeyboardButton(text=UserDataExpectedMessages.EDIT_PHONE_NUMBER, callback_data='edit_phone_number')
            ],
            [
                InlineKeyboardButton(text=UserDataExpectedMessages.EDIT_EMAIL, callback_data='edit_email'),
                InlineKeyboardButton(text=UserDataExpectedMessages.EDIT_STUDYING_PLACE_INFO, callback_data='edit_studying_place_info')
            ],
            [
                InlineKeyboardButton(text=UserDataExpectedMessages.EDIT_INN, callback_data='edit_inn'),
                InlineKeyboardButton(text=UserDataExpectedMessages.EDIT_SNILS, callback_data='edit_snils')
            ],
            [
                InlineKeyboardButton(text=UserDataExpectedMessages.EDIT_PASSPORT_DATA, callback_data='edit_passport_data'),
                InlineKeyboardButton(text=UserDataExpectedMessages.EDIT_SEX_DATA, callback_data='edit_sex_data')
            ],
            [
                InlineKeyboardButton(text=UserDataExpectedMessages.EDIT_WEIGHT_DATA, callback_data='edit_weight_data'),
                InlineKeyboardButton(text=UserDataExpectedMessages.EDIT_BONE_MARROW_TYPING_AGREEMENT_DATA, callback_data='edit_bone_marrow_typing_agreement_data')
            ],
            [
                InlineKeyboardButton(text=UserDataExpectedMessages.EDIT_DONATION_PLACE_AND_DATETIME, callback_data='edit_donation_place_and_datetime'),
            ]
        ]
    )


    @staticmethod
    def get_choose_donation_place_keyboard(db: Session) -> InlineKeyboardMarkup:
        donation_places = db_get_donation_places(db)

        keyboard_buttons = []
        for donation_place in donation_places:
            keyboard_buttons.append([InlineKeyboardButton(text=donation_place.name, 
                                                            callback_data=ChooseDonationPlaceCallback(
                                                                id=f"{donation_place.id}",
                                                                name=donation_place.name
                                                                ).pack()
                                                        )   
            ])
        
        return InlineKeyboardMarkup(
                inline_keyboard=keyboard_buttons
            )
    

    @staticmethod
    def get_choose_donation_datetime_keyboard(db: Session, donation_place_id: int) -> InlineKeyboardMarkup:
        donation_datetimes = db_get_donation_datetimes(db, donation_place_id)

        keyboard_buttons = []
        for donation_datetime in donation_datetimes:
            keyboard_buttons.append([InlineKeyboardButton(text=donation_datetime.datetime, 
                                                            callback_data=ChooseDonationDatetimeCallback(
                                                                id=f"{donation_datetime.id}",
                                                                place_id=f"{donation_datetime.place_id}",
                                                                datetime=donation_datetime.datetime
                                                                ).pack()
                                                        )   
            ])
        
        return InlineKeyboardMarkup(
                inline_keyboard=keyboard_buttons
            )

    