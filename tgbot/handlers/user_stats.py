from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils.i18n import gettext as _
from icecream import ic

from tgbot.keyboards.inline import go_back_keyboard
from tgbot.misc.init import cmc_client

user_stats_router = Router()


@user_stats_router.callback_query(F.data == "user_stats")
async def send_user_stats(callback: CallbackQuery):
    today_read = await cmc_client.get_user_read_count(chat_id=callback.from_user.id, today=True)
    ic(today_read)
    week_read = await cmc_client.get_user_read_count(chat_id=callback.from_user.id, week=True)
    total_read = await cmc_client.get_user_read_count(chat_id=callback.from_user.id)
    stats = [
        _("📊 All your statistics:"),
        _("📖 Number of hadiths you have read: <b>{total_read}</b>").format(total_read=total_read),
        # _("🔋 You have read <b>{a}</b> of the total number of hadiths!").format(a=0),
        _("📆 You read <b>{today_read}</b> hadiths in one day!").format(today_read=today_read),
        _("📆 You read <b>{week_read}</b> hadiths per week!").format(week_read=week_read),
        # _("👥 Number of people you have invited: <b>{count_invited}</b>").format(count_invited=0),
    ]
    result = "\n".join(stats)
    await callback.message.edit_text(text=result, reply_markup=go_back_keyboard())
