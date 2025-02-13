import logging
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from bot import TELEGRAM_TOKEN

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# URL вашего FastAPI сервиса
FASTAPI_URL = "http://127.0.0.1:8000"  # Замените на ваш URL, если он отличается

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Отправь мне артикул, и я верну информацию о товаре.')

# Обработка текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    art = update.message.text
    try:
        # Делаем запрос к вашему FastAPI сервису
        response = requests.get(f"{FASTAPI_URL}/{art}")
        if response.status_code == 201:
            data = response.json()
            message = (
                f"Название: {data.get('name', 'Не указано')}\n"
                f"Описание: {data.get('description', 'Не указано')}\n"
                f"Цена: {data.get('price', 'Не указано')}\n"
                f"Ссылка: {data.get('link', 'Не указано')}"
            )
            await update.message.reply_text(message)
        else:
            await update.message.reply_text("Произошла ошибка при запросе к серверу.")
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        await update.message.reply_text("Произошла ошибка при обработке вашего запроса.")

# Обработка ошибок
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.warning(f'Update {update} caused error {context.error}')

# Основная функция
def main() -> None:
    # Вставьте сюда ваш токен
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Регистрация обработчиков
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()