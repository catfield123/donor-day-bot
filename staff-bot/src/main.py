import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, ExceptionTypeFilter
from aiogram.types import Message
from aiogram import F
from aiogram.types.error_event import ErrorEvent

from aiogram.fsm.context import FSMContext

from common.exceptions import DatabaseConnectionError
from common.states import IdleStates
from common.keyboards import remove_keyboard
from common.utils import escape_markdown_v2
from common.responses import BOT_IS_UNAVAILABLE_RESPONSE

from exceptions.auth import NotAdminException, NotVolunteerException
from responses.auth import AuthResponses

from config import staff_settings
TOKEN = staff_settings.STAFF_BOT_TOKEN

from fsm import staff_fsm_storage
dp = Dispatcher(storage=staff_fsm_storage)

from handlers.new_volunteer import new_volunteer_router
from handlers.help_and_my_status import help_and_status_router

dp.include_router(new_volunteer_router)
dp.include_router(help_and_status_router)

@dp.error(ExceptionTypeFilter(NotAdminException), F.update.message.as_("message"))
async def handle_not_admin_exception(event: ErrorEvent, message: Message):
    await message.answer(AuthResponses.NOT_ADMIN_RESPONSE, reply_markup=remove_keyboard)

@dp.error(ExceptionTypeFilter(NotVolunteerException), F.update.message.as_("message"))
async def handle_not_volunteer_exception(event: ErrorEvent, message: Message):
    await message.answer(AuthResponses.NOT_VOLUNTEER_RESPONSE, reply_markup=remove_keyboard)

@dp.error(ExceptionTypeFilter(DatabaseConnectionError), F.update.message.as_("message"))
async def handle_database_connection_error(event: ErrorEvent, message: Message):
    await message.answer(BOT_IS_UNAVAILABLE_RESPONSE, reply_markup=remove_keyboard)

@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        await message.answer(f"Привет, {escape_markdown_v2(message.from_user.full_name)}\!")
        await state.set_state(IdleStates.idle)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
