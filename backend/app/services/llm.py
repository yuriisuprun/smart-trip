"""
LLM service for AI tutoring
"""
import logging
import json
from typing import Optional, Dict, List, AsyncGenerator
from openai import AsyncOpenAI
from app.core.config import settings
from app.services.language import language_service, Language

logger = logging.getLogger(__name__)


class LLMService:
    """LLM service for tutoring interactions"""

    def __init__(self):
        """Initialize LLM service"""
        self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.OPENAI_MODEL

    async def chat_stream(
        self,
        messages: List[Dict],
        system_prompt: str,
        temperature: float = settings.LLM_TEMPERATURE,
        max_tokens: int = settings.LLM_MAX_TOKENS,
    ) -> AsyncGenerator[str, None]:
        """Stream chat response"""
        try:
            full_messages = [
                {"role": "system", "content": system_prompt},
                *messages,
            ]

            stream = await self.client.chat.completions.create(
                model=self.model,
                messages=full_messages,
                temperature=temperature,
                max_tokens=max_tokens,
                stream=True,
            )

            async for chunk in stream:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content

        except Exception as e:
            logger.error(f"Error in chat stream: {e}")
            yield f"Error: {str(e)}"

    async def evaluate_answer(
        self,
        question: str,
        user_answer: str,
        correct_answer: Optional[str] = None,
        context: Optional[str] = None,
        language: str = "en",
    ) -> Dict:
        """Evaluate a student's answer"""
        
        # Validate and convert language
        if not language_service.is_supported_language(language):
            language = settings.DEFAULT_LANGUAGE
        
        lang = Language(language)
        
        # Build context strings
        correct_answer_str = f'Correct Answer: {correct_answer}' if correct_answer else ''
        context_str = f'Context: {context}' if context else ''
        
        prompt = language_service.get_system_prompt(
            language=lang,
            prompt_type="evaluation",
            question=question,
            user_answer=user_answer,
            correct_answer=correct_answer_str,
            context=context_str
        )

        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=1000,
            )

            response_text = response.choices[0].message.content
            # Extract JSON from response
            try:
                result = json.loads(response_text)
            except json.JSONDecodeError:
                # Try to extract JSON from text
                import re
                json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
                if json_match:
                    result = json.loads(json_match.group())
                else:
                    error_msg = language_service.get_message(lang, "error")
                    result = {
                        "score": 5,
                        "is_correct": False,
                        "corrections": [],
                        "explanation": response_text or error_msg,
                        "improvement_suggestions": [],
                        "grammar_errors": [],
                    }

            return result

        except Exception as e:
            logger.error(f"Error evaluating answer: {e}")
            error_msg = language_service.get_message(Language(language), "error")
            return {
                "score": 0,
                "is_correct": False,
                "corrections": [],
                "explanation": f"{error_msg}: {str(e)}",
                "improvement_suggestions": [],
                "grammar_errors": [],
            }

    async def generate_tutoring_response(
        self,
        user_message: str,
        topic: str,
        difficulty: str,
        short_term_memory: List[Dict],
        long_term_memory: Dict,
        retrieved_context: List[Dict],
        language: str = "en",
    ) -> str:
        """Generate a tutoring response with step-by-step guidance"""

        # Validate and convert language
        if not language_service.is_supported_language(language):
            language = settings.DEFAULT_LANGUAGE
        
        lang = Language(language)

        # Build context
        context_str = ""
        if retrieved_context:
            context_str = "\n\nRelevant Learning Material:\n"
            for item in retrieved_context[:3]:
                context_str += f"- {item['content'][:200]}...\n"

        weak_areas_str = ""
        if long_term_memory.get("weak_areas"):
            weak_areas_str = f"\nStudent's weak areas: {', '.join(long_term_memory['weak_areas'].keys())}"

        # Translate topic and difficulty for display
        translated_topic = language_service.translate_topic(topic, lang)
        translated_difficulty = language_service.translate_difficulty(difficulty, lang)

        system_prompt = language_service.get_system_prompt(
            language=lang,
            prompt_type="tutor_base",
            difficulty=translated_difficulty,
            cefr_level=long_term_memory.get('cefr_level', difficulty),
            topic=translated_topic,
            accuracy=long_term_memory.get('total_score', 0),
            weak_areas=weak_areas_str,
            context=context_str
        )

        messages = [
            {"role": msg["role"], "content": msg["content"]}
            for msg in short_term_memory[-10:]  # Last 10 messages
        ]
        messages.append({"role": "user", "content": user_message})

        response = ""
        async for chunk in self.chat_stream(
            messages=messages[:-1],  # Exclude the last user message from history
            system_prompt=system_prompt,
        ):
            response += chunk

        return response


# Global LLM service instance
llm_service = LLMService()
