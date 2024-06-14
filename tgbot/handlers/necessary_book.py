from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils.i18n import gettext as _
from icecream import ic

from tgbot.keyboards.inline import start_keyboard, go_back_keyboard, has_next_page_keyboard, has_prev_page_keyboard, \
    has_both_page_keyboard
from tgbot.misc.init import cmc_client

necessary_book_router = Router()


@necessary_book_router.callback_query(F.data == "necessary_books")
async def handle_current_books(callback: CallbackQuery):
    await process_current_books_initial(callback)


@necessary_book_router.callback_query(F.data.startswith("book:"))
async def handle_next_books(callback: CallbackQuery):
    ic()
    current_page: int = int(callback.data.split(':')[-1])
    ic(current_page)
    await process_current_books_initial(callback, current_page=current_page)


async def process_current_books_initial(callback: CallbackQuery, current_page=1):
    current_books = await cmc_client.get_current_books(skip=(current_page - 1) * 10 if current_page > 1 else 0)
    ic(current_books)
    if current_books is None or 'necessary_books' not in current_books:
        await callback.message.edit_text(_("There are no books uploaded yet"), reply_markup=start_keyboard())
        return

    total_books_count = current_books.get('total_books_count')
    total_pages_count = current_books.get('total_pages_count')
    current_page = current_books.get('current_page')
    ic(current_page)
    ic()
    reply_markup = go_back_keyboard()
    prev_page: int = current_page - 1
    next_page: int = current_page + 1
    if total_pages_count > 1:
        if current_page == total_pages_count:
            reply_markup = has_prev_page_keyboard(prev_page=prev_page)
        elif current_page < total_pages_count:
            if current_page > 1:
                reply_markup = has_both_page_keyboard(prev_page=prev_page, next_page=next_page)
            elif current_page == 1:
                reply_markup = has_next_page_keyboard(next_page=next_page)

    current_books = current_books.get('necessary_books')
    await display_books(callback, current_books, reply_markup, total_books_count)


async def display_books(callback: CallbackQuery, current_books, reply_markup, total_books_count):
    ic()
    pre_text: str = _("<em><b>{count} books in total.</b></em>").format(
        count=total_books_count
    )
    main_text: str = "".join([
        f"\n<em><b>{book.get('id')})</b></em> 📖  {book.get('title')}"
        for book in current_books
    ])
    result: str = pre_text + main_text

    await callback.message.edit_text(text=result, reply_markup=reply_markup)
