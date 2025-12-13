# Гайд по установке WSL2 на Windows

Windows Subsystem for Linux 2 (WSL2) позволяет запускать дистрибутивы Linux прямо в Windows без виртуальной машины.

## Требования

- Windows 10 версии 2004 и выше (сборка 19041 и выше) или Windows 11
- 64-разрядная система
- Поддержка виртуализации в BIOS/UEFI

## Проверка версии Windows

1. Нажмите `Win + R`
2. Введите `winver` и нажмите Enter
3. Проверьте версию Windows (должна быть 2004 или выше)

## Метод 1: Установка через PowerShell (рекомендуется)

### Шаг 1: Откройте PowerShell от имени администратора

1. Нажмите `Win + X`
2. Выберите "Windows PowerShell (администратор)" или "Терминал (администратор)"
3. Подтвердите запрос контроля учетных записей

### Шаг 2: Включите компоненты Windows

Выполните следующую команду в PowerShell:

```powershell
wsl --install
```

Эта команда автоматически:
- Включит необходимые компоненты Windows (WSL, Virtual Machine Platform)
- Установит WSL2 как версию по умолчанию
- Установит дистрибутив Ubuntu по умолчанию
- Попросит перезагрузить компьютер

### Шаг 3: Перезагрузка

После выполнения команды перезагрузите компьютер:

```powershell
Restart-Computer
```

### Шаг 4: Первый запуск

После перезагрузки:

1. Откройте меню "Пуск"
2. Найдите и запустите "Ubuntu" (или другой установленный дистрибутив)
3. Дождитесь завершения установки
4. Создайте имя пользователя и пароль для Linux (пароль не будет отображаться при вводе)

## Метод 2: Ручная установка

Если автоматическая установка не работает, выполните шаги вручную:

### Шаг 1: Включение компонентов Windows

Выполните в PowerShell от имени администратора:

```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

### Шаг 2: Перезагрузка

Перезагрузите компьютер:

```powershell
Restart-Computer
```

### Шаг 3: Установка обновления ядра WSL2

1. Скачайте последний пакет обновления ядра WSL2:
   - Перейдите на: https://aka.ms/wsl2kernel
   - Или выполните в PowerShell:

```powershell
Invoke-WebRequest -Uri https://aka.ms/wsl2kernel -OutFile $env:TEMP\wsl_update_x64.msi
Start-Process msiexec.exe -Wait -ArgumentList "/i $env:TEMP\wsl_update_x64.msi /quiet /norestart"
```

2. Запустите установщик и следуйте инструкциям

### Шаг 4: Установка WSL2 как версии по умолчанию

```powershell
wsl --set-default-version 2
```

### Шаг 5: Установка дистрибутива Linux

#### Через Microsoft Store (рекомендуется):

1. Откройте Microsoft Store
2. Найдите "Ubuntu" (или другой дистрибутив)
3. Нажмите "Получить" или "Установить"
4. После установки запустите из меню "Пуск"

#### Через командную строку:

```powershell
# Просмотр доступных дистрибутивов
wsl --list --online

# Установка Ubuntu (пример)
wsl --install -d Ubuntu

# Установка других дистрибутивов
wsl --install -d Debian
wsl --install -d openSUSE-Leap-15-3
```

## Проверка установки

### Проверка версии WSL

```powershell
wsl --version
```

Должно отображаться:
```
WSL version: 2.x.x
Kernel version: 5.x.x
```

### Проверка установленных дистрибутивов

```powershell
wsl --list --verbose
```

Пример вывода:
```
  NAME      STATE           VERSION
* Ubuntu    Running         2
```

### Проверка из Linux

Откройте терминал WSL и выполните:

```bash
uname -a
cat /etc/os-release
```

## Настройка WSL2

### Изменение версии дистрибутива на WSL2

Если дистрибутив установлен в WSL1, переключите на WSL2:

```powershell
wsl --set-version Ubuntu 2
```

Замените `Ubuntu` на имя вашего дистрибутива.

### Настройка пользователя по умолчанию

```powershell
ubuntu config --default-user username
```

### Обновление WSL2

```powershell
wsl --update
```

### Остановка и перезапуск WSL

```powershell
# Остановка всех дистрибутивов
wsl --shutdown

# Запуск конкретного дистрибутива
wsl -d Ubuntu
```

## Устранение проблем

### Проблема: "WSL 2 requires an update to its kernel component"

**Решение:**
1. Скачайте и установите обновление ядра: https://aka.ms/wsl2kernel
2. Перезагрузите компьютер

### Проблема: "Virtualization is not enabled"

**Решение:**
1. Перезагрузите компьютер
2. Войдите в BIOS/UEFI (обычно F2, F10, F12 или Del при загрузке)
3. Найдите опцию виртуализации (Intel VT-x или AMD-V)
4. Включите виртуализацию
5. Сохраните изменения и перезагрузите

### Проблема: "The requested operation could not be completed"

**Решение:**
1. Убедитесь, что Hyper-V отключен (если не используется)
2. Выполните в PowerShell от имени администратора:

```powershell
bcdedit /set hypervisorlaunchtype auto
```

3. Перезагрузите компьютер

### Проблема: Дистрибутив не запускается

**Решение:**
1. Проверьте версию WSL:

```powershell
wsl --list --verbose
```

2. Если версия 1, переключите на WSL2:

```powershell
wsl --set-version Ubuntu 2
```

3. Если проблема сохраняется, переустановите дистрибутив:

```powershell
wsl --unregister Ubuntu
wsl --install -d Ubuntu
```

### Проблема: Медленная работа файловой системы

**Решение:**
Храните файлы проекта в файловой системе Linux (`/home/username/`), а не в Windows (`/mnt/c/`).

## Полезные команды WSL

```powershell
# Список всех дистрибутивов
wsl --list --verbose

# Запуск конкретного дистрибутива
wsl -d Ubuntu

# Остановка всех дистрибутивов
wsl --shutdown

# Обновление WSL
wsl --update

# Экспорт дистрибутива
wsl --export Ubuntu backup.tar

# Импорт дистрибутива
wsl --import Ubuntu C:\WSL\Ubuntu backup.tar

# Удаление дистрибутива
wsl --unregister Ubuntu
```

## Интеграция с VS Code

1. Установите расширение "Remote - WSL" в VS Code
2. Откройте папку в WSL: `code .` из терминала WSL
3. Или используйте команду: `code --remote wsl+Ubuntu /path/to/project`

## Интеграция с Docker

WSL2 может использоваться с Docker Desktop:

1. Установите Docker Desktop для Windows
2. В настройках Docker включите "Use the WSL 2 based engine"
3. Выберите дистрибутивы WSL для интеграции

## Дополнительные ресурсы

- [Официальная документация Microsoft](https://docs.microsoft.com/windows/wsl/)
- [Руководство по WSL2](https://docs.microsoft.com/windows/wsl/install)
- [Список доступных дистрибутивов](https://docs.microsoft.com/windows/wsl/install-manual#step-6---install-your-linux-distribution-of-choice)

## Рекомендуемые дистрибутивы

- **Ubuntu** - самый популярный, хорошо документирован
- **Debian** - стабильный, минималистичный
- **openSUSE** - для корпоративного использования
- **Alpine** - очень легкий, для контейнеров

## Следующие шаги

После установки WSL2:

1. Обновите систему:

```bash
sudo apt update && sudo apt upgrade -y
```

2. Установите необходимые инструменты:

```bash
sudo apt install -y build-essential git curl wget
```

3. Настройте Git:

```bash
git config --global user.name "Ваше имя"
git config --global user.email "ваш@email.com"
```

4. Начните использовать WSL2 для разработки!

