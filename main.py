import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from db import Database
from aiogram.filters import CommandStart
from aiogram.types import Message
import sys
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import datetime

scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
import sys
print(os.getenv("TOKEN"))
bot = Bot(os.getenv("TOKEN"))

dp = Dispatcher(bot=bot)
db = Database("database.db")


@dp.message(CommandStart())
async def start(message: Message) -> None:
    if message.chat.type == 'private':
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Добро пожаловать!")


from events import events


def update_event(name):
    for i in range(len(events)):
        if events[i]['name'] == name:
            events[i]['date'] += events[i]['respawn']
            print('\n')
            print(f"Следующее событие {events[i]['name']} произойдет: ", events[i]['date'])
            print('\n')
            return events[i]


def push_jobs(event):
    scheduler.add_job(send_all, trigger='date', next_run_time=event['date'], kwargs={'event': event})


async def send_all(event):
    users = db.get_users()
    for row in users:
        user = row[0]
        await bot.send_message(chat_id=user, text=event['name'])
    print("\n")
    print("Рассылка разослана")
    print("\n")
    event = update_event(event['name'])
    push_jobs(event)
    print(scheduler.get_jobs())


async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    for i in events:
        scheduler.add_job(send_all, trigger='date', next_run_time=i['date'], kwargs={'event': i})

    scheduler.print_jobs()
    scheduler.start()
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
