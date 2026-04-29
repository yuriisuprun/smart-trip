'use client'

import React, { useState, useEffect } from 'react'
import { adminAPI } from '@/lib/api'
import { SignedIn, SignedOut, SignInButton } from '@/lib/auth-wrapper'

export default function AdminTestPage() {
  const [loading, setLoading] = useState<string | null>(null)
  const [results, setResults] = useState<any>(null)
  const [error, setError] = useState<string | null>(null)
  const [statistics, setStatistics] = useState<any>(null)

  const handleAction = async (action: string, apiCall: () => Promise<any>) => {
    setLoading(action)
    setError(null)
    setResults(null)
    
    try {
      const result = await apiCall()
      setResults(result)
      if (action === 'comprehensive') {
        loadStatistics() // Refresh stats after seeding
      }
    } catch (err: any) {
      setError(err.message || 'An error occurred')
    } finally {
      setLoading(null)
    }
  }

  const loadStatistics = async () => {
    try {
      const stats = await adminAPI.getContentStatistics()
      setStatistics(stats.statistics)
    } catch (err: any) {
      setError(err.message || 'Failed to load statistics')
    }
  }

  useEffect(() => {
    loadStatistics()
  }, [])

  return (
    <div style={{ minHeight: '100vh', backgroundColor: '#f8fafc', padding: '2rem' }}>
      <div style={{ maxWidth: '800px', margin: '0 auto' }}>
        <h1 style={{ fontSize: '2rem', fontWeight: 'bold', marginBottom: '2rem', color: '#1e293b' }}>
          Italian Grammar Admin Test Page
        </h1>

        <SignedOut>
          <div style={{
            backgroundColor: 'white',
            padding: '2rem',
            borderRadius: '8px',
            textAlign: 'center',
            boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)'
          }}>
            <h2 style={{ marginBottom: '1rem' }}>Please Sign In</h2>
            <SignInButton mode="modal">
              <button style={{
                backgroundColor: '#4f46e5',
                color: 'white',
                padding: '0.75rem 1.5rem',
                borderRadius: '6px',
                border: 'none',
                cursor: 'pointer',
                fontSize: '1rem'
              }}>
                Sign In to Access Admin Features
              </button>
            </SignInButton>
          </div>
        </SignedOut>

        <SignedIn>
          {/* Statistics Section */}
          {statistics && (
            <div style={{ 
              backgroundColor: 'white', 
              padding: '1.5rem', 
              borderRadius: '8px', 
              marginBottom: '2rem',
              boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)'
            }}>
              <h2 style={{ fontSize: '1.25rem', fontWeight: '600', marginBottom: '1rem', color: '#1e293b' }}>
                📊 Content Statistics
              </h2>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem' }}>
                <div style={{ padding: '1rem', backgroundColor: '#f0fdf4', borderRadius: '6px' }}>
                  <p style={{ fontSize: '0.875rem', color: '#166534', margin: 0 }}>Grammar Rules</p>
                  <p style={{ fontSize: '2rem', fontWeight: 'bold', color: '#059669', margin: 0 }}>
                    {statistics.total_grammar_rules || 0}
                  </p>
                </div>
                <div style={{ padding: '1rem', backgroundColor: '#eff6ff', borderRadius: '6px' }}>
                  <p style={{ fontSize: '0.875rem', color: '#1e40af', margin: 0 }}>Exercises</p>
                  <p style={{ fontSize: '2rem', fontWeight: 'bold', color: '#0ea5e9', margin: 0 }}>
                    {statistics.total_exercises || 0}
                  </p>
                </div>
                <div style={{ padding: '1rem', backgroundColor: '#faf5ff', borderRadius: '6px' }}>
                  <p style={{ fontSize: '0.875rem', color: '#7c2d12', margin: 0 }}>Version</p>
                  <p style={{ fontSize: '1.25rem', fontWeight: 'bold', color: '#7c3aed', margin: 0 }}>
                    {statistics.content_version || 'N/A'}
                  </p>
                </div>
              </div>

              {/* CEFR Distribution */}
              {statistics.cefr_level_distribution && (
                <div style={{ marginTop: '1rem' }}>
                  <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.5rem' }}>CEFR Level Distribution</h3>
                  <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
                    {Object.entries(statistics.cefr_level_distribution).map(([level, counts]: [string, any]) => (
                      (counts.grammar_rules > 0 || counts.exercises > 0) && (
                        <div key={level} style={{ 
                          padding: '0.5rem 1rem', 
                          backgroundColor: '#f1f5f9', 
                          borderRadius: '6px',
                          textAlign: 'center'
                        }}>
                          <div style={{ fontWeight: '600', color: '#1e293b' }}>{level}</div>
                          <div style={{ fontSize: '0.75rem', color: '#6b7280' }}>
                            {counts.grammar_rules}G + {counts.exercises}E
                          </div>
                        </div>
                      )
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}

          {/* Action Buttons */}
          <div style={{ 
            backgroundColor: 'white', 
            padding: '1.5rem', 
            borderRadius: '8px', 
            marginBottom: '2rem',
            boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)'
          }}>
            <h2 style={{ fontSize: '1.25rem', fontWeight: '600', marginBottom: '1rem', color: '#1e293b' }}>
              🚀 Content Management
            </h2>
            
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '1rem' }}>
              <button
                onClick={() => handleAction('comprehensive', adminAPI.seedComprehensiveContent)}
                disabled={loading !== null}
                style={{
                  padding: '1rem',
                  backgroundColor: loading === 'comprehensive' ? '#9ca3af' : '#059669',
                  color: 'white',
                  border: 'none',
                  borderRadius: '8px',
                  cursor: loading !== null ? 'not-allowed' : 'pointer',
                  fontSize: '0.875rem',
                  fontWeight: '500'
                }}
              >
                {loading === 'comprehensive' ? '⏳ Seeding...' : '📚 Seed Comprehensive Content (500+ Rules)'}
              </button>

              <button
                onClick={() => handleAction('b1', () => adminAPI.seedByCefrLevel('B1'))}
                disabled={loading !== null}
                style={{
                  padding: '1rem',
                  backgroundColor: loading === 'b1' ? '#9ca3af' : '#0ea5e9',
                  color: 'white',
                  border: 'none',
                  borderRadius: '8px',
                  cursor: loading !== null ? 'not-allowed' : 'pointer',
                  fontSize: '0.875rem',
                  fontWeight: '500'
                }}
              >
                {loading === 'b1' ? '⏳ Seeding...' : '🎓 Seed B1 Level Content'}
              </button>

              <button
                onClick={() => handleAction('b2', () => adminAPI.seedByCefrLevel('B2'))}
                disabled={loading !== null}
                style={{
                  padding: '1rem',
                  backgroundColor: loading === 'b2' ? '#9ca3af' : '#7c3aed',
                  color: 'white',
                  border: 'none',
                  borderRadius: '8px',
                  cursor: loading !== null ? 'not-allowed' : 'pointer',
                  fontSize: '0.875rem',
                  fontWeight: '500'
                }}
              >
                {loading === 'b2' ? '⏳ Seeding...' : '🎓 Seed B2 Level Content'}
              </button>

              <button
                onClick={loadStatistics}
                disabled={loading !== null}
                style={{
                  padding: '1rem',
                  backgroundColor: '#6b7280',
                  color: 'white',
                  border: 'none',
                  borderRadius: '8px',
                  cursor: 'pointer',
                  fontSize: '0.875rem',
                  fontWeight: '500'
                }}
              >
                🔄 Refresh Statistics
              </button>
            </div>
          </div>

          {/* Results Display */}
          {error && (
            <div style={{
              padding: '1rem',
              backgroundColor: '#fef2f2',
              border: '1px solid #fecaca',
              borderRadius: '8px',
              marginBottom: '1rem'
            }}>
              <div style={{ color: '#dc2626', fontWeight: '500' }}>❌ Error</div>
              <p style={{ margin: '0.5rem 0 0 0', fontSize: '0.875rem', color: '#7f1d1d' }}>{error}</p>
            </div>
          )}

          {results && (
            <div style={{
              padding: '1rem',
              backgroundColor: '#f0fdf4',
              border: '1px solid #bbf7d0',
              borderRadius: '8px',
              marginBottom: '1rem'
            }}>
              <div style={{ color: '#059669', fontWeight: '500', marginBottom: '0.5rem' }}>✅ Success</div>
              <p style={{ margin: 0, fontSize: '0.875rem', color: '#14532d' }}>{results.message}</p>
              {results.results && (
                <div style={{ marginTop: '0.5rem', fontSize: '0.75rem', color: '#166534' }}>
                  <p style={{ margin: 0 }}>Grammar Content: {results.results.grammar_content || 0}</p>
                  <p style={{ margin: 0 }}>Exercises: {results.results.exercises || 0}</p>
                  <p style={{ margin: 0 }}>Total Documents: {results.results.total_documents || 0}</p>
                  {results.results.errors && results.results.errors.length > 0 && (
                    <p style={{ margin: 0, color: '#dc2626' }}>Errors: {results.results.errors.length}</p>
                  )}
                </div>
              )}
            </div>
          )}

          {/* Instructions */}
          <div style={{
            padding: '1rem',
            backgroundColor: '#fffbeb',
            border: '1px solid #fed7aa',
            borderRadius: '8px',
            fontSize: '0.875rem',
            color: '#92400e'
          }}>
            <h3 style={{ margin: '0 0 0.5rem 0', fontWeight: '600' }}>📋 Instructions:</h3>
            <ol style={{ margin: 0, paddingLeft: '1.25rem' }}>
              <li>Click "Seed Comprehensive Content" to load all 500+ grammar rules</li>
              <li>Wait for the success message and check updated statistics</li>
              <li>Go back to the main chat interface and ask grammar questions</li>
              <li>Try questions like: "How do I use the subjunctive mood in Italian?"</li>
              <li>You should get detailed, comprehensive responses with examples</li>
            </ol>
          </div>

          {/* Navigation */}
          <div style={{ marginTop: '2rem', textAlign: 'center' }}>
            <a 
              href="/"
              style={{
                display: 'inline-block',
                padding: '0.75rem 1.5rem',
                backgroundColor: '#4f46e5',
                color: 'white',
                textDecoration: 'none',
                borderRadius: '6px',
                fontWeight: '500'
              }}
            >
              ← Back to Main Chat Interface
            </a>
          </div>
        </SignedIn>
      </div>
    </div>
  )
}