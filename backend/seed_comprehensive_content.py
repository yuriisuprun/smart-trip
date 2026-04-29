#!/usr/bin/env python3
"""
Startup script to seed comprehensive Italian grammar content
Run this after starting the application to populate the RAG system with B1-B2 content
"""

import asyncio
import logging
import sys
import os
from pathlib import Path

# Add the backend directory to Python path
backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    """Main function to seed comprehensive content"""
    try:
        logger.info("Starting comprehensive Italian grammar content seeding...")
        
        # Import after path setup
        from app.services.content_seeder import content_seeder
        from app.services.rag import rag_service
        
        # Ensure RAG service is initialized
        logger.info("Initializing RAG service...")
        
        # Seed comprehensive grammar content
        logger.info("Seeding comprehensive B1-B2 Italian grammar content...")
        results = content_seeder.seed_comprehensive_grammar_content()
        
        logger.info("Content seeding completed successfully!")
        logger.info(f"Results: {results}")
        
        # Print statistics
        stats = content_seeder.get_content_statistics()
        logger.info("Content Statistics:")
        logger.info(f"  Total Grammar Rules: {stats['total_grammar_rules']}")
        logger.info(f"  Total Exercises: {stats['total_exercises']}")
        logger.info(f"  Total Documents: {stats['total_documents']}")
        logger.info(f"  Content Version: {stats['content_version']}")
        
        logger.info("CEFR Level Distribution:")
        for level, counts in stats['cefr_level_distribution'].items():
            if counts['grammar_rules'] > 0 or counts['exercises'] > 0:
                logger.info(f"  {level}: {counts['grammar_rules']} grammar rules, {counts['exercises']} exercises")
        
        logger.info("Available Topics:")
        for topic in stats['available_topics']:
            logger.info(f"  - {topic}")
        
        return True
        
    except Exception as e:
        logger.error(f"Error during content seeding: {e}")
        return False

def seed_by_level(cefr_level: str):
    """Seed content for a specific CEFR level"""
    try:
        logger.info(f"Seeding content for CEFR level: {cefr_level}")
        
        from app.services.content_seeder import content_seeder
        
        results = content_seeder.seed_by_cefr_level(cefr_level)
        logger.info(f"CEFR {cefr_level} seeding completed: {results}")
        
        return True
        
    except Exception as e:
        logger.error(f"Error seeding CEFR {cefr_level} content: {e}")
        return False

def seed_by_topic(topic: str):
    """Seed content for a specific topic"""
    try:
        logger.info(f"Seeding content for topic: {topic}")
        
        from app.services.content_seeder import content_seeder
        
        results = content_seeder.seed_by_topic(topic)
        logger.info(f"Topic {topic} seeding completed: {results}")
        
        return True
        
    except Exception as e:
        logger.error(f"Error seeding topic {topic} content: {e}")
        return False

def show_statistics():
    """Show content statistics"""
    try:
        from app.services.content_seeder import content_seeder
        
        stats = content_seeder.get_content_statistics()
        
        print("\n" + "="*60)
        print("ITALIAN GRAMMAR CONTENT STATISTICS")
        print("="*60)
        print(f"Content Version: {stats['content_version']}")
        print(f"Last Updated: {stats['last_updated']}")
        print(f"Total Grammar Rules: {stats['total_grammar_rules']}")
        print(f"Total Exercises: {stats['total_exercises']}")
        print(f"Total Documents: {stats['total_documents']}")
        
        print("\nCEFR Level Distribution:")
        print("-" * 30)
        for level, counts in stats['cefr_level_distribution'].items():
            if counts['grammar_rules'] > 0 or counts['exercises'] > 0:
                print(f"{level:4}: {counts['grammar_rules']:3} grammar rules, {counts['exercises']:3} exercises")
        
        print("\nTopic Distribution:")
        print("-" * 30)
        for topic, counts in stats['topic_distribution'].items():
            if counts['grammar_rules'] > 0:
                print(f"{topic:25}: {counts['grammar_rules']:3} grammar rules")
        
        print("\nAvailable Topics:")
        print("-" * 30)
        for i, topic in enumerate(stats['available_topics'], 1):
            print(f"{i:2}. {topic}")
        
        print("="*60)
        
        return True
        
    except Exception as e:
        logger.error(f"Error getting statistics: {e}")
        return False

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Seed comprehensive Italian grammar content")
    parser.add_argument("--level", help="Seed content for specific CEFR level (A1, A2, B1, B2, C1, C2)")
    parser.add_argument("--topic", help="Seed content for specific topic")
    parser.add_argument("--stats", action="store_true", help="Show content statistics")
    parser.add_argument("--all", action="store_true", help="Seed all comprehensive content (default)")
    
    args = parser.parse_args()
    
    success = False
    
    if args.stats:
        success = show_statistics()
    elif args.level:
        valid_levels = ["A1", "A2", "B1", "B2", "C1", "C2"]
        if args.level in valid_levels:
            success = seed_by_level(args.level)
        else:
            logger.error(f"Invalid CEFR level. Must be one of: {valid_levels}")
    elif args.topic:
        success = seed_by_topic(args.topic)
    else:
        # Default: seed all content
        success = asyncio.run(main())
    
    if success:
        logger.info("Script completed successfully!")
        sys.exit(0)
    else:
        logger.error("Script failed!")
        sys.exit(1)