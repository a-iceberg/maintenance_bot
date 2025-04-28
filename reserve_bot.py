import sys
import logging
import asyncio
from telebot import async_telebot
from telebot.asyncio_helper import ApiTelegramException


logging.basicConfig(
    filename='reserve_bot.log',
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if len(sys.argv) != 2:
    logger.error("Usage: python reserve_bot.py <bot_token>")
    sys.exit(1)
token = sys.argv[1]

bot = async_telebot.AsyncTeleBot(token)

@bot.message_handler(func=lambda message: True)
async def answer(message):
    if message.text:
        user_message = message.text
        chat_id = message.chat.id
        message_id = message.message_id

        if user_message.startswith("/start"):
            await bot.delete_message(
                chat_id,
                message_id
            )
            welcome_message = """
                Здраствуйте, это сервисный центр.
Извините, ассистент временно недоступен.
Пожалуйста, свяжитесь с нами по телефону +74954635046 для дальнейшей помощи
            """
            await bot.send_message(
                chat_id,
                welcome_message
            )
        else:   
            auto_message = """
                Извините, ассистент временно недоступен.
Пожалуйста, свяжитесь с нами по телефону +74954635046 для дальнейшей помощи
            """
            await bot.send_message(
                chat_id,
                auto_message
            )

async def main():
    try:
        try:
            await bot.remove_webhook()
        except ApiTelegramException as e:
            if e.error_code == 404:
                logger.info("Webhook was not set. Continuing without removal")
            else:
                raise
        await bot.polling(non_stop=True, interval=0)
    except Exception as e:
        logger.error(f"Error in pooling: {e}")
    finally:
        await bot.close_session()

if __name__ == "__main__":
    asyncio.run(main())
