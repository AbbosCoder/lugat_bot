from aiogram.dispatcher.filters.state import State, StatesGroup


class PanelStates(StatesGroup):
    add_admin = State()
    remove_admin = State()

class SendMsg(StatesGroup):
    xabar = State()

class NEW_user(StatesGroup):
    user_id = State()

class SendADS(StatesGroup):
    ads = State()

