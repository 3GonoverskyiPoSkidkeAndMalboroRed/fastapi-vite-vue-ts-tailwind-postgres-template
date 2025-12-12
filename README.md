# Как запустить контейнеры

*Используйте shell-скрипт с предустановленными параметрами для Buildkit*

```bash
./docker-build.sh

# Аналогично командам:
# docker-compose down && docker-compose up --build
```

Если скрипт выводит ошибки измените параметры export DOCKER_BUILDKIT=1 и export COMPOSE_DOCKER_CLI_BUILD=1 на:
```shell
export DOCKER_BUILDKIT=0
export COMPOSE_DOCKER_CLI_BUILD=0
```



# Как создать миграцию Alembic

1. Создать модель SQLAlchemy:
```
- Файл: backend/app/models/ваша_модель.py

- Наследовать от Base

- Определить поля и __tablename__

- взять за пример уже готовый файл изменив название класса и __tablename__
```

2. Импортировать модель в __init__.py:
```
- Файл: backend/app/models/__init__.py

- Добавить: from app.models.ваша_модель import ВашаМодель

- Добавить в __all__ = ["User", "ВашаМодель"]
```

3. Создать миграцию (автогенерация):
```bash
docker-compose exec backend alembic revision --autogenerate -m "описание_изменений"
```

4. Добавить в backend/alembic/env.py для автомиграции:
```python
from app.models import User, Test, <Ваша модель>
```

5. Проверить миграцию:
```bash
docker-compose exec backend alembic upgrade head
```

# Что содержит проект?

- Vite + Vue-ts(Vue с TypeScript) + TailwindCSS

- Alembic для обеспечения версионности миграций в БД

- FastApi и зависимости к нему для ассинхронных запросов