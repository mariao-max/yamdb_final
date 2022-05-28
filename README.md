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
Пример:
```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```
Измените файл settings.py, чтобы значения загружались из переменных окружения:
```
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT')
    }
} 
```
**Шаг 3. Запуск docker-compose**
Для запуска необходимо выполнить из директории с проектом команду:

```docker-compose up -d```

**Шаг 4. База данных**
Создаем и применяем миграции:

```docker-compose exec web python manage.py makemigrations```
```docker-compose exec web python manage.py migrate ```

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
