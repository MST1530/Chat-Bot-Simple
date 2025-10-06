import telebot

TOKEN = '7478122580:AAH1CFCZOuXPSpVghisD_-S9DPARmdfZMQQ'
bot = telebot.TeleBot(TOKEN)

# ID двух пользователей
USER_1_ID = 1621964347  # me
USER_2_ID = 7135496592  # partner

# Функция для получения ID получателя
def get_receiver_id(sender_id):
    if sender_id == USER_1_ID:
        return USER_2_ID
    elif sender_id == USER_2_ID:
        return USER_1_ID
    return None

@bot.message_handler(content_types=['text', 'photo', 'video', 'audio', 'document',
                                    'voice', 'video_note', 'sticker', 'animation', 'location', 'contact'])
def relay_message(message):
    receiver_id = get_receiver_id(message.from_user.id)

    if not receiver_id:
        bot.send_message(message.chat.id, "У вас нет доступа к чату.")
        return

    if message.text:
        bot.send_message(receiver_id, message.text)

    elif message.photo:
        file_id = message.photo[-1].file_id  # Самое большое фото
        bot.send_photo(receiver_id, file_id, caption=message.caption)

    elif message.video:
        bot.send_video(receiver_id, message.video.file_id, caption=message.caption)

    elif message.audio:
        bot.send_audio(receiver_id, message.audio.file_id, caption=message.caption)

    elif message.document:
        bot.send_document(receiver_id, message.document.file_id, caption=message.caption)

    elif message.voice:
        bot.send_voice(receiver_id, message.voice.file_id, caption=message.caption)

    elif message.video_note:
        bot.send_video_note(receiver_id, message.video_note.file_id)

    elif message.sticker:
        bot.send_sticker(receiver_id, message.sticker.file_id)

    elif message.animation:
        bot.send_animation(receiver_id, message.animation.file_id, caption=message.caption)

    elif message.location:
        bot.send_location(receiver_id, latitude=message.location.latitude, longitude=message.location.longitude)

    elif message.contact:
        bot.send_contact(receiver_id, phone_number=message.contact.phone_number, first_name=message.contact.first_name)

bot.polling()
