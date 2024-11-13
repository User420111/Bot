# from aiogram import Router, F
# from aiogram.filters import Command
# from aiogram.types import Message, ReplyKeyboardRemove
#
# from keyboards.for_questions import get_yes_no_kb, ease_link_kb
#
# router = Router()
#
# @router.message(Command("start"))
# async def cmd_start(message: Message):
#     await message.answer(
#         "Выберите задание",
#         reply_markup=ease_link_kb()
#     )

# @router.message(F.text.lower() == "да")
# async def answer_yes(message: Message):
#     await message.answer(
#         "Это здорово!",
#         reply_markup=ReplyKeyboardRemove()
#     )
#
# @router.message(F.text.lower() == "нет")
# async def answer_no(message: Message):
#     await message.answer(
#         "Жаль...",
#         reply_markup=ReplyKeyboardRemove()
#     )