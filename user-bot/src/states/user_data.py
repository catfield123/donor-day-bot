from aiogram.fsm.state import State, StatesGroup

class NewVolunteerStates(StatesGroup):
    waiting_for_name = State()
    confirm_name = State()
    waiting_for_surname = State()
    confirm_surname = State()
    waiting_for_patronymic = State()
    confirm_patronymic = State()


    waiting_for_phone_number = State()
    confirm_phone_number = State()
    waiting_for_email = State()
    confirm_email = State()


    waiting_for_is_polytech_student = State()
    confirm_is_polytech_student = State()
    waiting_for_grade_book_number = State()
    confirm_grade_book_number = State()
    waiting_for_group_number = State()
    confirm_group_number = State()
    waiting_for_faculty = State()
    confirm_faculty = State()
    waiting_for_founding_source = State()
    confirm_founding_source = State()


    waiting_for_inn = State()
    confirm_inn = State()
    waiting_for_snils = State()
    confirm_snils = State()


    waiting_for_passport_series = State()
    confirm_passport_series = State()
    waiting_for_passport_number = State()
    confirm_passport_number = State()
    waiting_for_passport_issued_by = State()
    confirm_passport_issued_by = State()
    waiting_for_passport_issued_date = State()
    confirm_passport_issued_date = State()
    waiting_for_passport_issued_organization_code = State()
    confirm_passport_issued_organization_code = State()
    waiting_for_birth_date = State()
    confirm_birth_date = State()
    waiting_for_birth_place = State()
    confirm_birth_place = State()
    waiting_for_registration_address = State()
    confirm_registration_address = State()


    waiting_for_sex = State()
    confirm_sex = State()
    waiting_for_body_weight = State()
    confirm_body_weight = State()


    waiting_for_bone_marrow_typing_agreement = State()
    confirm_bone_marrow_typing_agreement = State()

    waiting_for_donation_place = State()
    confirm_donation_place = State()
    waiting_for_donation_datetime = State()
    confirm_donation_datetime = State()

    recheck_data = State()
