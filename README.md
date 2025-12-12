# Запуск БД

1. Запуск docker контейнера:

```bash
docker compose up --build
```

Также можно попробовать через shell-скрипт(потребуется Git Bash или WSL терминал):
```bash
./docker-build.sh
```

2. В консоли появятся такие сообщения:
```bash
fastapi_postgres  | The files belonging to this database system will be owned by user "postgres".
fastapi_postgres  | This user must also own the server process.
fastapi_postgres  | 
fastapi_postgres  | The database cluster will be initialized with locale "en_US.utf8".
fastapi_postgres  | The default database encoding has accordingly been set to "UTF8".
fastapi_postgres  | The default text search configuration will be set to "english".
fastapi_postgres  | 
fastapi_postgres  | Data page checksums are disabled.
fastapi_postgres  | 
fastapi_postgres  | fixing permissions on existing directory /var/lib/postgresql/data ... ok
fastapi_postgres  | creating subdirectories ... ok
fastapi_postgres  | selecting dynamic shared memory implementation ... posix
fastapi_postgres  | selecting default "max_connections" ... 100
fastapi_postgres  | selecting default "shared_buffers" ... 128MB
fastapi_postgres  | selecting default time zone ... UTC
fastapi_postgres  | creating configuration files ... ok
fastapi_postgres  | running bootstrap script ... ok
fastapi_postgres  | sh: locale: not found
fastapi_postgres  | 2025-12-12 18:01:27.813 UTC [35] WARNING:  no usable system locales were found
fastapi_postgres  | performing post-bootstrap initialization ... ok
fastapi_postgres  | syncing data to disk ... ok
fastapi_postgres  | 
fastapi_postgres  | 
fastapi_postgres  | Success. You can now start the database server using:
fastapi_postgres  | 
fastapi_postgres  |     pg_ctl -D /var/lib/postgresql/data -l logfile start
fastapi_postgres  | 
fastapi_postgres  | initdb: warning: enabling "trust" authentication for local connections
fastapi_postgres  | initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or --auth-local and --auth-host, the next time you run initdb.
fastapi_postgres  | waiting for server to start....2025-12-12 18:01:28.635 UTC [41] LOG:  starting PostgreSQL 17.7 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
fastapi_postgres  | 2025-12-12 18:01:28.639 UTC [41] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
fastapi_postgres  | 2025-12-12 18:01:28.650 UTC [44] LOG:  database system was shut down at 2025-12-12 18:01:28 UTC
fastapi_postgres  | 2025-12-12 18:01:28.657 UTC [41] LOG:  database system is ready to accept connections
fastapi_postgres  |  done
fastapi_postgres  | server started
fastapi_postgres  | CREATE DATABASE
fastapi_postgres  | 
fastapi_postgres  | 
fastapi_postgres  | /usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/*
fastapi_postgres  | 
fastapi_postgres  | waiting for server to shut down....2025-12-12 18:01:28.845 UTC [41] LOG:  received fast shutdown request
fastapi_postgres  | 2025-12-12 18:01:28.849 UTC [41] LOG:  aborting any active transactions
fastapi_postgres  | 2025-12-12 18:01:28.852 UTC [41] LOG:  background worker "logical replication launcher" (PID 47) exited with exit code 1
fastapi_postgres  | 2025-12-12 18:01:28.853 UTC [42] LOG:  shutting down
fastapi_postgres  | 2025-12-12 18:01:28.856 UTC [42] LOG:  checkpoint starting: shutdown immediate
fastapi_postgres  |                                                                                     ; 0 WAL file(s) added, 0 removed, 0 recycled; write=0.027 s, sync=0.038 s, total=0.084 s; sy
fastapi_postgres  | 2025-12-12 18:01:29.077 UTC [1] LOG:  stfor start up.                               lsn=0/19150D0arting PostgreSQL 17.7 on x86_64-pc-linux-musl, compiled by 
gcc (Alpine 15.2.0) 15.2.0, 64-bit                          arting PostgreSQL 17.7 on x86_64-pc-linux-mu
fastapi_postgres  | 2025-12-12 18:01:29.077 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432                stening on IPv4 address "0.0.0.0", port 5432
fastapi_postgres  | 2025-12-12 18:01:29.077 UTC [1] LOG:  listening on IPv6 address "::", port 5432                     stening on IPv6 address "::", port 5432     
fastapi_postgres  | 2025-12-12 18:01:29.086 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/sl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bitstening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"  
fastapi_postgres  | 2025-12-12 18:01:29.094 UTC [57] LOG:  database system was shut down at 2025-12-12 1atabase system was shut down at 2025-12-12 18:01:28 UTC                                                 .s.PGSQL.5432"
fastapi_postgres  | 2025-12-12 18:01:29.101 UTC [1] LOG:  database system is ready to accept connections8:01:28 UTCtabase system is ready to accept connections


fastapi_postgres  | 2025-12-12 18:06:37.626 UTC [55] LOG:  checkpoint starting: time
fastapi_postgres  | 2025-12-12 18:06:42.055 UTC [55] LOG:  checkpoint complete: wrote 47 buffers (0.3%); 0 WAL file(s) added, 0 removed, 0 recycled; write=4.413 s, sync=0.007 s, total=4.430 s; sync files=12, longest=0.004 s, average=0.001 s; distance=270 kB, estimate=270 kB; lsn=0/19589B0, redo lsn=0/1958958
```
Ключевая фраза об успешном запуске БД: ```database system is ready to accept connections```

#### Чтобы просматривать БД(типо как в phpMyAdmin) нужен pgAdmin4(качать .exe файл) - https://www.postgresql.org/ftp/pgadmin/pgadmin4/v9.11/windows/

# Запуск бэкэнда(FastApi сервера)
1. Создать виртуальное окружение и запустить его:
```bash
# Сначала перейти в директорию backend
cd backend
# Создать виртуальное окружение
python -m venv venv
# После создания папки venv
source venv/Scripts/Activate
```

2. Установка зависимостей:
```bash
pip install -r requirements.txt
```

3. Запуск миграциия через alembic:
```bash 
alembic upgrade head

#Ещё команды для alembic
# alembic history
```

4. Запуск FastApi-сервера:
```bash
python run.py

#Получить доступ к голому Api для отладки можно по адресу в браузере http://localhost:8000/docs
```

# Запуск Vite-сервера(фронтенда)

1. Перейти в директорию фронтенда:
```bash
cd frontend
```

2. Установить зависимости:
```bash
npm install
```

3. Установить зависимости:
```bash
npm run dev

# Доступ к фронтенду можно получить по адресу http://localhost:5173
```


