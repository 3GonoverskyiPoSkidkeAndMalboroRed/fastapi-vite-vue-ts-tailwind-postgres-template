#!/bin/bash
set -e

echo "Ожидание готовности базы данных..."

# Функция для проверки доступности PostgreSQL
wait_for_postgres() {
    local max_attempts=30
    local attempt=1
    
    until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_SERVER" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q' 2>/dev/null; do
        if [ $attempt -ge $max_attempts ]; then
            echo "Ошибка: База данных недоступна после $max_attempts попыток"
            exit 1
        fi
        echo "Попытка $attempt/$max_attempts: База данных недоступна - ожидание..."
        sleep 2
        attempt=$((attempt + 1))
    done
    echo "✓ База данных готова!"
}

# Ждем готовности базы данных
wait_for_postgres

echo "Выполнение миграций Alembic..."
cd /app
alembic upgrade head

if [ $? -eq 0 ]; then
    echo "✓ Миграции успешно применены"
else
    echo "⚠ Ошибка при выполнении миграций"
    exit 1
fi

echo "Запуск приложения..."
exec "$@"

