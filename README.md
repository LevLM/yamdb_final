[![Django-app workflow](https://github.com/levlm/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/levlm/yamdb_final/actions/workflows/yamdb_workflow.yml)

# Проект YaMDb

Проект YaMDb собирает отзывы пользователей на различные произведения такие как
фильмы, книги и музыка.

## Описание проекта:

API YaMDb позволяет работать со следующими сущностями:

* JWT-токен (Auth): отправить confirmation_code на переданный email, получить
  JWT-токен
  в обмен на email и confirmation_code;
* Пользователи (Users): получить список всех пользователей, создать
  пользователя,
  получить пользователя по username, изменить данные пользователя по username,
  удалить
  пользователя по username, получить данные своей учётной записи, изменить
  данные своей учётной записи;
* Произведения (Titles), к которым пишут отзывы: получить список всех объектов,
  создать
  произведение для отзывов, информация об объекте, обновить информацию об
  объекте, удалить произведение.
  пользователя по username, получить данные своей учётной записи, изменить
  данные своей учётной записи;
* Категории (Categories) произведений: получить список всех категорий, создать
  категорию, удалить категорию;
* Жанры (Genres): получить список всех жанров, создать жанр, удалить жанр;
* Отзывы (Review): получить список всех отзывов, создать новый отзыв, получить
  отзыв по id,
  частично обновить отзыв по id, удалить отзыв по id;
* Комментарии (Comments) к отзывам: получить список всех комментариев к отзыву
  по id, создать
  новый комментарий для отзыва, получить комментарий для отзыва по id, частично
  обновить комментарий к отзыву по id, удалить комментарий к отзыву по id.

## Стек технологий:

* [Python 3.7+](https://www.python.org/downloads/)
* [Django 2.2.16](https://www.djangoproject.com/download/)
* [Django Rest Framework 3.12.4](https://pypi.org/project/djangorestframework/#files)
* [Pytest 6.2.4](https://pypi.org/project/pytest/)
* [Simple-JWT 1.7.2](https://pypi.org/project/djangorestframework-simplejwt/)
* [pytest 6.2.4](https://pypi.org/project/pytest/)
* [pytest-pythonpath 0.7.3](https://pypi.org/project/pytest-pythonpath/)
* [pytest-django 4.4.0](https://pypi.org/project/pytest-django/)
* [djangorestframework-simplejwt 4.7.2](https://pypi.org/project/djangorestframework-simplejwt/)
* [Pillow 9.2.0](https://pypi.org/project/Pillow/)
* [PyJWT 2.1.0](https://pypi.org/project/PyJWT/)
* [requests 2.26.0](https://pypi.org/project/requests/)
* [nginx](https://nginx.org/ru/)
* [PostgreSQL](https://www.postgresql.org)

## Workflow:

* Тестирование проекта (pytest, flake8).
* Сборка и публикация образа на DockerHub.
* Автоматический деплой на удаленный сервер.
* Отправка уведомления в телеграм-чат.

## Как запустить проект

### Клонировать репозиторий и перейти в него в командной строке

```
git clone git@github.com:levlm/yamdb_final.git
```

#### Выполните вход на свой удаленный сервер

#### Установите docker на сервер

```
sudo apt install docker.io
```

#### Установите docker-compose на сервер(https://github.com/docker/compose/releases)

```
sudo curl -L "https://github.com/docker/compose/releases/download/v2.6.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
```

#### Скопируйте файлы docker-compose.yaml и nginx/default.conf из проекта на сервер

```
scp docker-compose.yaml <username>@<host>:/home/<username>/docker-compose.yaml

scp -r nginx <username>@<host>:/home/<username>/
```

#### Добавьте в Secrets GitHub переменные окружения для работы

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=admin
POSTGRES_PASSWORD=ghbdtn11
DB_HOST=db
DB_PORT=5432

DOCKER_PASSWORD=<Docker password>
DOCKER_USERNAME=<Docker username>
USER=<username для подключения к серверу>
HOST=<IP сервера>
PASSPHRASE=<пароль для сервера, если он установлен>
SSH_KEY=<ваш SSH ключ(получить его на локальном компьютере: cat ~/.ssh/id_rsa)>
TG_CHAT_ID=<ID чата, в который придет сообщение>
TELEGRAM_TOKEN=<токен вашего бота>
```

#### Запушить на Github. После успешного деплоя зайдите на боевой сервер и выполните команды

#### Собрать статические файлы в STATIC_ROOT

```
docker-compose exec web python3 manage.py collectstatic --noinput
```

#### Применить миграции

```
docker-compose exec web python3 manage.py migrate --noinput
```

#### Заполнить базу данных

```
docker-compose exec web python3 manage.py loaddata fixtures.json
```

#### Создать суперпользователя Django

```
docker-compose exec web python manage.py createsuperuser
```

#### Проект будет доступен по адресу

```
http://158.160.43.47/admin

http://158.160.43.47/api/v1/[]
```

#### Документация API

```
http://158.160.43.47/redoc/
```

#### [Образ на DockerHub]

```
https://hub.docker.com/repository/docker/levlm/api_yamdb
```

#### Переменные окружения

Для подключения и выполненя запросов к базе данных PostgreSQL необходимо создать и заполнить файл ".env" с переменными окружения в папке "./infra/".

Шаблон для заполнения файла ".env":
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=admin
POSTGRES_PASSWORD=ghbdtn11
DB_HOST=db
DB_PORT=5432
```

#### Directed by [Lisus Lev](https://github.com/LevLM)
