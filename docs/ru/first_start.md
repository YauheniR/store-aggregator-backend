# Первый старт

**Русский** | [English](../en/first_start.md)

Вы можете запустить проект **store-aggregator-backend** локально или в докер контейнерах используя Makefile

### Зависимости

* [Python 3.7.4](https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html)
* [Docker](https://docs.docker.com/engine/install/)
* [Docker-Compose](https://docs.docker.com/compose/install/)

### Установка

Прежде всего, установите [Docker](https://docs.docker.com/engine/install/) и [Docker-Compose](https://docs.docker.com/compose/install/)

Следующим шагом является настройка переменных среды.
Вы можете прочитать, как настроить файл переменных среды, в разделе [Переменные среды](enviroment.md)

После того, как все было настроено, вы можете запустить проект локально либо развернуть его в докер контейнерах.

Для запуска проекта локально в [корне](../..) проекта выполните комманду:

    make run_local

Теперь откройте проект в [браузере](http://localhost:8000).

Для запуска всех сервисов проекта в докер контейнерах в [корне](../..) проекта выполните комманду:

    make run_docker