from telebot import TeleBot

bot = TeleBot('7823088620:AAFNeY073G_iRBjxGpeyKxP8g7rrXYnkb0w')
 
@bot.message_handler(commands=['start'])
def botic(message):
    bot.send_message(message.chat.id, 'Привет, дорогой человек')
    

@bot.message_handler(commands=['watch'])
def botic(message):
    bot.send_message(message.chat.id, 'https://rutube.ru/video/347df5353ea60cfe5f8ef715c942ba6f/?r=wd')
    
    
@bot.message_handler(commands=['collection'])
def botic(message):
    bot.send_message(message.chat.id, 'У меня было 634 фантика, не считая 3 обёрток от жвачек. Но ты ведь помнишь, что сейчас у меня нет коллекции? Зачем тогда спрашиваешь?')
    

@bot.message_handler(commands=['think'])
def botic(message):
    bot.send_message(message.chat.id, 'Мне вот иногда кажется, что наш мир кем-то нарисован, и за нами всё время кто-то наблюдает. Вон оттуда.')
    

@bot.message_handler(commands=['hello'])
def botic(message):
    bot.send_message(message.chat.id, 'Я Ёжик. Будем знакомы. С помощью команды watch ты сможешь посмотреть новогоднюю серию')

 

bot.infinity_polling()