from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils.i18n import gettext as _

from tgbot.keyboards.inline import go_back_keyboard
from tgbot.misc.init import cmc_client

top_stats_router = Router()


@top_stats_router.callback_query(F.data == "top_stats")
async def send_top_stats(callback: CallbackQuery):
    total_top_users = await cmc_client.get_top_users_stats(top_total=True)
    week_top_users = await cmc_client.get_top_users_stats(top_week=True)
    today_top_users = await cmc_client.get_top_users_stats(top_today=True)

    def format_stats(users, title):
        stats = [f"{title}:"]
        for index, user_data in enumerate(users, start=1):
            user = user_data['user']
            stats.append(
                f"<b>{index}.</b> <a href='https://t.me/{user['username']}'>{user['full_name']}</a>  <b>{user_data['read_count']}</b> 📖")
        return "\n".join(stats)

    overall_stats = format_stats(total_top_users, _("<b>🥇 Overall Top Rating:</b>"))
    weekly_stats = format_stats(week_top_users, _("<b>🥈 Weekly Top Rating:</b>"))
    daily_stats = format_stats(today_top_users, _("<b>🥉 Daily Top Rating:</b>"))

    result = "\n\n".join([overall_stats, weekly_stats, daily_stats])

    await callback.message.edit_text(text=result, reply_markup=go_back_keyboard())