from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os
from dotenv import load_dotenv
import time

load_dotenv()



bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)

print ("\nBot started")

@dp.message_handler(commands=["start"])
async def send_msg(message: types.Message):
    import vk_parser
    while True:
        vk_parser.print_counter()
        await message.answer(vk_parser.result())
        time.sleep (30)
    

if __name__ == "__main__":
    executor.start_polling(dp)
    

 
