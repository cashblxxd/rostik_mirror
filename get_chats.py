from telethon.sync import TelegramClient, events

with TelegramClient('MyApp', "22055655", "41c7a28e86fb150fc4cc9b92e3166200") as client:
    for dialog in client.iter_dialogs():
        print('{:>14}: {}'.format(dialog.id, dialog.title))

    client.run_until_disconnected()
