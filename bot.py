import requests

import os

TOKEN = os.environ["BOT_TOKEN"]

CHAT_ID = os.environ["CHAT_ID"]

requests.post(

    f"https://api.telegram.org/bot{TOKEN}/sendMessage",

    data={

        "chat_id": CHAT_ID,

        "text": "✅ Pokemon Stock Bot funguje."

    }

)

print("Message sent")
