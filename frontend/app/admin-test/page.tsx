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
        <div style={{ 
          display: 'flex', 
          alignItems: 'center', 
          gap: '1rem', 
          marginBottom: '2rem' 
        }}>
          <div style={{
            width: '56px',
            height: '56px',
            background: 'linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%)',
            borderRadius: '16px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: 'white',
            fontWeight: 'bold',
            fontSize: '24px',
            boxShadow: '0 4px 16px rgba(79, 70, 229, 0.3)'
          }}>
            🇮🇹
          </div>
          <div>
            <h1 style={{ 
              fontSize: '2.5rem', 
              fontWeight: '800', 
              margin: 0, 
              color: '#1e293b',
              letterSpacing: '-0.025em'
            }}>
              AmicoLingua Admin
            </h1>
            <p style={{ 
              fontSize: '1.125rem', 
              color: '#64748b', 
              margin: 0,
              fontWeight: '500'
            }}>
              Content Management & System Administration
            </p>
          </div>
        </div>

        <SignedOut>
          <div style={{
            backgroundColor: 'white',
            padding: '3rem',
            borderRadius: '16px',
            textAlign: 'center',
            boxShadow: '0 8px 32px rgba(0, 0, 0, 0.1)',
            border: '1px solid #e2e8f0'
          }}>
            <div style={{ fontSize: '4rem', marginBottom: '1.5rem' }}>🔐</div>
            <h2 style={{ 
              fontSize: '1.75rem', 
              fontWeight: '700', 
              marginBottom: '1rem',
              color: '#1e293b'
            }}>
              Admin Access Required
            </h2>
            <p style={{ 
              fontSize: '1rem', 
              color: '#64748b', 
              marginBottom: '2rem',
              lineHeight: '1.6'
            }}>
              Please sign in to access AmicoLingua's content management features and system administration tools.
            </p>
            <SignInButton mode="modal">
              <button style={{
                backgroundColor: '#4f46e5',
                color: 'white',
                padding: '1rem 2rem',
                borderRadius: '12px',
                border: 'none',
                cursor: 'pointer',
                fontSize: '1.1rem',
                fontWeight: '600',
                transition: 'all 0.3s ease',
                boxShadow: '0 4px 14px rgba(79, 70, 229, 0.4)'
              }}
              onMouseOver={(e) => {
                e.currentTarget.style.backgroundColor = '#4338ca'
                e.currentTarget.style.transform = 'translateY(-2px)'
              }}
              onMouseOut={(e) => {
                e.currentTarget.style.backgroundColor = '#4f46e5'
                e.currentTarget.style.transform = 'translateY(0)'
              }}>
                Sign In to Continue
              </button>
            </SignInButton>
          </div>
        </SignedOut>

        <SignedIn>
          {/* Statistics Section */}
          {statistics && (
            <div style={{ 
              backgroundColor: 'white', 
              padding: '2rem', 
              borderRadius: '16px', 
              marginBottom: '2rem',
              boxShadow: '0 4px 16px rgba(0, 0, 0, 0.08)',
              border: '1px solid #e2e8f0'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '1.5rem' }}>
                <span style={{ fontSize: '1.5rem' }}>📊</span>
                <h2 style={{ fontSize: '1.5rem', fontWeight: '700', margin: 0, color: '#1e293b' }}>
                  Content Statistics
                </h2>
              </div>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '1.5rem' }}>
                <div style={{ 
                  padding: '1.5rem', 
                  background: 'linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%)', 
                  borderRadius: '12px',
                  border: '1px solid #bbf7d0'
                }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.75rem' }}>
                    <span style={{ fontSize: '1.25rem' }}>📚</span>
                    <p style={{ fontSize: '0.9rem', color: '#166534', margin: 0, fontWeight: '600' }}>Grammar Rules</p>
                  </div>
                  <p style={{ fontSize: '2.5rem', fontWeight: '800', color: '#059669', margin: 0 }}>
                    {statistics.total_grammar_rules || 0}
                  </p>
                </div>
                <div style={{ 
                  padding: '1.5rem', 
                  background: 'linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%)', 
                  borderRadius: '12px',
                  border: '1px solid #bfdbfe'
                }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.75rem' }}>
                    <span style={{ fontSize: '1.25rem' }}>✏️</span>
                    <p style={{ fontSize: '0.9rem', color: '#1e40af', margin: 0, fontWeight: '600' }}>Exercises</p>
                  </div>
                  <p style={{ fontSize: '2.5rem', fontWeight: '800', color: '#0ea5e9', margin: 0 }}>
                    {statistics.total_exercises || 0}
                  </p>
                </div>
                <div style={{ 
                  padding: '1.5rem', 
                  background: 'linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%)', 
                  borderRadius: '12px',
                  border: '1px solid #d8b4fe'
                }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.75rem' }}>
                    <span style={{ fontSize: '1.25rem' }}>🏷️</span>
                    <p style={{ fontSize: '0.9rem', color: '#7c2d12', margin: 0, fontWeight: '600' }}>Version</p>
                  </div>
                  <p style={{ fontSize: '1.5rem', fontWeight: '700', color: '#7c3aed', margin: 0 }}>
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
            padding: '2rem', 
            borderRadius: '16px', 
            marginBottom: '2rem',
            boxShadow: '0 4px 16px rgba(0, 0, 0, 0.08)',
            border: '1px solid #e2e8f0'
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '1.5rem' }}>
              <span style={{ fontSize: '1.5rem' }}>🚀</span>
              <h2 style={{ fontSize: '1.5rem', fontWeight: '700', margin: 0, color: '#1e293b' }}>
                Content Management
              </h2>
            </div>
            
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '1.5rem' }}>
              <button
                onClick={() => handleAction('comprehensive', adminAPI.seedComprehensiveContent)}
                disabled={loading !== null}
                style={{
                  padding: '1.5rem',
                  background: loading === 'comprehensive' ? '#9ca3af' : 'linear-gradient(135deg, #059669 0%, #047857 100%)',
                  color: 'white',
                  border: 'none',
                  borderRadius: '12px',
                  cursor: loading !== null ? 'not-allowed' : 'pointer',
                  fontSize: '1rem',
                  fontWeight: '600',
                  transition: 'all 0.3s ease',
                  boxShadow: '0 4px 12px rgba(5, 150, 105, 0.3)',
                  textAlign: 'left'
                }}
                onMouseOver={(e) => {
                  if (loading === null) {
                    e.currentTarget.style.transform = 'translateY(-2px)'
                    e.currentTarget.style.boxShadow = '0 8px 20px rgba(5, 150, 105, 0.4)'
                  }
                }}
                onMouseOut={(e) => {
                  if (loading === null) {
                    e.currentTarget.style.transform = 'translateY(0)'
                    e.currentTarget.style.boxShadow = '0 4px 12px rgba(5, 150, 105, 0.3)'
                  }
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '0.5rem' }}>
                  <span style={{ fontSize: '1.5rem' }}>📚</span>
                  <span>{loading === 'comprehensive' ? 'Seeding Content...' : 'Seed All Content'}</span>
                </div>
                <div style={{ fontSize: '0.85rem', opacity: 0.9 }}>
                  Load 500+ comprehensive grammar rules and exercises
                </div>
              </button>

              <button
                onClick={() => handleAction('b1', () => adminAPI.seedByCefrLevel('B1'))}
                disabled={loading !== null}
                style={{
                  padding: '1.5rem',
                  background: loading === 'b1' ? '#9ca3af' : 'linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%)',
                  color: 'white',
                  border: 'none',
                  borderRadius: '12px',
                  cursor: loading !== null ? 'not-allowed' : 'pointer',
                  fontSize: '1rem',
                  fontWeight: '600',
                  transition: 'all 0.3s ease',
                  boxShadow: '0 4px 12px rgba(14, 165, 233, 0.3)',
                  textAlign: 'left'
                }}
                onMouseOver={(e) => {
                  if (loading === null) {
                    e.currentTarget.style.transform = 'translateY(-2px)'
                    e.currentTarget.style.boxShadow = '0 8px 20px rgba(14, 165, 233, 0.4)'
                  }
                }}
                onMouseOut={(e) => {
                  if (loading === null) {
                    e.currentTarget.style.transform = 'translateY(0)'
                    e.currentTarget.style.boxShadow = '0 4px 12px rgba(14, 165, 233, 0.3)'
                  }
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '0.5rem' }}>
                  <span style={{ fontSize: '1.5rem' }}>🎓</span>
                  <span>{loading === 'b1' ? 'Seeding B1...' : 'Seed B1 Level'}</span>
                </div>
                <div style={{ fontSize: '0.85rem', opacity: 0.9 }}>
                  Intermediate level grammar content
                </div>
              </button>

              <button
                onClick={() => handleAction('b2', () => adminAPI.seedByCefrLevel('B2'))}
                disabled={loading !== null}
                style={{
                  padding: '1.5rem',
                  background: loading === 'b2' ? '#9ca3af' : 'linear-gradient(135deg, #7c3aed 0%, #6d28d9 100%)',
                  color: 'white',
                  border: 'none',
                  borderRadius: '12px',
                  cursor: loading !== null ? 'not-allowed' : 'pointer',
                  fontSize: '1rem',
                  fontWeight: '600',
                  transition: 'all 0.3s ease',
                  boxShadow: '0 4px 12px rgba(124, 58, 237, 0.3)',
                  textAlign: 'left'
                }}
                onMouseOver={(e) => {
                  if (loading === null) {
                    e.currentTarget.style.transform = 'translateY(-2px)'
                    e.currentTarget.style.boxShadow = '0 8px 20px rgba(124, 58, 237, 0.4)'
                  }
                }}
                onMouseOut={(e) => {
                  if (loading === null) {
                    e.currentTarget.style.transform = 'translateY(0)'
                    e.currentTarget.style.boxShadow = '0 4px 12px rgba(124, 58, 237, 0.3)'
                  }
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '0.5rem' }}>
                  <span style={{ fontSize: '1.5rem' }}>🏆</span>
                  <span>{loading === 'b2' ? 'Seeding B2...' : 'Seed B2 Level'}</span>
                </div>
                <div style={{ fontSize: '0.85rem', opacity: 0.9 }}>
                  Upper-intermediate level content
                </div>
              </button>

              <button
                onClick={loadStatistics}
                disabled={loading !== null}
                style={{
                  padding: '1.5rem',
                  background: 'linear-gradient(135deg, #6b7280 0%, #4b5563 100%)',
                  color: 'white',
                  border: 'none',
                  borderRadius: '12px',
                  cursor: 'pointer',
                  fontSize: '1rem',
                  fontWeight: '600',
                  transition: 'all 0.3s ease',
                  boxShadow: '0 4px 12px rgba(107, 114, 128, 0.3)',
                  textAlign: 'left'
                }}
                onMouseOver={(e) => {
                  e.currentTarget.style.transform = 'translateY(-2px)'
                  e.currentTarget.style.boxShadow = '0 8px 20px rgba(107, 114, 128, 0.4)'
                }}
                onMouseOut={(e) => {
                  e.currentTarget.style.transform = 'translateY(0)'
                  e.currentTarget.style.boxShadow = '0 4px 12px rgba(107, 114, 128, 0.3)'
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '0.5rem' }}>
                  <span style={{ fontSize: '1.5rem' }}>🔄</span>
                  <span>Refresh Statistics</span>
                </div>
                <div style={{ fontSize: '0.85rem', opacity: 0.9 }}>
                  Update content metrics and status
                </div>
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
            padding: '2rem',
            background: 'linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%)',
            border: '1px solid #fed7aa',
            borderRadius: '16px',
            fontSize: '0.95rem',
            color: '#92400e'
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '1rem' }}>
              <span style={{ fontSize: '1.5rem' }}>📋</span>
              <h3 style={{ margin: 0, fontWeight: '700', fontSize: '1.25rem' }}>Quick Start Guide</h3>
            </div>
            <ol style={{ margin: 0, paddingLeft: '1.5rem', lineHeight: '1.6' }}>
              <li style={{ marginBottom: '0.5rem' }}>Click <strong>"Seed All Content"</strong> to load comprehensive Italian grammar rules</li>
              <li style={{ marginBottom: '0.5rem' }}>Wait for the success confirmation and check updated statistics</li>
              <li style={{ marginBottom: '0.5rem' }}>Navigate back to the main chat interface</li>
              <li style={{ marginBottom: '0.5rem' }}>Try asking: <em>"How do I use the subjunctive mood in Italian?"</em></li>
              <li>Enjoy detailed, comprehensive responses with examples and exercises!</li>
            </ol>
          </div>

          {/* Navigation */}
          <div style={{ marginTop: '2rem', textAlign: 'center' }}>
            <a 
              href="/"
              style={{
                display: 'inline-flex',
                alignItems: 'center',
                gap: '0.5rem',
                padding: '1rem 2rem',
                background: 'linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%)',
                color: 'white',
                textDecoration: 'none',
                borderRadius: '12px',
                fontWeight: '600',
                fontSize: '1rem',
                transition: 'all 0.3s ease',
                boxShadow: '0 4px 12px rgba(79, 70, 229, 0.3)'
              }}
              onMouseOver={(e) => {
                e.currentTarget.style.transform = 'translateY(-2px)'
                e.currentTarget.style.boxShadow = '0 8px 20px rgba(79, 70, 229, 0.4)'
              }}
              onMouseOut={(e) => {
                e.currentTarget.style.transform = 'translateY(0)'
                e.currentTarget.style.boxShadow = '0 4px 12px rgba(79, 70, 229, 0.3)'
              }}
            >
              <span>←</span>
              Back to AmicoLingua Chat
            </a>
          </div>
        </SignedIn>
      </div>
    </div>
  )
}