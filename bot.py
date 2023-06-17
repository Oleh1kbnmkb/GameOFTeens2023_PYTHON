import logging
from keyboards import *
from site_url import tar1
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(token='6218827645:AAGX4szbc3raeGnkxcp2MStPqE4nCx7y-Nk')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)




# 1. Привітання та пояснення мети бота
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
  await message.answer("Привіт! 😊 Я твій особистий помічник у виборі тарифу від lifecell. 📱💙 Моя мета - допомогти тобі знайти найкращу пропозицію, яка відповідає всім твоїм потребам. 🎯🔎 Якщо ти готовий, натисни кнопку <u>Поїхали</u>! 🚀\n\nP.S.: Більш детально про тарифи ти можеш дізнатися на сайті <b><a href='https://www.lifecell.ua/mobilnij-zvyazok/taryfy/'>Lifecell</a></b>. 😉✨", parse_mode='html', disable_web_page_preview=1, reply_markup=question1)




# 2. Запитання про використання мобільного зв'язку
@dp.message_handler(commands=['Поїхали']) 
async def get_answer(message: types.Message, state: FSMContext): 
  question1 = "Хто є твоїм поточним мобільним оператором? 📱💼\n\n"\
              "1. lifecell 💙\n"\
              "2. Київстар 🌟\n"\
              "3. Vodafone 🔴\n"
   
   
  await message.answer('Я тобі задам декілька питань, щоб віднайти для тебе найкращі тарифи lifecell!', reply_markup=question2) 
   
  await message.answer(question1) 
  await state.set_state('not_goods') 
@dp.message_handler(state='not_goods') 
async def not_goods(message: types.Message, state: FSMContext):   
  if (message.text == '2'):   
    await message.answer('Ви обрали що ваш оператор не Lifecell тому придбайте картку Lifecell або ось посилання на Київстар - https://t.me/Kyivstar_Ukraine ') 
  elif (message.text == '3'): 
    await message.answer('Ви обрали що ваш оператор не Lifecell тому придбайте картку Lifecell або ось посилання на Vodafone - @VFUkraineBot ')     
  dp.register_message_handler(get_answer) 
  await state.set_state('answer_2')
  





# 3. Запитання про потреби
@dp.message_handler(state='answer_2')
async def answer_2(message: types.Message, state: FSMContext):
  quest2 = "Які з наступних функцій мобільного зв'язку є для тебе найважливішими? 📲✨ Вибери одну або декілька варіантів.👇🏼\n\n"\
            "1. Безлімітні дзвінки 📞💬\n"\
            "2. Міжнародні дзвінки або роумінг 🌍📞\n"\
            "3. Великий обсяг Інтернет-трафіку 🌐💻\n"\
            "4. Додаткові послуги 🛡️💼\n"\
            "5. Інші функції (вкажи свої варіанти) ✨🔍"

  await message.answer(quest2)
  dp.register_message_handler(answer_2)
  await state.set_state('answer_3')
  
  
  
# 4. Запитання про попередній оператор
@dp.message_handler(state='answer_3')
async def answer_3(message: types.Message, state: FSMContext):
  quest3 = "Як часто ти використовуєш мобільний зв'язок? 📲🕒\n\n"\
          "1. Активно користуюся 🚀📞\n"\
          "2. Іноді користуюся 🌤️📱\n"\
          "3. Рідко використовую ⏳📵"
  await message.answer(quest3, reply_markup=question3)
  dp.register_message_handler(answer_3)
  await state.set_state('answer_4')
  
  
  
# 5. Запитання про мобільний бюджет
@dp.message_handler(state='answer_4')
async def answer_4(message: types.Message, state: FSMContext):
  quest4 ="Яким є твій бюджет на мобільний зв'язок? 💰📲\n\n"\
          "1. До 100 гривень на місяць 💸💯\n"\
          "2. Від 100 до 300 гривень на місяць 💸💰\n"\
          "3. Понад 300 гривень на місяць 💸💲"
             
  await message.answer(quest4, reply_markup=question4)
  dp.register_message_handler(answer_4)
  await state.set_state('answer_5')
  
   
   
# 6. Запитання про функції, які є менш важливими для користувача
@dp.message_handler(state='answer_5')
async def answer_5(message: types.Message, state: FSMContext):
  quest5 ="Які функції або послуги є для тебе менш важливими? 🤔📲\n\n"\
          "1. Мобільний Інтернет 🌐💻\n"\
          "2. Висока вартість дзвінків 💸📞\n"\
          "3. Неможливість використання роумінгу 🌍🔌\n"\
          "4. Обмеження використання послуги в певні часи ⏰🔒" 
            
  await message.answer(quest5, reply_markup=question5)
  await state.set_state('goods')
  


# Підбір тарифів для користувача
@dp.message_handler(state='goods')
async def goods(message: types.Message, state: FSMContext):
  if message.text == "Мобільний Інтернет 🌐💻":
    await message.answer('Ось 4 рекомендованих тарифів, які відповідають твоїм потребам: ', reply_markup=taf1)
  elif message.text == "Висока вартість дзвінків 💸📞":
    await message.answer('Ось 5 рекомендованих тарифи, які відповідають твоїм потребам: ', reply_markup=taf2)
  elif message.text == "Неможливість використання роумінгу 🌍🔌":
    await message.answer('Ось 3 рекомендованих тарифи, які відповідають твоїм потребам: ', reply_markup=taf3)
  elif message.text == "Обмеження використання послуги в певні часи ⏰🔒":
    await message.answer('Ось 3 рекомендованих тарифи, які відповідають твоїм потребам: ', reply_markup=taf4)
  await state.set_state('tarif')
  
  
  
  
@dp.callback_query_handler(state='*', text='0')
async def end_reading(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('Перегляд завершено. Щоб підібрати тариф ще раз - напишіть /start')
    await state.finish()
    
  

@dp.callback_query_handler(state='tarif')
async def get_tarif_info(callback_query: types.CallbackQuery):
    if callback_query.data in tar1.keys():
       await bot.send_photo(callback_query.message.chat.id, tar1[callback_query.data]["photo"])
       price = tar1[callback_query.data]['price']
       name = tar1[callback_query.data]['name']
       url= tar1[callback_query.data]["site_url"]
       message = f"<b>Назва: </b> {name}\n<b>Посилання на сайт: </b> {url}\n<b>Ціна тарифу: </b> {price}" 
       await bot.send_message(callback_query.message.chat.id, message, parse_mode="html")
    else:
       await bot.send_message(callback_query.message.chat.id, "Такого товару нажаль немає в наявності😟")




if __name__ == "__main__":
  executor.start_polling(dp)