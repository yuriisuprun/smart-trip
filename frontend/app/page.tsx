'use client'

import React, { useState, useEffect } from 'react'
import { useChatStore, ChatSession } from '@/lib/store'
import { getTranslations, formatDifficultyLevel } from '@/lib/i18n'
import ChatInterface from '@/components/ChatInterface'
import ProgressDashboard from '@/components/ProgressDashboard'
import QuizInterface from '@/components/QuizInterface'
import LanguageSelector from '@/components/LanguageSelector'
import { BookOpen, BarChart3, HelpCircle, Plus, User } from 'lucide-react'
import { v4 as uuidv4 } from 'uuid'

// Conditional imports based on Clerk configuration
const isClerkConfigured = !!process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY

let SignedIn, SignedOut, SignInButton, UserButton, useUser
if (isClerkConfigured) {
  const clerk = require('@clerk/nextjs')
  SignedIn = clerk.SignedIn
  SignedOut = clerk.SignedOut
  SignInButton = clerk.SignInButton
  UserButton = clerk.UserButton
  useUser = clerk.useUser
} else {
  const mock = require('@/lib/auth-mock')
  SignedIn = mock.MockSignedIn
  SignedOut = mock.MockSignedOut
  SignInButton = mock.MockSignInButton
  UserButton = mock.MockUserButton
  useUser = mock.mockUseUser
}

type TabType = 'chat' | 'quiz' | 'progress'

export default function Home() {
  const [activeTab, setActiveTab] = useState<TabType>('chat')
  const [mounted, setMounted] = useState(false)
  const { currentSession, setCurrentSession, language } = useChatStore()
  const { user } = useUser()
  const t = getTranslations(language)

  useEffect(() => {
    setMounted(true)
    // Create initial session
    if (!currentSession && user) {
      const newSession: ChatSession = {
        id: `session_${uuidv4()}`,
        topic: 'grammar',
        difficulty: 'A2',
        messages: [],
        language,
      }
      setCurrentSession(newSession)
    }
  }, [currentSession, setCurrentSession, language, user])

  const createNewSession = (topic: string, difficulty: string) => {
    const newSession: ChatSession = {
      id: `session_${uuidv4()}`,
      topic,
      difficulty,
      messages: [],
      language,
    }
    setCurrentSession(newSession)
    setActiveTab('chat')
  }

  if (!mounted) {
    return null
  }

  const topicItems = [
    { topic: 'grammar', label: t.grammar, color: '#dbeafe' },
    { topic: 'vocabulary', label: t.vocabulary, color: '#dcfce7' },
    { topic: 'reading', label: t.reading, color: '#fae8ff' },
    { topic: 'listening', label: t.listening, color: '#fed7aa' },
  ]

  return (
    <div style={{ minHeight: '100vh', backgroundColor: '#f8fafc' }}>
      {/* Header */}
      <header style={{ 
        backgroundColor: 'white', 
        borderBottom: '1px solid #e2e8f0',
        padding: '1rem 0'
      }}>
        <div style={{ 
          maxWidth: '1200px', 
          margin: '0 auto', 
          padding: '0 1.5rem',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between'
        }}>
          <div style={{
            display: 'flex',
            alignItems: 'center',
            gap: '0.75rem'
          }}>
            <div style={{
              width: '40px',
              height: '40px',
              backgroundColor: '#4f46e5',
              borderRadius: '8px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              color: 'white',
              fontWeight: 'bold',
              fontSize: '14px'
            }}>
              IT
            </div>
            <div>
              <h1 style={{ 
                fontSize: '1.5rem', 
                fontWeight: 'bold', 
                color: '#1e293b',
                margin: 0
              }}>
                {t.appTitle}
              </h1>
              <p style={{ 
                fontSize: '0.875rem', 
                color: '#64748b',
                margin: 0
              }}>
                {t.appSubtitle}
              </p>
            </div>
          </div>
          
          <div style={{
            display: 'flex',
            alignItems: 'center',
            gap: '1rem'
          }}>
            <LanguageSelector />
            
            <SignedIn>
              <a
                href="/profile"
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '0.5rem',
                  padding: '0.5rem 1rem',
                  backgroundColor: '#f1f5f9',
                  borderRadius: '6px',
                  textDecoration: 'none',
                  color: '#64748b',
                  fontSize: '0.875rem',
                  fontWeight: '500',
                  transition: 'all 0.2s'
                }}
                onMouseOver={(e) => {
                  e.currentTarget.style.backgroundColor = '#e2e8f0'
                }}
                onMouseOut={(e) => {
                  e.currentTarget.style.backgroundColor = '#f1f5f9'
                }}
              >
                <User size={16} />
                Profile
              </a>
              <UserButton />
            </SignedIn>
            
            <SignedOut>
              <SignInButton mode="modal">
                <button style={{
                  backgroundColor: '#4f46e5',
                  color: 'white',
                  padding: '0.5rem 1rem',
                  borderRadius: '6px',
                  border: 'none',
                  cursor: 'pointer',
                  fontSize: '0.875rem',
                  fontWeight: '500'
                }}>
                  Sign In
                </button>
              </SignInButton>
            </SignedOut>
          </div>
        </div>
      </header>

      <SignedOut>
        <div style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          minHeight: 'calc(100vh - 80px)',
          textAlign: 'center',
          padding: '2rem'
        }}>
          <div style={{
            maxWidth: '500px',
            backgroundColor: 'white',
            padding: '3rem',
            borderRadius: '12px',
            boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
            border: '1px solid #e2e8f0'
          }}>
            <div style={{ fontSize: '4rem', marginBottom: '1rem' }}>🇮🇹</div>
            <h2 style={{
              fontSize: '2rem',
              fontWeight: 'bold',
              color: '#1e293b',
              marginBottom: '1rem'
            }}>
              Welcome to Italian AI Tutor
            </h2>
            <p style={{
              fontSize: '1.125rem',
              color: '#64748b',
              marginBottom: '2rem',
              lineHeight: '1.6'
            }}>
              Your personalized AI-powered Italian language learning companion. 
              Get instant feedback, practice conversations, and track your progress 
              as you prepare for Italian language exams.
            </p>
            <SignInButton mode="modal">
              <button style={{
                backgroundColor: '#4f46e5',
                color: 'white',
                padding: '0.75rem 2rem',
                borderRadius: '8px',
                border: 'none',
                cursor: 'pointer',
                fontSize: '1rem',
                fontWeight: '600',
                transition: 'all 0.2s'
              }}
              onMouseOver={(e) => {
                e.currentTarget.style.backgroundColor = '#4338ca'
              }}
              onMouseOut={(e) => {
                e.currentTarget.style.backgroundColor = '#4f46e5'
              }}>
                Get Started - Sign In
              </button>
            </SignInButton>
            <p style={{
              fontSize: '0.875rem',
              color: '#9ca3af',
              marginTop: '1rem'
            }}>
              Free to use • No credit card required
            </p>
          </div>
        </div>
      </SignedOut>

      <SignedIn>
        <div style={{ 
          maxWidth: '1200px', 
          margin: '0 auto', 
          padding: '1.5rem'
        }}>
          {/* Tabs */}
          <div style={{
            display: 'flex',
            gap: '4px',
            marginBottom: '1.5rem',
            backgroundColor: '#f1f5f9',
            padding: '4px',
            borderRadius: '8px',
            width: 'fit-content'
          }}>
            <button
              onClick={() => setActiveTab('chat')}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '0.5rem',
                padding: '0.5rem 1rem',
                borderRadius: '6px',
                fontWeight: '500',
                border: 'none',
                cursor: 'pointer',
                transition: 'all 0.2s',
                backgroundColor: activeTab === 'chat' ? 'white' : 'transparent',
                color: activeTab === 'chat' ? '#4f46e5' : '#64748b',
                boxShadow: activeTab === 'chat' ? '0 1px 2px rgba(0, 0, 0, 0.05)' : 'none'
              }}
            >
              <BookOpen size={16} />
              {t.chatTutor}
            </button>
            <button
              onClick={() => setActiveTab('quiz')}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '0.5rem',
                padding: '0.5rem 1rem',
                borderRadius: '6px',
                fontWeight: '500',
                border: 'none',
                cursor: 'pointer',
                transition: 'all 0.2s',
                backgroundColor: activeTab === 'quiz' ? 'white' : 'transparent',
                color: activeTab === 'quiz' ? '#4f46e5' : '#64748b',
                boxShadow: activeTab === 'quiz' ? '0 1px 2px rgba(0, 0, 0, 0.05)' : 'none'
              }}
            >
              <HelpCircle size={16} />
              {t.quiz}
            </button>
            <button
              onClick={() => setActiveTab('progress')}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '0.5rem',
                padding: '0.5rem 1rem',
                borderRadius: '6px',
                fontWeight: '500',
                border: 'none',
                cursor: 'pointer',
                transition: 'all 0.2s',
                backgroundColor: activeTab === 'progress' ? 'white' : 'transparent',
                color: activeTab === 'progress' ? '#4f46e5' : '#64748b',
                boxShadow: activeTab === 'progress' ? '0 1px 2px rgba(0, 0, 0, 0.05)' : 'none'
              }}
            >
              <BarChart3 size={16} />
              {t.progress}
            </button>
          </div>

          {/* Quick Actions */}
          {activeTab === 'chat' && (
            <div style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))',
              gap: '0.75rem',
              marginBottom: '1.5rem'
            }}>
              {topicItems.map((item) => (
                <button
                  key={item.topic}
                  onClick={() => createNewSession(item.topic, 'A2')}
                  style={{
                    backgroundColor: item.color,
                    border: '1px solid #e2e8f0',
                    borderRadius: '8px',
                    padding: '1rem',
                    fontWeight: '500',
                    cursor: 'pointer',
                    transition: 'all 0.2s',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    gap: '0.5rem'
                  }}
                  onMouseOver={(e) => {
                    e.currentTarget.style.transform = 'translateY(-1px)'
                    e.currentTarget.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)'
                  }}
                  onMouseOut={(e) => {
                    e.currentTarget.style.transform = 'translateY(0)'
                    e.currentTarget.style.boxShadow = 'none'
                  }}
                >
                  <Plus size={16} />
                  {item.label}
                </button>
              ))}
            </div>
          )}

          {/* Content */}
          <div style={{
            backgroundColor: 'white',
            borderRadius: '8px',
            boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)',
            border: '1px solid #e2e8f0',
            minHeight: '600px'
          }}>
            {activeTab === 'chat' && <ChatInterface />}
            {activeTab === 'quiz' && <QuizInterface />}
            {activeTab === 'progress' && <ProgressDashboard />}
          </div>

          {/* Session Info */}
          {currentSession && activeTab === 'chat' && (
            <div style={{
              marginTop: '1rem',
              backgroundColor: '#eff6ff',
              borderRadius: '8px',
              border: '1px solid #bfdbfe',
              padding: '1rem'
            }}>
              <div style={{
                display: 'flex',
                alignItems: 'center',
                gap: '0.5rem'
              }}>
                <div style={{
                  width: '8px',
                  height: '8px',
                  backgroundColor: '#4f46e5',
                  borderRadius: '50%'
                }}></div>
                <p style={{
                  fontSize: '0.875rem',
                  color: '#1e40af',
                  margin: 0
                }}>
                  <span style={{ fontWeight: '500' }}>{t.currentSession}:</span> {
                    topicItems.find(item => item.topic === currentSession.topic)?.label || currentSession.topic.toUpperCase()
                  } • {t.level}: {formatDifficultyLevel(currentSession.difficulty, language)}
                </p>
              </div>
            </div>
          )}
        </div>
      </SignedIn>
    </div>
  )
}
