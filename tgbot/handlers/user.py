from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _
from icecream import ic

from tgbot.keyboards.inline import start_keyboard
from tgbot.misc.init import cmc_client

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    user = await cmc_client.get_user(chat_id=message.from_user.id)
    if user is None:
        await cmc_client.add_user(chat_id=message.from_user.id, full_name=message.from_user.full_name,
                                  username=message.from_user.username, language=message.from_user.language_code)

    await message.answer(_("Welcome to the main menu!"), reply_markup=start_keyboard())
