
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
# Импортируем функции из database.py
from database.database import read_blob, convert_to_img, save_users, read_count, update_users, read_answer
from aiogram.types import FSInputFile

import json


ans = 0
num_task = 0



router = Router()

# При запуске бота id пользователя сохраняетя в таблице users для того, чтобы бот знал, какие задания пользователь уже посмотрел
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'], reply_markup=start_choice())
    # await message.answer(str(message.from_user.id))
    save_users(message.from_user.id, json.dumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))

# Функция для того, чтобы перейти на сайт
@router.callback_query(F.data == "web")
async def Web(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON["choice_website"], reply_markup=website_choice())

# Функция для того, чтобы посмотреть задания здесь
@router.callback_query(F.data == "tg")
async def TG(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON["choice_task"], reply_markup=tasks())


# Фукция для просмотра ответа
@router.callback_query(F.data == "answer")
async def answer(callback: CallbackQuery):
    global ans
    # f = open(f"database/db_data/answer_{ans}.txt", "r")

    await callback.message.answer(text = f"Ответ: {read_answer(ans)}", reply_markup=next_kb())


    # os.remove("database/db_data/answer_1.txt")
    # os.remove("database/db_data/img_1.png")
    # os.remove("database/db_data/answer_1.txt")
    # except:
    #     print("Файлы уже удалены")
    #     os.remove("database/db_data/img_1.png")
    #     os.remove("database/db_data/answer_1.txt")

# Функция для того, чтобы посмотреть следующее задание
@router.callback_query(F.data == "next")
async def next(callback: CallbackQuery):
    global ans
    global num_task
    # os.remove(f"database/db_data/answer_{ans}.txt")
    c = read_count(callback.from_user.id)
    lst = json.loads(c)
    if int(lst[num_task]) > 8:
        await callback.message.answer(text="Вы посмотрели все задания")
        lst[num_task] = 1
    read_blob(lst[num_task])

    f = FSInputFile(f"database/db_data/img_{lst[num_task]}.png")

    await callback.message.answer_photo(f, reply_markup=task_kb())

    os.remove(f"database/db_data/img_{lst[num_task]}.png")
    ans = lst[num_task]
    lst[num_task] = lst[num_task] + 1
    print(json.dumps(lst))
    update_users(callback.from_user.id, json.dumps(lst))


@router.callback_query(F.data == "other_type")
async def other_type(callback: CallbackQuery):
    global ans
    await callback.message.answer(text=LEXICON["choice_task"], reply_markup=tasks())
    # os.remove(f"database/db_data/answer_{ans}.txt")



# Функция для того, чтобы посмотреть первое задание
@router.callback_query(F.data == "first")
async def First(callback: CallbackQuery):
    global ans
    global num_task
    num_task = 1 - 1
    c = read_count(callback.from_user.id)
    lst = json.loads(c)
    read_blob(lst[0])

    f = FSInputFile(f"database/db_data/img_{lst[0]}.png")

    await callback.message.answer_photo(f, reply_markup=task_kb())

    os.remove(f"database/db_data/img_{lst[0]}.png")
    ans = lst[0]
    lst[0] = lst[0] + 1
    print(json.dumps(lst))
    update_users(callback.from_user.id, json.dumps(lst))




