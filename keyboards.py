from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# from bot import tarifs
question1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

b1 = KeyboardButton('/Поїхали')

question1.add(b1)




question2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

asn1 = KeyboardButton('1')
asn2 = KeyboardButton('2')
asn3 = KeyboardButton('3')
question2.row(asn1, asn2, asn3,)





question3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

an1 = KeyboardButton('1')
an2 = KeyboardButton('2')
an3 = KeyboardButton('3')

question3.row(an1, an2, an3,)





question4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
asn1 = KeyboardButton('1')
asn2 = KeyboardButton('2')
asn3 = KeyboardButton('3')

question4.row(asn1, asn2, asn3)







asn1 = KeyboardButton('Мобільний Інтернет 🌐💻')
asn2 = KeyboardButton('Висока вартість дзвінків 💸📞')
asn3 = KeyboardButton('Неможливість використання роумінгу 🌍🔌')
asn4 = KeyboardButton('Обмеження використання послуги в певні часи ⏰🔒')
question5 = ReplyKeyboardMarkup(resize_keyboard=True)
question5.add(asn1)
question5.add(asn2)
question5.add(asn3)
question5.add(asn4)

    
    
    
taf1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Ґаджет Безпека", callback_data="Ґаджет Безпека"),
            InlineKeyboardButton(text = "Ґаджет Смарт", callback_data="Ґаджет Смарт"),
            InlineKeyboardButton(text = "Шкільний Лайф", callback_data="Шкільний Лайф"),
            InlineKeyboardButton(text = "Просто Лайф", callback_data="Просто Лайф")
        ],
        [
            InlineKeyboardButton(text='Завершити перегляд', callback_data='0')
        ]
    ]
)



taf2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Інтернет БЕЗМЕЖ", callback_data="Інтернет БЕЗМЕЖ"),
            InlineKeyboardButton(text = "Дзвінкий БЕЗМЕЖ", callback_data="Дзвінкий БЕЗМЕЖ"),
            InlineKeyboardButton(text = "Вільний Лайф. Регіон", callback_data="Вільний Лайф. Регіон"),
            InlineKeyboardButton(text = "Platinum Лайф", callback_data="Platinum Лайф"),
            InlineKeyboardButton(text = "Шкільний Лайф", callback_data="Шкільний Лайф")
        ],
        [
            InlineKeyboardButton(text='Завершити перегляд', callback_data='0')
        ]
    
    
    ]
)


taf3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Смарт Сім'я S", callback_data="Смарт Сім'я S"),
            InlineKeyboardButton(text = "Смарт Сім'я M", callback_data="Смарт Сім'я M"),
            InlineKeyboardButton(text = "Смарт Сім'я L", callback_data="Смарт Сім'я L")
        ],
        [
            InlineKeyboardButton(text='Завершити перегляд', callback_data='0')
        ]
    ]
)


taf4 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Інтернет БЕЗМЕЖ", callback_data="Інтернет БЕЗМЕЖ"),
            InlineKeyboardButton(text = "Вільний Лайф. Регіон", callback_data="Вільний Лайф. Регіон"),
            InlineKeyboardButton(text = "Platinum Лайф", callback_data="Platinum Лайф")
        ],
        [
            InlineKeyboardButton(text='Завершити перегляд', callback_data='0')
        ]
    ]
)


