from http.client import responses
from telegram.ext import *
import telegram
import token_key
from datetime import datetime

KEY = token_key.TOKEN_KEY
bot = telegram.Bot(token=KEY)
chat = '760332987'
pic = './garbarge_recycling.JPG'
today = datetime.today() #heutiger Tag

def umfrage(update,  context):
    
    if today.weekday() == 0: #Freitag mal nachfragen
        #update.message.reply_text("Beginning of inline keyboard")
        keyboard = [
            [
                telegram.InlineKeyboardButton("Tim", callback_data='1'),
                telegram.InlineKeyboardButton("Luca", callback_data='2'),
                telegram.InlineKeyboardButton("Elena", callback_data='3'),
                telegram.InlineKeyboardButton("Bin im Urlaub", callback_data='4'),
            ]
        ]

        reply_markup = telegram.InlineKeyboardMarkup(keyboard)
        update.message.reply_text("Na schon fleißig geputzt?", reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    query.answer()
    # This will define which button the user tapped on (from what you assigned to "callback_data". As I assigned them "1" and "2"):
    choice = query.data
    
    # Now u can define what choice ("callback_data") do what like this:
    if choice  == '1':
        bot.send_message(chat_id=chat, text="Yey Tim!")

    if choice == '2':
        bot.send_message(chat_id=chat, text="Yey Luca!")

    if choice == '3':
        bot.send_message(chat_id=chat, text="Yey Elena!")
    
    if choice == '4':
        bot.send_message(chat_id=chat, text="Ok dann viel Spaß da!")

def main ():
    updater = Updater(KEY) #kommunukation mit Telegram
    dp = updater.dispatcher #Senden

    week= today.isocalendar()[1]
    week_no = week%3

    if today.weekday() == 0: #Sonntags Putzplan posten
        if week_no == 0:
            bot.send_photo(chat_id=chat, photo=open(pic, 'rb'))
            bot.send_message(chat_id=chat, text="Bad!")
        if week_no == 1:
            bot.send_photo(chat_id=chat, photo=open(pic, 'rb'))
            bot.send_message(chat_id=chat, text="Küche!")
        if week_no == 2:
            bot.send_photo(chat_id=chat, photo=open(pic, 'rb'))
            bot.send_message(chat_id=chat, text="Flur+Wozi!")

    if today.weekday() == 0: #Sonntags Putzplan posten
        bot.send_message(chat_id=chat, text="Na wollt ihr die Umfrage? Dann /umfrage eingeben :)")

    dp.add_handler(CommandHandler('umfrage', umfrage)) #Dispatcher kann Nachrichten verarbeiten
    dp.add_handler(CallbackQueryHandler(button))
    updater.start_polling(0) #wie oft gecheckt werden soll in sekunden
 


if __name__ == "__main__":
    main()
    
 

