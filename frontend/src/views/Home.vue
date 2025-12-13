<template>
  <div class="px-4 py-6 sm:px-0">
    <div class="bg-white overflow-hidden shadow rounded-lg">
      <div class="px-4 py-5 sm:p-6">
        <h1 class="text-3xl font-bold text-gray-900 mb-4">
          Добро пожаловать, узкоглазая тварь!
        </h1>
        <p class="text-gray-600 mb-6">
          Это шаблон проекта с FastAPI, PostgreSQL, Vue 3, TypeScript и Tailwind CSS.
        </p>
        
        <!-- Кнопка для показа Alert -->
        <div class="mb-6">
          <button
            @click="showAlert = !showAlert"
            class="bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md transition-colors"
          >
            {{ showAlert ? 'Скрыть уведомление' : 'Показать уведомление' }}
          </button>
        </div>

        <!-- Alert компонент -->
        <div v-if="showAlert" class="mb-6">
          <Alert :variant="alertVariant">
            <AlertTitle>Уведомление</AlertTitle>
            <AlertDescription>
              Это пример использования компонента Alert из библиотеки Sigma UI.
              Вы можете изменить вариант на "destructive" для предупреждений.
            </AlertDescription>
          </Alert>
        </div>

        <!-- Переключатель варианта Alert -->
        <div v-if="showAlert" class="mb-6">
          <button
            @click="toggleAlertVariant"
            class="bg-gray-600 hover:bg-gray-700 text-white font-medium py-2 px-4 rounded-md transition-colors text-sm"
          >
            Переключить на {{ alertVariant === 'default' ? 'destructive' : 'default' }}
          </button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="bg-blue-50 p-4 rounded-lg">
            <h2 class="text-xl font-semibold text-blue-900 mb-2">Backend</h2>
            <ul class="text-blue-700 space-y-1">
              <li>✓ FastAPI</li>
              <li>✓ PostgreSQL</li>
              <li>✓ SQLAlchemy (async) - для асинхронных запросов и ORM</li>
              <li>✓ Pydantic - для валидации модели данных</li>
              <li>✓ Alembic миграции -  для версионности миграций в БД</li>
            </ul>
          </div>
          <div class="bg-green-50 p-4 rounded-lg">
            <h2 class="text-xl font-semibold text-green-900 mb-2">Frontend</h2>
            <ul class="text-green-700 space-y-1">
              <li>✓ Vue 3</li>
              <li>✓ TypeScript</li>
              <li>✓ Vite</li>
              <li>✓ Tailwind CSS</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Alert, AlertTitle, AlertDescription, type AlertVariants } from '@/components/ui/alert'

const showAlert = ref(false)
const alertVariant = ref<AlertVariants['variant']>('default')

const toggleAlertVariant = () => {
  alertVariant.value = alertVariant.value === 'default' ? 'destructive' : 'default'
}
</script>

