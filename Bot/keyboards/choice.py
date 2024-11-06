from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

# def get_yes_no_kb() -> ReplyKeyboardMarkup:
#     kb = ReplyKeyboardBuilder()
#     kb.button(text="Yes")
#     kb.button(text="No")
#     kb.adjust(2)
#     return kb.as_markup(resize_keyboard=True)

def start_choice():
    lst = [
        [InlineKeyboardButton(text="Перейти на сайт", callback_data="First")],
        [InlineKeyboardButton(text="Посмотреть здесь", callback_data="Second")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=lst)

def website_choice():
    inline_kb_list = [
        [InlineKeyboardButton(text="КЕГЭ", url="https://kompege.ru/")],
        [InlineKeyboardButton(text="ФИПИ", url="https://ege.fipi.ru/bank/index.php?proj=B9ACA5BBB2E19E434CD6BEC25284C67F")],
        [InlineKeyboardButton(text="РЕШУ ЕГЭ", url="https://inf-ege.sdamgia.ru/")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def tasks():
    tasks_kb = [
        [InlineKeyboardButton(text=" задание", callback_data="One")],
        [InlineKeyboardButton(text=" задание", callback_data="Two")],
        [InlineKeyboardButton(text=" задание", callback_data="Three")],
        [InlineKeyboardButton(text=" задание", callback_data="dcd")],
        [InlineKeyboardButton(text=" задание", callback_data="cdc")],
        [InlineKeyboardButton(text=" задание", callback_data="ecd")],
        [InlineKeyboardButton(text="задание", callback_data="eferf")],
        [InlineKeyboardButton(text="задание", callback_data="cerver")],
        [InlineKeyboardButton(text=" задание", callback_data="ecever")],
        [InlineKeyboardButton(text=" задание", callback_data="reverv")],
        [InlineKeyboardButton(text=" задание", callback_data="ververe")],
        [InlineKeyboardButton(text=" задание", callback_data="ververv")],
        [InlineKeyboardButton(text=" задание", callback_data="vevevfrervr")]

    ]
    return InlineKeyboardMarkup(inline_keyboard=tasks_kb)










