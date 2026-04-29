import axios from 'axios'

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

export interface ChatRequest {
  session_id: string
  user_id: string
  message: string
  topic?: string
  difficulty?: string
  language?: string
}

export interface EvaluateRequest {
  user_id: string
  question: string
  user_answer: string
  correct_answer?: string
  question_type?: string
  topic?: string
  language?: string
}

export const chatAPI = {
  async sendMessage(request: ChatRequest): Promise<ReadableStream<Uint8Array>> {
    const response = await fetch(`${API_URL}/api/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(request),
    })

    if (!response.ok) {
      throw new Error(`Chat error: ${response.statusText}`)
    }

    return response.body!
  },

  async getHistory(sessionId: string) {
    const response = await api.get(`/api/chat/history/${sessionId}`)
    return response.data
  },
}

export const evaluateAPI = {
  async evaluateAnswer(request: EvaluateRequest) {
    const response = await api.post('/api/evaluate', request)
    return response.data
  },
}

export const progressAPI = {
  async getUserProgress(userId: string) {
    const response = await api.get(`/api/progress/user/${userId}`)
    return response.data
  },

  async getTopicProgress(userId: string) {
    const response = await api.get(`/api/progress/topics?user_id=${userId}`)
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
}

export default api
