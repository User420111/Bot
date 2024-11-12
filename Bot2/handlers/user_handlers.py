from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, InputFile

from lexicon.lexicon import LEXICON
from keyboards.choice import *
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)
import sqlite3
import os







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

@router.callback_query(F.data == "One")
async def One(callback: CallbackQuery):
    f = open("C:\\Users\\user\\Desktop\\Bot\\tasks\\1\\0000\\question.txt", "r", encoding='utf-8')
    # f2 = InputFile("C:\\Users\\user\\Desktop\\Bot\\tasks\\1\\0000\\img.png")
    t = f.read()

    await callback.message.answer(text=t)
    # await callback.message.answer(imghdr=f2)



# @router.callback_query(F.data == "Big")
# async def process_button_1_press(callback: CallbackQuery):
#     await callback.message(text="Вы выбрали сайт КЕГЭ")

# await callback.message.answer("Hello!")