from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.i18n import gettext as _
from icecream import ic

from tgbot.keyboards.inline import go_back_keyboard
from tgbot.misc.init import cmc_client

user_stats_router = Router()


@user_stats_router.callback_query(F.data == "user_stats")
async def send_user_stats(callback: CallbackQuery, state: FSMContext):
    today_read = await cmc_client.get_user_read_count(chat_id=callback.from_user.id, today=True)
    week_read = await cmc_client.get_user_read_count(chat_id=callback.from_user.id, week=True)
    total_read = await cmc_client.get_user_read_count(chat_id=callback.from_user.id, total=True)
    user_data = await state.get_data()
    current_locale = user_data.get("locale")  # Default to 'uz' if not set
    ic(current_locale)
    a = _("📊 All your statistics:")
    ic(a)
    b = _("📖 Number of hadiths you have read: <b>{total_read}</b>").format(total_read=total_read)
    c = _("📆 You read <b>{today_read}</b> hadiths in one day!").format(today_read=today_read)
    d = _("📆 You read <b>{week_read}</b> hadiths per week!").format(week_read=week_read)
    result = "\n".join([a, b, c, d])
    ic(result)
    await callback.message.edit_text(text=result, reply_markup=go_back_keyboard())
