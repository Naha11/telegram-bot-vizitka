"""Обработчики callback-кнопок."""

from aiogram import Router, F
from aiogram.types import CallbackQuery

from config import COMPANY, SERVICES, WORKING_HOURS, ABOUT_TEXT
from keyboards import (
    main_menu_kb,
    services_list_kb,
    service_detail_kb,
    contacts_kb,
    back_to_menu_kb,
)

router = Router()


@router.callback_query(F.data == "menu")
async def cb_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        "Главное меню:",
        reply_markup=main_menu_kb(),
    )
    await callback.answer()


@router.callback_query(F.data == "services")
async def cb_services(callback: CallbackQuery):
    text = "📋 <b>Наши услуги</b>\n\nВыберите услугу для подробной информации:"
    await callback.message.edit_text(
        text,
        reply_markup=services_list_kb(),
    )
    await callback.answer()


@router.callback_query(F.data.startswith("service_"))
async def cb_service_detail(callback: CallbackQuery):
    index = int(callback.data.split("_")[1])
    if index < 0 or index >= len(SERVICES):
        await callback.answer("Услуга не найдена", show_alert=True)
        return

    service = SERVICES[index]
    text = (
        f"🔹 <b>{service['name']}</b>\n\n"
        f"{service['description']}\n\n"
        f"💰 Стоимость: {service['price']}\n"
        f"⏱ Срок: {service['time']}"
    )
    await callback.message.edit_text(
        text,
        reply_markup=service_detail_kb(index),
    )
    await callback.answer()


@router.callback_query(F.data == "about")
async def cb_about(callback: CallbackQuery):
    text = ABOUT_TEXT.format(
        company_name=COMPANY["name"],
        description=COMPANY["description"],
    )
    await callback.message.edit_text(
        text,
        reply_markup=back_to_menu_kb(),
    )
    await callback.answer()


@router.callback_query(F.data == "contacts")
async def cb_contacts(callback: CallbackQuery):
    text = (
        f"📞 <b>Контакты</b>\n\n"
        f"📱 Телефон: {COMPANY['phone']}\n"
        f"📧 Email: {COMPANY['email']}\n"
        f"💬 Telegram: {COMPANY['telegram']}\n"
        f"🌐 Сайт: {COMPANY['website']}\n"
        f"📍 Адрес: {COMPANY['address']}"
    )
    await callback.message.edit_text(
        text,
        reply_markup=contacts_kb(),
    )
    await callback.answer()


@router.callback_query(F.data == "hours")
async def cb_hours(callback: CallbackQuery):
    lines = [f"📅 <b>{day}:</b> {hours}" for day, hours in WORKING_HOURS.items()]
    text = "🕐 <b>Часы работы</b>\n\n" + "\n".join(lines)
    await callback.message.edit_text(
        text,
        reply_markup=back_to_menu_kb(),
    )
    await callback.answer()
