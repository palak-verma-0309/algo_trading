import requests
import os
from dotenv import load_dotenv

load_dotenv()

def send_telegram_message(message):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    data = {
        "chat_id": chat_id,
        "text": message
    }

    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error sending message: {e}")
        return False
