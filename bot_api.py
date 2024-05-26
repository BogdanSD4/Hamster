import telebot

# Replace with your bot's token
BOT_TOKEN = "6013670733:AAE6_Am2-dfoJ5PDN1LSnc1S2hvDbgkSL7w"

# Create a TelegramBot object
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_any_message(message):
    # Get the message text
    message_text = message.text

    # Print the received message to the console
    print(f"[Received Message] User: {message.from_user.username}, Chat: {message.chat.title}, Message: {message_text}")

# Start the bot polling for updates
bot.polling()