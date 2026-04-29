'use client'

import React, { useState } from 'react'
import { useChatStore } from '@/lib/store'
import { Language, getTranslations } from '@/lib/i18n'
import { Globe, ChevronDown } from 'lucide-react'

export default function LanguageSelector() {
  const { language, setLanguage } = useChatStore()
  const [isOpen, setIsOpen] = useState(false)
  const t = getTranslations(language)

  const handleLanguageChange = (newLanguage: Language) => {
    setLanguage(newLanguage)
    setIsOpen(false)
  }

  return (
    <div style={{ position: 'relative', display: 'inline-block' }}>
      <button
        onClick={() => setIsOpen(!isOpen)}
        style={{
          display: 'flex',
          alignItems: 'center',
          gap: '0.5rem',
          padding: '0.5rem 0.75rem',
          backgroundColor: '#f8fafc',
          border: '1px solid #e2e8f0',
          borderRadius: '6px',
          cursor: 'pointer',
          fontSize: '0.875rem',
          fontWeight: '500',
          color: '#475569',
          transition: 'all 0.2s'
        }}
        onMouseOver={(e) => {
          e.currentTarget.style.backgroundColor = '#f1f5f9'
          e.currentTarget.style.borderColor = '#cbd5e1'
        }}
        onMouseOut={(e) => {
          e.currentTarget.style.backgroundColor = '#f8fafc'
          e.currentTarget.style.borderColor = '#e2e8f0'
        }}
      >
        <Globe size={16} />
        <span>{language === 'en' ? '🇺🇸 EN' : '🇮🇹 IT'}</span>
        <ChevronDown size={14} style={{ 
          transform: isOpen ? 'rotate(180deg)' : 'rotate(0deg)',
          transition: 'transform 0.2s'
        }} />
      </button>
      
      {isOpen && (
        <>
          {/* Backdrop */}
          <div 
            style={{
              position: 'fixed',
              top: 0,
              left: 0,
              right: 0,
              bottom: 0,
              zIndex: 40
            }}
            onClick={() => setIsOpen(false)}
          />
          
          {/* Dropdown */}
          <div style={{
            position: 'absolute',
            top: '100%',
            right: 0,
            marginTop: '0.25rem',
            backgroundColor: 'white',
            border: '1px solid #e2e8f0',
            borderRadius: '6px',
            boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
            zIndex: 50,
            minWidth: '120px'
          }}>
            <button
              onClick={() => handleLanguageChange('en')}
              style={{
                width: '100%',
                padding: '0.5rem 0.75rem',
                textAlign: 'left',
                border: 'none',
                backgroundColor: language === 'en' ? '#f1f5f9' : 'transparent',
                color: language === 'en' ? '#4f46e5' : '#475569',
                cursor: 'pointer',
                fontSize: '0.875rem',
                borderRadius: '6px 6px 0 0',
                transition: 'background-color 0.2s',
                display: 'flex',
                alignItems: 'center',
                gap: '0.5rem'
              }}
              onMouseOver={(e) => {
                if (language !== 'en') {
                  e.currentTarget.style.backgroundColor = '#f8fafc'
                }
              }}
              onMouseOut={(e) => {
                if (language !== 'en') {
                  e.currentTarget.style.backgroundColor = 'transparent'
                }
              }}
            >
              🇺🇸 {t.english}
            </button>
            <button
              onClick={() => handleLanguageChange('it')}
              style={{
                width: '100%',
                padding: '0.5rem 0.75rem',
                textAlign: 'left',
                border: 'none',
                backgroundColor: language === 'it' ? '#f1f5f9' : 'transparent',
                color: language === 'it' ? '#4f46e5' : '#475569',
                cursor: 'pointer',
                fontSize: '0.875rem',
                borderRadius: '0 0 6px 6px',
                transition: 'background-color 0.2s',
                display: 'flex',
                alignItems: 'center',
                gap: '0.5rem'
              }}
              onMouseOver={(e) => {
                if (language !== 'it') {
                  e.currentTarget.style.backgroundColor = '#f8fafc'
                }
              }}
              onMouseOut={(e) => {
                if (language !== 'it') {
                  e.currentTarget.style.backgroundColor = 'transparent'
                }
              }}
            >
              🇮🇹 {t.italian}
            </button>
          </div>
        </>
      )}
    </div>
  )
}