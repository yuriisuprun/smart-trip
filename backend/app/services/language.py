"""
Language service for internationalization
"""
from typing import Dict, Any
from enum import Enum


class Language(str, Enum):
    """Supported languages"""
    ENGLISH = "en"
    ITALIAN = "it"


class LanguageService:
    """Service for handling language-specific content and prompts"""

    def __init__(self):
        self.translations = {
            Language.ENGLISH: {
                "system_prompts": {
                    "tutor_base": """You are an expert Italian language tutor for the Prefettura di Milano exam (CEFR {difficulty} level).

TUTORING PRINCIPLES:
1. NEVER give direct answers - guide the student through reasoning
2. Provide: explanation → guided questions → hints → final answer only if needed
3. Adapt to the student's level and weak areas
4. Be encouraging and supportive
5. Correct mistakes with clear explanations
6. Reference past mistakes to help learning

STUDENT PROFILE:
- CEFR Level: {cefr_level}
- Topic: {topic}
- Accuracy: {accuracy}%{weak_areas}

{context}

Respond in English, but use Italian examples when relevant. Be conversational and supportive.""",
                    
                    "evaluation": """You are an expert Italian language tutor evaluating a student's answer.

Question: {question}
Student's Answer: {user_answer}
{correct_answer}
{context}

Provide evaluation in JSON format:
{{
    "score": <0-10>,
    "is_correct": <true/false>,
    "corrections": [<list of corrections>],
    "explanation": "<detailed explanation in English>",
    "improvement_suggestions": [<list of suggestions in English>],
    "grammar_errors": [
        {{"error": "<error>", "correction": "<correction>", "explanation": "<why in English>"}}
    ]
}}

Be encouraging but honest. Focus on learning, not just correctness."""
                },
                "messages": {
                    "welcome": "Welcome! I'm your Italian language tutor. How can I help you today?",
                    "session_started": "Great! Let's start working on {topic} at {difficulty} level.",
                    "error": "I'm sorry, there was an error processing your request. Please try again.",
                    "loading": "Processing your request...",
                }
            },
            
            Language.ITALIAN: {
                "system_prompts": {
                    "tutor_base": """Sei un esperto tutor di lingua italiana per l'esame della Prefettura di Milano (livello CEFR {difficulty}).

PRINCIPI DI TUTORAGGIO:
1. NON dare mai risposte dirette - guida lo studente attraverso il ragionamento
2. Fornisci: spiegazione → domande guidate → suggerimenti → risposta finale solo se necessario
3. Adattati al livello dello studente e alle aree deboli
4. Sii incoraggiante e di supporto
5. Correggi gli errori con spiegazioni chiare
6. Fai riferimento agli errori passati per aiutare l'apprendimento

PROFILO STUDENTE:
- Livello CEFR: {cefr_level}
- Argomento: {topic}
- Precisione: {accuracy}%{weak_areas}

{context}

Rispondi in italiano in modo conversazionale e di supporto.""",
                    
                    "evaluation": """Sei un esperto tutor di lingua italiana che valuta la risposta di uno studente.

Domanda: {question}
Risposta dello Studente: {user_answer}
{correct_answer}
{context}

Fornisci la valutazione in formato JSON:
{{
    "score": <0-10>,
    "is_correct": <true/false>,
    "corrections": [<lista di correzioni>],
    "explanation": "<spiegazione dettagliata in italiano>",
    "improvement_suggestions": [<lista di suggerimenti in italiano>],
    "grammar_errors": [
        {{"error": "<errore>", "correction": "<correzione>", "explanation": "<perché in italiano>"}}
    ]
}}

Sii incoraggiante ma onesto. Concentrati sull'apprendimento, non solo sulla correttezza."""
                },
                "messages": {
                    "welcome": "Benvenuto! Sono il tuo tutor di lingua italiana. Come posso aiutarti oggi?",
                    "session_started": "Perfetto! Iniziamo a lavorare su {topic} al livello {difficulty}.",
                    "error": "Mi dispiace, c'è stato un errore nell'elaborazione della tua richiesta. Riprova per favore.",
                    "loading": "Elaborazione della tua richiesta...",
                }
            }
        }

    def get_system_prompt(
        self, 
        language: Language, 
        prompt_type: str, 
        **kwargs
    ) -> str:
        """Get a system prompt in the specified language"""
        try:
            template = self.translations[language]["system_prompts"][prompt_type]
            return template.format(**kwargs)
        except KeyError:
            # Fallback to English if translation not found
            template = self.translations[Language.ENGLISH]["system_prompts"][prompt_type]
            return template.format(**kwargs)

    def get_message(
        self, 
        language: Language, 
        message_key: str, 
        **kwargs
    ) -> str:
        """Get a message in the specified language"""
        try:
            template = self.translations[language]["messages"][message_key]
            return template.format(**kwargs)
        except KeyError:
            # Fallback to English if translation not found
            template = self.translations[Language.ENGLISH]["messages"][message_key]
            return template.format(**kwargs)

    def translate_topic(self, topic: str, language: Language) -> str:
        """Translate topic names"""
        topic_translations = {
            Language.ENGLISH: {
                "grammar": "Grammar",
                "vocabulary": "Vocabulary", 
                "reading": "Reading",
                "listening": "Listening",
                "writing": "Writing",
                "speaking": "Speaking"
            },
            Language.ITALIAN: {
                "grammar": "Grammatica",
                "vocabulary": "Vocabolario",
                "reading": "Lettura", 
                "listening": "Ascolto",
                "writing": "Scrittura",
                "speaking": "Conversazione"
            }
        }
        
        return topic_translations.get(language, {}).get(topic, topic)

    def translate_difficulty(self, difficulty: str, language: Language) -> str:
        """Translate difficulty levels"""
        difficulty_translations = {
            Language.ENGLISH: {
                "A1": "Beginner (A1)",
                "A2": "Elementary (A2)", 
                "B1": "Intermediate (B1)",
                "B2": "Upper Intermediate (B2)",
                "C1": "Advanced (C1)",
                "C2": "Proficiency (C2)"
            },
            Language.ITALIAN: {
                "A1": "Principiante (A1)",
                "A2": "Elementare (A2)",
                "B1": "Intermedio (B1)", 
                "B2": "Intermedio Superiore (B2)",
                "C1": "Avanzato (C1)",
                "C2": "Competenza (C2)"
            }
        }
        
        return difficulty_translations.get(language, {}).get(difficulty, difficulty)

    def is_supported_language(self, language: str) -> bool:
        """Check if a language is supported"""
        try:
            Language(language)
            return True
        except ValueError:
            return False


# Global language service instance
language_service = LanguageService()