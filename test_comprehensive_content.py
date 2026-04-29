#!/usr/bin/env python3
"""
Test script for comprehensive Italian grammar content system
"""

import sys
import os
sys.path.append('./backend')
sys.path.append('./backend/content')

def test_content_loading():
    """Test that all content modules load correctly"""
    print("🧪 Testing Content Loading...")
    
    try:
        from backend.content.italian_grammar_b1_b2 import italian_grammar_b1_b2
        from backend.content.italian_grammar_b1_b2_part2 import italian_grammar_b1_b2_part2
        from backend.content.italian_exercises_b1_b2 import italian_grammar_exercises
        
        # Test Part 1 content
        content_1 = italian_grammar_b1_b2.get_all_content()
        print(f"✅ Part 1: {len(content_1)} grammar topics loaded")
        
        # Test Part 2 content
        content_2 = italian_grammar_b1_b2_part2.get_all_content()
        print(f"✅ Part 2: {len(content_2)} grammar topics loaded")
        
        # Test exercises
        exercises = italian_grammar_exercises.get_all_exercises()
        print(f"✅ Exercises: {len(exercises)} exercise sets loaded")
        
        total_content = len(content_1) + len(content_2) + len(exercises)
        print(f"📊 Total Content Items: {total_content}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error loading content: {e}")
        return False

def test_cefr_filtering():
    """Test CEFR level filtering functionality"""
    print("\n🎯 Testing CEFR Level Filtering...")
    
    try:
        from backend.content.italian_grammar_b1_b2 import italian_grammar_b1_b2
        from backend.content.italian_grammar_b1_b2_part2 import italian_grammar_b1_b2_part2
        from backend.content.italian_exercises_b1_b2 import italian_grammar_exercises
        
        # Test B1 level filtering
        b1_content_1 = italian_grammar_b1_b2.get_by_cefr_level("B1")
        b1_content_2 = italian_grammar_b1_b2_part2.get_by_cefr_level("B1")
        b1_exercises = italian_grammar_exercises.get_by_cefr_level("B1")
        
        print(f"✅ B1 Level - Grammar: {len(b1_content_1) + len(b1_content_2)}, Exercises: {len(b1_exercises)}")
        
        # Test B2 level filtering
        b2_content_1 = italian_grammar_b1_b2.get_by_cefr_level("B2")
        b2_content_2 = italian_grammar_b1_b2_part2.get_by_cefr_level("B2")
        b2_exercises = italian_grammar_exercises.get_by_cefr_level("B2")
        
        print(f"✅ B2 Level - Grammar: {len(b2_content_1) + len(b2_content_2)}, Exercises: {len(b2_exercises)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing CEFR filtering: {e}")
        return False

def test_topic_filtering():
    """Test topic-based filtering functionality"""
    print("\n📚 Testing Topic Filtering...")
    
    try:
        from backend.content.italian_grammar_b1_b2 import italian_grammar_b1_b2
        from backend.content.italian_grammar_b1_b2_part2 import italian_grammar_b1_b2_part2
        
        # Get all available topics
        all_content = {**italian_grammar_b1_b2.get_all_content(), **italian_grammar_b1_b2_part2.get_all_content()}
        topics = set()
        for content in all_content.values():
            topics.add(content["metadata"]["subtopic"])
        
        print(f"📋 Available Topics: {len(topics)}")
        for topic in sorted(topics):
            topic_content_1 = italian_grammar_b1_b2.get_by_topic(topic)
            topic_content_2 = italian_grammar_b1_b2_part2.get_by_topic(topic)
            total_topic_content = len(topic_content_1) + len(topic_content_2)
            if total_topic_content > 0:
                print(f"  - {topic}: {total_topic_content} items")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing topic filtering: {e}")
        return False

def test_content_structure():
    """Test content structure and metadata"""
    print("\n🏗️ Testing Content Structure...")
    
    try:
        from backend.content.italian_grammar_b1_b2 import italian_grammar_b1_b2
        
        content = italian_grammar_b1_b2.get_all_content()
        
        # Test first item structure
        first_key = list(content.keys())[0]
        first_item = content[first_key]
        
        # Check required fields
        required_fields = ["content", "metadata"]
        for field in required_fields:
            if field not in first_item:
                print(f"❌ Missing required field: {field}")
                return False
        
        # Check metadata structure
        metadata = first_item["metadata"]
        required_metadata = ["topic", "subtopic", "cefr_level", "difficulty", "skill"]
        for field in required_metadata:
            if field not in metadata:
                print(f"❌ Missing metadata field: {field}")
                return False
        
        print("✅ Content structure validation passed")
        print(f"📝 Sample content preview: {first_item['content'][:100]}...")
        print(f"🏷️ Sample metadata: {metadata}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing content structure: {e}")
        return False

def test_difficulty_filtering():
    """Test difficulty-based filtering"""
    print("\n⚡ Testing Difficulty Filtering...")
    
    try:
        from backend.content.italian_grammar_b1_b2 import italian_grammar_b1_b2
        from backend.content.italian_grammar_b1_b2_part2 import italian_grammar_b1_b2_part2
        
        # Test difficulty ranges
        easy_content_1 = italian_grammar_b1_b2.get_by_difficulty(1, 5)
        easy_content_2 = italian_grammar_b1_b2_part2.get_by_difficulty(1, 5)
        
        medium_content_1 = italian_grammar_b1_b2.get_by_difficulty(6, 7)
        medium_content_2 = italian_grammar_b1_b2_part2.get_by_difficulty(6, 7)
        
        hard_content_1 = italian_grammar_b1_b2.get_by_difficulty(8, 10)
        hard_content_2 = italian_grammar_b1_b2_part2.get_by_difficulty(8, 10)
        
        print(f"✅ Easy (1-5): {len(easy_content_1) + len(easy_content_2)} items")
        print(f"✅ Medium (6-7): {len(medium_content_1) + len(medium_content_2)} items")
        print(f"✅ Hard (8-10): {len(hard_content_1) + len(hard_content_2)} items")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing difficulty filtering: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Comprehensive Italian Grammar Content System Test")
    print("=" * 60)
    
    tests = [
        test_content_loading,
        test_cefr_filtering,
        test_topic_filtering,
        test_content_structure,
        test_difficulty_filtering
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        else:
            print("❌ Test failed!")
    
    print("\n" + "=" * 60)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The comprehensive content system is ready.")
        return True
    else:
        print("⚠️ Some tests failed. Please check the implementation.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)