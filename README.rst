This project was made as a test task .
In it, you can create notes and assign them a priority, status, and description.
Enjoy your use



Необходимые компоненты
======================

Для запуска вам необходимо установить следующие компоненты:

-  ``docker`` (версии ``18.06`` или выше)
-  ``docker-compose`` (версии ``1.22`` или выше)

Запуск
======

Для запуска проекта необходимо выполнить следующие команды:

Стянуть проект с git репозитория

Сбилдить образы проекта

    docker-compose build

Поднять проект
    docker-compose up
Выполнить миграции

    docker-compose run --rm to_do_web python manage.py migrate