import telebot

bot = telebot.TeleBot('1756217731:AAFJZYYU9GrQezzgSrHCHOdZ1hvW0Cg5Zoo')

<<<<<<< Updated upstream

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
                 f'Я бот-гид по Солнечной системе. Приятно познакомиться, {message.from_user.first_name}, и да '
                 f'прибудет с тобой сила!')

=======
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуй путник! Ты написал мне /start')
>>>>>>> Stashed changes

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, это гид по Солнечной системе!')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай!')


bot.polling()
