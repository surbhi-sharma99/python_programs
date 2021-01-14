import telebot

#surbhi_second_bot
my_bot = telebot.TeleBot("1272569672:AAEznV1hQ7d06VU10TOUjYIlXVHmrTy8wRE")

@my_bot.message_handler(commands = ["start" , "say_again"])
def send_welcome(message):

    my_bot.reply_to(message , "welcome," + str(message.from_user.first_name) + "this is chatstore" , f)
    print("message from: " + message.from.user.first_name)
my_bot.polling()
    
