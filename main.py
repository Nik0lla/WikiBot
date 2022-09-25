import telebot
import wikipedia


bot = telebot.TeleBot('some_digit')
wikipedia.set_lang('ru')

def getwiki(messge):
    try:
        page = wikipedia.page(messge)
        wikitext = page.content[:2000]

        return wikitext
    except Exception as e:
        return 'В базе нет информации об этом'

# Функция - обработчика команды /start
@bot.message_handler(commands=['start'])
def start(messge, res=False):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = telebot.types.KeyboardButton('Yandex')
    markup.add(button)
    bot.send_message(messge.chat.id, 'Я на сязи!', reply_markup=markup)
    print(messge)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))

bot.polling(none_stop=True, interval=10)
