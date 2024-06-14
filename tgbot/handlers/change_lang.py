from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.utils import i18n
from aiogram.utils.i18n import gettext as _

from tgbot.config import load_config
from tgbot.keyboards.inline import start_keyboard, change_lang_keyboard

change_lang_router = Router()
config = load_config(".env")


@change_lang_router.message(Command('language'))
async def change_lang_start(message: Message, state: FSMContext):
    # await state.set_state(ChangeLangState.choose_lang)
    await message.reply(
        """Please select a language:\nПожалуйста, выберите язык:\nIltimos tilni tanlang:""",
        reply_markup=change_lang_keyboard())


@change_lang_router.callback_query(F.data.in_({'en', 'ru', 'uz'}))
async def send_back_to_menu(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'en':
        # logging.warning('en') # = 'en'
        await state.update_data({"locale": 'en'})
        config.tg_bot.i18n.current_locale = 'en'
        i18n.current_locale = 'en'
    elif callback.data == 'ru':
        # await callback.answer(_("Language set.", locale='ru'))
        # await callback.answer(_("Language set.", locale='uz'))
        await state.update_data({"locale": 'ru'})
        config.tg_bot.i18n.current_locale = 'ru'
        i18n.current_locale = 'ru'
    elif callback.data == 'uz':
        await state.update_data({"locale": 'uz'})
        config.tg_bot.i18n.current_locale = 'uz'
        i18n.current_locale = 'uz'
    await callback.message.reply(_("Welcome to the main menu!"), reply_markup=start_keyboard())
