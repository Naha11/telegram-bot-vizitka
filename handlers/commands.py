"""Обработчики команд /start, /help, /menu."""

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import COMPANY, WELCOME_MESSAGE
from keyboards import main_menu_kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    text = WELCOME_MESSAGE.format(
        company_name=COMPANY["name"],
        description=COMPANY["description"],
    )
    await message.answer(text, reply_markup=main_menu_kb())


@router.message(Command("menu"))
async def cmd_menu(message: Message):
    await message.answer("Главное меню:", reply_markup=main_menu_kb())


@router.message(Command("help"))
async def cmd_help(message: Message):
    text = (
        "<b>Доступные команды:</b>\n\n"
        "/start — Запустить бота\n"
        "/menu — Главное меню\n"
        "/help — Список команд\n\n"
        "Или используйте кнопки меню ниже."
    )
    await message.answer(text, reply_markup=main_menu_kb())
