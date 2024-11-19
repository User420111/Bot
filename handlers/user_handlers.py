
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
from database.database import read_blob, write_to_file, write_to_fileStr, save_users, read_count
from aiogram.types import FSInputFile

import json



router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'], reply_markup=start_choice())
    await message.answer(str(message.from_user.id))
    save_users(message.from_user.id, json.dumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))

@router.callback_query(F.data == "web")
async def Web(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON["choice_website"], reply_markup=website_choice())

@router.callback_query(F.data == "tg")
async def TG(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON["choice_task"], reply_markup=tasks())


@router.callback_query(F.data == "answer")
async def answer(callback: CallbackQuery):
    f = open("database/db_data/answer_1.txt", "r")
    await callback.message.answer(text = f"Ответ: {f.read()}                                                        ", reply_markup=next_kb())
    # os.remove("database/db_data/img_1.png")
    # os.remove("database/db_data/answer_1.txt")
    # except:
    #     print("Файлы уже удалены")
    #     os.remove("database/db_data/img_1.png")
    #     os.remove("database/db_data/answer_1.txt")

# @router.callback_query(F.data == "other_type")
# async def other_type(callback: CallbackQuery):
    # os.remove("database/db_data/img_1.png")
    # os.remove("database/db_data/answer_1.txt")

@router.callback_query(F.data == "first")
async def First(callback: CallbackQuery):
    c = read_count(callback.from_user.id)
    read_blob(c + 2)

    f = FSInputFile(f"database/db_data/img_{c + 2}.png")
    await callback.message.answer_photo(f, reply_markup=task_kb())

    # os.remove("database/db_data/img_1.png")
    # os.remove("database/db_data/answer_1.txt")







# @router.callback_query(F.data == "Big")
# async def process_button_1_press(callback: CallbackQuery):
#     await callback.message(text="Вы выбрали сайт КЕГЭ")

# await callback.message.answer("He