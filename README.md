# Задание
Необходимо разработать скрипт на языке Python 3, 

который будет выполнять следующие функции:

1. Получать данные с документа при помощи Google API, сделанного в [Google Sheets](https://docs.google.com/spreadsheets/d/1f-qZEX1k_3nj5cahOzntYAnvO4ignbyesVO7yuBdv_g/edit) (необходимо копировать в свой Google аккаунт и выдать самому себе права).
2. Данные должны добавляться в БД, в том же виде, что и в файле –источнике, с добавлением колонки «стоимость в руб.»
    
    a. Необходимо создать DB самостоятельно, СУБД на основе PostgreSQL.
    
    b. Данные для перевода $ в рубли необходимо получать по курсу [ЦБ РФ](https://www.cbr.ru/development/SXML/).
    
3. Скрипт работает постоянно для обеспечения обновления данных в онлайн режиме (необходимо учитывать, что строки в Google Sheets таблицу могут удаляться, добавляться и изменяться).

# Инструкция по запуску

Для работы скрипта нужно установить Redis, Postgresql как указано в их документации для вашей ОС

Перед запуском скрипта рекомендуется создать и запустить виртульное окружение

Установить зависимости из файла requirements.txt

 `pip install -r  requirements.txt`

В отдельном терминале  1 запустить сам проект

Запускаем миграции

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver`

В отдельном терминале  2 запустить Redis

`redis-server`

отдельная командная строка 3 в паке с проектом 

`celery -A google_sheet beat`


отдельная командная строка 4 в паке с проектом

`celery -A google_sheet  worker --loglevel=debug --concurrency=4`

Ссылка на документ excel https://docs.google.com/spreadsheets/d/1DgxlpfIAQCXdpNX9-_YWgeCz9HumXEAKPyeQYcwsJ7o/edit#gid=0
