@echo off
REM Italian Grammar Tutor - Startup Script with Content Seeding
REM This script starts the application and seeds the comprehensive grammar content

echo 🚀 Starting Italian Grammar Tutor with Comprehensive Content...

REM Check if .env file exists
if not exist ".env" (
    echo ❌ Error: .env file not found!
    echo Please create a .env file with your OPENAI_API_KEY
    echo Example: OPENAI_API_KEY=your_key_here
    pause
    exit /b 1
)

REM Start services with Docker Compose
echo 📦 Starting Docker services...
docker-compose up -d

REM Wait for services to be ready
echo ⏳ Waiting for services to start...
timeout /t 30 /nobreak > nul

REM Check if backend is ready
echo 🔍 Checking backend health...
for /l %%i in (1,1,10) do (
    curl -s http://localhost:8000/health > nul 2>&1
    if !errorlevel! equ 0 (
        echo ✅ Backend is ready!
        goto :backend_ready
    ) else (
        echo ⏳ Waiting for backend... (attempt %%i/10)
        timeout /t 5 /nobreak > nul
    )
)

echo ❌ Backend failed to start. Check logs with: docker-compose logs backend
pause
exit /b 1

:backend_ready
REM Seed comprehensive content
echo 📚 Seeding comprehensive Italian grammar content...
curl -s -X POST "http://localhost:8000/admin/seed-comprehensive-content" > temp_response.txt

findstr /c:"successfully" temp_response.txt > nul
if !errorlevel! equ 0 (
    echo ✅ Content seeded successfully!
    
    REM Get and display statistics
    echo 📊 Content Statistics:
    curl -s "http://localhost:8000/admin/content-statistics"
) else (
    echo ⚠️ Content seeding may have failed.
    echo You can manually seed content using the admin panel in the frontend.
)

del temp_response.txt > nul 2>&1

echo.
echo 🎉 Italian Grammar Tutor is ready!
echo.
echo 📱 Frontend: http://localhost:3000
echo 🔧 Backend API: http://localhost:8000
echo 📖 API Docs: http://localhost:8000/docs
echo.
echo 🧪 Testing Instructions:
echo 1. Open http://localhost:3000
echo 2. Sign in with Clerk authentication
echo 3. Click the 'Admin' button to verify content statistics
echo 4. Start asking Italian grammar questions!
echo.
echo 📚 Try these sample questions:
echo - 'How do I use the subjunctive mood in Italian?'
echo - 'Explain the conditional tense with examples'
echo - 'What are CI and NE pronouns?'
echo - 'Give me some imperative mood exercises'
echo.
echo 🛑 To stop: docker-compose down
echo.
pause