'use client'

import { useUser, UserButton } from '@clerk/nextjs'
import { useState, useEffect } from 'react'
import { api } from '../lib/api'

interface UserProfile {
  id: string
  email: string
  name: string
  cefr_level: string
  total_score: number
  total_questions: number
  created_at: string
  updated_at: string
}

export default function ProfilePage() {
  const { user, isLoaded } = useUser()
  const [profile, setProfile] = useState<UserProfile | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [editing, setEditing] = useState(false)
  const [editForm, setEditForm] = useState({
    name: '',
    cefr_level: ''
  })

  useEffect(() => {
    if (isLoaded && user) {
      fetchProfile()
    }
  }, [isLoaded, user])

  const fetchProfile = async () => {
    try {
      setLoading(true)
      const response = await api.get('/api/user/profile')
      setProfile(response.data)
      setEditForm({
        name: response.data.name,
        cefr_level: response.data.cefr_level
      })
    } catch (err) {
      setError('Failed to load profile')
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  const handleSave = async () => {
    try {
      const response = await api.put('/api/user/profile', editForm)
      setProfile(response.data)
      setEditing(false)
    } catch (err) {
      setError('Failed to update profile')
      console.error(err)
    }
  }

  if (!isLoaded || loading) {
    return (
      <div style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        minHeight: '100vh'
      }}>
        <div>Loading...</div>
      </div>
    )
  }

  if (!user) {
    return (
      <div style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        minHeight: '100vh'
      }}>
        <div>Please sign in to view your profile.</div>
      </div>
    )
  }

  return (
    <div style={{
      maxWidth: '800px',
      margin: '0 auto',
      padding: '2rem',
      backgroundColor: '#ffffff',
      minHeight: '100vh'
    }}>
      <div style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        marginBottom: '2rem'
      }}>
        <h1 style={{
          fontSize: '2rem',
          fontWeight: 'bold',
          color: '#1e293b'
        }}>
          User Profile
        </h1>
        <UserButton />
      </div>

      {error && (
        <div style={{
          backgroundColor: '#fee2e2',
          color: '#dc2626',
          padding: '1rem',
          borderRadius: '0.5rem',
          marginBottom: '1rem'
        }}>
          {error}
        </div>
      )}

      {profile && (
        <div style={{
          backgroundColor: '#f8fafc',
          padding: '2rem',
          borderRadius: '0.5rem',
          border: '1px solid #e2e8f0'
        }}>
          <div style={{ marginBottom: '1.5rem' }}>
            <h2 style={{
              fontSize: '1.25rem',
              fontWeight: 'semibold',
              marginBottom: '1rem',
              color: '#374151'
            }}>
              Account Information
            </h2>
            
            <div style={{ marginBottom: '1rem' }}>
              <label style={{
                display: 'block',
                fontSize: '0.875rem',
                fontWeight: 'medium',
                color: '#6b7280',
                marginBottom: '0.25rem'
              }}>
                Email
              </label>
              <div style={{
                padding: '0.5rem',
                backgroundColor: '#f3f4f6',
                borderRadius: '0.25rem',
                color: '#374151'
              }}>
                {profile.email}
              </div>
            </div>

            <div style={{ marginBottom: '1rem' }}>
              <label style={{
                display: 'block',
                fontSize: '0.875rem',
                fontWeight: 'medium',
                color: '#6b7280',
                marginBottom: '0.25rem'
              }}>
                Name
              </label>
              {editing ? (
                <input
                  type="text"
                  value={editForm.name}
                  onChange={(e) => setEditForm({ ...editForm, name: e.target.value })}
                  style={{
                    width: '100%',
                    padding: '0.5rem',
                    border: '1px solid #d1d5db',
                    borderRadius: '0.25rem',
                    fontSize: '0.875rem'
                  }}
                />
              ) : (
                <div style={{
                  padding: '0.5rem',
                  backgroundColor: '#f3f4f6',
                  borderRadius: '0.25rem',
                  color: '#374151'
                }}>
                  {profile.name}
                </div>
              )}
            </div>

            <div style={{ marginBottom: '1rem' }}>
              <label style={{
                display: 'block',
                fontSize: '0.875rem',
                fontWeight: 'medium',
                color: '#6b7280',
                marginBottom: '0.25rem'
              }}>
                CEFR Level
              </label>
              {editing ? (
                <select
                  value={editForm.cefr_level}
                  onChange={(e) => setEditForm({ ...editForm, cefr_level: e.target.value })}
                  style={{
                    width: '100%',
                    padding: '0.5rem',
                    border: '1px solid #d1d5db',
                    borderRadius: '0.25rem',
                    fontSize: '0.875rem'
                  }}
                >
                  <option value="A1">A1 - Beginner</option>
                  <option value="A2">A2 - Elementary</option>
                  <option value="B1">B1 - Intermediate</option>
                  <option value="B2">B2 - Upper Intermediate</option>
                </select>
              ) : (
                <div style={{
                  padding: '0.5rem',
                  backgroundColor: '#f3f4f6',
                  borderRadius: '0.25rem',
                  color: '#374151'
                }}>
                  {profile.cefr_level}
                </div>
              )}
            </div>
          </div>

          <div style={{ marginBottom: '1.5rem' }}>
            <h2 style={{
              fontSize: '1.25rem',
              fontWeight: 'semibold',
              marginBottom: '1rem',
              color: '#374151'
            }}>
              Learning Progress
            </h2>
            
            <div style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
              gap: '1rem'
            }}>
              <div style={{
                backgroundColor: '#ffffff',
                padding: '1rem',
                borderRadius: '0.5rem',
                border: '1px solid #e5e7eb'
              }}>
                <div style={{
                  fontSize: '0.875rem',
                  color: '#6b7280',
                  marginBottom: '0.25rem'
                }}>
                  Total Score
                </div>
                <div style={{
                  fontSize: '1.5rem',
                  fontWeight: 'bold',
                  color: '#1f2937'
                }}>
                  {profile.total_score.toFixed(1)}
                </div>
              </div>
              
              <div style={{
                backgroundColor: '#ffffff',
                padding: '1rem',
                borderRadius: '0.5rem',
                border: '1px solid #e5e7eb'
              }}>
                <div style={{
                  fontSize: '0.875rem',
                  color: '#6b7280',
                  marginBottom: '0.25rem'
                }}>
                  Questions Answered
                </div>
                <div style={{
                  fontSize: '1.5rem',
                  fontWeight: 'bold',
                  color: '#1f2937'
                }}>
                  {profile.total_questions}
                </div>
              </div>
            </div>
          </div>

          <div style={{
            display: 'flex',
            gap: '1rem'
          }}>
            {editing ? (
              <>
                <button
                  onClick={handleSave}
                  style={{
                    backgroundColor: '#3b82f6',
                    color: 'white',
                    padding: '0.5rem 1rem',
                    borderRadius: '0.25rem',
                    border: 'none',
                    cursor: 'pointer',
                    fontSize: '0.875rem'
                  }}
                >
                  Save Changes
                </button>
                <button
                  onClick={() => {
                    setEditing(false)
                    setEditForm({
                      name: profile.name,
                      cefr_level: profile.cefr_level
                    })
                  }}
                  style={{
                    backgroundColor: '#6b7280',
                    color: 'white',
                    padding: '0.5rem 1rem',
                    borderRadius: '0.25rem',
                    border: 'none',
                    cursor: 'pointer',
                    fontSize: '0.875rem'
                  }}
                >
                  Cancel
                </button>
              </>
            ) : (
              <button
                onClick={() => setEditing(true)}
                style={{
                  backgroundColor: '#059669',
                  color: 'white',
                  padding: '0.5rem 1rem',
                  borderRadius: '0.25rem',
                  border: 'none',
                  cursor: 'pointer',
                  fontSize: '0.875rem'
                }}
              >
                Edit Profile
              </button>
            )}
          </div>
        </div>
      )}

      <div style={{
        marginTop: '2rem',
        textAlign: 'center'
      }}>
        <a
          href="/"
          style={{
            color: '#3b82f6',
            textDecoration: 'underline',
            fontSize: '0.875rem'
          }}
        >
          ← Back to Tutor
        </a>
      </div>
    </div>
  )
}