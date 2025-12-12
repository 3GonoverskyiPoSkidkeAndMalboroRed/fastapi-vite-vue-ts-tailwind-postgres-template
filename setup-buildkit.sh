#!/bin/bash
# Скрипт настройки BuildKit для проекта
# BuildKit ускоряет сборку Docker образов в 2-5 раз и улучшает кэширование
# 
# Использование: ./setup-buildkit.sh
# Запустите один раз после клонирования репозитория

set -e

echo "🔧 Настройка Docker BuildKit для проекта..."

# Определяем shell конфигурацию
SHELL_CONFIG=""
SHELL_NAME=""

if [ -n "$ZSH_VERSION" ]; then
    SHELL_CONFIG="$HOME/.zshrc"
    SHELL_NAME="zsh"
elif [ -n "$BASH_VERSION" ]; then
    SHELL_CONFIG="$HOME/.bashrc"
    SHELL_NAME="bash"
else
    echo "❌ Не удалось определить shell (поддерживаются только zsh и bash)"
    echo "   Вручную добавьте в ваш shell конфигурационный файл:"
    echo "   export DOCKER_BUILDKIT=1"
    echo "   export COMPOSE_DOCKER_CLI_BUILD=1"
    exit 1
fi

# Проверяем существование файла конфигурации
if [ ! -f "$SHELL_CONFIG" ]; then
    echo "⚠️  Файл $SHELL_CONFIG не найден. Создаю..."
    touch "$SHELL_CONFIG"
fi

# Проверяем, не добавлены ли уже переменные
if grep -q "DOCKER_BUILDKIT" "$SHELL_CONFIG" 2>/dev/null; then
    echo "✅ BuildKit уже настроен в $SHELL_CONFIG"
    echo "   Переменные уже присутствуют в конфигурации"
    
    # Проверяем, загружены ли переменные в текущей сессии
    if [ -z "$DOCKER_BUILDKIT" ]; then
        echo ""
        echo "💡 Для применения в текущей сессии выполните:"
        echo "   source $SHELL_CONFIG"
    else
        echo "✅ Переменные активны в текущей сессии"
    fi
else
    echo "📝 Добавляю переменные BuildKit в $SHELL_CONFIG..."
    
    # Добавляем разделитель и комментарии
    echo "" >> "$SHELL_CONFIG"
    echo "# ============================================" >> "$SHELL_CONFIG"
    echo "# Docker BuildKit - автоматическое включение" >> "$SHELL_CONFIG"
    echo "# Добавлено скриптом setup-buildkit.sh" >> "$SHELL_CONFIG"
    echo "# BuildKit ускоряет сборку Docker образов в 2-5 раз" >> "$SHELL_CONFIG"
    echo "# ============================================" >> "$SHELL_CONFIG"
    echo "export DOCKER_BUILDKIT=1" >> "$SHELL_CONFIG"
    echo "export COMPOSE_DOCKER_CLI_BUILD=1" >> "$SHELL_CONFIG"
    
    echo "✅ BuildKit успешно настроен!"
    echo ""
    echo "📌 Для применения изменений:"
    echo "   1. Перезапустите терминал, ИЛИ"
    echo "   2. Выполните: source $SHELL_CONFIG"
    echo ""
    echo "🚀 После этого BuildKit будет автоматически включаться"
    echo "   для всех команд docker-compose build и docker-compose up --build"
fi

echo ""
echo "✨ Готово! Теперь можно использовать стандартные команды:"
echo "   docker-compose build"
echo "   docker-compose up --build"
echo "   docker-compose up -d --build"

