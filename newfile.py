from pyrogram import Client, filters, enums
import random
import time
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import os

#app = Client('jekmant', api_hash='24254fae76540d9fb88ff6fc03132248', api_id='27248876')
app = Client('jekmant2', api_hash='5a27fb556bada09feddbaa982b0da2c0', api_id='22328635')

@app.on_message(filters.command("sendvoice", prefixes="/") & filters.me)
def memoryreboot(client, message):
    cmd='sendvoice'
    try:
        _, delay_time, audio_name = message.text.split(maxsplit=2)
        delay_time = int(delay_time)
    except ValueError:
        client.edit_message_text(
        	chat_id=message.chat.id,
        	message_id=message.id,
        	text=f"Неверный формат команды. Используйте: /{cmd} <задержка_в_сек> <имя_аудиофайла>"
        )
        return
    if message.reply_to_message:
        rtmi = message.reply_to_message.id
    else:
        rtmi = False
    audio_file = f"{audio_name}.ogg"
    if not os.path.exists(audio_file):
        client.edit_message_text(
        	chat_id=message.chat.id,
        	message_id=message.id,
        	text=f"Файл {audio_file} не найден в папке со скриптом. Автотудаление через 10 секунд."
        )
        time.sleep(10)
        client.delete_messages(
        	chat_id=message.chat.id,
        	message_ids=message.id,
        	revoke=False
    	)
        return
    if os.path.exists(audio_file):
    	client.delete_messages(
        	chat_id=message.chat.id,
        	message_ids=message.id,
        	revoke=False
    	)
    time.sleep(delay_time)
    client.send_voice(
        chat_id=message.chat.id,
        voice=audio_file,
        reply_to_message_id=rtmi
    )

@app.on_message(filters.command("soundlist", prefixes='/') & filters.me)
def list_ogg_files(client, message):
    folder_path = os.path.dirname(os.path.abspath(__file__))
    ogg_files = [file for file in os.listdir(folder_path) if file.endswith(".ogg")]
    if ogg_files:
        files_list = "\n".join(ogg_files)
        client.edit_message_text(
        	chat_id=message.chat.id,
        	message_id=message.id,
        	text=f"```Список файлов\n{files_list}```",
        	parse_mode=enums.ParseMode.MARKDOWN
        )
    else:
        client.edit_message_text(
        	chat_id=message.chat.id,
        	message_id=message.id,
        	text="В папке нет файлов .ogg"
        )



@app.on_message(filters.command("debug", prefixes='/') & filters.me)
def debug_reply_message(client, message):
	client.send_message(
		chat_id=message.chat.id,
		text=message.reply_to_message,
		reply_to_message_id=message.reply_to_message.id
	)

@app.on_message(filters.command("alo2", prefixes="/") & filters.me)
def echo(client, message):
	mention_text = f'<a href="tg://user?id={message.reply_to_message.from_user.id}">\u200B</a>'
	client.send_message(
		chat_id=message.chat.id,
		text=f"ㅤ{mention_text}",
		reply_to_message_id=message.reply_to_message.id
	)

@app.on_message(filters.command("sent", prefixes="/") & filters.me)
def send_random_numbers(client, message):
    chat_id = message.chat.id
    while True:
        time.sleep(32)
        random_numbers = "-".join(["{:04d}".format(random.randint(0, 9999)) for _ in range(4)])
        app.send_message(chat_id, random_numbers)

@app.on_message(filters.command('трахать', prefixes='/') & filters.me)
def mention_random_user(client, message):
    chat_id = message.chat.id
    members = client.get_chat_members(chat_id)
    active_users = [user for user in members if not user.user.is_bot]
    while active_users:
        time.sleep(32)
        random_user = random.choice(active_users)
        mention_text = f'<a href="tg://user?id={random_user.user.id}">\u200B</a>'
        client.send_message(chat_id, f'В СПЯЧКУ МЕДВЕДИ{mention_text}', parse_mode=enums.ParseMode.HTML)

@app.on_message(filters.text & filters.regex('apihash'))
def mention_random_user(client, message):
    chat_id = message.chat.id
    members = client.get_chat_members(chat_id)
    active_users = [user for user in members if not user.user.is_bot]
    while active_users:
        time.sleep(32)
        random_user = random.choice(active_users)
        mention_text = f'<a href="tg://user?id={random_user.user.id}">\u200B</a>'
        client.send_message(chat_id, f'Спать любишь?Планеты знаешь, это прочитаешь пиздюк{mention_text}', parse_mode=enums.ParseMode.HTML)

app.run()