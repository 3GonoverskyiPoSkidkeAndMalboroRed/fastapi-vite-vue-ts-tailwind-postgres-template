FROM node:20-alpine

WORKDIR /app

# Копирование package файлов
COPY package*.json ./

# Установка зависимостей
RUN npm install

# Копирование остальных файлов
COPY . .

# Порт для Vite
EXPOSE 5173

# Команда запуска
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]


