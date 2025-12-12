import axios from 'axios'
import type { User, UserCreate } from '../types/user'

const api = axios.create({
  baseURL: '/api/v1',
  headers: {
    'Content-Type': 'application/json',
  },
})

export const userApi = {
  async getUsers(): Promise<User[]> {
    const response = await api.get<User[]>('/users/')
    return response.data
  },

  async getUser(id: number): Promise<User> {
    const response = await api.get<User>(`/users/${id}`)
    return response.data
  },

  async createUser(user: UserCreate): Promise<User> {
    const response = await api.post<User>('/users/', user)
    return response.data
  },
}

