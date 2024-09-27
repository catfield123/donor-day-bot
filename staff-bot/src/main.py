import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from aiogram.fsm.context import FSMContext

from common.states import IdleStates

from config import staff_settings
TOKEN = staff_settings.STAFF_BOT_TOKEN

from fsm import staff_fsm_storage
dp = Dispatcher(storage=staff_fsm_storage)

from handlers.new_volunteer import new_volunteer_router

dp.include_router(new_volunteer_router)

@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        await message.answer(f"Hello, {message.from_user.full_name}\!")
        await state.set_state(IdleStates.idle)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
