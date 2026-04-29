'use client'

import React, { useState } from 'react'
import { adminAPI } from '@/lib/api'
import { Database, BookOpen, GraduationCap, BarChart3, RefreshCw, CheckCircle, AlertCircle } from 'lucide-react'

interface AdminPanelProps {
  onClose?: () => void
}

export default function AdminPanel({ onClose }: AdminPanelProps) {
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

  React.useEffect(() => {
    loadStatistics()
  }, [])

  return (
    <div style={{
      position: 'fixed',
      top: 0,
      left: 0,
      right: 0,
      bottom: 0,
      backgroundColor: 'rgba(0, 0, 0, 0.5)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      zIndex: 1000,
      padding: '1rem'
    }}>
      <div style={{
        backgroundColor: 'white',
        borderRadius: '12px',
        padding: '2rem',
        maxWidth: '800px',
        width: '100%',
        maxHeight: '90vh',
        overflowY: 'auto',
        boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.25)'
      }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
          <h2 style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#1e293b', margin: 0 }}>
            <Database style={{ display: 'inline', marginRight: '0.5rem', verticalAlign: 'middle' }} size={24} />
            Admin Panel - Italian Grammar Content
          </h2>
          {onClose && (
            <button
              onClick={onClose}
              style={{
                background: 'none',
                border: 'none',
                fontSize: '1.5rem',
                cursor: 'pointer',
                color: '#6b7280'
              }}
            >
              ×
            </button>
          )}
        </div>

        {/* Statistics Section */}
        {statistics && (
          <div style={{ marginBottom: '2rem', padding: '1rem', backgroundColor: '#f8fafc', borderRadius: '8px' }}>
            <h3 style={{ fontSize: '1.125rem', fontWeight: '600', marginBottom: '1rem', color: '#1e293b' }}>
              <BarChart3 style={{ display: 'inline', marginRight: '0.5rem', verticalAlign: 'middle' }} size={20} />
              Content Statistics
            </h3>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem' }}>
              <div>
                <p style={{ fontSize: '0.875rem', color: '#6b7280', margin: 0 }}>Total Grammar Rules</p>
                <p style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#059669', margin: 0 }}>
                  {statistics.total_grammar_rules}
                </p>
              </div>
              <div>
                <p style={{ fontSize: '0.875rem', color: '#6b7280', margin: 0 }}>Total Exercises</p>
                <p style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#0ea5e9', margin: 0 }}>
                  {statistics.total_exercises}
                </p>
              </div>
              <div>
                <p style={{ fontSize: '0.875rem', color: '#6b7280', margin: 0 }}>Content Version</p>
                <p style={{ fontSize: '1.125rem', fontWeight: '600', color: '#7c3aed', margin: 0 }}>
                  {statistics.content_version}
                </p>
              </div>
            </div>
            
            {/* CEFR Level Distribution */}
            <div style={{ marginTop: '1rem' }}>
              <h4 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.5rem', color: '#1e293b' }}>
                CEFR Level Distribution
              </h4>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(120px, 1fr))', gap: '0.5rem' }}>
                {Object.entries(statistics.cefr_level_distribution || {}).map(([level, counts]: [string, any]) => (
                  counts.grammar_rules > 0 || counts.exercises > 0 ? (
                    <div key={level} style={{ textAlign: 'center', padding: '0.5rem', backgroundColor: 'white', borderRadius: '6px' }}>
                      <p style={{ fontSize: '0.875rem', fontWeight: '600', color: '#1e293b', margin: 0 }}>{level}</p>
                      <p style={{ fontSize: '0.75rem', color: '#6b7280', margin: 0 }}>
                        {counts.grammar_rules}G + {counts.exercises}E
                      </p>
                    </div>
                  ) : null
                ))}
              </div>
            </div>
          </div>
        )}

        {/* Action Buttons */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '1rem', marginBottom: '2rem' }}>
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
              display: 'flex',
              alignItems: 'center',
              gap: '0.5rem',
              fontSize: '0.875rem',
              fontWeight: '500'
            }}
          >
            {loading === 'comprehensive' ? (
              <RefreshCw size={16} className="animate-spin" />
            ) : (
              <BookOpen size={16} />
            )}
            Seed Comprehensive Content (500+ Rules)
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
              display: 'flex',
              alignItems: 'center',
              gap: '0.5rem',
              fontSize: '0.875rem',
              fontWeight: '500'
            }}
          >
            {loading === 'b1' ? (
              <RefreshCw size={16} className="animate-spin" />
            ) : (
              <GraduationCap size={16} />
            )}
            Seed B1 Level Content
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
              display: 'flex',
              alignItems: 'center',
              gap: '0.5rem',
              fontSize: '0.875rem',
              fontWeight: '500'
            }}
          >
            {loading === 'b2' ? (
              <RefreshCw size={16} className="animate-spin" />
            ) : (
              <GraduationCap size={16} />
            )}
            Seed B2 Level Content
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
              display: 'flex',
              alignItems: 'center',
              gap: '0.5rem',
              fontSize: '0.875rem',
              fontWeight: '500'
            }}
          >
            <RefreshCw size={16} />
            Refresh Statistics
          </button>
        </div>

        {/* Topic-specific seeding */}
        <div style={{ marginBottom: '2rem' }}>
          <h3 style={{ fontSize: '1.125rem', fontWeight: '600', marginBottom: '1rem', color: '#1e293b' }}>
            Seed by Topic
          </h3>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '0.5rem' }}>
            {[
              'subjunctive_mood',
              'conditional_mood', 
              'imperative_mood',
              'prepositions',
              'pronouns',
              'relative_pronouns',
              'complex_sentences',
              'advanced_verbs',
              'discourse_markers'
            ].map(topic => (
              <button
                key={topic}
                onClick={() => handleAction(`topic-${topic}`, () => adminAPI.seedByTopic(topic))}
                disabled={loading !== null}
                style={{
                  padding: '0.5rem 0.75rem',
                  backgroundColor: loading === `topic-${topic}` ? '#9ca3af' : '#f1f5f9',
                  color: loading === `topic-${topic}` ? 'white' : '#1e293b',
                  border: '1px solid #e2e8f0',
                  borderRadius: '6px',
                  cursor: loading !== null ? 'not-allowed' : 'pointer',
                  fontSize: '0.75rem',
                  textAlign: 'center'
                }}
              >
                {loading === `topic-${topic}` ? '...' : topic.replace('_', ' ')}
              </button>
            ))}
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
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: '#dc2626' }}>
              <AlertCircle size={16} />
              <span style={{ fontWeight: '500' }}>Error</span>
            </div>
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
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: '#059669', marginBottom: '0.5rem' }}>
              <CheckCircle size={16} />
              <span style={{ fontWeight: '500' }}>Success</span>
            </div>
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
          <h4 style={{ margin: '0 0 0.5rem 0', fontWeight: '600' }}>Instructions:</h4>
          <ol style={{ margin: 0, paddingLeft: '1.25rem' }}>
            <li>Start with "Seed Comprehensive Content" to load all 500+ grammar rules</li>
            <li>Use CEFR level buttons to load specific level content (B1 or B2)</li>
            <li>Use topic buttons to load specific grammar topics</li>
            <li>Check statistics to verify content is loaded</li>
            <li>Test the chat interface with grammar questions</li>
          </ol>
        </div>
      </div>
    </div>
  )
}