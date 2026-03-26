"""Inline-клавиатуры бота-визитки."""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import SERVICES, COMPANY


def main_menu_kb() -> InlineKeyboardMarkup:
    """Главное меню."""
    buttons = [
        [InlineKeyboardButton(text="📋 Наши услуги", callback_data="services")],
        [InlineKeyboardButton(text="ℹ️ О нас", callback_data="about")],
        [InlineKeyboardButton(text="📞 Контакты", callback_data="contacts")],
        [InlineKeyboardButton(text="🕐 Часы работы", callback_data="hours")],
        [InlineKeyboardButton(text="💬 Написать нам", url=f"https://t.me/{COMPANY['telegram'].lstrip('@')}")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def services_list_kb() -> InlineKeyboardMarkup:
    """Список услуг."""
    buttons = []
    for i, service in enumerate(SERVICES):
        buttons.append([
            InlineKeyboardButton(
                text=f"🔹 {service['name']}",
                callback_data=f"service_{i}",
            )
        ])
    buttons.append([InlineKeyboardButton(text="◀️ Назад", callback_data="menu")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def service_detail_kb(service_index: int) -> InlineKeyboardMarkup:
    """Кнопки под карточкой услуги."""
    buttons = [
        [InlineKeyboardButton(
            text="📩 Заказать эту услугу",
            url=f"https://t.me/{COMPANY['telegram'].lstrip('@')}?text=Хочу заказать: {SERVICES[service_index]['name']}",
        )],
        [InlineKeyboardButton(text="◀️ К списку услуг", callback_data="services")],
        [InlineKeyboardButton(text="🏠 Главное меню", callback_data="menu")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def contacts_kb() -> InlineKeyboardMarkup:
    """Кнопки контактов."""
    buttons = [
        [InlineKeyboardButton(text="💬 Telegram", url=f"https://t.me/{COMPANY['telegram'].lstrip('@')}")],
        [InlineKeyboardButton(text="🌐 Сайт", url=COMPANY["website"])],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="menu")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def back_to_menu_kb() -> InlineKeyboardMarkup:
    """Кнопка возврата в меню."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="◀️ Главное меню", callback_data="menu")],
    ])
