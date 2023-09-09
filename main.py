from  aiogram import Bot,Dispatcher,executor,types
from api import shahar
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN=os.getenv('BOT_TOKEN')

bot=Bot(token=BOT_TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(msg:types.Message):
    await msg.answer('Assalomu allaykum')

@dp.message_handler()
async def weather(msg:types.Message):
    data=msg.text
    
    await msg.answer(shahar(data))



if __name__ == '__main__':
    executor.start_polling(dp)