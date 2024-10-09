from aiogram.fsm.state import State, StatesGroup

# FSM состояния для добавления данных пользователя
class AddUserDetails(StatesGroup):
    waiting_for_name = State()
    waiting_for_city = State()
    waiting_for_dob = State()

# FSM состояния для запроса к GPT
class Req_GPT(StatesGroup):
    question = State()