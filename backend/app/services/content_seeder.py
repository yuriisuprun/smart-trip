"""
Content seeding service for Italian grammar B1-B2 content
Handles loading, versioning, and categorization of grammar content
"""

import logging
import uuid
from typing import Dict, List, Any, Optional
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.rag import rag_service

# Import the comprehensive grammar content
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../content'))

from italian_grammar_b1_b2 import italian_grammar_b1_b2
from italian_grammar_b1_b2_part2 import italian_grammar_b1_b2_part2
from italian_exercises_b1_b2 import italian_grammar_exercises

logger = logging.getLogger(__name__)

class ContentSeeder:
    """Service for seeding comprehensive Italian grammar content"""
    
    def __init__(self):
        self.content_version = "2.0.0"
        self.last_updated = datetime.now(timezone.utc).isoformat()
    
    def seed_comprehensive_grammar_content(self) -> Dict[str, Any]:
        """Seed all comprehensive B1-B2 Italian grammar content"""
        try:
            results = {
                "grammar_content": 0,
                "exercises": 0,
                "total_documents": 0,
                "errors": []
            }
            
            # Seed main grammar content (Part 1)
            grammar_content_1 = italian_grammar_b1_b2.get_all_content()
            for doc_id, content_data in grammar_content_1.items():
                try:
                    self._seed_document(
                        doc_id=f"grammar_b1_b2_{doc_id}",
                        content=content_data["content"],
                        metadata={
                            **content_data["metadata"],
                            "content_version": self.content_version,
                            "last_updated": self.last_updated,
                            "content_type": "grammar_rule",
                            "language": "italian",
                            "source": "comprehensive_b1_b2_part1"
                        }
                    )
                    results["grammar_content"] += 1
                except Exception as e:
                    logger.error(f"Error seeding grammar content {doc_id}: {e}")
                    results["errors"].append(f"Grammar {doc_id}: {str(e)}")
            
            # Seed additional grammar content (Part 2)
            grammar_content_2 = italian_grammar_b1_b2_part2.get_all_content()
            for doc_id, content_data in grammar_content_2.items():
                try:
                    self._seed_document(
                        doc_id=f"grammar_b1_b2_part2_{doc_id}",
                        content=content_data["content"],
                        metadata={
                            **content_data["metadata"],
                            "content_version": self.content_version,
                            "last_updated": self.last_updated,
                            "content_type": "grammar_rule",
                            "language": "italian",
                            "source": "comprehensive_b1_b2_part2"
                        }
                    )
                    results["grammar_content"] += 1
                except Exception as e:
                    logger.error(f"Error seeding grammar content part 2 {doc_id}: {e}")
                    results["errors"].append(f"Grammar Part 2 {doc_id}: {str(e)}")
            
            # Seed exercises
            exercises = italian_grammar_exercises.get_all_exercises()
            for doc_id, exercise_data in exercises.items():
                try:
                    self._seed_document(
                        doc_id=f"exercise_b1_b2_{doc_id}",
                        content=exercise_data["content"],
                        metadata={
                            **exercise_data["metadata"],
                            "content_version": self.content_version,
                            "last_updated": self.last_updated,
                            "content_type": "exercise",
                            "language": "italian",
                            "source": "comprehensive_b1_b2_exercises"
                        }
                    )
                    results["exercises"] += 1
                except Exception as e:
                    logger.error(f"Error seeding exercise {doc_id}: {e}")
                    results["errors"].append(f"Exercise {doc_id}: {str(e)}")
            
            results["total_documents"] = results["grammar_content"] + results["exercises"]
            
            logger.info(f"Content seeding completed: {results}")
            return results
            
        except Exception as e:
            logger.error(f"Error in comprehensive content seeding: {e}")
            raise
    
    def seed_by_cefr_level(self, cefr_level: str) -> Dict[str, Any]:
        """Seed content filtered by CEFR level"""
        try:
            results = {
                "grammar_content": 0,
                "exercises": 0,
                "total_documents": 0,
                "cefr_level": cefr_level,
                "errors": []
            }
            
            # Filter and seed grammar content by CEFR level
            grammar_content_1 = italian_grammar_b1_b2.get_by_cefr_level(cefr_level)
            grammar_content_2 = italian_grammar_b1_b2_part2.get_by_cefr_level(cefr_level)
            exercises = italian_grammar_exercises.get_by_cefr_level(cefr_level)
            
            # Combine all content
            all_content = {
                **{f"grammar_part1_{k}": v for k, v in grammar_content_1.items()},
                **{f"grammar_part2_{k}": v for k, v in grammar_content_2.items()},
                **{f"exercise_{k}": v for k, v in exercises.items()}
            }
            
            for doc_id, content_data in all_content.items():
                try:
                    self._seed_document(
                        doc_id=f"{cefr_level}_{doc_id}",
                        content=content_data["content"],
                        metadata={
                            **content_data["metadata"],
                            "content_version": self.content_version,
                            "last_updated": self.last_updated,
                            "content_type": content_data["metadata"].get("question_type", "grammar_rule"),
                            "language": "italian",
                            "source": f"comprehensive_b1_b2_{cefr_level}"
                        }
                    )
                    
                    if "exercise" in doc_id:
                        results["exercises"] += 1
                    else:
                        results["grammar_content"] += 1
                        
                except Exception as e:
                    logger.error(f"Error seeding {cefr_level} content {doc_id}: {e}")
                    results["errors"].append(f"{cefr_level} {doc_id}: {str(e)}")
            
            results["total_documents"] = results["grammar_content"] + results["exercises"]
            
            logger.info(f"CEFR {cefr_level} content seeding completed: {results}")
            return results
            
        except Exception as e:
            logger.error(f"Error seeding CEFR {cefr_level} content: {e}")
            raise
    
    def seed_by_topic(self, topic: str) -> Dict[str, Any]:
        """Seed content filtered by grammar topic"""
        try:
            results = {
                "grammar_content": 0,
                "exercises": 0,
                "total_documents": 0,
                "topic": topic,
                "errors": []
            }
            
            # Filter content by topic
            grammar_content_1 = italian_grammar_b1_b2.get_by_topic(topic)
            grammar_content_2 = italian_grammar_b1_b2_part2.get_by_topic(topic)
            
            # Combine content
            all_content = {
                **{f"grammar_part1_{k}": v for k, v in grammar_content_1.items()},
                **{f"grammar_part2_{k}": v for k, v in grammar_content_2.items()}
            }
            
            for doc_id, content_data in all_content.items():
                try:
                    self._seed_document(
                        doc_id=f"topic_{topic}_{doc_id}",
                        content=content_data["content"],
                        metadata={
                            **content_data["metadata"],
                            "content_version": self.content_version,
                            "last_updated": self.last_updated,
                            "content_type": "grammar_rule",
                            "language": "italian",
                            "source": f"comprehensive_b1_b2_topic_{topic}"
                        }
                    )
                    results["grammar_content"] += 1
                except Exception as e:
                    logger.error(f"Error seeding topic {topic} content {doc_id}: {e}")
                    results["errors"].append(f"Topic {topic} {doc_id}: {str(e)}")
            
            results["total_documents"] = results["grammar_content"]
            
            logger.info(f"Topic {topic} content seeding completed: {results}")
            return results
            
        except Exception as e:
            logger.error(f"Error seeding topic {topic} content: {e}")
            raise
    
    def update_content_version(self, new_version: str) -> Dict[str, Any]:
        """Update content version and re-seed all content"""
        try:
            old_version = self.content_version
            self.content_version = new_version
            self.last_updated = datetime.now(timezone.utc).isoformat()
            
            # Re-seed all content with new version
            results = self.seed_comprehensive_grammar_content()
            results["version_update"] = {
                "old_version": old_version,
                "new_version": new_version,
                "updated_at": self.last_updated
            }
            
            logger.info(f"Content version updated from {old_version} to {new_version}")
            return results
            
        except Exception as e:
            logger.error(f"Error updating content version: {e}")
            raise
    
    def get_content_statistics(self) -> Dict[str, Any]:
        """Get statistics about the seeded content"""
        try:
            # Get all content
            grammar_1 = italian_grammar_b1_b2.get_all_content()
            grammar_2 = italian_grammar_b1_b2_part2.get_all_content()
            exercises = italian_grammar_exercises.get_all_exercises()
            
            # Count by CEFR level
            cefr_stats = {}
            for level in ["A1", "A2", "B1", "B2", "C1", "C2"]:
                cefr_stats[level] = {
                    "grammar_rules": (
                        len(italian_grammar_b1_b2.get_by_cefr_level(level)) +
                        len(italian_grammar_b1_b2_part2.get_by_cefr_level(level))
                    ),
                    "exercises": len(italian_grammar_exercises.get_by_cefr_level(level))
                }
            
            # Count by topic
            all_topics = set()
            for content in [grammar_1, grammar_2]:
                for item in content.values():
                    all_topics.add(item["metadata"]["subtopic"])
            
            topic_stats = {}
            for topic in all_topics:
                topic_stats[topic] = {
                    "grammar_rules": (
                        len(italian_grammar_b1_b2.get_by_topic(topic)) +
                        len(italian_grammar_b1_b2_part2.get_by_topic(topic))
                    )
                }
            
            return {
                "total_grammar_rules": len(grammar_1) + len(grammar_2),
                "total_exercises": len(exercises),
                "total_documents": len(grammar_1) + len(grammar_2) + len(exercises),
                "content_version": self.content_version,
                "last_updated": self.last_updated,
                "cefr_level_distribution": cefr_stats,
                "topic_distribution": topic_stats,
                "available_topics": list(all_topics)
            }
            
        except Exception as e:
            logger.error(f"Error getting content statistics: {e}")
            raise
    
    def _seed_document(self, doc_id: str, content: str, metadata: Dict[str, Any]):
        """Seed a single document into the RAG system"""
        try:
            # Add document to RAG system with enhanced metadata
            rag_service.add_document(
                doc_id=doc_id,
                content=content,
                metadata=metadata,
                chunk_size=600  # Slightly larger chunks for grammar content
            )
            
            logger.debug(f"Successfully seeded document: {doc_id}")
            
        except Exception as e:
            logger.error(f"Error seeding document {doc_id}: {e}")
            raise

# Initialize the content seeder
content_seeder = ContentSeeder()