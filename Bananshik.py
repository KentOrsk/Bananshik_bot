
import csv
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import datetime
from datetime import datetime, date, time

def plural_days(n):
	days = ['день', 'дня', 'дней']
	if n % 10 == 1 and n % 100 != 11:
		p = 0
	elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
		p = 1
	else:
		p = 2
	return str(n) + ' ' + days[p]

mes = {'янв':'1',
       'фев':'2',
       'мар':'3',
       'апр':'4',
       'мая':'5',
       'июн':'6',
       'июл':'7',
       'авг':'8',
       'сен':'9',
       'окт':'10',
       'ноя':'11',
       'дек':'12',
       }
TG_TOKEN="5601856257:AAED92UNP0ntfPvXz-LnZJG3IrD2MZzU3j8"
bot = Bot(token=TG_TOKEN, parse_mode=types.ParseMode.HTML)
dp=Dispatcher(bot)

@dp.message_handler(hashtags = 'адрес')
async def otvet(message: types.Message):
	await message.answer("""<b>Серёга</b>: Вавилова 45, 2 подъезд, 5 этаж, кв 30, ❗️домофон 1ключ1111
	<b>Илья</b>: ул. Новодмитровская 2к7 кв. 380  ❗️Этаж 27 квартира 380 🚇Дмитровская
	<b>Дима</b>: РнД
	<b>Саша</b>: ул. Ул. Болотниковская, 54к1, 1 подъезд, кв.4
	❗️Домофон: В4В1268В
	<b>Стас</b>: ул. Гримау 9к1, 2 этаж, 95 кв, ❗️ Домофон: К117К1190 (0 задержите)""")
def vozrast():
	s=''
	today = date.today()
	with open('dr.csv') as csvfile:
		dr = csv.DictReader(csvfile, delimiter = ";")
		for row in dr:
			diff = today - date(int(row["Год"]),int(mes[row["Месяца"][0:3]]),int(row["День"]))
			s+=f'\n{row["Имя"]} - {row["День"]} {row["Месяца"]} {row["Год"]} Сегодня {plural_days(diff.days)}'
	return s


@dp.message_handler(hashtags = 'др')
async def otvet(message: types.Message):
	await message.answer(vozrast())

if __name__ == '__main__':
	executor.start_polling(dp)