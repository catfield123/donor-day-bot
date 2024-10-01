from schemas import UserRecheckData

def generate_user_recheck_data_from_state_data(state_data) -> UserRecheckData:
    return UserRecheckData(
        name=state_data.get('name'),
        surname=state_data.get('surname'),
        patronymic=state_data.get('patronymic'),

        phone_number=state_data.get('phone_number'),
        email=state_data.get('email'),

        is_polytech_student=state_data.get('is_polytech_student'),
        grade_book_number=state_data.get('grade_book_number'),
        group_number=state_data.get('group_number'),
        faculty=state_data.get('faculty'),
        founding_source=state_data.get('founding_source'),

        inn=state_data.get('inn'),
        snils=state_data.get('snils'),

        passport_series=state_data.get('passport_series'),
        passport_number=state_data.get('passport_number'),
        passport_issued_by=state_data.get('passport_issued_by'),
        passport_issued_date=state_data.get('passport_issued_date'),
        passport_issued_organization_code=state_data.get('passport_issued_organization_code'),
        registration_address=state_data.get('registration_address'),

        birth_date=state_data.get('birth_date'),
        birth_place=state_data.get('birth_place'),

        sex=state_data.get('sex'),
        body_weight=state_data.get('body_weight'),
        bone_marrow_typing_agreement=state_data.get('bone_marrow_typing_agreement'),

        donation_place=state_data.get('donation_place'),
        donation_datetime=state_data.get('donation_datetime'),

    )