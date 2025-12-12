"""
Скрипт для проверки подключения к базе данных PostgreSQL
"""
import asyncio
import sys
import traceback
import os
from app.core.config import settings
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text


async def check_sync_via_async():
    """Проверяет синхронное подключение через asyncpg"""
    print("\n=== Проверка через asyncpg (синхронный режим) ===")
    try:
        import asyncpg
        safe_url = f"postgresql://{settings.POSTGRES_USER}:***@{settings.POSTGRES_SERVER}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
        print(f"URL: {safe_url}")
        
        conn = await asyncpg.connect(
            host=settings.POSTGRES_SERVER,
            port=settings.POSTGRES_PORT,
            user=settings.POSTGRES_USER,
            password=settings.POSTGRES_PASSWORD,
            database=settings.POSTGRES_DB
        )
        version = await conn.fetchval("SELECT version();")
        await conn.close()
        print(f"[OK] Подключение через asyncpg успешно!")
        print(f"  Версия PostgreSQL: {version}")
        return True
    except Exception as e:
        print(f"[ERROR] Ошибка подключения через asyncpg: {e}")
        return False


async def check_async_connection():
    """Проверяет асинхронное подключение"""
    print("\n=== Проверка асинхронного подключения ===")
    engine = None
    try:
        async_url = settings.database_url
        print(f"URL: {async_url.replace(settings.POSTGRES_PASSWORD, '***')}")
        engine = create_async_engine(
            async_url, 
            echo=False,
            pool_pre_ping=True,
            connect_args={"server_settings": {"application_name": "check_db"}}
        )
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT version();"))
            version = result.scalar()
            print(f"[OK] Асинхронное подключение успешно!")
            print(f"  Версия PostgreSQL: {version}")
            return True
    except Exception as e:
        print(f"[ERROR] Ошибка асинхронного подключения: {e}")
        print(f"  Тип ошибки: {type(e).__name__}")
        traceback.print_exc()
        return False
    finally:
        if engine:
            await engine.dispose()


async def main():
    """Основная функция проверки"""
    print("=" * 60)
    print("Проверка подключения к PostgreSQL")
    print("=" * 60)
    print(f"Сервер: {settings.POSTGRES_SERVER}:{settings.POSTGRES_PORT}")
    print(f"База данных: {settings.POSTGRES_DB}")
    print(f"Пользователь: {settings.POSTGRES_USER}")
    
    # Проверяем через asyncpg (работает лучше на Windows)
    asyncpg_ok = await check_sync_via_async()
    
    # Затем асинхронное через SQLAlchemy
    async_ok = await check_async_connection()
    
    print("\n" + "=" * 60)
    if asyncpg_ok and async_ok:
        print("[OK] Все проверки пройдены успешно!")
        return True
    else:
        print("[ERROR] Некоторые проверки не прошли")
        if not asyncpg_ok:
            print("  - Подключение через asyncpg не работает")
        if not async_ok:
            print("  - Асинхронное подключение через SQLAlchemy не работает")
        print("\nВозможные решения:")
        print("1. Убедитесь, что PostgreSQL запущен: docker-compose ps")
        print("2. Проверьте логи: docker logs fastapi_postgres")
        print("3. Проверьте настройки в .env файле")
        return False


if __name__ == "__main__":
    if sys.platform == "win32":
        # Используем SelectorEventLoop вместо ProactorEventLoop для лучшей совместимости
        # ProactorEventLoop может иметь проблемы с некоторыми сетевыми операциями
        try:
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        except AttributeError:
            # Для Python 3.8+ используем ProactorEventLoop
            asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    
    try:
        success = asyncio.run(main())
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nПрервано пользователем")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nКритическая ошибка: {e}")
        traceback.print_exc()
        sys.exit(1)

