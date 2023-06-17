import logging
from keyboards import *
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
  await message.answer("Привіт! Я твій особистий помічник у виборі тарифу від lifecell.\nМоя мета - допомогти тобі знайти найкращу пропозицію, яка відповідає всім твоїм потребам.\nЯкщо ти готовий натисни кнопку <u>Поїхали</u>!\n\nP.S.:Більш детальніше про тариф ти можеш дізнатися на сайті <b><a href='https://www.lifecell.ua/mobilnij-zvyazok/taryfy/'>Lifecell.</a></b>", parse_mode='html', disable_web_page_preview=1, reply_markup=question1)




# 2. Запитання про використання мобільного зв'язку
@dp.message_handler(commands=['Поїхали'])
async def get_answer(message: types.Message, state: FSMContext):
  question1 = "Хто є твоїм поточним мобільним оператором?\n\n" \
            "1. lifecell\n" \
            "2. Київстар\n" \
            "3. Vodafone\n" \

  
  await message.answer('Я тобі задам декілька питань, щоб віднайти для тебе найкращі тарифи lifecell!', reply_markup=question2)
  await message.answer(question1)
  dp.register_message_handler(get_answer)
  await state.set_state('answer_2')
  





# 3. Запитання про потреби
@dp.message_handler(state='answer_2')
async def answer_2(message: types.Message, state: FSMContext):
  quest2 = "Які з наступних функцій мобільного зв'язку є для тебе найважливішими? Вибери одну або декілька варіантів.\n\n" \
              "1. Безлімітні дзвінки \n" \
              "2. Міжнародні дзвінки або роумінг\n" \
              "3. Великий обсяг Інтернет-трафіку\n" \

  await message.answer(quest2)
  dp.register_message_handler(answer_2)
  await state.set_state('answer_3')
  
  
  
# 4. Запитання про попередній оператор
@dp.message_handler(state='answer_3')
async def answer_3(message: types.Message, state: FSMContext):
  quest3 = "Як часто ти використовуєш мобільний зв'язок?\n\n" \
              "1. Активно користуюся\n" \
              "2. Іноді користуюся\n" \
              "3. Рідко використовую"
  await message.answer(quest3, reply_markup=question3)
  dp.register_message_handler(answer_3)
  await state.set_state('answer_4')
  
  
  
# 5. Запитання про мобільний бюджет
@dp.message_handler(state='answer_4')
async def answer_4(message: types.Message, state: FSMContext):
  quest4 ="Яким є твій бюджет на мобільний зв'язок?\n\n" \
            "1. До 100 гривень на місяць\n" \
            "2. Від 100 до 300 гривень на місяць\n" \
            "3. Понад 300 гривень на місяць"
             
  await message.answer(quest4, reply_markup=question4)
  dp.register_message_handler(answer_4)
  await state.set_state('answer_5')
  
   
   
# 6. Запитання про функції, які є менш важливими для користувача
@dp.message_handler(state='answer_5')
async def answer_5(message: types.Message, state: FSMContext):
  quest5 ="Які функції або послуги є для тебе менш важливими?\n\n" \
            "1. Мобільний Інтернет\n" \
            "2. Висока вартість дзвінків\n" \
            "3. Неможливість використання роумінгу\n" \
            "4. Обмеження використання послуги в певні часи" 
            
  await message.answer(quest5, reply_markup=question5)
  await state.set_state('goods')
  



@dp.message_handler(state='goods')
async def goods(message: types.Message):
  if message.text == "Мобільний Інтернет":
    await message.answer('Ось 4 рекомендованих тарифів, які відповідають твоїм потребам: ', reply_markup=tarif_choice1)
  elif message.text == "Висока вартість дзвінків":
    await message.answer('Ось 5 рекомендованих тарифи, які відповідають твоїм потребам: ', reply_markup=tarif_choice2)
  elif message.text == "Неможливість використання роумінгу":
    await message.answer('Ось 3 рекомендованих тарифи, які відповідають твоїм потребам: ', reply_markup=tarif_choice3)
  elif message.text == "Обмеження використання послуги в певні часи":
    await message.answer('Ось 3 рекомендованих тарифи, які відповідають твоїм потребам: ', reply_markup=tarif_choice4)

@dp.callback_query_handler(state='tarif')
async def get_tarif_info(callback_query: types.CallbackQuery):
    if callback_query.data in tarifs.keys():
       await bot.send_photo(callback_query.message.chat.id, tarif[callback_query.data]["photo"])
       price = tarif[callback_query.data]['price']
       name = tarif[callback_query.data]['name']
       url= tarif[callback_query.data]["site_url"]
       message = f"Назва - {name}\nСилка на сайт :{url}\nКоштує - {price} " 
       await bot.send_message(callback_query.message.chat.id, message, parse_mode="html")

tarifs = {
  'Ґаджет Безпека':{
    'name': 'Ґаджет Безпека',
    'site_url':'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-bezpeka/',
    'photo':'https://www.lifecell.ua/products/uploads/__sized__/tariffs/__640%D1%85640_%D0%93%D0%B0%D0%B4%D0%B6%D0%B5%D1%82_IQJbNuo-crop-c0-5__0-5-160x160.png',
    'price': 'Від 90 грн' 
  },
   'Ґаджет Смарт':{
     'name': 'Ґаджет Смарт',
     'site_url':'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-smart21/',
     'photo':'https://www.lifecell.ua/products/uploads/__sized__/tariffs/__640%D1%85640_%D0%93%D0%B0%D0%B4%D0%B6%D0%B5%D1%82_IQJbNuo-crop-c0-5__0-5-160x160.png',
     'price': 'Від 150 грн'      
   },
   'Шкільний Лайф':{
    'name': 'Шкільний Лайф',
    'site_url':'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/shkilniy/',
    'photo':'https://www.lifecell.ua/products/uploads/__sized__/tariffs/______640%D1%85640_school_1_Qkh7WdM-crop-c0-5__0-5-160x160.png',
    'price': '150 грн'     
   },
   'Просто Лайф':{
    'name': 'Просто Лайф',
    'site_url':'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/prosto-life-2021/',
    'photo':'https://www.lifecell.ua/products/uploads/__sized__/tariffs/__640%D1%85640_%D0%9F%D1%80%D0%BE%D1%81%D1%82%D0%BE_%D0%9B%D0%B0%D0%B9%D1%84-crop-c0-5__0-5-160x160.png',
    'price': 'Від 90 грн'     
   }
}
tarif2 = {
  'Інтернет БЕЗМЕЖ':{
     'name': 'Інтернет БЕЗМЕЖ',
     'site_url':'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/int-bezmezh-2021/',
     'photo':'https://www.lifecell.ua/products/uploads/__sized__/tariffs/_640x640_%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82_%D0%91%D0%95%D0%97%D0%9C%D0%95%D0%96_ukr-crop-c0-5__0-5-160x160.png',
     'price': '100 грн'      
   },
   'Дзвінкий БЕЗМЕЖ':{
     'name': 'Дзвінкий БЕЗМЕЖ',
     'site_url':'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/dzvinkiy/',
     'photo':'https://www.lifecell.ua/products/uploads/__sized__/tariffs/_640%D1%85640_%D0%91%D0%95%D0%97%D0%9C%D0%95%D0%96_ukr-crop-c0-5__0-5-160x160.png',
     'price': '75 грн'      
   },
   'Вільний Лайф. Регіон':{
     'name': 'Вільний Лайф. Регіон',
     'site_url':'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-reg-2021/',
     'photo':'https://www.lifecell.ua/products/uploads/__sized__/tariffs/__640%D1%85640_%D0%92%D1%96%D0%BB%D1%8C%D0%BD%D0%B8%D0%B9_%D0%9B%D0%B0%D0%B9%D1%84-crop-c0-5__0-5-160x160.png',
     'price': '150 грн'      
   },
   'Platinum Лайф':{
     'name': 'Platinum Лайф',
     'site_url':'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/platinum-life-2021/',
     'photo':'https://www.lifecell.ua/products/uploads/__sized__/tariffs/__640%D1%85640_Platinum_%D0%9B%D0%B0%D0%B9%D1%84_update-crop-c0-5__0-5-160x160.png',
     'price': '250 грн'      
   },
   'Шкільний Лайф':{
    'name': 'Шкільний Лайф',
    'site_url':'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/shkilniy/',
    'photo':'https://www.lifecell.ua/products/uploads/__sized__/tariffs/______640%D1%85640_school_1_Qkh7WdM-crop-c0-5__0-5-160x160.png',
    'price': '150 грн'     
   }   
}   
tarif3 = {
   
   'Смарт Сімя S':{
     'name': 'Смарт Сімя S',
     'site_url':'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-family-s/',
     'photo':'https://www.lifecell.ua/products/uploads/__sized__/tariffs/__640%D1%85640_%D0%A1%D0%BC%D0%B0%D1%80%D1%82_%D0%A1%D0%B5%D0%BC%D1%8C%D1%8F-crop-c0-5__0-5-160x160.png',
     'price': '375 грн'      
   },
   'Смарт Сімя M':{
     'name': 'Смарт Сімя M',
     'site_url':'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart_simja-m/',
     'photo':'https://www.lifecell.ua/products/uploads/__sized__/tariffs/__640%D1%85640_%D0%A1%D0%BC%D0%B0%D1%80%D1%82_%D0%A1%D0%B5%D0%BC%D1%8C%D1%8F-crop-c0-5__0-5-160x160.png',
     'price': '425 грн'      
   },
   'Смарт Сімя L':{
     'name': 'Смарт Сімя L',
     'site_url':'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-family-l/',
     'photo':'https://www.lifecell.ua/products/uploads/__sized__/tariffs/__640%D1%85640_%D0%A1%D0%BC%D0%B0%D1%80%D1%82_%D0%A1%D0%B5%D0%BC%D1%8C%D1%8F-crop-c0-5__0-5-160x160.png',
     'price': '500 грн'      
   }
}
tarif4 = {
   
  'Інтернет БЕЗМЕЖ':{
     'name': 'Інтернет БЕЗМЕЖ',
     'site_url':'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/int-bezmezh-2021/',
     'photo':'https://www.lifecell.ua/products/uploads/__sized__/tariffs/_640x640_%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82_%D0%91%D0%95%D0%97%D0%9C%D0%95%D0%96_ukr-crop-c0-5__0-5-160x160.png',
     'price': '100 грн'      
   },
   'Вільний Лайф. Регіон':{
     'name': 'Вільний Лайф. Регіон',
     'site_url':'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-reg-2021/',
     'photo':'https://www.lifecell.ua/products/uploads/__sized__/tariffs/__640%D1%85640_%D0%92%D1%96%D0%BB%D1%8C%D0%BD%D0%B8%D0%B9_%D0%9B%D0%B0%D0%B9%D1%84-crop-c0-5__0-5-160x160.png',
     'price': '150 грн'      
   },
   'Platinum Лайф':{
     'name': 'Platinum Лайф',
     'site_url':'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/platinum-life-2021/',
     'photo':'https://www.lifecell.ua/products/uploads/__sized__/tariffs/__640%D1%85640_Platinum_%D0%9B%D0%B0%D0%B9%D1%84_update-crop-c0-5__0-5-160x160.png',
     'price': '250 грн'      
   }
}




if __name__ == "__main__":
  executor.start_polling(dp)