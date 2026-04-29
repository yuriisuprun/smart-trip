import axios from 'axios'

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

// Create axios instance for client-side use
const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Client-side API helper that includes auth token
export const createAuthenticatedApi = (getToken: () => Promise<string | null>) => {
  const authenticatedApi = axios.create({
    baseURL: API_URL,
    headers: {
      'Content-Type': 'application/json',
    },
  })

  authenticatedApi.interceptors.request.use(async (config) => {
    try {
      const token = await getToken()
      if (token) {
        config.headers.Authorization = `Bearer ${token}`
      }
    } catch (error) {
      console.error('Error getting auth token:', error)
    }
    return config
  })

  return authenticatedApi
}

export interface ChatRequest {
  session_id: string
  message: string
  topic?: string
  difficulty?: string
  language?: string
}

export interface EvaluateRequest {
  question: string
  user_answer: string
  correct_answer?: string
  question_type?: string
  topic?: string
  language?: string
}

export const chatAPI = {
  async sendMessage(request: ChatRequest, getToken: () => Promise<string | null>): Promise<ReadableStream<Uint8Array>> {
    const token = await getToken()
    const response = await fetch(`${API_URL}/api/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        ...(token && { Authorization: `Bearer ${token}` }),
      },
      body: JSON.stringify(request),
    })

    if (!response.ok) {
      throw new Error(`Chat error: ${response.statusText}`)
    }

    return response.body!
  },

  async getHistory(sessionId: string, getToken: () => Promise<string | null>) {
    const authenticatedApi = createAuthenticatedApi(getToken)
    const response = await authenticatedApi.get(`/api/chat/history/${sessionId}`)
    return response.data
  },
}

export const evaluateAPI = {
  async evaluateAnswer(request: EvaluateRequest, getToken: () => Promise<string | null>) {
    const authenticatedApi = createAuthenticatedApi(getToken)
    const response = await authenticatedApi.post('/api/evaluate', request)
    return response.data
  },
}

export const progressAPI = {
  async getUserProgress(getToken: () => Promise<string | null>) {
    const authenticatedApi = createAuthenticatedApi(getToken)
    const response = await authenticatedApi.get('/api/progress/user')
    return response.data
  },

  async getTopicProgress(getToken: () => Promise<string | null>) {
    const authenticatedApi = createAuthenticatedApi(getToken)
    const response = await authenticatedApi.get('/api/progress/topics')
    return response.data
  },
}

export const adminAPI = {
  async seedContent() {
    const response = await api.post('/api/admin/seed-content')
    return response.data
  },

  async seedExams() {
    const response = await api.post('/api/admin/seed-exams')
    return response.data
  },

  async seedAll() {
    const response = await api.post('/api/admin/seed-all')
    return response.data
  },

  // New comprehensive content seeding endpoints
  async seedComprehensiveContent() {
    const response = await api.post('/api/admin/seed-comprehensive-content')
    return response.data
  },

  async seedByCefrLevel(level: string) {
    const response = await api.post(`/api/admin/seed-by-cefr-level/${level}`)
    return response.data
  },

  async seedByTopic(topic: string) {
    const response = await api.post(`/api/admin/seed-by-topic/${topic}`)
    return response.data
  },

  async updateContentVersion(version: string) {
    const response = await api.post(`/api/admin/update-content-version/${version}`)
    return response.data
  },

  async getContentStatistics() {
    const response = await api.get('/api/admin/content-statistics')
    return response.data
  },
}

export { api }
export default api
