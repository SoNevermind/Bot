import telebot

bot = telebot.TeleBot('1756217731:AAFJZYYU9GrQezzgSrHCHOdZ1hvW0Cg5Zoo')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
                 f'Я бот-гид по Солнечной системе. Приятно познакомиться, {message.from_user.first_name}, и да '
                 f'прибудет с тобой сила!')


@bot.message_handler(commands=['Привет'])
def send_text(message):
    bot.send_message(message.chat.id, 'Привет, вот что я могу!')

    
bot.polling(none_stop=True, interval=0)
