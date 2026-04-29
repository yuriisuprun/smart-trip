'use client'

import React, { useState, useEffect } from 'react'
import { useAuth } from '@clerk/nextjs'
import { evaluateAPI } from '@/lib/api'
import { CheckCircle, XCircle, Loader } from 'lucide-react'

interface QuizQuestion {
  id: string
  question: string
  type: 'open' | 'multiple_choice'
  options?: string[]
  correctAnswer?: string
  topic: string
}

interface EvaluationResult {
  score: number
  is_correct: boolean
  corrections: string[]
  explanation: string
  improvement_suggestions: string[]
  grammar_errors: Array<{
    error: string
    correction: string
    explanation: string
  }>
}

export default function QuizInterface() {
  const [currentQuestion, setCurrentQuestion] = useState<QuizQuestion | null>(null)
  const [userAnswer, setUserAnswer] = useState('')
  const [evaluation, setEvaluation] = useState<EvaluationResult | null>(null)
  const [isEvaluating, setIsEvaluating] = useState(false)
  const [showFeedback, setShowFeedback] = useState(false)
  const [mounted, setMounted] = useState(false)
  const { getToken } = useAuth()

  useEffect(() => {
    setMounted(true)
  }, [])

  const sampleQuestion: QuizQuestion = {
    id: 'q1',
    question: 'Completa la frase: "Ieri io _____ al cinema con i miei amici."',
    type: 'multiple_choice',
    options: ['vado', 'sono andato', 'andrò', 'andrei'],
    correctAnswer: 'sono andato',
    topic: 'grammar',
  }

  const handleSubmitAnswer = async () => {
    if (!userAnswer.trim() || !currentQuestion) return

    setIsEvaluating(true)
    try {
      const result = await evaluateAPI.evaluateAnswer({
        question: currentQuestion.question,
        user_answer: userAnswer,
        correct_answer: currentQuestion.correctAnswer,
        question_type: currentQuestion.type,
        topic: currentQuestion.topic,
      }, getToken)

      setEvaluation(result.feedback)
      setShowFeedback(true)
    } catch (error) {
      console.error('Error evaluating answer:', error)
    } finally {
      setIsEvaluating(false)
    }
  }

  const handleNextQuestion = () => {
    setUserAnswer('')
    setEvaluation(null)
    setShowFeedback(false)
    // Load next question
    setCurrentQuestion(sampleQuestion)
  }

  if (!mounted) {
    return (
      <div style={{ padding: '1.5rem', textAlign: 'center' }}>
        <p style={{ color: '#6b7280' }}>Loading...</p>
      </div>
    )
  }

  if (!currentQuestion) {
    return (
      <div style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '4rem 1.5rem',
        textAlign: 'center'
      }}>
        <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>🎯</div>
        <h2 style={{ 
          fontSize: '1.25rem', 
          fontWeight: 'bold', 
          color: '#1e293b', 
          marginBottom: '0.5rem',
          margin: 0
        }}>
          Ready to Test Your Knowledge?
        </h2>
        <p style={{ 
          color: '#64748b', 
          marginBottom: '1.5rem', 
          maxWidth: '28rem',
          fontSize: '0.875rem',
          margin: '0.5rem 0 1.5rem 0'
        }}>
          Challenge yourself with interactive quizzes designed to improve your Italian skills
        </p>
        <button
          onClick={() => setCurrentQuestion(sampleQuestion)}
          style={{
            backgroundColor: '#4f46e5',
            color: 'white',
            padding: '0.75rem 1.5rem',
            borderRadius: '8px',
            border: 'none',
            fontWeight: '500',
            cursor: 'pointer',
            transition: 'background-color 0.2s'
          }}
          onMouseOver={(e) => {
            e.currentTarget.style.backgroundColor = '#4338ca'
          }}
          onMouseOut={(e) => {
            e.currentTarget.style.backgroundColor = '#4f46e5'
          }}
        >
          Start Quiz
        </button>
      </div>
    )
  }

  return (
    <div style={{ 
      maxWidth: '48rem', 
      margin: '0 auto', 
      padding: '1.5rem' 
    }}>
      <div style={{ marginBottom: '1.5rem' }}>
        <div style={{
          backgroundColor: '#f8fafc',
          borderRadius: '8px',
          padding: '1rem',
          marginBottom: '1rem',
          border: '1px solid #e2e8f0'
        }}>
          <h2 style={{ 
            fontSize: '1.125rem', 
            fontWeight: '600', 
            color: '#1e293b',
            margin: 0
          }}>
            {currentQuestion.question}
          </h2>
        </div>

        {currentQuestion.type === 'multiple_choice' ? (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
            {currentQuestion.options?.map((option, idx) => (
              <label 
                key={idx} 
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  padding: '0.75rem',
                  border: '1px solid #e2e8f0',
                  borderRadius: '8px',
                  cursor: 'pointer',
                  transition: 'background-color 0.2s',
                  backgroundColor: 'white'
                }}
                onMouseOver={(e) => {
                  e.currentTarget.style.backgroundColor = '#f8fafc'
                }}
                onMouseOut={(e) => {
                  e.currentTarget.style.backgroundColor = 'white'
                }}
              >
                <input
                  type="radio"
                  name="answer"
                  value={option}
                  checked={userAnswer === option}
                  onChange={(e) => setUserAnswer(e.target.value)}
                  style={{ 
                    marginRight: '0.75rem',
                    accentColor: '#4f46e5'
                  }}
                />
                <span style={{ color: '#1e293b' }}>{option}</span>
              </label>
            ))}
          </div>
        ) : (
          <textarea
            value={userAnswer}
            onChange={(e) => setUserAnswer(e.target.value)}
            placeholder="Write your answer here..."
            rows={4}
            style={{
              width: '100%',
              padding: '0.75rem',
              border: '1px solid #d1d5db',
              borderRadius: '8px',
              outline: 'none',
              fontSize: '0.875rem',
              fontFamily: 'inherit',
              resize: 'vertical'
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
        )}
      </div>

      {!showFeedback ? (
        <button
          onClick={handleSubmitAnswer}
          disabled={!userAnswer.trim() || isEvaluating}
          style={{
            width: '100%',
            backgroundColor: !userAnswer.trim() || isEvaluating ? '#9ca3af' : '#4f46e5',
            color: 'white',
            padding: '0.75rem',
            borderRadius: '8px',
            border: 'none',
            fontWeight: '500',
            cursor: !userAnswer.trim() || isEvaluating ? 'not-allowed' : 'pointer',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            gap: '0.5rem',
            transition: 'background-color 0.2s'
          }}
          onMouseOver={(e) => {
            if (userAnswer.trim() && !isEvaluating) {
              e.currentTarget.style.backgroundColor = '#4338ca'
            }
          }}
          onMouseOut={(e) => {
            if (userAnswer.trim() && !isEvaluating) {
              e.currentTarget.style.backgroundColor = '#4f46e5'
            }
          }}
        >
          {isEvaluating ? (
            <>
              <Loader style={{ width: '16px', height: '16px' }} className="animate-spin" />
              Evaluating...
            </>
          ) : (
            'Submit Answer'
          )}
        </button>
      ) : evaluation ? (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <div style={{
            padding: '1rem',
            borderRadius: '8px',
            display: 'flex',
            alignItems: 'center',
            gap: '0.75rem',
            backgroundColor: evaluation.is_correct ? '#f0fdf4' : '#fef2f2',
            color: evaluation.is_correct ? '#166534' : '#dc2626',
            border: `1px solid ${evaluation.is_correct ? '#bbf7d0' : '#fecaca'}`
          }}>
            {evaluation.is_correct ? (
              <CheckCircle style={{ width: '24px', height: '24px' }} />
            ) : (
              <XCircle style={{ width: '24px', height: '24px' }} />
            )}
            <div>
              <p style={{ fontWeight: '600', margin: 0 }}>
                {evaluation.is_correct ? 'Correct!' : 'Not quite right'}
              </p>
              <p style={{ fontSize: '0.875rem', margin: 0 }}>
                Score: {evaluation.score}/10
              </p>
            </div>
          </div>

          <div style={{
            backgroundColor: '#eff6ff',
            padding: '1rem',
            borderRadius: '8px',
            border: '1px solid #bfdbfe'
          }}>
            <h3 style={{ 
              fontWeight: '600', 
              marginBottom: '0.5rem', 
              color: '#1e40af',
              margin: '0 0 0.5rem 0'
            }}>
              Explanation
            </h3>
            <p style={{ 
              fontSize: '0.875rem', 
              color: '#1e40af',
              margin: 0
            }}>
              {evaluation.explanation}
            </p>
          </div>

          {evaluation.corrections.length > 0 && (
            <div style={{
              backgroundColor: '#fffbeb',
              padding: '1rem',
              borderRadius: '8px',
              border: '1px solid #fed7aa'
            }}>
              <h3 style={{ 
                fontWeight: '600', 
                marginBottom: '0.5rem', 
                color: '#92400e',
                margin: '0 0 0.5rem 0'
              }}>
                Corrections
              </h3>
              <ul style={{ 
                fontSize: '0.875rem', 
                color: '#92400e',
                margin: 0,
                paddingLeft: '1rem'
              }}>
                {evaluation.corrections.map((correction, idx) => (
                  <li key={idx} style={{ marginBottom: '0.25rem' }}>
                    {correction}
                  </li>
                ))}
              </ul>
            </div>
          )}

          {evaluation.improvement_suggestions.length > 0 && (
            <div style={{
              backgroundColor: '#faf5ff',
              padding: '1rem',
              borderRadius: '8px',
              border: '1px solid #e9d5ff'
            }}>
              <h3 style={{ 
                fontWeight: '600', 
                marginBottom: '0.5rem', 
                color: '#7c2d12',
                margin: '0 0 0.5rem 0'
              }}>
                Tips for Improvement
              </h3>
              <ul style={{ 
                fontSize: '0.875rem', 
                color: '#7c2d12',
                margin: 0,
                paddingLeft: '1rem'
              }}>
                {evaluation.improvement_suggestions.map((suggestion, idx) => (
                  <li key={idx} style={{ marginBottom: '0.25rem' }}>
                    {suggestion}
                  </li>
                ))}
              </ul>
            </div>
          )}

          <button
            onClick={handleNextQuestion}
            style={{
              width: '100%',
              backgroundColor: '#4f46e5',
              color: 'white',
              padding: '0.75rem',
              borderRadius: '8px',
              border: 'none',
              fontWeight: '500',
              cursor: 'pointer',
              transition: 'background-color 0.2s'
            }}
            onMouseOver={(e) => {
              e.currentTarget.style.backgroundColor = '#4338ca'
            }}
            onMouseOut={(e) => {
              e.currentTarget.style.backgroundColor = '#4f46e5'
            }}
          >
            Next Question
          </button>
        </div>
      ) : null}
    </div>
  )
}
