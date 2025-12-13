<template>
  <div class="px-4 py-6 sm:px-0">
    <div class="bg-white shadow rounded-lg">
      <div class="px-4 py-5 sm:p-6">
        <div class="flex justify-between items-center mb-6">
          <h1 class="text-2xl font-bold text-gray-900">Пользователи</h1>
          <button
            @click="showCreateForm = !showCreateForm"
            class="bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md transition-colors"
          >
            {{ showCreateForm ? 'Отмена' : 'Создать пользователя' }}
          </button>
        </div>

        <!-- Форма создания пользователя -->
        <div v-if="showCreateForm" class="mb-6 p-4 bg-gray-50 rounded-lg">
          <h2 class="text-lg font-semibold mb-4">Новый пользователь</h2>
          <form @submit.prevent="createUser" class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">
                Email
              </label>
              <input
                v-model="newUser.email"
                type="email"
                required
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">
                Имя пользователя
              </label>
              <input
                v-model="newUser.username"
                type="text"
                required
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">
                Пароль
              </label>
              <input
                v-model="newUser.password"
                type="password"
                required
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
            <button
              type="submit"
              :disabled="loading"
              class="bg-green-600 hover:bg-green-700 text-white font-medium py-2 px-4 rounded-md transition-colors disabled:opacity-50"
            >
              {{ loading ? 'Создание...' : 'Создать' }}
            </button>
          </form>
        </div>

        <!-- Список пользователей -->
        <div v-if="loading && users.length === 0" class="text-center py-8">
          <p class="text-gray-500">Загрузка...</p>
        </div>
        <div v-else-if="error" class="text-center py-8">
          <p class="text-red-500">{{ error }}</p>
        </div>
        <div v-else-if="users.length === 0" class="text-center py-8">
          <p class="text-gray-500">Пользователи не найдены</p>
        </div>
        <div v-else class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  ID
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Email
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Имя пользователя
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Статус
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Создан
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="user in users" :key="user.id" class="hover:bg-gray-50">
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                  {{ user.id }}
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                  {{ user.email }}
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                  {{ user.username }}
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <span
                    :class="[
                      user.is_active
                        ? 'bg-green-100 text-green-800'
                        : 'bg-red-100 text-red-800',
                      'px-2 inline-flex text-xs leading-5 font-semibold rounded-full'
                    ]"
                  >
                    {{ user.is_active ? 'Активен' : 'Неактивен' }}
                  </span>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  {{ formatDate(user.created_at) }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { userApi } from '../api/users'
import type { User, UserCreate } from '../types/user'

const users = ref<User[]>([])
const loading = ref(false)
const error = ref<string | null>(null)
const showCreateForm = ref(false)
const newUser = ref<UserCreate>({
  email: '',
  username: '',
  password: '',
  is_active: true,
})

const fetchUsers = async () => {
  loading.value = true
  error.value = null
  try {
    users.value = await userApi.getUsers()
  } catch (err) {
    error.value = 'Ошибка при загрузке пользователей'
    console.error(err)
  } finally {
    loading.value = false
  }
}

const createUser = async () => {
  loading.value = true
  error.value = null
  try {
    await userApi.createUser(newUser.value)
    newUser.value = { email: '', username: '', password: '', is_active: true }
    showCreateForm.value = false
    await fetchUsers()
  } catch (err: any) {
    error.value = err.response?.data?.detail || 'Ошибка при создании пользователя'
    console.error(err)
  } finally {
    loading.value = false
  }
}

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleString('ru-RU')
}

onMounted(() => {
  fetchUsers()
})
</script>


