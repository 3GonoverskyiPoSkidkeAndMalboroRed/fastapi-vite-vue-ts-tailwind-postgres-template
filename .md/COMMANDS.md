## Docker Compose - Выполнение команд в контейнерах

### Войти в терминал контейнера(например для автогенерации миграций через alembic):
```bash
# Пример: открыть интерактивную оболочку Bash
docker-compose exec backend bash
```

### PostgreSQL контейнер (fastapi_postgres)
```bash
# Выполнить команду в контейнере postgres
docker-compose exec postgres <команда>

# Пример: подключиться к PostgreSQL через psql
docker-compose exec postgres psql -U postgres -d postgres

# Пример: выполнить SQL команду
docker-compose exec postgres psql -U postgres -d postgres -c "SELECT version();"
```

## Alembic - Миграции базы данных

```bash
# Применить все миграции до последней версии
alembic upgrade head

# Откатить последнюю миграцию (на одну версию назад)
alembic downgrade -1

# Откатить все миграции до начального состояния (базовая версия)
alembic downgrade base

# Показать текущую версию миграции в базе данных
alembic current

# Показать историю всех миграций
alembic history

# Создать новую миграцию с автогенерацией на основе изменений в моделях
alembic revision --autogenerate -m "описание_изменений"

# Создать пустую миграцию для ручного написания SQL-кода
alembic revision -m "описание_изменений"
```

## Очистка данных Docker

### Остановка и удаление контейнеров
```bash
# Остановить все контейнеры
docker-compose down

# Остановить и удалить контейнеры, сети
docker-compose down --remove-orphans

# Остановить, удалить контейнеры и volumes (ОСТОРОЖНО: удалит данные БД!)
docker-compose down -v
```

### Очистка volumes
```bash
# Удалить все неиспользуемые volumes
docker volume prune

# Удалить конкретный volume (например, postgres_data)
docker volume rm fastapi-vite-postgres-templete_postgres_data

# Показать список всех volumes
docker volume ls
```

### Очистка образов
```bash
# Удалить все неиспользуемые образы
docker image prune

# Удалить все неиспользуемые образы (включая используемые)
docker image prune -a

# Удалить конкретный образ
docker rmi <image_id>
```

### Полная очистка Docker
```bash
# Удалить все остановленные контейнеры, неиспользуемые сети, образы и кэш сборки
docker system prune

# Полная очистка (включая volumes - ОСТОРОЖНО!)
docker system prune -a --volumes
```

### Очистка логов
```bash
# Просмотр логов контейнера
docker-compose logs <service_name>

# Просмотр логов с обновлением в реальном времени
docker-compose logs -f <service_name>

# Очистка логов контейнера (требует остановки контейнера)
docker-compose stop <service_name>
truncate -s 0 $(docker inspect --format='{{.LogPath}}' <container_id>)
docker-compose start <service_name>
```

## Управление контейнерами

```bash
# Запустить контейнеры в фоновом режиме
docker-compose up -d

# Перезапустить конкретный сервис
docker-compose restart <service_name>

# Остановить конкретный сервис
docker-compose stop <service_name>

# Показать статус контейнеров
docker-compose ps

# Показать логи всех сервисов
docker-compose logs

# Пересобрать и запустить контейнеры
docker-compose up --build
```

## Полезные команды для разработки

```bash
# Просмотр переменных окружения контейнера
docker-compose exec backend env

# Проверка подключения к базе данных
docker-compose exec backend python check_db.py

# Выполнить команду в контейнере без привязки к терминалу
docker-compose exec -T backend alembic upgrade head

# Просмотр использования ресурсов
docker stats

# Просмотр информации о контейнере
docker inspect <container_name>
```

## Если .sh скрипты не запускаются(Permission denied)

```bash
chmod +x ./setup-buildkit.sh
chmod +x ./backend/entrypoint.sh
chmod +x ./docker-build.sh
```
