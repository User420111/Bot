import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from handlers import questions, different_types
from aiogram.filters.command import Command

from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from keyboards.main_menu import set_main_menu


from config_reader import config


# from aiogram.enums.dice_emoji import DiceEmoji
from datetime import datetime


async def main():

    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.bot_token.get_secret_value(),
              default=DefaultBotProperties(
                  parse_mode=ParseMode.HTML
              )
        )
    dp = Dispatcher()
    await set_main_menu(bot)
    dp.include_routers(questions.router, different_types.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)












if __name__ == "__main__":
    asyncio.run(main())