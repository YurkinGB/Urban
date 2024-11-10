from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup

api = '7658059209:AAGs2TyqlQCo6J9nAyUr75mbKABzbv6b_G0'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['Start',])
async def chat_start(message):
    await message.answer(f'Введите слово "Calories"')

@dp.message_handler(text='Calories')
async def set_age(message):
    await message.answer(f'Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer(f'Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer(f'Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 10 * int(data['growth']) + 6,25 * int(data['weight']) - 5 * int(data['age']) - 161
    await message.answer(f'Ваша норма калорий {calories}')
    await state.finish

@dp.message_handler()
async def all_message(message):
    await message.answer(f'чтобы продолжить введите слово "Calories"')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
