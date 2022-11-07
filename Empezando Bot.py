from telegram.ext import Updater, CommandHandler

def start(update, context):
    
    update.message.reply_text('Hola humano!')

if __name__ == '__main__':
    
    updater = Updater(token='5775123118:AAFpf08LJEqIAduaFTO-TKI_f_52Cau9dRo', use_context=True)
    
dp = updater.dispatcher

# add handler

dp.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()