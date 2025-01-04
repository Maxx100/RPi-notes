from dotenv import load_dotenv
import telebot
import os
import time
import socket
import requests

load_dotenv()
TG_TOKEN = os.getenv('TG_TOKEN')
ADMIN_ID = int(os.getenv('ADMIN_ID'))

started = time.time()
bot = telebot.TeleBot(TG_TOKEN)


@bot.message_handler(commands=['ip'])
def get_ip(message):
	host = socket.gethostname()
	local_ip = socket.gethostbyname(host)
	public_ip = requests.get('https://api.ipify.org').content.decode('utf8')

	# Another ways to get ip
	# public_ip = requests.get('https://ident.me').content.decode('utf8')
	# public_ip = requests.get('https://checkip.amazonaws.com').content.decode('utf8')

	if message.chat.id == ADMIN_ID:
		bot.send_message(ADMIN_ID, f"Host: {host}\nLocal IP: {local_ip}\nNet IP: {public_ip}")
	else:
		bot.send_message(
			ADMIN_ID,
			f"Warning: Bot found\n"
			f"ID: {message.chat.id}\n"
			f"User: @{message.from_user.username}\n"
			f"Name: {message.from_user.first_name}\n"
			f"Lastname: {message.from_user.last_name}\n"
			f"Time: {time.strftime("%H:%M:%S", time.localtime(message.date))}"
		)


while True:
	try:
		bot.infinity_polling()
	except Exception as error:
		print(time.strftime(
			f"\033[91mTIME: %d days, %H:%M:%S\033[0m",
			time.gmtime(int(time.time() - started))
		))
		print(error)
	time.sleep(10)
