'use client'

import React, { useEffect, useState } from 'react'
import { useAuth } from '@clerk/nextjs'
import { progressAPI } from '@/lib/api'
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'
import { TrendingUp } from 'lucide-react'

interface SkillData {
  skill: string
  level: string
  score: number
  accuracy: number
}

export default function ProgressDashboard() {
  const [skillData, setSkillData] = useState<SkillData[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [mounted, setMounted] = useState(false)
  const { getToken } = useAuth()

  useEffect(() => {
    setMounted(true)
  }, [])

  useEffect(() => {
    const fetchProgress = async () => {
      try {
        const response = await progressAPI.getUserProgress(getToken)
        setSkillData(response.skill_progress || [])
      } catch (err) {
        setError('Failed to load progress')
        console.error(err)
      } finally {
        setLoading(false)
      }
    }

    if (mounted) {
      fetchProgress()
    }
  }, [mounted, getToken])

  if (!mounted) {
    return (
      <div style={{ padding: '1.5rem', textAlign: 'center' }}>
        <p style={{ color: '#6b7280' }}>Loading...</p>
      </div>
    )
  }

  if (loading) {
    return (
      <div style={{ textAlign: 'center', padding: '2rem' }}>
        Loading progress...
      </div>
    )
  }

  if (error) {
    return (
      <div style={{ textAlign: 'center', padding: '2rem', color: '#ef4444' }}>
        {error}
      </div>
    )
  }

  const chartData = skillData.map((skill) => ({
    name: skill.skill,
    score: skill.score,
    accuracy: Math.round(skill.accuracy * 100),
  }))

  return (
    <div style={{ padding: '1.5rem' }}>
      <div style={{ 
        display: 'flex', 
        alignItems: 'center', 
        gap: '0.75rem', 
        marginBottom: '1.5rem' 
      }}>
        <TrendingUp style={{ 
          width: '24px', 
          height: '24px', 
          color: '#4f46e5' 
        }} />
        <h2 style={{ 
          fontSize: '1.5rem', 
          fontWeight: 'bold', 
          color: '#1e293b',
          margin: 0
        }}>
          Your Progress
        </h2>
      </div>

      {skillData.length === 0 ? (
        <div style={{ 
          textAlign: 'center', 
          padding: '3rem 0' 
        }}>
          <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>📊</div>
          <h3 style={{ 
            fontSize: '1.125rem', 
            fontWeight: '600', 
            color: '#1e293b', 
            marginBottom: '0.5rem',
            margin: 0
          }}>
            No Progress Data Yet
          </h3>
          <p style={{ 
            color: '#64748b',
            margin: '0.5rem 0 0 0'
          }}>
            Start learning with the Chat Tutor or take some quizzes to see your progress here!
          </p>
        </div>
      ) : (
        <>
          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
            gap: '1rem',
            marginBottom: '1.5rem'
          }}>
            {skillData.map((skill) => (
              <div 
                key={skill.skill} 
                style={{
                  backgroundColor: '#f8fafc',
                  border: '1px solid #e2e8f0',
                  borderRadius: '8px',
                  padding: '1rem'
                }}
              >
                <h3 style={{ 
                  fontWeight: '600', 
                  fontSize: '1.125rem', 
                  textTransform: 'capitalize', 
                  color: '#1e293b',
                  margin: '0 0 0.75rem 0'
                }}>
                  {skill.skill}
                </h3>
                <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                    <span style={{ fontSize: '0.875rem', color: '#64748b' }}>Level:</span>
                    <span style={{ fontSize: '0.875rem', fontWeight: '500' }}>{skill.level}</span>
                  </div>
                  <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                    <span style={{ fontSize: '0.875rem', color: '#64748b' }}>Score:</span>
                    <span style={{ fontSize: '0.875rem', fontWeight: '500' }}>{skill.score.toFixed(1)}/100</span>
                  </div>
                  <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                    <span style={{ fontSize: '0.875rem', color: '#64748b' }}>Accuracy:</span>
                    <span style={{ fontSize: '0.875rem', fontWeight: '500' }}>{Math.round(skill.accuracy * 100)}%</span>
                  </div>
                  <div style={{
                    width: '100%',
                    backgroundColor: '#e2e8f0',
                    borderRadius: '9999px',
                    height: '8px',
                    marginTop: '0.75rem'
                  }}>
                    <div 
                      style={{
                        backgroundColor: '#4f46e5',
                        borderRadius: '9999px',
                        height: '8px',
                        transition: 'width 0.3s ease',
                        width: `${Math.round(skill.accuracy * 100)}%`
                      }}
                    ></div>
                  </div>
                </div>
              </div>
            ))}
          </div>

          <div style={{
            backgroundColor: 'white',
            border: '1px solid #e2e8f0',
            borderRadius: '8px',
            padding: '1.5rem'
          }}>
            <h3 style={{ 
              fontSize: '1.125rem', 
              fontWeight: '600', 
              color: '#1e293b', 
              marginBottom: '1rem',
              margin: '0 0 1rem 0'
            }}>
              Score Overview
            </h3>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={chartData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Bar dataKey="score" fill="#4f46e5" name="Score" />
                <Bar dataKey="accuracy" fill="#10b981" name="Accuracy %" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </>
      )}
    </div>
  )
}
