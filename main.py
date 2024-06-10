from aiogram import Dispatcher, Bot, executor, types
from config import API_KEY
import database

bot = Bot(token=API_KEY)
dp = Dispatcher(bot)

database.init_db()

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('Привет! Я бот для управления задачами. Используйте /add для добавления задачи, /list для просмотра всех задач и /delete для удаления задачи.')

@dp.message_handler(commands='add')
async def add(message: types.Message):
    task = message.get_args()
    if task:
        username = message.from_user.username
        database.add_task(username, task)
        await message.reply(f"Задача '{task}' добавлена!")
    else:
        await message.reply('Пожалуйста, укажите задачу через команду /add. Пример: /add Написать отчет')

@dp.message_handler(commands=['list'])
async def list_tasks(message: types.Message):
    tasks = database.get_tasks()
    if tasks:
        tasks_list = "\n".join([f"{task[0]}. {task[1]} (Добавлено пользователем @{task[2]})" for task in tasks])
        await message.reply(f"Ваши задачи:\n{tasks_list}")
    else:
        await message.reply("У вас нет задач.")

@dp.message_handler(commands=['delete'])
async def delete_task(message: types.Message):
    task_id = message.get_args()
    if task_id.isdigit():
        database.delete_task(int(task_id))
        await message.reply(f"Задача с ID {task_id} удалена.")
    else:
        await message.reply("Пожалуйста, укажите корректный ID задачи после команды /delete. Пример: /delete 1")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
