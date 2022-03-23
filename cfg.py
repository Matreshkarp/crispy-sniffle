from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
valuta = types.KeyboardButton('💱 Игровая Валюта')
kabinet = types.KeyboardButton('🗄️ Личный Кабинет')
svyaz = types.KeyboardButton('🌿 Связь с Админ.')
markup.add(valuta, kabinet, svyaz)

markup2 = types.ReplyKeyboardMarkup(resize_keyboard = True)
moya = types.KeyboardButton('🀄Моя статистика')
popo= types.KeyboardButton('🏧 Пополнить')
glav = types.KeyboardButton('🌴В главное меню🌴')
markup2.add(moya, popo, glav)

markup3 = types.ReplyKeyboardMarkup(resize_keyboard = True)
qiwi = types.KeyboardButton('🥝 Qiwi')
yamooney = types.KeyboardButton('🎴YandexMoney')
backs = types.KeyboardButton('🛰️К лич. кабинету')
markup3.add(qiwi, yamooney, backs)

markup4 = types.ReplyKeyboardMarkup(resize_keyboard = True)
pc = types.KeyboardButton('📺Доступный ДОНАТ📺')
backm = types.KeyboardButton('🌴В главное меню🌴')
markup4.add(pc, backm)

markup5 = types.ReplyKeyboardMarkup(resize_keyboard = True)
gta = types.KeyboardButton('🌴GTA V online🌴')
pubg = types.KeyboardButton('🔫PUBG🔫')
steam = types.KeyboardButton('🧿STEAM')
backmm = types.KeyboardButton('🌴В главное меню🌴')
markup5.add(gta, pubg, steam, backmm)

opl = types.ReplyKeyboardMarkup(resize_keyboard=True)
yes = types.KeyboardButton('🍁Оплатил🍁')
no = types.KeyboardButton('⛔Отмена⛔')
opl.add(yes, no)

warface = types.ReplyKeyboardMarkup(resize_keyboard = True)
sto = types.KeyboardButton('☄️ 100 DONATE')
pyat = types.KeyboardButton('☄️ 500 DONATE')
tus = types.KeyboardButton('☄️ 1000 DONATE')
backmg = types.KeyboardButton('🌴В главное меню🌴')
warface.add(sto, pyat, tus, backmg)

pubg = types.ReplyKeyboardMarkup(resize_keyboard = True)
stop = types.KeyboardButton('☄️ 100 DONATE')
pyatp = types.KeyboardButton('☄️ 500 DONATE')
tusp = types.KeyboardButton('☄️ 1000 DONATE')
backmgp = types.KeyboardButton('🌴В главное меню🌴')
pubg.add(stop, pyatp, tusp, backmgp)

pub = types.ReplyKeyboardMarkup(resize_keyboard = True)
stopp = types.KeyboardButton('☄️ 100 DONATE')
pyatpp = types.KeyboardButton('☄️ 500 DONATE')
tuspp = types.KeyboardButton('☄️ 1000 DONATE')
backmgpp = types.KeyboardButton('🌴В главное меню🌴')
pub.add(stopp, pyatpp, tuspp, backmgpp)

