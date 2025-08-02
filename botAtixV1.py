

import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# Configurazione logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Il tuo token
TOKEN = '8209059450:AAFFP8iSoH1pS1YiZCGFcvAI68Pz0GzNd7s'  # tastiera


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /start con menu fisso sopra la tastiera"""
    keyboard = [
        [KeyboardButton("Temperatura CP 123")],  # Tc123
        [KeyboardButton("Temperatura CP 45")],  # Tc45
        [KeyboardButton("Temperatura Cella 8")],  # Tc8
    ]
    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,     # adatta la tastiera alla larghezza
        one_time_keyboard=False   # rimane visibile
    )
    await update.message.reply_text(
        'Scegli un’opzione dal menu:',
        reply_markup=reply_markup
    )


async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if (
        text == "Temperatura CP 123"
        or text == "Temperatura CP 45"
        or text == "Temperatura Cella 8"
    ):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            # text=f'Ecco i dati per la zona {text}:'
            text='Waiting for data from the plant...'
        )
    else:
        return


def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler)
    )

    application.run_polling()


if __name__ == '__main__':
    main()
