'use client'

import React, { useState } from 'react'
import { adminAPI } from '@/lib/api'

export default function SimpleAdminTest() {
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState<string>('')

  const testContentSeeding = async () => {
    setLoading(true)
    setResult('')
    
    try {
      const response = await adminAPI.seedComprehensiveContent()
      setResult(`Success: ${response.message}`)
    } catch (error: any) {
      setResult(`Error: ${error.message}`)
    } finally {
      setLoading(false)
    }
  }

  const testStatistics = async () => {
    setLoading(true)
    setResult('')
    
    try {
      const response = await adminAPI.getContentStatistics()
      setResult(`Statistics: ${JSON.stringify(response.statistics, null, 2)}`)
    } catch (error: any) {
      setResult(`Error: ${error.message}`)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div style={{
      position: 'fixed',
      top: '10px',
      right: '10px',
      backgroundColor: 'white',
      border: '2px solid #4f46e5',
      borderRadius: '8px',
      padding: '1rem',
      boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
      zIndex: 1000,
      maxWidth: '300px'
    }}>
      <h4 style={{ margin: '0 0 1rem 0', color: '#1e293b' }}>Admin Test Panel</h4>
      
      <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem', marginBottom: '1rem' }}>
        <button
          onClick={testContentSeeding}
          disabled={loading}
          style={{
            padding: '0.5rem',
            backgroundColor: loading ? '#9ca3af' : '#059669',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: loading ? 'not-allowed' : 'pointer',
            fontSize: '0.875rem'
          }}
        >
          {loading ? 'Loading...' : 'Seed Content'}
        </button>
        
        <button
          onClick={testStatistics}
          disabled={loading}
          style={{
            padding: '0.5rem',
            backgroundColor: loading ? '#9ca3af' : '#0ea5e9',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: loading ? 'not-allowed' : 'pointer',
            fontSize: '0.875rem'
          }}
        >
          {loading ? 'Loading...' : 'Get Statistics'}
        </button>
      </div>
      
      {result && (
        <div style={{
          padding: '0.5rem',
          backgroundColor: '#f8fafc',
          border: '1px solid #e2e8f0',
          borderRadius: '4px',
          fontSize: '0.75rem',
          maxHeight: '200px',
          overflowY: 'auto',
          whiteSpace: 'pre-wrap'
        }}>
          {result}
        </div>
      )}
    </div>
  )
}