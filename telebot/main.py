import telebot


TOKEN = '6184019795:AAFMfypMhUBOEPEb0y7jXfDAtXt5zubNSIA'

bot = telebot.TeleBot(TOKEN)

# content_types -> тип контента (text, sticker, audio, document, photo, video, animation ...)
# func=lambda message: True -> чтобы бот реагировал на любое сообщения ()
# @bot.message_handler(content_types=['sticker', 'text'], func=lambda message: True)
# def start_message(message):
#     print(message)
#     bot.send_message(message.chat.id, 'Привет')
#     if message.sticker:
#         bot.send_sticker(message.chat.id, message.sticker.file_id)


# keyboard = telebot.types.ReplyKeyboardMarkup()
# button1 = telebot.types.KeyboardButton('Да')
# button2 = telebot.types.KeyboardButton('Нет')
# keyboard.add(button1, button2)

'''для клавиатуры ReplyKeyboardMarkup'''
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, 'Выберите кнопку', reply_markup=keyboard)
#     bot.register_next_step_handler(message, reply_to_button)

# def reply_to_button(message):
#     if message.text == 'Да':
#         bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAEJmEJkpPe56vyQGJ4ET4HuzVxLrhM5mAACYhcAAqbxcR7grCXPxKbhFS8E')
#     elif message.text == 'Нет':
#         pass
#     else:
#         bot.send_message(message.chat.id, 'Нажмите на кнопку')
#         bot.register_next_step_handler(message, reply_to_button)




'''для клавиатуры Inline'''
    
keyboard = telebot.types.InlineKeyboardMarkup()
button1 = telebot.types.InlineKeyboardButton('Да', callback_data='yes')
button2 = telebot.types.InlineKeyboardButton('Нет', callback_data='no')

keyboard.row(button1, button2)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Выберите кнопку', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def handler_callback(call):
    # print(call.data)
    if call.data == 'yes':
        bot.send_sticker(call.message.chat.id, 'CAACAgQAAxkBAAEJmEJkpPe56vyQGJ4ET4HuzVxLrhM5mAACYhcAAqbxcR7grCXPxKbhFS8E')
    elif call.data == 'no':
        pass







bot.polling()