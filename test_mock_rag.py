#!/usr/bin/env python3
"""
Test script to verify the mock RAG service is working correctly
"""
import sys
import os
import requests
import json

def test_backend_health():
    """Test if backend is responding"""
    try:
        response = requests.get("http://localhost:8000/health", timeout=5)
        print(f"✅ Backend health check: {response.status_code}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Backend health check failed: {e}")
        return False

def test_admin_statistics():
    """Test admin statistics endpoint"""
    try:
        response = requests.get("http://localhost:8000/api/admin/content-statistics", timeout=10)
        print(f"✅ Admin statistics: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Mock content items: {data['statistics']['total_grammar_rules']}")
            print(f"   Content version: {data['statistics']['content_version']}")
            return True
        return False
    except Exception as e:
        print(f"❌ Admin statistics failed: {e}")
        return False

def test_content_seeding():
    """Test content seeding endpoint"""
    try:
        response = requests.post("http://localhost:8000/api/admin/seed-comprehensive-content", timeout=15)
        print(f"✅ Content seeding: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Seeded grammar rules: {data['results']['grammar_content']}")
            print(f"   Message: {data['message']}")
            return True
        return False
    except Exception as e:
        print(f"❌ Content seeding failed: {e}")
        return False

def test_frontend_accessibility():
    """Test if frontend is accessible"""
    try:
        response = requests.get("http://localhost:3000", timeout=5)
        print(f"✅ Frontend accessibility: {response.status_code}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Frontend accessibility failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing Italian Grammar Tutor System")
    print("=" * 50)
    
    tests = [
        ("Backend Health", test_backend_health),
        ("Frontend Accessibility", test_frontend_accessibility),
        ("Admin Statistics", test_admin_statistics),
        ("Content Seeding", test_content_seeding),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 Running: {test_name}")
        if test_func():
            passed += 1
        else:
            print(f"   ⚠️ {test_name} failed")
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The system is working correctly.")
        print("\n📋 Next Steps:")
        print("1. Open http://localhost:3000 in your browser")
        print("2. Sign in to access the chat interface")
        print("3. Click the 'Content Admin' button to access admin features")
        print("4. Or visit http://localhost:3000/admin-test for the dedicated admin page")
        print("5. Try asking grammar questions like 'How do I use the subjunctive mood?'")
    else:
        print("❌ Some tests failed. Check the logs above for details.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)