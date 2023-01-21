import requests
import json
from telegram.ext import Updater, CommandHandler, MessageHandler
updater1 = Updater(token='5891342745:AAEHt_8MJyU3GN8Njb5GeMMK_EHDXa6WOkg', use_context = True)
dispatcher = updater1.dispatcher

#def hello(update, context):
#    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello World")

#hello_handler = CommandHandler('hello', hello)
#dispatcher.add_handler(hello_handler)

updater1.start_polling()

def info(update, context):
    response = requests.get('https://api.covid19api.com/summary')
    if(response.status_code==200):
        data = response.json()
        date = data['Date'][:10]
        ans = f"Covid 19 Summary (as of {date}): \n";
        
        for attribute, value in data['Global'].items():
            if attribute not in ['NewConfirmed', 'NewDeaths', 'NewRecovered']:
                ans += 'Total ' + attribute[5::].lower() + " : " + str(value) + "\n"

        print(ans)
        context.bot.send_message(chat_id=update.effective_chat.id, text=ans)
    else:
        context.bot.send_message(chat_id=update.effective_chat_id, text="Error, something went wrong")

corona_info_handler = CommandHandler('info', info)
dispatcher.add_handler(corona_info_handler)