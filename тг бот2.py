import telebot
import con1
bot=telebot.TeleBot(con1.TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "привет", parse_mode='html')
@bot.message_handler(commands=['rar'])
def rar(message):
    for i in open('idmymom.txt', 'r').readlines():
        bot.send_message(i, "привет")
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'ты написал: ' + message.text)
bot.polling(none_stop=True) 
