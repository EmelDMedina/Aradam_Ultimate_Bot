import os
import qrcode
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from telegram import ChatAction

INPUT_TEXT = 0

def start(update, context):
    
    update.message.reply_text("Hola humano, bienvenido, ¿Que desea hacer?\n\nUsa /qr para generar un código QR.")
    
def qr_command_handler(update, context):
    update.message.reply_text("Envíame el texto para generar un código QR.")
    
    return INPUT_TEXT

def generate_qr(text):
    
    filename = text + '.jpg'
    
    img = qrcode.make(text)
    img.save(filename)
    
    return filename

def send_qr(filename, chat):
    
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )
    
    chat.send_photo(
        photo=open(filename, 'rb')
    )
    
    os.unlink(filename)

def input_text(update, context):
    
    text = update.message.text
    
    filename = generate_qr(text)
    
    chat = update.message.chat
    
    send_qr(filename, chat)
    
    return ConversationHandler.END

if __name__ == '__main__':
    
    updater = Updater(token='5775123118:AAFpf08LJEqIAduaFTO-TKI_f_52Cau9dRo', use_context=True)
    
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start)) # add handler

dp.add_handler(ConversationHandler(
    entry_points=[
        CommandHandler('qr', qr_command_handler)],
    states={
        INPUT_TEXT: [MessageHandler(Filters.text, input_text)]},
    fallbacks=[]
))

updater.start_polling()
updater.idle()