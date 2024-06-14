from aiogram import types, Router
from aiogram.utils.i18n import gettext as _

echo_router = Router()


@echo_router.message()
async def bot_echo(message: types.Message):
    await message.reply(_("Echo message"))
