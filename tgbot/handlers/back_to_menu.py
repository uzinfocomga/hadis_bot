from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils.i18n import gettext as _

from tgbot.keyboards.inline import start_keyboard

back_to_menu_router = Router()


@back_to_menu_router.callback_query(F.data == "back_to_menu")
async def send_back_to_menu(callback: CallbackQuery):
    await callback.message.edit_text(_("Welcome to the main menu!"), reply_markup=start_keyboard())
