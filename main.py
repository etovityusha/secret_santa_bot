import asyncio
import copy
import random
from typing import Coroutine, Any

from aiogram import Bot, Dispatcher, executor, types

from settings import API_TOKEN, OWNER
from users import User, users

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)


async def cmd_start(message: types.Message) -> None:
    if users:
        sub = f"{', '.join([f'@{user.username} ' for user in users])}уже здесь!"
    else:
        sub = "Пока ты первый!"
    message_text = f"""
    Привет! {sub}
    \nМой хозяин нажмет /roll и ты сможешь узнать, кому ты даришь подарок!
    \nНадеюсь, ты не забудешь!
    """
    tasks = [bot.send_message(u.id, f"Пользователь @{message.from_user.username} с нами! Ура!") for u in users]
    users.add(User(id=message.from_user.id, username=message.from_user.username))
    await message.answer(message_text)
    await asyncio.gather(*tasks)


async def cmd_off(message: types.Message) -> None:
    users.remove(User(id=message.from_user.id, username=message.from_user.username))
    for u in users:
        await bot.send_message(u.id, f"Пользователь @{message.from_user.username} покинул нас! Позор!")
    await message.answer("Пока! (Позор)")


async def cmd_here(message: types.Message) -> None:
    await message.answer(f"{', '.join([f'@{user.username} ' for user in users])}уже здесь!")


async def cmd_roll(message: types.Message) -> None:
    if message.from_user.username == OWNER:
        already_has_gift: set[User] = set()
        if len(users) == 1:
            await message.answer("Forever alone. Покупай себе подарок!")
        messages: list[Coroutine[Any, Any, Any]] = []
        for u in users:
            if c := copy.copy(users) - already_has_gift - {u}:
                gift = random.choice(list(c))
                messages.append(
                    bot.send_message(u.id, f"Поздравляю! Ты покупаешь подарок для @{gift.username}! "
                                           f"Ну и не повезло тебе!"))

                already_has_gift.add(gift)
        await asyncio.gather(*messages)
    else:
        await message.answer("Ты не мой хозяин!")


async def all_other(message: types.Message) -> None:
    await message.answer("Писать сюда не нужно, пожалуйста, используй команду /here, чтобы узнать кто уже с нами!"
                         "Можешь написать /off, чтобы не участвовать. Но все об этом узнают и получится позор!")


def register_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.register_message_handler(cmd_start, commands='start')
    dispatcher.register_message_handler(cmd_off, commands='off')
    dispatcher.register_message_handler(cmd_here, commands='here')
    dispatcher.register_message_handler(cmd_roll, commands='roll')
    dispatcher.register_message_handler(all_other)


if __name__ == '__main__':
    dp = Dispatcher(bot)
    register_handlers(dp)
    executor.start_polling(dp, skip_updates=True)
