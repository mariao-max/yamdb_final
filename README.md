# Проект yamdb_final

![workflow](https://github.com/mariao-max/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

### Краткое описание проекта
- Данный сервис собирает отзывы (Review) пользователей на произведения (Titles). Произведения делятся на категории: "Книги", "Фильмы", "Музыка". Список категорий (Category) может быть расширен администратором (например, можно добавить категорию "Ювелирные украшения").
- В сервисе предусмотрены разные наборы разрешений на действия в зависимости от роли пользователя: Аноним, Просто аутентифицированный пользователь, Модератор, Администратор, Суперпользователь. 
 
### Установка
Все описанное ниже относится к ОС Linux. 
Клонируем репозиторий и и переходим в него: 

**Шаг 1. Клонируйте репозиторий себе на компьютер**
Введите команду:
```git clone https://github.com/mariao-max/yamdb_final.git```

**Шаг 2. Создайте в клонированной директории файл .env**
# Требования и пример заполнения файла .env

Файл .env должен содержать следующие переменные:

```
DB_ENGINE - драйвер СУБД для Django
DB_NAME - имя базы данных для api_yamdb
POSTGRES_USER - имя пользователя, владельца базы данных или администратора СУБД
POSTGRES_PASSWORD - пароль пользователя из предыдущего пункта
BD_HOST - имя хоста (docker-контейнера)
DB_PORT - порт для подключения к базе данных
SECRET_KEY - секретный ключ для нужд Django
```

Пример заполнения значениями по умолчанию:

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
BD_HOST=db
DB_PORT=5432
SECRET_KEY=Here_shoud_be_something_long_and_complex
```

**Шаг 3. Запуск docker-compose**
Для запуска необходимо выполнить из директории с проектом команду:

```docker-compose up -d```

**Шаг 4. База данных**
Создаем и применяем миграции:

```
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

**Шаг 5. Подгружаем статику**
Выполните команду:

```docker-compose exec web python manage.py collectstatic```

**Другие команды**
Создание суперпользователя:
```docker-compose exec web python manage.py createsuperuser```

Остановить работу всех контейнеров можно командой:
```docker-compose down```

Для пересборки и запуска контейнеров воспользуйтесь командой:
```docker-compose up -d --build ```

Мониторинг запущенных контейнеров:
```docker status```

Останавливаем и удаляем контейнеры, сети, тома и образы:
```docker-compose down -v```
