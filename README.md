# **Описание проекта API для Yatube**
### REST API для Yatube разработан для Yandex Practicum.
### Поддерживает запросы GET, POST, PUT, PATCH, DELETE

## **Как запустить проект**
### Клонировать репозиторий и вписать его в командой строке
git clone https://github.com/tapp41k/api_final_yatube.git
### Создать и активировать виртуальное окружение
+'python -m venv venv'
+'source venv/bin/activate'
+'python -m pip install --upgrage pip'
### Установить из файла зависимости
'pip install -r requirements.txt'
### Выполнить миграции
'python manage.py migrate'
### Запустить проект
'python manage.py runserver'

## **Примеры запросов на сервере**

POST-запрос с токеном, добавление новой публикации в коллекцию публикаций.

`POST http://localhost:port/api/v1/posts/`

'''
>{
>   "text": "Тестовый пост 1",
>   "group": 1
>}
'''

## **Пример ответа**

'''
>{
>    "id": 1,
>    "author": "root",
>    "text": "Тестовый пост 1",
>    "pub_date": "2021-12-22T16:11:54.331905Z",
>    "image": null,
>    "group": 1
>}
'''