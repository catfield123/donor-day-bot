from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from common.middleware import DatabaseMiddleware


from keyboards.reply.user_data import UserDataReplyKeyboard
from keyboards.inline.user_data import UserDataInlineKeyboard
from states.user_data import UserDataStates
import keyboards
from responses.user_data import UserDataResponses
from expected_messages.user_data import UserDataExpectedMessages

from filters import ReenterData, ConfirmEnteredData, AllowedAnswers


import common.keyboards
from common.states import IdleStates

user_data_router = Router()

from handlers.database_required.user_data import user_data_db_required_router
user_data_router.include_router(user_data_db_required_router)


@user_data_router.message(IdleStates.idle, F.text == UserDataExpectedMessages.ENTER_DATA)
@user_data_router.message(IdleStates.idle, Command('enter_data'))
async def start_entering_data(message: Message, state: FSMContext):
    await message.answer(UserDataResponses.ASK_FOR_NAME, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_name)


@user_data_router.message(UserDataStates.waiting_for_name)
async def process_name(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(name=message.text)
    await message.answer(UserDataResponses.get_confirm_name_text(name), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
    await state.set_state(UserDataStates.confirm_name)


@user_data_router.message(UserDataStates.confirm_name, ReenterData())
async def cancel(message: Message, state: FSMContext):
    await state.update_data(name=None)
    await message.answer(UserDataResponses.ASK_FOR_NAME, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_name)


@user_data_router.message(UserDataStates.confirm_name, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext):
    await message.answer(UserDataResponses.ASK_FOR_SURNAME, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_surname)


@user_data_router.message(UserDataStates.waiting_for_surname)
async def process_surname(message: Message, state: FSMContext):
    surname = message.text
    await state.update_data(surname=message.text)
    await message.answer(UserDataResponses.get_confirm_surname_text(surname), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
    await state.set_state(UserDataStates.confirm_surname)


@user_data_router.message(UserDataStates.confirm_surname, ReenterData())
async def cancel(message: Message, state: FSMContext):
    await state.update_data(surname=None)
    await message.answer(UserDataResponses.ASK_FOR_SURNAME, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_surname)


@user_data_router.message(UserDataStates.confirm_surname, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext):
    await message.answer(UserDataResponses.ASK_FOR_PATRONIMYC, reply_markup=UserDataReplyKeyboard.i_have_no_patronymic_keyboard)
    await state.set_state(UserDataStates.waiting_for_patronymic)


@user_data_router.message(UserDataStates.waiting_for_patronymic)
async def process_patronymic(message: Message, state: FSMContext):
    patronymic = message.text
    await state.update_data(patronymic=message.text)
    await message.answer(UserDataResponses.get_confirm_patronymic_text(patronymic), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
    await state.set_state(UserDataStates.confirm_patronymic)


@user_data_router.message(UserDataStates.confirm_patronymic, ReenterData())
async def cancel(message: Message, state: FSMContext):
    await state.update_data(patronymic=None)
    await message.answer(UserDataResponses.ASK_FOR_PATRONIMYC, reply_markup=UserDataReplyKeyboard.i_have_no_patronymic_keyboard)
    await state.set_state(UserDataStates.waiting_for_patronymic)


@user_data_router.message(UserDataStates.confirm_patronymic, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext):
    await message.answer(UserDataResponses.ASK_FOR_SEX, reply_markup=UserDataReplyKeyboard.generate_choose_sex_keyboard())
    await state.set_state(UserDataStates.waiting_for_sex)


@user_data_router.message(UserDataStates.waiting_for_sex, AllowedAnswers(UserDataExpectedMessages.SEX_EXPECTED_MESSAGES))
async def process_sex(message: Message, state: FSMContext):
    sex = message.text
    await state.update_data(sex=message.text)
    await message.answer(UserDataResponses.get_confirm_sex_text(sex), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
    await state.set_state(UserDataStates.confirm_sex)


@user_data_router.message(UserDataStates.confirm_sex, ReenterData())
async def cancel(message: Message, state: FSMContext):
    await state.update_data(sex=None)
    await message.answer(UserDataResponses.ASK_FOR_SEX, UserDataReplyKeyboard.generate_choose_sex_keyboard())
    await state.set_state(UserDataStates.waiting_for_sex)


@user_data_router.message(UserDataStates.confirm_sex, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext):
    await message.answer(UserDataResponses.ASK_FOR_PHONE_NUMBER, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_phone_number)



@user_data_router.message(UserDataStates.waiting_for_phone_number)
async def process_phone_number(message: Message, state: FSMContext):
    phone_number = message.text
    await state.update_data(phone_number=message.text)
    await message.answer(UserDataResponses.get_confirm_phone_number_text(phone_number), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
    await state.set_state(UserDataStates.confirm_phone_number)


@user_data_router.message(UserDataStates.confirm_phone_number, ReenterData())
async def cancel(message: Message, state: FSMContext):
    await state.update_data(phone_number=None)
    await message.answer(UserDataResponses.ASK_FOR_PHONE_NUMBER, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_phone_number)


@user_data_router.message(UserDataStates.confirm_phone_number, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext):
    await message.answer(UserDataResponses.ASK_FOR_EMAIL, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_email)


@user_data_router.message(UserDataStates.waiting_for_email)
async def process_email(message: Message, state: FSMContext):
    email = message.text
    await state.update_data(email=message.text)
    await message.answer(UserDataResponses.get_confirm_email_text(email), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
    await state.set_state(UserDataStates.confirm_email)


@user_data_router.message(UserDataStates.confirm_email, ReenterData())
async def cancel(message: Message, state: FSMContext):
    await state.update_data(email=None)
    await message.answer(UserDataResponses.ASK_FOR_EMAIL, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_email)


@user_data_router.message(UserDataStates.confirm_email, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext):
    await message.answer(UserDataResponses.ASK_FOR_IS_POLYTECH_STUDENT, reply_markup=UserDataReplyKeyboard.choose_is_polytech_student_keyboard)
    await state.set_state(UserDataStates.waiting_for_is_polytech_student)


@user_data_router.message(UserDataStates.waiting_for_is_polytech_student, AllowedAnswers(UserDataExpectedMessages.POLYTECH_STUDENT_EXPECTED_MESSAGES))
async def process_is_polytech_student(message: Message, state: FSMContext):
    is_polytech_student = True if message.text == UserDataExpectedMessages.YES_IS_POLYTECH_STUDENT else False
    await state.update_data(is_polytech_student=is_polytech_student)
    await message.answer(UserDataResponses.get_confirm_is_polytech_student_text(is_polytech_student), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
    await state.set_state(UserDataStates.confirm_is_polytech_student)


@user_data_router.message(UserDataStates.confirm_is_polytech_student, ReenterData())
async def cancel(message: Message, state: FSMContext):
    await state.update_data(is_polytech_student=None)
    await message.answer(UserDataResponses.ASK_FOR_IS_POLYTECH_STUDENT, reply_markup=UserDataReplyKeyboard.choose_is_polytech_student_keyboard)
    await state.set_state(UserDataStates.waiting_for_is_polytech_student)


@user_data_router.message(UserDataStates.confirm_is_polytech_student, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext):
    state_data = await state.get_data()
    is_polytech_student = state_data.get("is_polytech_student")
    if is_polytech_student:
        await message.answer(UserDataResponses.ASK_FOR_GRADE_BOOK_NUMBER, reply_markup=UserDataReplyKeyboard.i_dont_remember_my_grade_book_number_keyboard)
        await state.set_state(UserDataStates.waiting_for_grade_book_number)
    else:
        await message.answer(UserDataResponses.ASK_FOR_INN, reply_markup=UserDataReplyKeyboard.i_have_no_inn_keyboard)
        await state.set_state(UserDataStates.waiting_for_inn)



@user_data_router.message(UserDataStates.waiting_for_grade_book_number)
async def process_grade_book_number(message: Message, state: FSMContext):
    grade_book_number = message.text
    if grade_book_number == UserDataExpectedMessages.I_DONT_REMEMBER_MY_GRADE_BOOK_NUMBER:
        grade_book_number = None
    await state.update_data(grade_book_number=grade_book_number)
    await message.answer(UserDataResponses.get_confirm_grade_book_number_text(grade_book_number), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
    await state.set_state(UserDataStates.confirm_grade_book_number)


@user_data_router.message(UserDataStates.confirm_grade_book_number, ReenterData())
async def cancel(message: Message, state: FSMContext):
    await state.update_data(grade_book_number=None)
    await message.answer(UserDataResponses.ASK_FOR_GRADE_BOOK_NUMBER, reply_markup=UserDataReplyKeyboard.i_dont_remember_my_grade_book_number_keyboard)
    await state.set_state(UserDataStates.waiting_for_grade_book_number)


@user_data_router.message(UserDataStates.confirm_grade_book_number, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext):
    await message.answer(UserDataResponses.ASK_FOR_GROUP_NUMBER, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_group_number)


@user_data_router.message(UserDataStates.waiting_for_group_number)
async def process_group_number(message: Message, state: FSMContext):
    group_number = message.text
    await state.update_data(group_number=message.text)
    await message.answer(UserDataResponses.get_confirm_group_number_text(group_number), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
    await state.set_state(UserDataStates.confirm_group_number)


@user_data_router.message(UserDataStates.confirm_group_number, ReenterData())
async def cancel(message: Message, state: FSMContext):
    await state.update_data(group_number=None)
    await message.answer(UserDataResponses.ASK_FOR_GROUP_NUMBER, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_group_number)


# ASKING FOR FACULTY REQUIRES DATABASE
# FACULTY HANDLERS ARE IN database_required/user_data.py

@user_data_router.message(UserDataStates.confirm_faculty, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext):
    await message.answer(UserDataResponses.ASK_FOR_FOUNDING_SOURCE, reply_markup=UserDataReplyKeyboard.generate_choose_founding_source_keyboard())
    await state.set_state(UserDataStates.waiting_for_founding_source)


@user_data_router.message(UserDataStates.waiting_for_founding_source, AllowedAnswers(UserDataExpectedMessages.FOUNDING_SOURCE_EXPECTED_MESSAGES))
async def process_founding_source(message: Message, state: FSMContext):
    founding_source = message.text
    await state.update_data(founding_source=message.text)
    await message.answer(UserDataResponses.get_confirm_founding_source_text(founding_source), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
    await state.set_state(UserDataStates.confirm_founding_source)


@user_data_router.message(UserDataStates.confirm_founding_source, ReenterData())
async def cancel(message: Message, state: FSMContext):
    await state.update_data(founding_source=None)
    await message.answer(UserDataResponses.ASK_FOR_FOUNDING_SOURCE, reply_markup=UserDataReplyKeyboard.generate_choose_founding_source_keyboard())
    await state.set_state(UserDataStates.waiting_for_founding_source)


@user_data_router.message(UserDataStates.confirm_founding_source, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext):
    await message.answer(UserDataResponses.ASK_FOR_INN, reply_markup=UserDataReplyKeyboard.i_have_no_inn_keyboard)
    await state.set_state(UserDataStates.waiting_for_inn)


@user_data_router.message(UserDataStates.waiting_for_inn)
async def process_inn(message: Message, state: FSMContext):
    inn = message.text
    if inn == UserDataExpectedMessages.I_HAVE_NO_INN:
        inn = None
    await state.update_data(inn=message.text)
    await message.answer(UserDataResponses.get_confirm_inn_text(inn), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
    await state.set_state(UserDataStates.confirm_inn)


@user_data_router.message(UserDataStates.confirm_inn, ReenterData())
async def cancel(message: Message, state: FSMContext):
    await state.update_data(inn=None)
    await message.answer(UserDataResponses.ASK_FOR_INN, reply_markup=UserDataReplyKeyboard.i_have_no_inn_keyboard)
    await state.set_state(UserDataStates.waiting_for_inn)


@user_data_router.message(UserDataStates.confirm_inn, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext):
    await message.answer(UserDataResponses.ASK_FOR_SNILS, reply_markup=UserDataReplyKeyboard.i_have_no_snils_keyboard)
    await state.set_state(UserDataStates.waiting_for_snils)


@user_data_router.message(UserDataStates.waiting_for_snils)
async def process_snils(message: Message, state: FSMContext):
    snils = message.text
    if snils == UserDataExpectedMessages.I_HAVE_NO_SNILS:
        snils = None
    await state.update_data(snils=message.text)
    await message.answer(UserDataResponses.get_confirm_snils_text(snils), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
    await state.set_state(UserDataStates.confirm_snils)


@user_data_router.message(UserDataStates.confirm_snils, ReenterData())
async def cancel(message: Message, state: FSMContext):
    await state.update_data(snils=None)
    await message.answer(UserDataResponses.ASK_FOR_SNILS, reply_markup=UserDataReplyKeyboard.i_have_no_snils_keyboard)
    await state.set_state(UserDataStates.waiting_for_snils)


@user_data_router.message(UserDataStates.confirm_snils, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext):
    await message.answer(UserDataResponses.ASK_FOR_PASSPORT_SERIES, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_passport_series)


@user_data_router.message(UserDataStates.waiting_for_passport_series)
async def process_passport_series(message: Message, state: FSMContext):
    passport_series = message.text
    await state.update_data(passport_series=message.text)
    await message.answer(UserDataResponses.get_confirm_passport_series_text(passport_series), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
    await state.set_state(UserDataStates.confirm_passport_series)


@user_data_router.message(UserDataStates.confirm_passport_series, ReenterData())
async def cancel(message: Message, state: FSMContext):
    await state.update_data(passport_series=None)
    await message.answer(UserDataResponses.ASK_FOR_PASSPORT_SERIES, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_passport_series)


@user_data_router.message(UserDataStates.confirm_passport_series, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext):
    await message.answer(UserDataResponses.ASK_FOR_PASSPORT_NUMBER, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_passport_number)


@user_data_router.message(UserDataStates.waiting_for_passport_number)
async def process_passport_number(message: Message, state: FSMContext):
    passport_number = message.text
    await state.update_data(passport_number=message.text)
    await message.answer(UserDataResponses.get_confirm_passport_number_text(passport_number), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
    await state.set_state(UserDataStates.confirm_passport_number)


@user_data_router.message(UserDataStates.confirm_passport_number, ReenterData())
async def cancel(message: Message, state: FSMContext):
    await state.update_data(passport_number=None)
    await message.answer(UserDataResponses.ASK_FOR_PASSPORT_NUMBER, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_passport_number)


@user_data_router.message(UserDataStates.confirm_passport_number, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext):
    await message.answer(UserDataResponses.ASK_FOR_PASSPORT_ISSUED_BY, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_passport_issued_by)


@user_data_router.message(UserDataStates.waiting_for_passport_issued_by)
async def process_passport_date(message: Message, state: FSMContext):
    passport_issued_by = message.text
    await state.update_data(passport_issued_by=message.text)
    await message.answer(UserDataResponses.get_confirm_passport_issued_by_text(passport_issued_by), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
    await state.set_state(UserDataStates.confirm_passport_issued_by)


@user_data_router.message(UserDataStates.confirm_passport_issued_by, ReenterData())
async def cancel(message: Message, state: FSMContext):
    await state.update_data(passport_issued_by=None)
    await message.answer(UserDataResponses.ASK_FOR_PASSPORT_ISSUED_BY, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_passport_issued_by)


@user_data_router.message(UserDataStates.confirm_passport_issued_by, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext):
    await message.answer(UserDataResponses.ASK_FOR_PASSPORT_ISSUED_DATE, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_passport_issued_date)


@user_data_router.message(UserDataStates.waiting_for_passport_issued_date)
async def process_passport_issued_date(message: Message, state: FSMContext):
    passport_issued_date = message.text
    await state.update_data(passport_issued_date=message.text)
    await message.answer(UserDataResponses.get_confirm_passport_issued_date_text(passport_issued_date), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
    await state.set_state(UserDataStates.confirm_passport_issued_date)


@user_data_router.message(UserDataStates.confirm_passport_issued_date, ReenterData())
async def cancel(message: Message, state: FSMContext):
    await state.update_data(passport_issued_date=None)
    await message.answer(UserDataResponses.ASK_FOR_PASSPORT_ISSUED_DATE, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_passport_issued_date)


@user_data_router.message(UserDataStates.confirm_passport_issued_date, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext):
    await message.answer(UserDataResponses.ASK_FOR_PASSPORT_ISSUED_ORGANIZATION_CODE, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_passport_issued_organization_code)


@user_data_router.message(UserDataStates.waiting_for_passport_issued_organization_code)
async def process_passport_issued_organization_code(message: Message, state: FSMContext):
    passport_issued_organization_code = message.text
    await state.update_data(passport_issued_organization_code=message.text)
    await message.answer(UserDataResponses.get_confirm_passport_issued_organization_code_text(passport_issued_organization_code), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
    await state.set_state(UserDataStates.confirm_passport_issued_organization_code)


@user_data_router.message(UserDataStates.confirm_passport_issued_organization_code, ReenterData())
async def cancel(message: Message, state: FSMContext):
    await state.update_data(passport_issued_organization_code=None)
    await message.answer(UserDataResponses.ASK_FOR_PASSPORT_ISSUED_ORGANIZATION_CODE, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_passport_issued_organization_code)


@user_data_router.message(UserDataStates.confirm_passport_issued_organization_code, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext):
    await message.answer(UserDataResponses.ASK_FOR_BIRTH_DATE, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_birth_date)


@user_data_router.message(UserDataStates.waiting_for_birth_date)
async def process_birth_date(message: Message, state: FSMContext):
    birth_date = message.text
    await state.update_data(birth_date=message.text)
    await message.answer(UserDataResponses.get_confirm_birth_date_text(birth_date), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
    await state.set_state(UserDataStates.confirm_birth_date)


@user_data_router.message(UserDataStates.confirm_birth_date, ReenterData())
async def cancel(message: Message, state: FSMContext):
    await state.update_data(birth_date=None)
    await message.answer(UserDataResponses.ASK_FOR_BIRTH_DATE, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_birth_date)


@user_data_router.message(UserDataStates.confirm_birth_date, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext):
    await message.answer(UserDataResponses.ASK_FOR_BIRTH_PLACE, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_birth_place)


@user_data_router.message(UserDataStates.waiting_for_birth_place)
async def process_birth_place(message: Message, state: FSMContext):
    birth_place = message.text
    await state.update_data(birth_place=message.text)
    await message.answer(UserDataResponses.get_confirm_birth_place_text(birth_place), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
    await state.set_state(UserDataStates.confirm_birth_place)


@user_data_router.message(UserDataStates.confirm_birth_place, ReenterData())
async def cancel(message: Message, state: FSMContext):
    await state.update_data(birth_place=None)
    await message.answer(UserDataResponses.ASK_FOR_BIRTH_PLACE, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_birth_place)


@user_data_router.message(UserDataStates.confirm_birth_place, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext):
    await message.answer(UserDataResponses.ASK_FOR_REGISTRATION_ADDRESS, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_registration_address)


@user_data_router.message(UserDataStates.waiting_for_registration_address)
async def process_registration_address(message: Message, state: FSMContext):
    registration_address = message.text
    await state.update_data(registration_address=message.text)
    await message.answer(UserDataResponses.get_confirm_registration_address_text(registration_address), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
    await state.set_state(UserDataStates.confirm_registration_address)


@user_data_router.message(UserDataStates.confirm_registration_address, ReenterData())
async def cancel(message: Message, state: FSMContext):
    await state.update_data(registration_address=None)
    await message.answer(UserDataResponses.ASK_FOR_REGISTRATION_ADDRESS, reply_markup=common.keyboards.remove_keyboard)
    await state.set_state(UserDataStates.waiting_for_registration_address)


@user_data_router.message(UserDataStates.confirm_registration_address, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext):
    await message.answer(UserDataResponses.ASK_FOR_BODY_WEIGHT, reply_markup=UserDataReplyKeyboard.generate_choose_body_weight_keyboard())
    await state.set_state(UserDataStates.waiting_for_body_weight)


@user_data_router.message(UserDataStates.waiting_for_body_weight, AllowedAnswers(UserDataExpectedMessages.BODY_WEIGHT_EXPECTED_MESSAGES))
async def process_body_weight(message: Message, state: FSMContext):
    body_weight = message.text
    await state.update_data(body_weight=message.text)
    await message.answer(UserDataResponses.get_confirm_body_weight_text(body_weight), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
    await state.set_state(UserDataStates.confirm_body_weight)


@user_data_router.message(UserDataStates.confirm_body_weight, ReenterData())
async def cancel(message: Message, state: FSMContext):
    await state.update_data(body_weight=None)
    await message.answer(UserDataResponses.ASK_FOR_BODY_WEIGHT, reply_markup=UserDataReplyKeyboard.generate_choose_body_weight_keyboard())
    await state.set_state(UserDataStates.waiting_for_body_weight)


@user_data_router.message(UserDataStates.confirm_body_weight, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext):
    await message.answer(UserDataResponses.ASK_FOR_BONE_MARROW_TYPING_AGREEMENT, reply_markup=UserDataReplyKeyboard.choose_bone_marrow_typing_agreement_keyboard)
    await state.set_state(UserDataStates.waiting_for_bone_marrow_typing_agreement)


@user_data_router.message(UserDataStates.waiting_for_bone_marrow_typing_agreement, AllowedAnswers(UserDataExpectedMessages.BONE_MARROW_TYPING_AGREEMENT_EXPECTED_MESSAGES))
async def process_bone_marrow_typing_agreement(message: Message, state: FSMContext):
    bone_marrow_typing_agreement = True if message.text == UserDataExpectedMessages.I_AGREE_FOR_BONE_MARROW_TYPING else False
    await state.update_data(bone_marrow_typing_agreement=bone_marrow_typing_agreement)
    await message.answer(UserDataResponses.get_confirm_bone_marrow_typing_agreement_text(bone_marrow_typing_agreement), reply_markup=UserDataReplyKeyboard.confirmation_keyboard)
    await state.set_state(UserDataStates.confirm_bone_marrow_typing_agreement)


@user_data_router.message(UserDataStates.confirm_bone_marrow_typing_agreement, ReenterData())
async def cancel(message: Message, state: FSMContext):
    await state.update_data(bone_marrow_typing_agreement=None)
    await message.answer(UserDataResponses.ASK_FOR_BONE_MARROW_TYPING_AGREEMENT, reply_markup=UserDataReplyKeyboard.choose_bone_marrow_typing_agreement_keyboard)
    await state.set_state(UserDataStates.waiting_for_bone_marrow_typing_agreement)


@user_data_router.message(UserDataStates.confirm_bone_marrow_typing_agreement, ConfirmEnteredData())
async def confirm_data(message: Message, state: FSMContext):
    await message.answer(UserDataResponses.get_recheck_data_text(), reply_markup=UserDataInlineKeyboard.edit_data_keyboard)
    await state.set_state(UserDataStates.recheck_data)
