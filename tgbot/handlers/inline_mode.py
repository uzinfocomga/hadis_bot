from aiogram import Router, F, Bot
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from aiogram.utils.i18n import gettext as _
from icecream import ic

from tgbot.misc.init import cmc_client

inline_mode_router = Router()


@inline_mode_router.inline_query(F.query == "friends")
async def search_friend(inline_query: InlineQuery):
    results = []
    offset = int(inline_query.offset) if inline_query.offset else 0
    all_items = await cmc_client.get_friends(offset)
    for item in all_items:
        url = f'https://t.me/{item.get("username")}'
        thumb_url: str = "https://i.pinimg.com/736x/2d/75/50/2d7550d033be4f1f61b27bce357f6ff0.jpg"
        result = InlineQueryResultArticle(
            id=str(item.get("chat_id")),
            title=item.get("full_name"),
            input_message_content=InputTextMessageContent(message_text=url),
            description=url,
            thumb_url=thumb_url,
        )
        results.append(result)
    if len(results) < 50:
        await inline_query.answer(
            results, is_personal=True
        )
    else:
        await inline_query.answer(
            results, is_personal=True,
            next_offset=str(offset + 50)
        )

@inline_mode_router.inline_query(F.query.contains('friends'))
async def search_friend(inline_query: InlineQuery):
    query = inline_query.query.split('friends ')[1]
    results = []
    offset = int(inline_query.offset) if inline_query.offset else 0
    all_items = await cmc_client.get_friends(offset, q=query)
    for item in all_items:
        url = f'https://t.me/{item.get("username")}'
        thumb_url: str = "https://i.pinimg.com/736x/2d/75/50/2d7550d033be4f1f61b27bce357f6ff0.jpg"
        result = InlineQueryResultArticle(
            id=str(item.get("chat_id")),
            title=item.get("full_name"),
            input_message_content=InputTextMessageContent(message_text=url),
            description=url,
            thumb_url=thumb_url,
        )
        results.append(result)
    await inline_query.answer(
            results, is_personal=True
        )



@inline_mode_router.inline_query(F.query == "share_the_bot")
async def ulashish(query: InlineQuery):
    await query.answer(
        results=[
            InlineQueryResultArticle(
                id="56464df",
                title=_("Click to share the bot!"),
                input_message_content=InputTextMessageContent(
                    message_text=f"https://t.me/KameraUzumBot?start={query.from_user.id}"),
            )
        ], cache_time=1000
    )


@inline_mode_router.inline_query(F.query == "hadiths")
async def search_hadith(inline_query: InlineQuery):
    offset = int(inline_query.offset) if inline_query.offset else 0
    all_items = await cmc_client.get_hadiths(offset)

    results = []
    for hadith in all_items[:50]:
        title = hadith.get('UZBEKCHA_SARLAVHA', 'No Title')
        description = hadith.get('UZBEKCHA', '')
        hadith_id = hadith.get('hadith_id', 0)
        input_content = InputTextMessageContent(
            message_text=f"https://t.me/KameraUzumBot?start={inline_query.from_user.id}\n\n{description}"
        )

        result = InlineQueryResultArticle(
            id=str(hadith_id),
            title=title,
            description=description[:200],
            input_message_content=input_content,
        )
        results.append(result)

    await inline_query.answer(results=results, cache_time=10)

@inline_mode_router.inline_query(F.query.contains('hadiths '))
async def search_hadith(inline_query: InlineQuery):
    query = inline_query.query.split('hadiths ')[1]
    results = []
    offset = int(inline_query.offset) if inline_query.offset else 1
    all_items = await cmc_client.get_hadiths(offset, q=query)
    if not all_items:
        return
    for hadith in all_items:
        title = hadith.get('UZBEKCHA_SARLAVHA', 'No Title')
        description = hadith.get('UZBEKCHA', '')
        hadith_id = hadith.get('hadith_id', 0)
        input_content = InputTextMessageContent(
            message_text=f"https://t.me/KameraUzumBot?start={inline_query.from_user.id}\n\n{description}"
        )

        result = InlineQueryResultArticle(
            id=str(hadith_id),
            title=title,
            description=description[:200],
            input_message_content=input_content,
        )
        results.append(result)
    if len(results) < 50:
        await inline_query.answer(
            results, is_personal=True
        )
    else:
        await inline_query.answer(
            results, is_personal=True,
            next_offset=str(offset + 50)
        )