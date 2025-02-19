
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
# Для работы с инлайн-кнопками
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

# def get_yes_no_kb() -> ReplyKeyboardMarkup:
#     kb = ReplyKeyboardBuilder()
#     kb.button(text="Yes")
#     kb.button(text="No")
#     kb.adjust(2)
#     return kb.as_markup(resize_keyboard=True)

# Функции для создания инлайн-кнопок
def start_choice():
    lst = [
        [InlineKeyboardButton(text="Перейти на сайт", callback_data="web")],
        [InlineKeyboardButton(text="Посмотреть задания здесь", callback_data="tg")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=lst)

def website_choice():
    inline_kb_list = [
        [InlineKeyboardButton(text="КЕГЭ", url="https://kompege.ru/")],
        [InlineKeyboardButton(text="ФИПИ", url="https://ege.fipi.ru/bank/index.php?proj=B9ACA5BBB2E19E434CD6BEC25284C67F")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def tasks():
    tasks_kb = [
        [InlineKeyboardButton(text="1 задание", callback_data="first")],
        [InlineKeyboardButton(text="2 задание", callback_data="Two")],
        [InlineKeyboardButton(text="3 задание", callback_data="Three")],
        [InlineKeyboardButton(text="4 задание", callback_data="dcd")],
        [InlineKeyboardButton(text="5 задание", callback_data="cdc")],
        [InlineKeyboardButton(text="6 задание", callback_data="ecd")],
        [InlineKeyboardButton(text="7 задание", callback_data="eferf")],
        [InlineKeyboardButton(text="8 задание", callback_data="cerver")],
        [InlineKeyboardButton(text="9 задание", callback_data="ecever")],
        [InlineKeyboardButton(text="10 задание", callback_data="reverv")],
        [InlineKeyboardButton(text="11 задание", callback_data="ververe")],
        [InlineKeyboardButton(text="12 задание", callback_data="ververv")],
        [InlineKeyboardButton(text="13 задание", callback_data="vevevfrervr")],
        [InlineKeyboardButton(text="14 задание", callback_data="vevevfrervr")],
        [InlineKeyboardButton(text="15 задание", callback_data="vevevfrervr")],
        [InlineKeyboardButton(text="16 задание", callback_data="vevevfrervr")]

    ]
    return InlineKeyboardMarkup(inline_keyboard=tasks_kb)

def task_kb():
    kb = [
        [InlineKeyboardButton(text="Посмотреть ответ", callback_data="answer")],
        [InlineKeyboardButton(text="Выбрать другой тип задания", callback_data="other_type")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)

def next_kb():
    nkb = [
        [InlineKeyboardButton(text="Следующее задание", callback_data="next")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=nkb)










