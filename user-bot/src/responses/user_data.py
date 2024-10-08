from common.utils import escape_markdown_v2
from schemas import UserRecheckData
from expected_messages.user_data import UserDataExpectedMessages

class UserDataResponses:
    ASK_FOR_NAME = "Пожалуйста, введите ваше имя\."
    @staticmethod
    def get_confirm_name_text(name: str) -> str:
        return f"*Ваше имя*: \n{escape_markdown_v2(name)}"
    
    ASK_FOR_SURNAME = "Пожалуйста, введите вашу фамилию\."
    @staticmethod
    def get_confirm_surname_text(surname: str) -> str:
        return f"*Ваша фамилия*: \n{escape_markdown_v2(surname)}"
    
    ASK_FOR_PATRONIMYC = "Пожалуйста, введите ваше отчество\."
    @staticmethod
    def get_confirm_patronymic_text(patronymic: str | None) -> str:
        answer = "Нет отчества" if patronymic is None else patronymic
        return f"*Ваше отчество*: \n{escape_markdown_v2(answer)}"
    
    ASK_FOR_PHONE_NUMBER = (
        "Пожалуйста, введите ваш номер телефона в следующем формате\:\n\n"
        "\+7\(xxx\)xxx\-xx\-xx"
    )
    @staticmethod
    def get_confirm_phone_number_text(phone_number: str) -> str:
        return f"*Ваш номер телефона*: \n{escape_markdown_v2(phone_number)}"
    
    ASK_FOR_EMAIL = "Пожалуйста, введите ваш email\."
    @staticmethod
    def get_confirm_email_text(email: str) -> str:
        return f"*Ваш email*: \n{escape_markdown_v2(email)}"
    
    ASK_FOR_IS_POLYTECH_STUDENT = "Являетесь ли вы студентом СПбПУ\?"

    @staticmethod
    def get_confirm_is_polytech_student_text(is_polytech_student: bool) -> str:
        answer = "Да" if is_polytech_student else "Нет"
        return f"*Являетесь ли вы студентом СПбПУ*: \n{escape_markdown_v2(answer)}"

    ASK_FOR_GRADE_BOOK_NUMBER = "Пожалуйста, введите ваш номер зачетной книжки\."
    @staticmethod
    def get_confirm_grade_book_number_text(grade_book_number: str | None) -> str:
        if grade_book_number is None:
            grade_book_number = "Не указан"
        return f"*Ваш номер зачетной книжки*: \n{escape_markdown_v2(grade_book_number)}"
    
    ASK_FOR_GROUP_NUMBER = "Пожалуйста, введите ваш номер группы\."
    @staticmethod
    def get_confirm_group_number_text(group_number: str) -> str:
        return f"*Ваш номер группы*: \n{escape_markdown_v2(group_number)}"
    
    ASK_FOR_FACULTY = "Пожалуйста, выберите институт в котором вы обучаетесь\."
    @staticmethod
    def get_confirm_faculty_text(faculty: str) -> str:
        return f"*Ваш институт*: \n{escape_markdown_v2(faculty)}"
    
    ASK_FOR_FOUNDING_SOURCE = "Пожалуйста, укажите, учитесь ли вы на бюджете или на контракте\."
    @staticmethod
    def get_confirm_founding_source_text(founding_source: str) -> str:
        return f"*Учитесь ли вы на бюджете или на контракте*: \n{escape_markdown_v2(founding_source)}"
    
    ASK_FOR_INN = "Пожалуйста, введите ваш ИНН\."
    @staticmethod
    def get_confirm_inn_text(inn: str | None) -> str:
        answer = "Не указан" if inn is None else inn
        return f"*Ваш ИНН*: \n{escape_markdown_v2(answer)}"
    
    ASK_FOR_SNILS = "Пожалуйста, введите ваш номер  СНИЛС в том формате, в котором он указан в документе\."
    @staticmethod
    def get_confirm_snils_text(snils: str | None) -> str:
        answer = "Не указан" if snils is None else snils
        return f"*Ваш СНИЛС*: \n{escape_markdown_v2(answer)}"
    
    ASK_FOR_PASSPORT_SERIES = "Пожалуйста, введите вашу серию паспорта \(4 цифры\)"
    @staticmethod
    def get_confirm_passport_series_text(passport_series: str) -> str:
        return f"*Ваша серия паспорта*: \n{escape_markdown_v2(passport_series)}"
    
    ASK_FOR_PASSPORT_NUMBER = "Пожалуйста, введите ваш номер паспорта \(6 цифр\)\."
    @staticmethod
    def get_confirm_passport_number_text(passport_number: str) -> str:
        return f"*Ваш номер паспорта*: \n{escape_markdown_v2(passport_number)}"
    
    ASK_FOR_PASSPORT_ISSUED_BY = "Пожалуйста, введите, кем был выдал паспорт \(как указано в документе\)\."
    @staticmethod
    def get_confirm_passport_issued_by_text(passport_issued_by: str) -> str:
        return f"*Кем вы выдали паспорт*: \n{escape_markdown_v2(passport_issued_by)}"
    
    ASK_FOR_PASSPORT_ISSUED_ORGANIZATION_CODE = "Пожалуйста, введите код органа, выдавшего паспорт\."
    @staticmethod
    def get_confirm_passport_issued_organization_code_text(passport_issued_organization_code: str) -> str:
        return f"*Код органа, выдавшего паспорт*: \n{escape_markdown_v2(passport_issued_organization_code)}"
    
    ASK_FOR_PASSPORT_ISSUED_DATE = (
        "Пожалуйста, введите дату выдачи паспорта в следующем формате\:\n\n"
        "дд\.мм\.гггг"
    )
    @staticmethod
    def get_confirm_passport_issued_date_text(passport_issued_date: str) -> str:
        return f"*Дата выдачи паспорта*: \n{escape_markdown_v2(passport_issued_date)}"
    
    
    ASK_FOR_BIRTH_DATE = (
        "Пожалуйста, введите дату рождения в следующем формате\:\n\n"
        "дд\.мм\.гггг"
    )
    @staticmethod
    def get_confirm_birth_date_text(birth_date: str) -> str:
        return f"*Дата рождения*: \n{escape_markdown_v2(birth_date)}"
    
    ASK_FOR_BIRTH_PLACE = "Пожалуйста, введите место рождения \(как в паспорте\)\."
    @staticmethod
    def get_confirm_birth_place_text(birth_place: str) -> str:
        return f"*Место рождения*: \n{escape_markdown_v2(birth_place)}"
    
    ASK_FOR_REGISTRATION_ADDRESS = "Пожалуйста, введите ваш адрес регистрации \(как в паспорте\)\."
    @staticmethod
    def get_confirm_registration_address_text(registration_address: str) -> str:
        return f"*Адрес регистрации*: \n{escape_markdown_v2(registration_address)}"
    
    ASK_FOR_SEX = "Пожалуйста, выберите ваш пол\."
    @staticmethod
    def get_confirm_sex_text(sex: str) -> str:
        return f"*Ваш пол*: \n{escape_markdown_v2(sex)}"
    
    ASK_FOR_BODY_WEIGHT = "Пожалуйста, выберите ваш вес\."
    @staticmethod
    def get_confirm_body_weight_text(weight: str) -> str:
        return f"*Ваш вес*: \n{escape_markdown_v2(weight)}"
    
    ASK_FOR_BONE_MARROW_TYPING_AGREEMENT = "Согласны ли вы на типирование костного мозга\?"
    @staticmethod
    def get_confirm_bone_marrow_typing_agreement_text(bone_marrow_typing_agreement: bool) -> str:
        answer = "Да" if bone_marrow_typing_agreement else "Нет"
        return f"*Согласие на типирование костного мозга*: \n{escape_markdown_v2(answer)}"
    
    ASK_FOR_DONATION_PLACE = "Пожалуйста, введите место для участие в акции\."
    @staticmethod
    def get_confirm_donation_place_text(donation_place: str) -> str:
        return f"*Место для участия в акции*: \n{escape_markdown_v2(donation_place)}"
    
    ASK_FOR_DONATION_DATETIME = "Пожалуйста, выберетие время участия в акции\."
    @staticmethod
    def get_confirm_donation_datetime_text(donation_place: str, donation_datetime: str) -> str:
        return (
                f"*Место для участия в акции*: \n{escape_markdown_v2(donation_place)}\n\n"
                f"*Время для участия в акции*: \n{escape_markdown_v2(donation_datetime)}"
                )

    WRONG_FACULTY_NAME = "Неправильное название факультета\. Пожалуйста, выберите один из предложенных вариантов\."


    @staticmethod
    def get_recheck_data_text(user_recheck_data : UserRecheckData) -> str:
        response = (
            "Пожалуйста\, проверьте правильность введенных данных\.\n\n"

            "*__ФИО\:__*\n"
            f"{escape_markdown_v2(user_recheck_data.full_name)}\n\n"

            "*__Номер телефона\:__*\n"
            f"{escape_markdown_v2(user_recheck_data.phone_number)}\n\n"

            "*__Адрес электронной почты\:__*\n"
            f"{escape_markdown_v2(user_recheck_data.email)}\n\n"

            "*__Данные о месте обучения\:__*\n"
            "Студент политеха\: " + ("Да" if user_recheck_data.is_polytech_student else "Нет") + "\n"
        )

        if user_recheck_data.is_polytech_student:
            response += (
                "Номер зачётной книжки\: " + (escape_markdown_v2(user_recheck_data.grade_book_number) if user_recheck_data.grade_book_number else "Не указан") + "\n"
                f"Номер группы\: {escape_markdown_v2(user_recheck_data.group_number)}\n"
                f"Институт\: {escape_markdown_v2(user_recheck_data.faculty)}\n"
                f"Источник финансирования\: {escape_markdown_v2(user_recheck_data.founding_source.value)}\n\n"
            )
        else:
            response += '\n'

        response += (
            "*__ИНН\:__*\n"
            f"{escape_markdown_v2(user_recheck_data.inn)}\n\n"
            "*__СНИЛС\:__*\n"
            f"{escape_markdown_v2(user_recheck_data.snils)}\n\n"
            "*__Данные паспорта\:__*\n"
            f"Серия\, номер\: {escape_markdown_v2(user_recheck_data.passport_full_number)}\n"
            f"Выдан\: {escape_markdown_v2(user_recheck_data.passport_issued_by_full_text)}\n"
            f"Дата рождения\: {escape_markdown_v2(user_recheck_data.birth_date)}\n"
            f"Место рождения\: {escape_markdown_v2(user_recheck_data.birth_place)}\n"
            f"Адрес регистрации\: {escape_markdown_v2(user_recheck_data.registration_address)}\n\n"

            "*__Пол\:__*\n"
            f"{escape_markdown_v2(user_recheck_data.sex.value)}\n\n"

            "*__Вес\:__*\n"
            f"{escape_markdown_v2(user_recheck_data.body_weight.value)}\n\n"

            "*__Согласие на типирование костного мозга\:__*\n"
            "" + ("Да" if user_recheck_data.bone_marrow_typing_agreement else "Нет") + "\n\n"

            "*__Место и время участия в акции\:__*\n"
            f"{escape_markdown_v2(user_recheck_data.donation_place)}\n"
            f"{escape_markdown_v2(user_recheck_data.donation_datetime)}\n\n"
        )

        response += escape_markdown_v2("Если какие-то данные не верны, нажмите на соответствующую кнопку, чтобы их изменить.")

        return response
        
    
    DATA_IS_WRITTEN = "Данные успешно записаны\."
    ENTER_NEW_DATA = "Укажите новые данные\."

    YOUR_DATA_IS_SAVED = (
        "Ваши данные были успешно сохранены\.\n"
        f"Если вы хотите изменить какие\-либо данные, введите команду /edit\_data или введите текст \"`{UserDataExpectedMessages.EDIT_DATA}`\"\.\n\n"
        "За несколько дней до выбранной даты участия акции наш волонтёр позвонит вам для подтверждения вашего участия\.\n\n"
        "Пожалуйста\, следите за ботом\, чтобы не пропустить полезную информацию об Акции\."
    )
    
    


    



    


    