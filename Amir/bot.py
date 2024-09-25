import asyncio
from aiogram import Bot, Dispatcher

async def main():
        bot = Bot(token="7979195363:AAFTSWEDwZxnSb6R7H-bhl6S1S711JTEGmk")
        dp = Dispatcher()

        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())