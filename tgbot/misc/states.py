from aiogram.fsm.state import StatesGroup, State


class ChangeLangState(StatesGroup):
    choose_lang = State()
