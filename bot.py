import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties


from config_reader import config

# from aiogram.enums.dice_emoji import DiceEmoji
from datetime import datetime


logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value(),
          default=DefaultBotProperties(
              parse_mode=ParseMode.HTML
          )
    )
dp = Dispatcher()






@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello")


@dp.message(Command("answer"))
async def cmd_answer(message: types.Message):
    await message.answer("Это просто ответ!")

@dp.message(Command("reply"))
async def cmd_reply(message: types.Message):
    await message.reply("Ответ на ответ")

# @dp.message(Command("dice"))
# async def cmd_dice(message: types.Message):
#     await message.answer_dice(emoji="🎲")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())