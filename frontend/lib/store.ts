import { create } from 'zustand'
import { persist } from 'zustand/middleware'
import { Language } from './i18n'

export interface Message {
  id: string
  role: 'user' | 'assistant'
  content: string
  timestamp: Date
}

export interface ChatSession {
  id: string
  topic: string
  difficulty: string
  messages: Message[]
  language: Language
}

export interface UserProgress {
  userId: string
  cefrLevel: string
  totalScore: number
  totalQuestions: number
  weakAreas: Record<string, number>
  skillProgress: Array<{
    skill: string
    level: string
    score: number
    accuracy: number
  }>
}

interface ChatStore {
  currentSession: ChatSession | null
  userProgress: UserProgress | null
  isLoading: boolean
  error: string | null
  language: Language

  setCurrentSession: (session: ChatSession) => void
  addMessage: (message: Message) => void
  setUserProgress: (progress: UserProgress) => void
  setLoading: (loading: boolean) => void
  setError: (error: string | null) => void
  clearError: () => void
  setLanguage: (language: Language) => void
}

export const useChatStore = create<ChatStore>()(
  persist(
    (set) => ({
      currentSession: null,
      userProgress: null,
      isLoading: false,
      error: null,
      language: 'en',

      setCurrentSession: (session) => set({ currentSession: session }),
      addMessage: (message) =>
        set((state) => ({
          currentSession: state.currentSession
            ? {
                ...state.currentSession,
                messages: [...state.currentSession.messages, message],
              }
            : null,
        })),
      setUserProgress: (progress) => set({ userProgress: progress }),
      setLoading: (loading) => set({ isLoading: loading }),
      setError: (error) => set({ error }),
      clearError: () => set({ error: null }),
      setLanguage: (language) => set({ language }),
    }),
    {
      name: 'italian-tutor-store',
      partialize: (state) => ({ language: state.language }),
    }
  )
)
