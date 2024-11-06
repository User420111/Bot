from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from lexicon.lexicon import LEXICON
from keyboards.choice import *
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)

router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'], reply_markup=start_choice())

@router.callback_query(F.data == "First")
async def First(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON["choice_website"], reply_markup=website_choice())

@router.callback_query(F.data == "Second")
async def Second(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON["choice_task"], reply_markup=tasks())


# @router.callback_query(F.data == "Big")
# async def process_button_1_press(callback: CallbackQuery):
#     await callback.message(text="Вы выбрали сайт КЕГЭ")

# await callback.message.answer("Hello!")