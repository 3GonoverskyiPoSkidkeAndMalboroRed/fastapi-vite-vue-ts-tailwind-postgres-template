export interface User {
  id: number
  email: string
  username: string
  is_active: boolean
  created_at: string
  updated_at?: string
}

export interface UserCreate {
  email: string
  username: string
  password: string
  is_active?: boolean
}

