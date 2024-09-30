from aiogram.filters import Filter
from aiogram.types import Message

from expected_messages.user_data import UserDataExpectedMessages


class AllowedAnswers(Filter):
    def __init__(self, allowed_answers_list: list[str]) -> None:
        self.allowed_answers_list = allowed_answers_list

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