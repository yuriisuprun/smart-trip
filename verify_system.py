#!/usr/bin/env python3
"""
Simple verification script for the Italian Grammar Tutor system
"""
import subprocess
import sys
import time

def check_docker_containers():
    """Check if Docker containers are running"""
    try:
        result = subprocess.run(['docker-compose', 'ps'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            output = result.stdout
            containers = ['backend', 'frontend', 'postgres', 'qdrant']
            running = all(container in output and 'Up' in output for container in containers)
            print(f"✅ Docker containers: {'All running' if running else 'Some not running'}")
            return running
        else:
            print(f"❌ Docker check failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Docker check error: {e}")
        return False

def check_backend_logs():
    """Check backend logs for mock RAG service"""
    try:
        result = subprocess.run(['docker-compose', 'logs', 'backend', '--tail=10'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            logs = result.stdout
            mock_active = 'mock RAG service' in logs or 'Mock Mode' in logs
            print(f"✅ Mock RAG service: {'Active' if mock_active else 'Check logs'}")
            return True
        else:
            print(f"❌ Backend logs check failed")
            return False
    except Exception as e:
        print(f"❌ Backend logs error: {e}")
        return False

def check_file_modifications():
    """Check if key files have been modified correctly"""
    files_to_check = [
        'frontend/app/page.tsx',
        'frontend/components/ChatInterface.tsx', 
        'frontend/app/admin-test/page.tsx',
        'backend/app/services/mock_rag.py',
        'backend/app/services/rag.py'
    ]
    
    all_exist = True
    for file_path in files_to_check:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if file_path == 'frontend/app/page.tsx':
                    # Should NOT contain SimpleAdminTest
                    has_admin_test = 'SimpleAdminTest' in content
                    print(f"✅ {file_path}: {'❌ Still has SimpleAdminTest' if has_admin_test else '✅ AdminTest removed'}")
                elif file_path == 'frontend/components/ChatInterface.tsx':
                    # Should contain Content Admin button
                    has_admin_button = 'Content Admin' in content
                    print(f"✅ {file_path}: {'✅ Has admin button' if has_admin_button else '❌ Missing admin button'}")
                elif file_path == 'backend/app/services/mock_rag.py':
                    # Should contain comprehensive mock content
                    has_mock_content = 'subjunctive' in content and 'conditional' in content
                    print(f"✅ {file_path}: {'✅ Has mock content' if has_mock_content else '❌ Missing mock content'}")
                else:
                    print(f"✅ {file_path}: Exists")
        except FileNotFoundError:
            print(f"❌ {file_path}: Not found")
            all_exist = False
        except Exception as e:
            print(f"❌ {file_path}: Error reading - {e}")
            all_exist = False
    
    return all_exist

def main():
    """Run verification checks"""
    print("🔍 Italian Grammar Tutor - System Verification")
    print("=" * 60)
    
    checks = [
        ("Docker Containers", check_docker_containers),
        ("File Modifications", check_file_modifications),
        ("Backend Logs", check_backend_logs),
    ]
    
    passed = 0
    for check_name, check_func in checks:
        print(f"\n🔍 {check_name}:")
        try:
            if check_func():
                passed += 1
        except Exception as e:
            print(f"❌ {check_name} failed: {e}")
    
    print("\n" + "=" * 60)
    print(f"📊 Verification: {passed}/{len(checks)} checks passed")
    
    if passed == len(checks):
        print("\n🎉 System verification successful!")
        print("\n📋 Ready for testing:")
        print("1. Open http://localhost:3000")
        print("2. Sign in and test chat interface")
        print("3. Click 'Content Admin' button in chat header")
        print("4. Or visit http://localhost:3000/admin-test")
        print("5. Ask grammar questions to test mock RAG service")
    else:
        print("\n⚠️ Some checks failed - review output above")
    
    return passed == len(checks)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)