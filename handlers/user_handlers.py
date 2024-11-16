
from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, InputFile

from lexicon.lexicon import LEXICON
from keyboards.choice import *
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)
import sqlite3
import os

from keyboards import choice
import database.database
from database.database import read_blob, write_to_file, write_to_fileStr
from aiogram.types import FSInputFile



router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'], reply_markup=start_choice())

@router.callback_query(F.data == "web")
async def Web(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON["choice_website"], reply_markup=website_choice())

@router.callback_query(F.data == "tg")
async def TG(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON["choice_task"], reply_markup=tasks())

@router.callback_query(F.data == "first")
async def First(callback: CallbackQuery):
    read_blob(1)
    f = FSInputFile("database/db_data/img_1.png")
    await callback.message.answer_photo(f, reply_markup=answers())





# @router.callback_query(F.data == "Big")
# async def process_button_1_press(callback: CallbackQuery):
#     await callback.message(text="Вы выбрали сайт КЕГЭ")

# await callback.message.answer("Hello!")
