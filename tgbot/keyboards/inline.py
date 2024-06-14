import time

from aiogram.types import InlineKeyboardButton
from aiogram.utils.i18n import gettext as _
from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        InlineKeyboardButton(text=_("📖 Hadiths!"), callback_data="hadith"),
        InlineKeyboardButton(text=_("📚 Necessary books!"), callback_data="necessary_books")
    )
    keyboard.row(
        InlineKeyboardButton(text=_("🔎 Search for friends!"), switch_inline_query_current_chat="friends"),
        InlineKeyboardButton(text=_("🔎 Search for hadith!"), switch_inline_query_current_chat="hadiths")
    )
    keyboard.row(
        InlineKeyboardButton(text=_("🏆 Top rating!"), callback_data="top_stats"),
        InlineKeyboardButton(text=_("📊 My statistics!"), callback_data="user_stats")
    )
    keyboard.row(
        InlineKeyboardButton(text=_("👥 Share the bot with friends!"), switch_inline_query="share_the_bot")
    )
    return keyboard.as_markup()


def go_back_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        InlineKeyboardButton(text=_("↩️ Main menu!"), callback_data="back_to_menu"),
        InlineKeyboardButton(text=_("📬 Share the bot!"), switch_inline_query="share_the_bot")
    )
    return keyboard.as_markup()


def change_lang_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        InlineKeyboardButton(text="🇺🇿 UZ", callback_data="uz"),
        InlineKeyboardButton(text="🇷🇺 RU", callback_data="ru"),
        InlineKeyboardButton(text="🇺🇸 US", callback_data="en"),
    )
    return keyboard.as_markup()


def hadith_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        InlineKeyboardButton(text=_("Skip ❌"), callback_data=f"hadith:skip:{time.time()}"),
        InlineKeyboardButton(text=_("Read ✅"), callback_data=f"hadith:read:{time.time()}"),
    )
    keyboard.row(
        InlineKeyboardButton(text=_("Like ⭐"), callback_data=f"hadith:like:{time.time()}"),
        InlineKeyboardButton(text=_("📬 Share the bot!"), switch_inline_query="share_the_bot"),
    )
    keyboard.row(
        InlineKeyboardButton(text=_("↩️ Main menu!"), callback_data="back_to_menu"),
    )
    return keyboard.as_markup()


def has_both_page_keyboard(prev_page=1, next_page=3):
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        InlineKeyboardButton(text="⬅️", callback_data=f"book:prev_page:{prev_page}"),
        InlineKeyboardButton(text="➡️", callback_data=f"book:next_page:{next_page}"),
    )
    keyboard.row(
        InlineKeyboardButton(text=_("↩️ Main menu!"), callback_data="back_to_menu"),
        InlineKeyboardButton(text=_("📬 Share the bot!"), switch_inline_query="share_the_bot")
    )
    return keyboard.as_markup()


def has_next_page_keyboard(next_page=2):
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        InlineKeyboardButton(text="➡️", callback_data=f"book:next_page:{next_page}"),
    )
    keyboard.row(
        InlineKeyboardButton(text=_("↩️ Main menu!"), callback_data="back_to_menu"),
        InlineKeyboardButton(text=_("📬 Share the bot!"), switch_inline_query="share_the_bot")
    )
    return keyboard.as_markup()


def has_prev_page_keyboard(prev_page=1):
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        InlineKeyboardButton(text="⬅️", callback_data=f"book:prev_page:{prev_page}"),
    )
    keyboard.row(
        InlineKeyboardButton(text=_("↩️ Main menu!"), callback_data="back_to_menu"),
        InlineKeyboardButton(text=_("📬 Share the bot!"), switch_inline_query="share_the_bot")
    )
    return keyboard.as_markup()
