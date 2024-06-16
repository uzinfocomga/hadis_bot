
    # ic(inline_query.query)
        # ic(inline_query.from_user.get_profile_photos().keys())
        # ic(thumb_url)
        # ic(results)
        # ic(results)

    # await inline_query.answer(results=results, cache_time=10)
    # if hadiths_response is None or 'hadiths' not in hadiths_response:
        # Handle case where the request timed out or failed
        # await inline_query.answer(results=[], cache_time=10)
        # return

    # all_items = hadiths_response['hadiths']

# @inline_mode_router.inline_query(F.query.contains('hadiths'))
# @inline_mode_router.inline_query(F.query == "hadiths")
# async def search_hadith(inline_query: InlineQuery):
#     results = []
#     # Высчитываем offset как число
#     offset = int(inline_query.offset) if inline_query.offset else 1
#     all_items = await cmc_client.get_hadiths(offset)
#     for hadith in all_items:
#         title = hadith.get('UZBEKCHA_SARLAVHA', 'No Title')
#         description = hadith.get('UZBEKCHA', '')
#         hadith_id = hadith.get('hadith_id', 0)
#         input_content = InputTextMessageContent(
#             message_text=f"https://t.me/KameraUzumBot?start={inline_query.from_user.id}\n\n{description}"
#         )
#
#         result = InlineQueryResultArticle(
#             id=str(hadith_id),
#             title=title,
#             description=description[:200],  # Trim description if it's too long
#             input_message_content=input_content,
#         )
#         results.append(result)
#
#     # await inline_query.answer(results=results, cache_time=10)
#     if len(results) < 50:
#         await inline_query.answer(
#             results, is_personal=True
#         )
#     else:
#         await inline_query.answer(
#             results, is_personal=True,
#             next_offset=str(offset + 50)
#         )


    # if inline_query.query == "hadiths":
    # if len(inline_query.query.split('hadiths')) > 1 else None
    # ic(query)
    # Высчитываем offset как число
    # ic(offset)


    # await inline_query.answer(results=results, cache_time=10)
        # logging.warning('en') # = 'en'
        # await callback.answer(_("Language set.", locale='ru'))
        # await callback.answer(_("Language set.", locale='uz'))
    # ic(all_items)


# @top_stats_router.callback_query(F.data == "top_stats")
# async def send_top_stats(callback: CallbackQuery):
#     total_top_users = await cmc_client.get_top_users_stats(top_total=True)
#     week_top_users = await cmc_client.get_top_users_stats(top_week=True)
#     today_top_users = await cmc_client.get_top_users_stats(top_today=True)
#     stats = [
#         _("🏆 Overall Top Rating:"),
#         f"{total_top_users} 📖",
#         _("🏆 Weekly Top Rating:"),
#         f"{week_top_users} 📖",
#         _("🏆 Daily Top Rating:"),
#         f"{today_top_users} 📖",
#     ]
#     result = "\n".join(stats)
#     await callback.message.edit_text(text=result, reply_markup=go_back_keyboard())
        # _("🔋 You have read <b>{a}</b> of the total number of hadiths!").format(a=0),
        # _("👥 Number of people you have invited: <b>{count_invited}</b>").format(count_invited=0),
        # i18n.current_locale = 'en'
        # i18n.current_locale = 'ru'
        # i18n.current_locale = 'uz'
        # ic(i18n.current_locale)
    # user_data = await state.get_data()
    # current_locale = user_data.get("locale", 'uz')  # Default to 'uz' if not set

# logging.basicConfig(level=logging.DEBUG)


# async def reload():
    # Implement async operations to reload translations here
    # For example:
    # await asyncio.sleep(1)  # Placeholder for actual async work
    # return  # Ensure this method returns an awaitable object (a coroutine)

    # await reload()

    # logging.debug(f"Current locale set to: {config.tg_bot.i18n.current_locale}")
    # logging.debug("Translations reloaded successfully")
    # except Exception as e:
    #     logging.error(f"Error reloading translations: {e}")
    # await callback.message.answer(_("Welcome to the main menu!"), reply_markup=start_keyboard(), locale=config.tg_bot.i18n.current_locale)
