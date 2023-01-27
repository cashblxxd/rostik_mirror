from telethon.sync import TelegramClient
from json import load, dump
from datetime import datetime
import os

API_ID="22055655"
API_HASH="41c7a28e86fb150fc4cc9b92e3166200"
PRIVATE_CHAT_ID=-1001614559680
REDIRECT_CHAT_ID=430171400

print("STARTED", datetime.now())
client = TelegramClient('MyApp', API_ID, API_HASH)
client.start()
with open("last_message_id.json", "r+") as f:
    s = load(f)
    last_id = s["id"]
    print("last id", last_id)
    for message in client.iter_messages(PRIVATE_CHAT_ID, offset_id=s["id"], reverse=True):
        print("message id", message.id)
        last_id = message.id
        if message.message:
            text = message.message
            client.send_message(REDIRECT_CHAT_ID, message=text)
        if message.photo:
            filepath = client.download_media(message)
            client.send_file(REDIRECT_CHAT_ID, filepath)
            os.remove(filepath)
    print("last id", last_id)
with open("last_message_id.json", "w+") as f:
    dump({"id": last_id}, f)
client.disconnect()
print("DONE", datetime.now())
