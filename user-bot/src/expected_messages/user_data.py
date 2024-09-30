from common.models import SexEnum, FoundingSourceEnum, BodyWeightEnum

class UserDataExpectedMessages:
    ENTER_DATA = "Начать ввод данных"

    CONFIRM_ENTERED_DATA = "Подтвердить"
    REENTER_DATA = "Ввести заново"
    REENTER_PLACE_AND_DATETIME = "Указать другое место"
    
    YES_IS_POLYTECH_STUDENT = "Я студент Политеха"
    NO_IS_POLYTECH_STUDENT = "Я не студент Политеха"
    POLYTECH_STUDENT_EXPECTED_MESSAGES = [YES_IS_POLYTECH_STUDENT, NO_IS_POLYTECH_STUDENT]

    I_HAVE_NO_PATRONYMIC = "У меня нет отчества"

    I_HAVE_NO_INN = "У меня нет ИНН"

    I_HAVE_NO_SNILS = "У меня нет СНИЛС"

    BUDGET_FOUNDING_SOURCE = FoundingSourceEnum.budget.value
    CONTRACT_FOUNDING_SOURCE = FoundingSourceEnum.contract.value
    FOUNDING_SOURCE_EXPECTED_MESSAGES = [BUDGET_FOUNDING_SOURCE, CONTRACT_FOUNDING_SOURCE]

    MALE_SEX = SexEnum.male.value
    FEMALE_SEX = SexEnum.female.value
    SEX_EXPECTED_MESSAGES = [MALE_SEX, FEMALE_SEX]

    BODY_WEIGHT_LESS_58_KG = BodyWeightEnum.less_then_50_kg.value
    BODY_WEIGHT_MORE_58_KG = BodyWeightEnum.more_then_58_kg.value
    BODY_WEIGHT_BETWEEN_50_AND_58_KG = BodyWeightEnum.between_50_and_58_kg.value
    BODY_WEIGHT_EXPECTED_MESSAGES = [BODY_WEIGHT_LESS_58_KG, BODY_WEIGHT_MORE_58_KG, BODY_WEIGHT_BETWEEN_50_AND_58_KG]

    I_DONT_REMEMBER_MY_GRADE_BOOK_NUMBER = "Я не помню номер зачётной книжки"

    I_AGREE_FOR_BONE_MARROW_TYPING = "Согласен на типирование"
    I_DECLINE_FOR_BONE_MARROW_TYPING = "Не согласен на типирование"
    BONE_MARROW_TYPING_AGREEMENT_EXPECTED_MESSAGES = [I_AGREE_FOR_BONE_MARROW_TYPING, I_DECLINE_FOR_BONE_MARROW_TYPING]

    ALL_DATA_IS_CORRECT = "Все данные верны"

    EDIT_FULL_NAME = "Изменить ФИО"
    EDIT_PHONE_NUMBER = "Изменить номер телефона"
    EDIT_EMAIL = "Изменить почту"
    EDIT_STUDYING_PLACE_INFO = "Изменить информацию о месте обучения"
    EDIT_INN = "Изменить ИНН"
    EDIT_SNILS = "Изменить СНИЛС"

    EDIT_PASSPORT_DATA = "Изменить данные паспорта"
    EDIT_SEX_DATA = "Изменить данные о пол"
    EDIT_WEIGHT_DATA = "Изменить данные о весе"
    EDIT_BONE_MARROW_TYPING_AGREEMENT_DATA = "Изменить согласие на типирование"

    EDIT_DONATION_PLACE_AND_DATETIME = "Изменить место и время сдачи крови"

    CANCEL_OPERATION = "Отменить операцию"

    EDIT_DATA = "Изменить данные"



