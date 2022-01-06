## API социальной сети YaTube

### Стэк:

- Python 3.7
- Django 2.2.16
- Django Rest Framework 3.12.4

### Как запустить проект:

#### Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/patridon87/api_final_yatube.git
```
```
cd api_final_yatube
```
#### Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
#### Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
#### Выполнить миграции:
```
python3 manage.py migrate
```
#### Запустить проект:
```
python3 manage.py runserver
```
#### Примеры запросов:
```
GET /api/v1/posts/ - получение списка постов
POST /api/v1/posts/ - создание поста
GET /api/v1/posts/{post_id}/comments - получение списка комментариев к посту
POST /api/v1/posts/{post_id}/comments - создание комментария к посту
```
#### Автор
Алексей Останин

