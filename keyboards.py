from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

question1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

b1 = KeyboardButton('/Поїхали')

question1.add(b1)




question2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

asn1 = KeyboardButton('1')
asn2 = KeyboardButton('2')
asn3 = KeyboardButton('3')

question2.row(asn1, asn2, asn3)





question3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

an1 = KeyboardButton('1')
an2 = KeyboardButton('2')
an3 = KeyboardButton('3')
an4 = KeyboardButton('4')
question3.row(an1, an2, an3, an4)




question4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

asn1 = KeyboardButton('1')
asn2 = KeyboardButton('2')
asn3 = KeyboardButton('3')

question4.row(asn1, asn2, asn3)





question5 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

asn1 = KeyboardButton('Мобільний Інтернет')
asn2 = KeyboardButton('Висока вартість дзвінків')
asn3 = KeyboardButton('Неможливість використання роумінгу')
asn4 = KeyboardButton('Обмеження використання послуги в певні часи')

question5.add(asn1)
question5.add(asn2)
question5.add(asn3)
question5.add(asn4)





taf1 = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text = "Ґаджет Безпека", callback_data="1")],
    [InlineKeyboardButton(text = "Ґаджет Смарт", callback_data="2")],
    [InlineKeyboardButton(text = "Шкільний Лайф", callback_data="3")],
    [InlineKeyboardButton(text = "Просто Лайф", callback_data="4")]
    ]
)


taf2 = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text = "Інтернет БЕЗМЕЖ", callback_data="1")],
    [InlineKeyboardButton(text = "Дзвінкий БЕЗМЕЖ", callback_data="2")],
    [InlineKeyboardButton(text = "Вільний Лайф. Регіон", callback_data="3")],
    [InlineKeyboardButton(text = "Platinum Лайф", callback_data="4")],
    [InlineKeyboardButton(text = "Шкільний Лайф", callback_data="4")]
    ]
)


taf3 = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text = "Смарт Сім'я S", callback_data="1")],
    [InlineKeyboardButton(text = "Смарт Сім'я M", callback_data="2")],
    [InlineKeyboardButton(text = "Смарт Сім'я L", callback_data="3")]
    ]
)


taf4 = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text = "Інтернет БЕЗМЕЖ", callback_data="1")],
    [InlineKeyboardButton(text = "Вільний Лайф. Регіон", callback_data="2")],
    [InlineKeyboardButton(text = "Platinum Лайф", callback_data="3")]
    ]
)