import time

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils.i18n import gettext as _

from tgbot.keyboards.inline import hadith_keyboard
from tgbot.misc.init import cmc_client

hadith_router = Router()


@hadith_router.callback_query(F.data == "hadith")
async def handle_hadith_start(callback: CallbackQuery):
    await process_initial_hadith(callback)


@hadith_router.callback_query(F.data.startswith('hadith:'))
async def handle_hadith_action(callback: CallbackQuery):
    await process_subsequent_hadith(callback)


async def process_initial_hadith(callback: CallbackQuery):
    try:
        user = await get_user_for_initial(callback)
        hadith_id = user.get('pending_hadith_id')
        await display_initial_hadith(callback, hadith_id)
    except Exception as e:
        print(e)


async def get_user_for_initial(callback: CallbackQuery):
    user = await cmc_client.get_user(chat_id=callback.from_user.id)
    return user


async def display_initial_hadith(callback: CallbackQuery, hadith_id):
    hadith = await cmc_client.get_hadith(hadith_id=hadith_id)
    await callback.message.edit_text(
        text=hadith[_('UZBEKCHA')],
        reply_markup=hadith_keyboard()
    )


# Helper Functions for Subsequent Hadith Processing
async def process_subsequent_hadith(callback: CallbackQuery):
    try:
        if time.time() - float(callback.data.split(':')[-1]) <= 3.0:
            await callback.answer(_("Don't read hadith too fast!"), show_alert=True)
        user = await get_user_for_subsequent(callback)
        await update_read_history_and_id_for_subsequent(user)
        hadith_id = user.get('pending_hadith_id')
        if 'like' in callback.data or 'read' in callback.data:
            if 'like' in callback.data:
                await add_to_favorites(user_id=user.get("id"), hadith_id=hadith_id - 1)
            await add_to_read(user_id=user.get("id"), hadith_id=hadith_id - 1)
        await display_subsequent_hadith(callback, hadith_id)
    except Exception as e:
        print(e)


async def get_user_for_subsequent(callback: CallbackQuery):
    user = await cmc_client.get_user(chat_id=callback.from_user.id)
    return user


async def update_read_history_and_id_for_subsequent(user):
    user_id = user.get('id')
    hadith_id = user.get('pending_hadith_id')
    await cmc_client.create_read_history(user_id=user_id, hadith_id=hadith_id)
    await cmc_client.update_read_hadith_id(user_id=user.get("chat_id"), hadith_id=hadith_id + 1)
    user['pending_hadith_id'] += 1


async def display_subsequent_hadith(callback: CallbackQuery, hadith_id):
    hadith = await cmc_client.get_hadith(hadith_id=hadith_id)
    await callback.message.edit_text(
        text=hadith[_('UZBEKCHA')],
        reply_markup=hadith_keyboard()
    )


async def add_to_favorites(user_id, hadith_id):
    like = await cmc_client.add_liked_hadith(user_id, hadith_id)
    return like


async def add_to_read(user_id, hadith_id):
    like = await cmc_client.add_read_hadith(user_id, hadith_id)
    return like
