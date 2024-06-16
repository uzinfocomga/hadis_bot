import asyncio
import logging

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.utils.i18n import gettext as _
from icecream import ic

from tgbot.config import load_config
from tgbot.handlers.user import user_start
from tgbot.keyboards.inline import start_keyboard, change_lang_keyboard
from tgbot.misc.states import ChangeLangState

change_lang_router = Router()
config = load_config(".env")


@change_lang_router.message(Command('language'))
async def change_lang_start(message: Message, state: FSMContext):
    #
    await state.set_state(ChangeLangState.choose_lang)
    await message.reply(
        # "Please select a language:\n"
        """Пожалуйста, выберите язык:\nIltimos tilni tanlang:""",
        reply_markup=change_lang_keyboard())

@change_lang_router.callback_query(F.data.in_({'en', 'ru', 'uz'}))
async def send_back_to_menu(callback: CallbackQuery, state: FSMContext):
    selected_lang = callback.data
    logging.debug(f"Selected language: {selected_lang}")

    await state.update_data({"locale": selected_lang})
    config.tg_bot.i18n.current_locale = selected_lang

    await callback.message.delete()
    await callback.message.answer(_("The language has been changed successfully"))