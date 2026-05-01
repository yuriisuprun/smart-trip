'use client'

import React, { useState, useRef, useEffect } from 'react'
import { useAuth } from '@/lib/auth-wrapper'
import { useChatStore, Message } from '@/lib/store'
import { getTranslations } from '@/lib/i18n'
import { chatAPI } from '@/lib/api'
import { Send, Loader, Settings } from 'lucide-react'
import AdminPanel from './AdminPanel'

export default function ChatInterface() {
  const [input, setInput] = useState('')
  const [isStreaming, setIsStreaming] = useState(false)
  const [mounted, setMounted] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)
  const { currentSession, addMessage, language } = useChatStore()
  const { getToken } = useAuth()
  const t = getTranslations(language)

  const [showAdminPanel, setShowAdminPanel] = useState(false)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    setMounted(true)
  }, [])

  useEffect(() => {
    if (mounted) {
      scrollToBottom()
    }
  }, [currentSession?.messages, mounted])

  const handleSendMessage = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!input.trim() || !currentSession || isStreaming) return

    // Add user message
    const userMessage: Message = {
      id: `msg_${Date.now()}`,
      role: 'user',
      content: input,
      timestamp: new Date(),
    }
    addMessage(userMessage)
    setInput('')
    setIsStreaming(true)

    try {
      // Stream response
      const stream = await chatAPI.sendMessage({
        session_id: currentSession.id,
        message: input,
        topic: currentSession.topic,
        difficulty: currentSession.difficulty,
        language: language,
      }, getToken)

      const reader = stream.getReader()
      const decoder = new TextDecoder()
      let assistantContent = ''
      let assistantMessage: Message | null = null

      while (true) {
        const { done, value } = await reader.read()
        if (done) break

        const chunk = decoder.decode(value)
        assistantContent += chunk

        if (!assistantMessage) {
          assistantMessage = {
            id: `msg_${Date.now()}_assistant`,
            role: 'assistant',
            content: assistantContent,
            timestamp: new Date(),
          }
          addMessage(assistantMessage)
        } else {
          // Update the last message
          if (currentSession.messages.length > 0) {
            const lastMsg = currentSession.messages[currentSession.messages.length - 1]
            if (lastMsg.role === 'assistant') {
              lastMsg.content = assistantContent
            }
          }
        }
      }
    } catch (error) {
      console.error('Error sending message:', error)
    } finally {
      setIsStreaming(false)
    }
  }

  if (!mounted) {
    return (
      <div style={{ 
        display: 'flex', 
        alignItems: 'center', 
        justifyContent: 'center', 
        height: '100%' 
      }}>
        <p style={{ color: '#6b7280' }}>{t.loading}</p>
      </div>
    )
  }

  if (!currentSession) {
    return (
      <div style={{ 
        display: 'flex', 
        alignItems: 'center', 
        justifyContent: 'center', 
        height: '100%' 
      }}>
        <p style={{ color: '#6b7280' }}>
          {language === 'it' 
            ? 'Seleziona o crea una sessione di chat per iniziare'
            : 'Select or create a chat session to begin'
          }
        </p>
      </div>
    )
  }

  return (
    <div style={{ 
      display: 'flex', 
      flexDirection: 'column', 
      height: '100%' 
    }}>
      {/* Header with Admin Button */}
      <div style={{
        padding: '1rem',
        borderBottom: '1px solid #e2e8f0',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        backgroundColor: '#f8fafc'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
          <div style={{
            width: '32px',
            height: '32px',
            backgroundColor: '#4f46e5',
            borderRadius: '6px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: 'white',
            fontWeight: 'bold',
            fontSize: '12px'
          }}>
            IT
          </div>
          <div>
            <h3 style={{ margin: 0, color: '#1e293b', fontSize: '1.125rem', fontWeight: '600' }}>
              Italian Grammar Tutor
            </h3>
            <p style={{ margin: 0, color: '#64748b', fontSize: '0.75rem' }}>
              Advanced B1-B2 Grammar Assistant
            </p>
          </div>
        </div>
        
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
          <div style={{
            padding: '0.25rem 0.5rem',
            backgroundColor: '#dbeafe',
            borderRadius: '4px',
            fontSize: '0.75rem',
            color: '#1e40af',
            fontWeight: '500'
          }}>
            500+ Grammar Rules
          </div>
          
          <button
            onClick={() => setShowAdminPanel(true)}
            style={{
              padding: '0.5rem 0.75rem',
              backgroundColor: '#4f46e5',
              color: 'white',
              border: 'none',
              borderRadius: '6px',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '0.5rem',
              fontSize: '0.875rem',
              fontWeight: '500',
              transition: 'all 0.2s',
              boxShadow: '0 1px 2px rgba(0, 0, 0, 0.1)'
            }}
            onMouseOver={(e) => {
              e.currentTarget.style.backgroundColor = '#4338ca'
              e.currentTarget.style.transform = 'translateY(-1px)'
              e.currentTarget.style.boxShadow = '0 2px 4px rgba(0, 0, 0, 0.15)'
            }}
            onMouseOut={(e) => {
              e.currentTarget.style.backgroundColor = '#4f46e5'
              e.currentTarget.style.transform = 'translateY(0)'
              e.currentTarget.style.boxShadow = '0 1px 2px rgba(0, 0, 0, 0.1)'
            }}
          >
            <Settings size={16} />
            Content Admin
          </button>
        </div>
      </div>

      {/* Messages */}
      <div style={{ 
        flex: 1, 
        overflowY: 'auto', 
        padding: '1.5rem',
        display: 'flex',
        flexDirection: 'column',
        gap: '1rem'
      }}>
        {currentSession.messages.length === 0 && (
          <div style={{
            textAlign: 'center',
            padding: '2rem',
            backgroundColor: '#f8fafc',
            borderRadius: '8px',
            border: '1px solid #e2e8f0'
          }}>
            <div style={{ fontSize: '2rem', marginBottom: '1rem' }}>🇮🇹</div>
            <h3 style={{ 
              margin: '0 0 1rem 0', 
              color: '#1e293b', 
              fontSize: '1.25rem', 
              fontWeight: '600' 
            }}>
              Welcome to Advanced Italian Grammar
            </h3>
            <p style={{ 
              margin: '0 0 1.5rem 0', 
              color: '#64748b', 
              fontSize: '0.875rem',
              lineHeight: '1.5'
            }}>
              Ask me about B1-B2 level Italian grammar topics. I can help with:
            </p>
            <div style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
              gap: '0.75rem',
              marginBottom: '1.5rem'
            }}>
              {[
                '🎯 Subjunctive Mood (Congiuntivo)',
                '💬 Conditional Tense (Condizionale)', 
                '📢 Imperative Commands (Imperativo)',
                '🔗 Complex Prepositions',
                '🎪 CI/NE Pronouns',
                '🔄 Relative Pronouns'
              ].map((topic, index) => (
                <div key={index} style={{
                  padding: '0.5rem',
                  backgroundColor: 'white',
                  borderRadius: '6px',
                  border: '1px solid #e2e8f0',
                  fontSize: '0.75rem',
                  color: '#374151'
                }}>
                  {topic}
                </div>
              ))}
            </div>
            <div style={{
              padding: '1rem',
              backgroundColor: '#fffbeb',
              borderRadius: '6px',
              border: '1px solid #fed7aa',
              fontSize: '0.75rem',
              color: '#92400e'
            }}>
              💡 <strong>Try asking:</strong> "How do I use the subjunctive mood?" or "Explain conditional tense with examples"
            </div>
          </div>
        )}
        
        {currentSession.messages.map((message) => (
          <div
            key={message.id}
            style={{
              display: 'flex',
              justifyContent: message.role === 'user' ? 'flex-end' : 'flex-start'
            }}
          >
            <div
              style={{
                maxWidth: '70%',
                padding: '0.75rem 1rem',
                borderRadius: '12px',
                backgroundColor: message.role === 'user' ? '#4f46e5' : '#f1f5f9',
                color: message.role === 'user' ? 'white' : '#1e293b',
                borderBottomRightRadius: message.role === 'user' ? '4px' : '12px',
                borderBottomLeftRadius: message.role === 'user' ? '12px' : '4px'
              }}
            >
              <p style={{ 
                fontSize: '0.875rem', 
                lineHeight: '1.4',
                margin: 0,
                whiteSpace: 'pre-wrap'
              }}>
                {message.content}
              </p>
              <span style={{ 
                fontSize: '0.75rem', 
                opacity: 0.7, 
                marginTop: '0.25rem', 
                display: 'block' 
              }}>
                {message.timestamp.toLocaleTimeString()}
              </span>
            </div>
          </div>
        ))}
        {isStreaming && (
          <div style={{ display: 'flex', justifyContent: 'flex-start' }}>
            <div style={{
              backgroundColor: '#f1f5f9',
              color: '#1e293b',
              padding: '0.75rem 1rem',
              borderRadius: '12px',
              borderBottomLeftRadius: '4px'
            }}>
              <Loader style={{ width: '16px', height: '16px' }} className="animate-spin" />
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <form
        onSubmit={handleSendMessage}
        style={{
          borderTop: '1px solid #e2e8f0',
          padding: '1rem',
          display: 'flex',
          gap: '0.5rem'
        }}
      >
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder={t.typeMessage}
          disabled={isStreaming}
          style={{
            flex: 1,
            padding: '0.75rem 1rem',
            border: '1px solid #d1d5db',
            borderRadius: '8px',
            outline: 'none',
            fontSize: '0.875rem',
            backgroundColor: isStreaming ? '#f9fafb' : 'white'
          }}
          onFocus={(e) => {
            e.target.style.borderColor = '#4f46e5'
            e.target.style.boxShadow = '0 0 0 3px rgba(79, 70, 229, 0.1)'
          }}
          onBlur={(e) => {
            e.target.style.borderColor = '#d1d5db'
            e.target.style.boxShadow = 'none'
          }}
        />
        <button
          type="submit"
          disabled={isStreaming || !input.trim()}
          style={{
            backgroundColor: isStreaming || !input.trim() ? '#9ca3af' : '#4f46e5',
            color: 'white',
            padding: '0.75rem 1rem',
            borderRadius: '8px',
            border: 'none',
            cursor: isStreaming || !input.trim() ? 'not-allowed' : 'pointer',
            display: 'flex',
            alignItems: 'center',
            gap: '0.5rem',
            transition: 'background-color 0.2s'
          }}
          onMouseOver={(e) => {
            if (!isStreaming && input.trim()) {
              e.currentTarget.style.backgroundColor = '#4338ca'
            }
          }}
          onMouseOut={(e) => {
            if (!isStreaming && input.trim()) {
              e.currentTarget.style.backgroundColor = '#4f46e5'
            }
          }}
        >
          <Send size={16} />
        </button>
      </form>

      {/* Admin Panel Modal */}
      {showAdminPanel && (
        <AdminPanel onClose={() => setShowAdminPanel(false)} />
      )}
    </div>
  )
}
