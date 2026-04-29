/**
 * Internationalization (i18n) utilities for the Italian Language AI Tutor
 */

export type Language = 'en' | 'it'

export interface Translations {
  // Header
  appTitle: string
  appSubtitle: string
  
  // Navigation
  chatTutor: string
  quiz: string
  progress: string
  
  // Topics
  grammar: string
  vocabulary: string
  reading: string
  listening: string
  
  // Session
  currentSession: string
  level: string
  
  // Chat Interface
  typeMessage: string
  send: string
  newSession: string
  selectTopic: string
  selectDifficulty: string
  startSession: string
  
  // Quiz Interface
  startQuiz: string
  nextQuestion: string
  submitAnswer: string
  score: string
  correct: string
  incorrect: string
  
  // Progress Dashboard
  overallProgress: string
  weakAreas: string
  strengths: string
  sessionsCompleted: string
  averageScore: string
  
  // Difficulty Levels
  beginner: string
  elementary: string
  intermediate: string
  upperIntermediate: string
  advanced: string
  proficiency: string
  
  // Common
  loading: string
  error: string
  retry: string
  cancel: string
  save: string
  delete: string
  edit: string
  
  // Language Selector
  language: string
  english: string
  italian: string
}

const translations: Record<Language, Translations> = {
  en: {
    // Header
    appTitle: 'Italian Language AI Tutor',
    appSubtitle: 'Exam Preparation',
    
    // Navigation
    chatTutor: 'Chat Tutor',
    quiz: 'Quiz',
    progress: 'Progress',
    
    // Topics
    grammar: 'Grammar',
    vocabulary: 'Vocabulary',
    reading: 'Reading',
    listening: 'Listening',
    
    // Session
    currentSession: 'Current Session',
    level: 'Level',
    
    // Chat Interface
    typeMessage: 'Type your message...',
    send: 'Send',
    newSession: 'New Session',
    selectTopic: 'Select Topic',
    selectDifficulty: 'Select Difficulty',
    startSession: 'Start Session',
    
    // Quiz Interface
    startQuiz: 'Start Quiz',
    nextQuestion: 'Next Question',
    submitAnswer: 'Submit Answer',
    score: 'Score',
    correct: 'Correct',
    incorrect: 'Incorrect',
    
    // Progress Dashboard
    overallProgress: 'Overall Progress',
    weakAreas: 'Weak Areas',
    strengths: 'Strengths',
    sessionsCompleted: 'Sessions Completed',
    averageScore: 'Average Score',
    
    // Difficulty Levels
    beginner: 'Beginner (A1)',
    elementary: 'Elementary (A2)',
    intermediate: 'Intermediate (B1)',
    upperIntermediate: 'Upper Intermediate (B2)',
    advanced: 'Advanced (C1)',
    proficiency: 'Proficiency (C2)',
    
    // Common
    loading: 'Loading...',
    error: 'Error',
    retry: 'Retry',
    cancel: 'Cancel',
    save: 'Save',
    delete: 'Delete',
    edit: 'Edit',
    
    // Language Selector
    language: 'Language',
    english: 'English',
    italian: 'Italian',
  },
  
  it: {
    // Header
    appTitle: 'Tutor AI di Lingua Italiana',
    appSubtitle: 'Preparazione Esami',
    
    // Navigation
    chatTutor: 'Chat Tutor',
    quiz: 'Quiz',
    progress: 'Progresso',
    
    // Topics
    grammar: 'Grammatica',
    vocabulary: 'Vocabolario',
    reading: 'Lettura',
    listening: 'Ascolto',
    
    // Session
    currentSession: 'Sessione Corrente',
    level: 'Livello',
    
    // Chat Interface
    typeMessage: 'Scrivi il tuo messaggio...',
    send: 'Invia',
    newSession: 'Nuova Sessione',
    selectTopic: 'Seleziona Argomento',
    selectDifficulty: 'Seleziona Difficoltà',
    startSession: 'Inizia Sessione',
    
    // Quiz Interface
    startQuiz: 'Inizia Quiz',
    nextQuestion: 'Prossima Domanda',
    submitAnswer: 'Invia Risposta',
    score: 'Punteggio',
    correct: 'Corretto',
    incorrect: 'Sbagliato',
    
    // Progress Dashboard
    overallProgress: 'Progresso Generale',
    weakAreas: 'Aree Deboli',
    strengths: 'Punti di Forza',
    sessionsCompleted: 'Sessioni Completate',
    averageScore: 'Punteggio Medio',
    
    // Difficulty Levels
    beginner: 'Principiante (A1)',
    elementary: 'Elementare (A2)',
    intermediate: 'Intermedio (B1)',
    upperIntermediate: 'Intermedio Superiore (B2)',
    advanced: 'Avanzato (C1)',
    proficiency: 'Competenza (C2)',
    
    // Common
    loading: 'Caricamento...',
    error: 'Errore',
    retry: 'Riprova',
    cancel: 'Annulla',
    save: 'Salva',
    delete: 'Elimina',
    edit: 'Modifica',
    
    // Language Selector
    language: 'Lingua',
    english: 'Inglese',
    italian: 'Italiano',
  },
}

export function getTranslations(language: Language): Translations {
  return translations[language] || translations.en
}

export function formatDifficultyLevel(level: string, language: Language): string {
  const t = getTranslations(language)
  
  switch (level.toLowerCase()) {
    case 'a1':
      return t.beginner
    case 'a2':
      return t.elementary
    case 'b1':
      return t.intermediate
    case 'b2':
      return t.upperIntermediate
    case 'c1':
      return t.advanced
    case 'c2':
      return t.proficiency
    default:
      return level
  }
}