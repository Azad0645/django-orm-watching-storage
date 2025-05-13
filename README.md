# Пульт охраны банка

Описание проекта:
- Пульт охраны — это внутренняя система для сотрудников банка, позволяющая отслеживать их пропуска. Проект показывает, кто находится в хранилище, когда человек вошёл и как долго находился внутри.
 

## Как установить 

Создайте файл .env в корневой папке проекта и заполните его следующими переменными окружения:
- DB_ENGINE=Бэкенд для подключения к базе данных 
- DB_HOST=Адрес сервера базы данных
- DB_PORT=Порт для подключения к базе данных
- DB_NAME=Название базы данных
- DB_USER=Имя пользователя 
- DB_PASSWORD=Пароль пользователя 
- SECRET_KEY=Секретный ключ Django. Используется для обеспечения криптографической подписи и должен иметь уникальное, непредсказуемое значение
- DEBUG=True (Булевое значение, включающее/выключающее режим отладки)
- ALLOWED_HOSTS=localhost,127.0.0.1 (Список строк, представляющих имена хостов/доменов, которые может обслуживать этот сайт Django)

Установка зависимостей:
- Python 3.12 должен быть уже установлен.

```bash
pip install -r requirements.txt
```

Запустите сервер:

```bash
python manage.py runserver
```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).

# Bank security console

Project description:
- The security console is an internal system for bank employees, allowing to track their passes. The project shows who is in the vault, when the person entered and how long they were inside.

## How to install 

Create .env file in the project root folder and fill it with the following environment variables:
- DB_ENGINE=Backend for connecting to the database
- DB_HOST=Database server address
- DB_PORT=Port for connecting to the database
- DB_NAME=Database name
- DB_USER=Username
- DB_PASSWORD=User password 
- SECRET_KEY= Django secret key. This is used to provide cryptographic signing, and should be set to a unique, unpredictable value 
- DEBUG=True (A boolean that turns on/off debug mode)
- ALLOWED_HOSTS=localhost,127.0.0.1 (A list of strings representing the host/domain names that this Django site can serve) 

Installing dependencies:
- Python 3.12 must already be installed.

```bash
pip install -r requirements.txt
```

Run the server:

```bash
python manage.py runserver
```

## Project goal

The code was written for educational purposes in an online course for web developers [dvmn.org](https://dvmn.org).