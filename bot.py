import telebot 
import configure
from telebot import types

client = telebot.TeleBot(configure.config['token'])


# Welcom

@client.message_handler(commands = ['start'])
def welcom(message):
	sti = open('sticker/AnimatedSticker.tgs', 'rb')
	client.send_sticker(message.chat.id, sti)

	send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!"
	client.send_message(message.chat.id, send_mess, parse_mode = 'html')


# help

@client.message_handler(commands = ['help'])
def help(message):
	if message.text.lower() == '/help':
		client.send_message(message.chat.id, 'Если хочешь узнать свой НИК или ID напиши /info\nЧтобы получить рисунки из символов /pictures')

# hint
@client.message_handler(commands = ['hint'])
def hint(message):
	if message.text.lower() == '/hint':
		client.send_message(message.chat.id, 'Напишите "Привет"')


# pictures

@client.message_handler(commands = ['pictures'])
def WTF(message):
	markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
	item_nishtyaki = types.KeyboardButton('Картинки из символов')

	markup_reply.add(item_nishtyaki)

	if  message.text.lower() == '/pictures':
		client.send_message(message.chat.id, 'Чтобы получить картинку из символов нажмите на кнопку ниже.',
			reply_markup = markup_reply )


# get_user_info

@client.message_handler(commands = ['info'])
def get_user_info(message):
	markup_inline = types.InlineKeyboardMarkup()
	item_yes = types.InlineKeyboardButton(text = 'да', callback_data = 'yes')
	item_no = types.InlineKeyboardButton(text = 'нет', callback_data = 'no')

	markup_inline.add(item_yes, item_no)
	client.send_message(message.chat.id, 'Желаете узнать небольшую инфу про вас',
		reply_markup = markup_inline
	)


@client.callback_query_handler(func = lambda call: True)
def answer(call):
	if call.data == 'yes':
		markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
		item_id = types.KeyboardButton('мой id')
		item_username = types.KeyboardButton('мой ник')

		markup_reply.add(item_id, item_username)
		client.send_message(call.message.chat.id, 'Нажмите на одну из кнопок',
			reply_markup = markup_reply
		)	
	elif call.data == 'no':
		client.send_message(call.message.chat.id, 'Хорошо, попробуйте найти первую посхалку (команда для подсказки /hint)')

@client.message_handler(content_types = ['text'])
def get_text(message):

# picture
	markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
	markup_reply_love = types.ReplyKeyboardMarkup(resize_keyboard=True)
	markup_reply_others = types.ReplyKeyboardMarkup(resize_keyboard=True)
	markup_reply_device = types.ReplyKeyboardMarkup(resize_keyboard = True)


# categorie
	item_others = types.KeyboardButton('others')
	item_love = types.KeyboardButton('love')

# pictures
	item_friends = types.KeyboardButton('friends')


	item_love_1 = types.KeyboardButton('love_1')
	item_love_2 = types.KeyboardButton('love_2')
	item_love_3 = types.KeyboardButton('love_3')
	item_love_4 = types.KeyboardButton('love_4')
	item_love_5 = types.KeyboardButton('love_5')

	markup_reply.add(item_love, item_others)
	markup_reply_love.add(item_love_1, item_love_2, item_love_3, item_love_4, item_love_5)
	markup_reply_others.add(item_friends)

	if message.text.lower() == 'мой id':
		client.send_message(message.chat.id, f'Ваш ID: {message.from_user.id}')
	elif message.text.lower() == 'мой ник':
		client.send_message(message.chat.id, f'Ваш NIK: {message.from_user.first_name} {message.from_user.last_name}')

#Посхалка
	elif message.text.lower() == 'привет':
		sti_2 = open('sticker/posxalka.tgs', 'rb')
		client.send_sticker(message.chat.id, sti_2)

		client.send_message(message.chat.id, 'Привет, поздравляю тебя!!! Ты нашёл первую посхалку !!!')




# picture treatment
	elif message.text.lower() == 'картинки из символов':
		client.send_message(message.chat.id, "Выберите категорию", 
			reply_markup = markup_reply)


# picture send
	elif message.text.lower() == 'others':
		client.send_message(message.chat.id, "Выберите картнку",
			reply_markup = markup_reply_others)
	elif message.text.lower() == 'love':
		client.send_message(message.chat.id, "Выберите картнку", 
			reply_markup = markup_reply_love)

# others
	elif message.text.lower() == 'friends':
		client.send_message(message.chat.id, "♥─▀██▀▀▀█\n♥──██▄█\n♥──██▀█\n♥─▄██─ⓡⓘⓔⓝⓓⓢ")

# love
	elif message.text.lower() == 'love_1':
		client.send_message(message.chat.id, "╔╗ ╔╗╔═╦╦╦═╗╔╗╔╗═╦╦╗\n║║ ║╚╣║║║║╩╣╚╗╔╣║║║║\n╚╝ ╚═╩═╩═╩═╝═╚╝╚═╩═╝")
	elif message.text.lower() == 'love_2':
		client.send_message(message.chat.id, "╔╗ ╔╗╔═╦╦╦═╗╔╗╔╗═╦╦╗\n║║ ║╚╣║║║║╩╣╚╗╔╣║║║║\n╚╝ ╚═╩═╩═╩═╝═╚╝╚═╩═╝\n───────▄▄─▄▄▀▀▄▀▀▄\n──────███████───▄▀\n──────▀█████▀▀▄▀\n────────▀█▀")
	elif message.text.lower() == 'love_3':
		client.send_message(message.chat.id, "░░░░░░░░░░░░░░░\n░░░▄▀▀▄▄▄▀▀▄░░░\n░░█░▄██▄██▄░█░░\n░░▀▄▀█████▀▄▀░░\n░░░░▀▄▀█▀▄▀░░░░\n░░░░░░▀▄▀░░░░░░\n░░░░░░░░░░░░░░░")	
	elif message.text.lower() == 'love_4':
		client.send_message(message.chat.id, "─▀██▀─▄███▄─▀██─██▀██▀▀▀█─ \n──██─███─███─██─██─██▄█──\n──██─▀██▄██▀─▀█▄█▀─██▀█──\n─▄██▄▄█▀▀▀─────▀──▄██▄▄▄█")
	elif message.text.lower() == 'love_5':
		client.send_message(message.chat.id, "◢ ▇ ◣┈┈┈◢ ▇ ◣\n▇ ▇ ▇ ◣ ◢ ▇ ▇ ▇\n◥ ▇ ▇ ▇ ▇ ▇ ▇ ◤\n┈ ◥ ▇ ▇ ▇ ▇ ◤\n┈ ┈◥ ▇ ▇ ◤\n┈ ┈ ┈ ◥ ◤")



# don't understand
	else:
		client.send_message(message.chat.id, 'Я тебя не понимаю, напиши /help')


client.polling(none_stop = True, interval = 0)