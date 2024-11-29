import asyncio  # Модуль для асинхронности
import logging  # Модуль для логирования

from aiogram import Bot, Dispatcher  # Библиотека для работы с ботом
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode  # Форматирование сообщения
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers  # Для работы с хэндлерами
from database import database as db
from database.database import db_start  # Для работы с БД

logger = logging.getLogger(__name__)



# Функция для запуска бота
async def main():
    # Функция для создания таблиц в БД, если их не существует
    db_start()

    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    config: Config = load_config()

    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()


    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)



    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


# Запуск бота
asyncio.run(main())