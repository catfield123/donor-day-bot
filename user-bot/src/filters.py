from aiogram.filters import Filter
from aiogram.types import Message

from expected_messages.user_data import UserDataExpectedMessages


class AllowedAnswers(Filter):
    def __init__(self, allowed_answers: list[str] | str) -> None:
        if isinstance(allowed_answers, str):
            self.allowed_answers_list = [allowed_answers]
        elif isinstance(allowed_answers, list):
            self.allowed_answers_list = allowed_answers
        else:
            raise TypeError(f"allowed_answers must be list[str] or str, not {type(allowed_answers)}")

    async def __call__(self, message: Message) -> bool:
        return message.text in self.allowed_answers_list
    

class ConfirmEnteredData(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.text == UserDataExpectedMessages.CONFIRM_ENTERED_DATA

class ReenterData(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.text == UserDataExpectedMessages.REENTER_DATA
    
class ReenterPlaceAndDatetime(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.text == UserDataExpectedMessages.REENTER_PLACE_AND_DATETIME