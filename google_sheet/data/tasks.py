from google_sheet.celery import app
import pygsheets
from data.models import Record
from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime
import locale


# Реализация пунктов 1-3, задача которую будем вызывть каждую минуту
@app.task
def update_data():
    #Получаем данные с гугл таблиц

    # Авторизация а по ключу из файла
    gc = pygsheets.authorize(service_file='excel_key.json')
    sh = gc.open('test')
    wks = sh[0]
    # сохранеям данные с гугл таблиц в переменную
    data = wks.get_all_records()
    # получеем актульное значение доллара
    dollar = get_dollar()
    # Очищаем данные в таблице
    Record.objects.all().delete()
    # Сохраняем данные в таблицу
    for record in data:
        number = record.get("№")
        number_order = record.get("заказ №")
        cost = record.get("стоимость,$")
        delivery_time = record.get("срок поставки")
        delivery_time = datetime.strptime(delivery_time, "%d.%m.%Y").date()
        # Получаем стоимость по актуальному курсу
        cost_rub = int(float(cost) * float(dollar))
        Record.objects.create(number=number, number_order=number_order, cost=cost, delivery_time=delivery_time,
                              cost_rub=cost_rub, )

# получаем курс доллара с сайта ЦБ,
def get_dollar():
    r = requests.get('https://www.cbr.ru/scripts/XML_daily.asp')
    data = r.content
    # парсим XML
    soup = bs(data, "xml")
    result = soup.find("Valute", {"ID": "R01235"})
    dollar = result.Value.text
    # заменяем заяптую на точку
    locale.setlocale(locale.LC_ALL, 'nl_NL')
    dollar_result = locale.atof(dollar)
    return dollar_result