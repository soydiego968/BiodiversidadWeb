import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from telegram import Update
import responses  

API_TOKEN = '7573530917:AAG82y3nb4kkVDaPMiOimp3PctOt-1WbBG0'


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logging.info('Iniciando Bot...')


async def start_command(update: Update, context):
    
    await update.message.reply_text('¡Hola! Soy tu bot de Telegram. ¿En qué puedo ayudarte?')

async def help_command(update: Update, context):
   
    await update.message.reply_text(
        'Comandos disponibles:\n'
        '/start - Iniciar el bot\n'
        '/help - Mostrar ayuda\n'
        '/custom - Comando personalizado'
    )

async def custom_command(update: Update, context):
   
    await update.message.reply_text('Este es un comando personalizado. ¡Escribe lo que quieras!')

async def handle_message(update: Update, context):
    
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) escribió: {text}')
    
    
    response = responses.get_response(text)  
    
  
    await update.message.reply_text(response)

async def error(update: Update, context):
    
    logging.error(f'Update {update} causó el error: {context.error}')

if __name__ == '__main__':
    
    app = ApplicationBuilder().token(API_TOKEN).build()
    
   
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    
    
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    
    app.add_error_handler(error)
    
    
    logging.info('El bot está ejecutándose...')
    app.run_polling(poll_interval=1.0)
