from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

def get_yes_no_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Yes")
    kb.button(text="No")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def ease_link_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text="One", callback_data="Big")],
        [InlineKeyboardButton(text="Two",  callback_data="Big2")],
        [InlineKeyboardButton(text="Three",  callback_data="Big3")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)