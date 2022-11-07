from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

INPUT_TEXT = 0

def start(update, context):
    
    button1 = InlineKeyboardButton(
        text='Sobre el autor',
        url ='https://vulpxvenandi25.itch.io/'
    )
    
    button2 = InlineKeyboardButton(
        text='Twitter',
        url ='https://twitter.com/EmelD75746168'
    )
    
    update.message.reply_text(
        text='Haz click en un botón',
        reply_markup=InlineKeyboardMarkup([
            [button1],
            [button2]
        ]))

if __name__ == '__main__':
    
    updater = Updater(token='5775123118:AAFpf08LJEqIAduaFTO-TKI_f_52Cau9dRo', use_context=True)
    
dp = updater.dispatcher


dp.add_handler(CommandHandler('start', start)) # add handler

updater.start_polling()
updater.idle()