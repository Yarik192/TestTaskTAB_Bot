from aiogram.dispatcher.filters.state import StatesGroup, State


class RegistrationState(StatesGroup):
    """
    Состояние для отслеживания ввода пароля.
    """
    password = State()
