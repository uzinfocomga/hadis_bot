"""Import all routers and add them to routers_list."""
from . import necessary_book
from .admin import admin_router
from .back_to_menu import back_to_menu_router
from .change_lang import change_lang_router
from .echo import echo_router
from .hadith import hadith_router
from .inline_mode import inline_mode_router
from .necessary_book import necessary_book_router
from .top_stats import top_stats_router
from .user import user_router
from .user_stats import user_stats_router

routers_list = [
    # admin_router,
    user_router,
    user_stats_router,
    top_stats_router,
    back_to_menu_router,
    inline_mode_router,
    change_lang_router,
    necessary_book_router,
    hadith_router,
    # echo_router,  # echo_router must be last
]

__all__ = [
    "routers_list",
]
