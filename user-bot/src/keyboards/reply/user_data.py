from aiogram.types import  ReplyKeyboardMarkup,  KeyboardButton
from expected_messages.user_data import UserDataExpectedMessages

from common.models import SexEnum, FoundingSourceEnum, BodyWeightEnum
from crud.user_data import db_get_faculties_names

from sqlalchemy.orm import Session

class UserDataReplyKeyboard:
    confirmation_keyboard =  ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=UserDataExpectedMessages.CONFIRM_ENTERED_DATA),
            KeyboardButton(text=UserDataExpectedMessages.REENTER_DATA)],
        ],
        one_time_keyboard = True,
        resize_keyboard=True
    )

    i_have_no_inn_keyboard =  ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=UserDataExpectedMessages.I_HAVE_NO_INN)],
        ],
        one_time_keyboard = True
    )

    i_have_no_snils_keyboard =  ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=UserDataExpectedMessages.I_HAVE_NO_SNILS)],
        ],
        one_time_keyboard = True
    )

    choose_budget_or_contract_keyboard =  ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=UserDataExpectedMessages.BUDGET_FOUNDING_SOURCE),
            KeyboardButton(text=UserDataExpectedMessages.CONTRACT_FOUNDING_SOURCE)],
        ],
        one_time_keyboard = True,
        resize_keyboard=True
    )

    choose_is_polytech_student_keyboard =  ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=UserDataExpectedMessages.YES_IS_POLYTECH_STUDENT),
            KeyboardButton(text=UserDataExpectedMessages.NO_IS_POLYTECH_STUDENT)],
        ],
        one_time_keyboard = True,
        resize_keyboard=True
    )

    i_have_no_patronymic_keyboard =  ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=UserDataExpectedMessages.I_HAVE_NO_PATRONYMIC)],
        ],
        one_time_keyboard = True,
        resize_keyboard=True
    )

    i_dont_remember_my_grade_book_number_keyboard =  ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=UserDataExpectedMessages.I_DONT_REMEMBER_MY_GRADE_BOOK_NUMBER)],
        ],
        one_time_keyboard = True,
        resize_keyboard=True
    )

    choose_bone_marrow_typing_agreement_keyboard =  ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=UserDataExpectedMessages.I_AGREE_FOR_BONE_MARROW_TYPING)],
            [KeyboardButton(text=UserDataExpectedMessages.I_DECLINE_FOR_BONE_MARROW_TYPING)],
        ],
        one_time_keyboard = True,
        resize_keyboard=True
    )


    @staticmethod
    def generate_choose_sex_keyboard() -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text=SexEnum.male.value),
                KeyboardButton(text=SexEnum.female.value)]
            ],
            one_time_keyboard = True,
            resize_keyboard=True
    )

    @staticmethod
    def generate_choose_body_weight_keyboard() -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text=BodyWeightEnum.more_then_58_kg.value),
                KeyboardButton(text=BodyWeightEnum.between_50_and_58_kg.value)],
                [KeyboardButton(text=BodyWeightEnum.less_then_50_kg.value)]
            ],
            one_time_keyboard = True,
            resize_keyboard=True
    )

    @staticmethod
    def generate_choose_founding_source_keyboard() -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text=FoundingSourceEnum.budget.value),
                KeyboardButton(text=FoundingSourceEnum.contract.value)]
            ],
            one_time_keyboard = True,
            resize_keyboard=True
    )

    @staticmethod
    def generate_choose_faculty_keyboard(db: Session) -> ReplyKeyboardMarkup:
        faculty_names = [faculty.name for faculty in db_get_faculties_names(db)] 

        keyboard_buttons = []
        for i in range(0, len(faculty_names) - 1, 2):
            keyboard_buttons.append([
                KeyboardButton(text=faculty_names[i]),
                KeyboardButton(text=faculty_names[i + 1])
                ]
            )

        if len(faculty_names) % 2 != 0:
            keyboard_buttons.append([KeyboardButton(text=faculty_names[-1])])
        
        return ReplyKeyboardMarkup(keyboard=keyboard_buttons, 
                                   resize_keyboard=True,
                                   one_time_keyboard = True
                                   )

    confrimation_place_and_datetme_keyboard  =  ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=UserDataExpectedMessages.CONFIRM_ENTERED_DATA),
            KeyboardButton(text=UserDataExpectedMessages.REENTER_DATA)],
            [KeyboardButton(text=UserDataExpectedMessages.REENTER_PLACE_AND_DATETIME)]
        ],
        one_time_keyboard = True,
        resize_keyboard=True
    )