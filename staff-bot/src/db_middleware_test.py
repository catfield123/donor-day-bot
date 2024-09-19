import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from common.middleware import DatabaseMiddleware


from sqlalchemy import text

# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("STAFF_BOT_TOKEN")

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()

from aiogram import Router

router = Router()


router.message.middleware(DatabaseMiddleware())

dp.include_router(router)

@router.message(CommandStart())
async def command_start_handler(message: Message, db) -> None:

    result = db.execute(text("SELECT 1"))
    await message.answer(f"Database test result: {result.fetchone()[0]}")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
