# Переменные среды

**Русский** | [English](../en/enviroment.md)

Часть настроек проекта берётся из переменных окружения. 
Чтобы их определить, создайте файл **.env.example** рядом с **manage.py** в папке **src** и запишите туда данные в таком формате: **ПЕРЕМЕННАЯ=значение**.

Доступны следущие переменные:

- **POSTGRES_DB** - используется для определения другого имени для базы данных по умолчанию, которая создается при первом запуске образа;
- **POSTGRES_PORT** - порт, на котором будет работать база данных;
- **POSTGRES_HOST** - хост, на котором будет работать база данных;
- **POSTGRES_USER** - используется вместе с **POSTGRES_PASSWORD** для установки пользователя и его пароля;
- **POSTGRES_PASSWORD** - переменная окружения устанавливает пароль суперпользователя для PostgreSQL;
- **DEBUG** - дебаг-режим. Поставьте **True**, чтобы увидеть отладочную информацию в случае ошибки. Выключается значением **False**.
- **SECRET_KEY** - секретный ключ для конкретной установки Django.
Это используется для обеспечения криптографической подписи и должно иметь уникальное непредсказуемое значение;
- **ADMIN_USER_NAME** - логин для входа в админку;
- **ADMIN_USER_PASSWORD** - пароль администратора;
- **BROKER_URL** - хост на котором работает брокер;