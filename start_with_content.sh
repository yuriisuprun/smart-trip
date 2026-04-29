#!/bin/bash

# Italian Grammar Tutor - Startup Script with Content Seeding
# This script starts the application and seeds the comprehensive grammar content

echo "🚀 Starting Italian Grammar Tutor with Comprehensive Content..."

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "❌ Error: .env file not found!"
    echo "Please create a .env file with your OPENAI_API_KEY"
    echo "Example: OPENAI_API_KEY=your_key_here"
    exit 1
fi

# Start services with Docker Compose
echo "📦 Starting Docker services..."
docker-compose up -d

# Wait for services to be ready
echo "⏳ Waiting for services to start..."
sleep 30

# Check if backend is ready
echo "🔍 Checking backend health..."
for i in {1..10}; do
    if curl -s http://localhost:8000/health > /dev/null 2>&1; then
        echo "✅ Backend is ready!"
        break
    else
        echo "⏳ Waiting for backend... (attempt $i/10)"
        sleep 5
    fi
    
    if [ $i -eq 10 ]; then
        echo "❌ Backend failed to start. Check logs with: docker-compose logs backend"
        exit 1
    fi
done

# Seed comprehensive content
echo "📚 Seeding comprehensive Italian grammar content..."
response=$(curl -s -X POST "http://localhost:8000/admin/seed-comprehensive-content")

if echo "$response" | grep -q "successfully"; then
    echo "✅ Content seeded successfully!"
    
    # Get and display statistics
    echo "📊 Content Statistics:"
    curl -s "http://localhost:8000/admin/content-statistics" | python3 -m json.tool 2>/dev/null || echo "Statistics available via admin panel"
else
    echo "⚠️ Content seeding may have failed. Response: $response"
    echo "You can manually seed content using the admin panel in the frontend."
fi

echo ""
echo "🎉 Italian Grammar Tutor is ready!"
echo ""
echo "📱 Frontend: http://localhost:3000"
echo "🔧 Backend API: http://localhost:8000"
echo "📖 API Docs: http://localhost:8000/docs"
echo ""
echo "🧪 Testing Instructions:"
echo "1. Open http://localhost:3000"
echo "2. Sign in with Clerk authentication"
echo "3. Click the 'Admin' button to verify content statistics"
echo "4. Start asking Italian grammar questions!"
echo ""
echo "📚 Try these sample questions:"
echo "- 'How do I use the subjunctive mood in Italian?'"
echo "- 'Explain the conditional tense with examples'"
echo "- 'What are CI and NE pronouns?'"
echo "- 'Give me some imperative mood exercises'"
echo ""
echo "🛑 To stop: docker-compose down"