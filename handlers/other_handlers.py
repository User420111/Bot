from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import *

router = Router()


@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON['other'])