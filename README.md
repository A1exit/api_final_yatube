Проект API_YATUBE - новый проект для общения! Здесь вы сможете зарегистрироваться, авторизовываться и  начать создавать посты!
Для анонимных пользователей разрешен просмотр списка постов, а также просмотр каждого поста.
Если вы авторизовались, вы можете подписаться на понравившегося вам автора


Установка: Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/yandex-praktikum/kittygram.git
cd kittygram
Cоздать и активировать виртуальное окружение:

python3 -m venv env
source env/bin/activate
Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip
pip install -r requirements.txt
Выполнить миграции:

python3 manage.py migrate
Запустить проект:

python3 manage.py runserver

Примеры:

Ниже будут приведены примеры запросов к API_YATUBE
api/v1/posts/ - просмотр списка постов
api/v1/posts/{post_id}/comments/ - просмотр комментариев к посту с {post_id}
api/v1/jwt/create/ - здесь вы можете получить токен, который пригодится вам для дальнейших запросов
