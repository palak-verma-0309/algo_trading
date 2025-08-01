from telegram_alert import send_telegram_message

if send_telegram_message("Telegram alert working!"):
    print("Message sent successfully!")
else:
    print("Failed to send message.")
