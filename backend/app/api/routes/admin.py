"""
Admin endpoints for seeding content
"""
import logging
import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.rag import rag_service
from app.services.content_seeder import content_seeder

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/seed-comprehensive-content")
async def seed_comprehensive_content():
    """Seed comprehensive B1-B2 Italian grammar content (500+ rules)"""
    try:
        logger.info("Starting comprehensive content seeding...")
        results = content_seeder.seed_comprehensive_grammar_content()
        
        return {
            "message": "Comprehensive Italian grammar content seeded successfully",
            "results": results
        }
    except Exception as e:
        logger.error(f"Error seeding comprehensive content: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/seed-by-cefr-level/{cefr_level}")
async def seed_by_cefr_level(cefr_level: str):
    """Seed content filtered by CEFR level (A1, A2, B1, B2, C1, C2)"""
    try:
        valid_levels = ["A1", "A2", "B1", "B2", "C1", "C2"]
        if cefr_level not in valid_levels:
            raise HTTPException(
                status_code=400, 
                detail=f"Invalid CEFR level. Must be one of: {valid_levels}"
            )
        
        logger.info(f"Seeding content for CEFR level: {cefr_level}")
        results = content_seeder.seed_by_cefr_level(cefr_level)
        
        return {
            "message": f"Content for CEFR level {cefr_level} seeded successfully",
            "results": results
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error seeding CEFR {cefr_level} content: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/seed-by-topic/{topic}")
async def seed_by_topic(topic: str):
    """Seed content filtered by grammar topic"""
    try:
        logger.info(f"Seeding content for topic: {topic}")
        results = content_seeder.seed_by_topic(topic)
        
        return {
            "message": f"Content for topic '{topic}' seeded successfully",
            "results": results
        }
    except Exception as e:
        logger.error(f"Error seeding topic {topic} content: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/update-content-version/{version}")
async def update_content_version(version: str):
    """Update content version and re-seed all content"""
    try:
        logger.info(f"Updating content version to: {version}")
        results = content_seeder.update_content_version(version)
        
        return {
            "message": f"Content version updated to {version} and re-seeded successfully",
            "results": results
        }
    except Exception as e:
        logger.error(f"Error updating content version: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/content-statistics")
async def get_content_statistics():
    """Get statistics about the seeded content"""
    try:
        stats = content_seeder.get_content_statistics()
        return {
            "message": "Content statistics retrieved successfully",
            "statistics": stats
        }
    except Exception as e:
        logger.error(f"Error getting content statistics: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# Legacy endpoints for backward compatibility
@router.post("/seed-content")
async def seed_basic_content():
    """Legacy endpoint - now redirects to comprehensive content seeding"""
    return await seed_comprehensive_content()


@router.post("/seed-exams")
async def seed_exam_content():
    """Seed exam-specific content (exercises and quizzes)"""
    try:
        logger.info("Seeding exam content...")
        
        # Import here to avoid circular imports
        import sys
        import os
        sys.path.append(os.path.join(os.path.dirname(__file__), '../../../content'))
        
        from italian_exercises_b1_b2 import italian_grammar_exercises
        
        # Seed only exercises from the comprehensive content
        results = {
            "exercises": 0,
            "total_documents": 0,
            "errors": []
        }
        
        exercises = italian_grammar_exercises.get_all_exercises()
        
        for doc_id, exercise_data in exercises.items():
            try:
                rag_service.add_document(
                    doc_id=f"exam_{doc_id}",
                    content=exercise_data["content"],
                    metadata={
                        **exercise_data["metadata"],
                        "content_version": content_seeder.content_version,
                        "last_updated": content_seeder.last_updated,
                        "content_type": "exam_exercise",
                        "language": "italian",
                        "source": "exam_content"
                    }
                )
                results["exercises"] += 1
            except Exception as e:
                logger.error(f"Error seeding exam exercise {doc_id}: {e}")
                results["errors"].append(f"Exam {doc_id}: {str(e)}")
        
        results["total_documents"] = results["exercises"]
        
        return {
            "message": "Exam content seeded successfully",
            "results": results
        }
    except Exception as e:
        logger.error(f"Error seeding exam content: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/seed-all")
async def seed_all_content():
    """Seed all available content (comprehensive + exams)"""
    try:
        logger.info("Seeding all content...")
        
        # Seed comprehensive content
        comprehensive_results = content_seeder.seed_comprehensive_grammar_content()
        
        # Seed additional exam content
        exam_response = await seed_exam_content()
        exam_results = exam_response["results"]
        
        # Combine results
        total_results = {
            "grammar_content": comprehensive_results["grammar_content"],
            "exercises": comprehensive_results["exercises"] + exam_results["exercises"],
            "total_documents": comprehensive_results["total_documents"] + exam_results["total_documents"],
            "errors": comprehensive_results["errors"] + exam_results["errors"]
        }
        
        return {
            "message": "All content seeded successfully",
            "results": total_results
        }
    except Exception as e:
        logger.error(f"Error seeding all content: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# Legacy content for backward compatibility
GRAMMAR_CONTENT = {
    "present_tense": {
        "content": """
        Italian Present Tense (Presente Indicativo)
        
        Regular verbs are divided into three conjugations:
        1st conjugation: -ARE verbs (parlare - to speak)
        2nd conjugation: -ERE verbs (leggere - to read)
        3rd conjugation: -IRE verbs (partire - to leave)
        
        Parlare (to speak):
        io parlo - I speak
        tu parli - you speak
        lui/lei parla - he/she speaks
        noi parliamo - we speak
        voi parlate - you all speak
        loro parlano - they speak
        
        Common regular verbs:
        - abitare (to live)
        - amare (to love)
        - cantare (to sing)
        - leggere (to read)
        - scrivere (to write)
        - partire (to leave)
        - dormire (to sleep)
        """,
        "metadata": {
            "topic": "grammar",
            "subtopic": "verb_conjugation",
            "cefr_level": "A2",
            "difficulty": 1,
        },
    },
    "past_tense": {
        "content": """
        Italian Past Tense (Passato Prossimo)
        
        The passato prossimo is formed with:
        - Present tense of avere or essere + past participle
        
        Most verbs use avere:
        ho parlato - I spoke
        hai parlato - you spoke
        ha parlato - he/she spoke
        abbiamo parlato - we spoke
        avete parlato - you all spoke
        hanno parlato - they spoke
        
        Verbs of movement use essere:
        sono andato/a - I went
        sei andato/a - you went
        è andato/a - he/she went
        siamo andati/e - we went
        siete andati/e - you all went
        sono andati/e - they went
        
        Past participles:
        -ARE verbs: -ato (parlato, cantato)
        -ERE verbs: -uto (venduto, creduto)
        -IRE verbs: -ito (partito, dormito)
        """,
        "metadata": {
            "topic": "grammar",
            "subtopic": "past_tense",
            "cefr_level": "A2",
            "difficulty": 2,
        },
    },
    "gender_agreement": {
        "content": """
        Italian Gender and Agreement
        
        All Italian nouns are either masculine or feminine.
        
        Masculine articles:
        - il (the) - before consonants
        - lo (the) - before s+consonant, z, gn, ps
        - l' (the) - before vowels
        
        Feminine articles:
        - la (the) - before consonants
        - l' (the) - before vowels
        
        Adjectives must agree with the noun:
        - Masculine singular: -o (bello)
        - Feminine singular: -a (bella)
        - Masculine plural: -i (belli)
        - Feminine plural: -e (belle)
        
        Examples:
        il ragazzo bello - the handsome boy
        la ragazza bella - the beautiful girl
        i ragazzi belli - the handsome boys
        le ragazze belle - the beautiful girls
        """,
        "metadata": {
            "topic": "grammar",
            "subtopic": "gender_agreement",
            "cefr_level": "A1",
            "difficulty": 1,
        },
    },
}

# Sample exam questions
EXAM_QUESTIONS = {
    "q1": {
        "content": """
        Prefettura Exam Question - Grammar
        
        Question: Completa la frase con il verbo corretto.
        "Ieri io _____ al cinema con i miei amici."
        
        A) vado
        B) sono andato
        C) andrò
        D) andrei
        
        Correct Answer: B) sono andato
        Explanation: This requires passato prossimo (past tense) because the action happened yesterday.
        The verb "andare" (to go) uses "essere" as auxiliary, so: sono andato.
        """,
        "metadata": {
            "topic": "exam",
            "question_type": "multiple_choice",
            "cefr_level": "A2",
            "skill": "grammar",
        },
    },
    "q2": {
        "content": """
        Prefettura Exam Question - Vocabulary
        
        Question: Quale parola significa "to understand"?
        
        A) capire
        B) parlare
        C) leggere
        D) scrivere
        
        Correct Answer: A) capire
        Explanation: "Capire" means "to understand". The other options mean:
        - parlare: to speak
        - leggere: to read
        - scrivere: to write
        """,
        "metadata": {
            "topic": "exam",
            "question_type": "multiple_choice",
            "cefr_level": "A1",
            "skill": "vocabulary",
        },
    },
}