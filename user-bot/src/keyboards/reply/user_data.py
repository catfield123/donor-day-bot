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
        ]
    )

    i_have_no_inn_keyboard =  ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=UserDataExpectedMessages.I_HAVE_NO_INN)],
        ]
    )

    i_have_no_snils_keyboard =  ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=UserDataExpectedMessages.I_HAVE_NO_SNILS)],
        ]
    )

    choose_budget_or_contract_keyboard =  ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=UserDataExpectedMessages.BUDGET_FOUNDING_SOURCE),
            KeyboardButton(text=UserDataExpectedMessages.CONTRACT_FOUNDING_SOURCE)],
        ],
        resize_keyboard=True
    )

    choose_is_polytech_student_keyboard =  ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=UserDataExpectedMessages.YES_IS_POLYTECH_STUDENT),
            KeyboardButton(text=UserDataExpectedMessages.NO_IS_POLYTECH_STUDENT)],
        ],
        resize_keyboard=True
    )

    i_have_no_patronymic_keyboard =  ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=UserDataExpectedMessages.I_HAVE_NO_PATRONYMIC)],
        ],
        resize_keyboard=True
    )

    i_dont_remember_my_grade_book_number_keyboard =  ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=UserDataExpectedMessages.I_DONT_REMEMBER_MY_GRADE_BOOK_NUMBER)],
        ],
        resize_keyboard=True
    )

    choose_bone_marrow_typing_agreement_keyboard =  ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=UserDataExpectedMessages.I_AGREE_FOR_BONE_MARROW_TYPING)],
            [KeyboardButton(text=UserDataExpectedMessages.I_DECLINE_FOR_BONE_MARROW_TYPING)],
        ],
        resize_keyboard=True
    )


    @staticmethod
    def generate_choose_sex_keyboard() -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text=SexEnum.male.value),
                KeyboardButton(text=SexEnum.female.value)]
            ],
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
            resize_keyboard=True
    )

    @staticmethod
    def generate_choose_founding_source_keyboard() -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text=FoundingSourceEnum.budget.value),
                KeyboardButton(text=FoundingSourceEnum.contract.value)]
            ],
            resize_keyboard=True
    )

    @staticmethod
    def generate_choose_faculty_keyboard() -> ReplyKeyboardMarkup:
        faculty_names = db_get_faculties_names()
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        for i in range(0, len(faculty_names) - 1, 2):
            keyboard.add(
                KeyboardButton(text=faculty_names[i]),
                KeyboardButton(text=faculty_names[i + 1])
            )
        if len(faculty_names) % 2 != 0:
            keyboard.add(KeyboardButton(text=faculty_names[-1]))
        return keyboard

