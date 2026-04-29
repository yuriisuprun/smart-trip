import 'server-only'
import axios from 'axios'
import { auth } from '@clerk/nextjs/server'

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

// Create axios instance for server-side use
const serverApi = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Add auth interceptor for server-side requests
serverApi.interceptors.request.use(async (config) => {
  try {
    const { getToken } = auth()
    const token = await getToken()
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
  } catch (error) {
    console.error('Error getting auth token:', error)
  }
  return config
})

export { serverApi }
export default serverApi