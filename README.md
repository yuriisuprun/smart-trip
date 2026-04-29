# Italian Language AI Tutor - MVP

A full-stack AI tutoring system for preparing students for the Italian language exam at Prefettura di Milano. Features context-aware learning, RAG-based knowledge retrieval, adaptive difficulty, and **Clerk.dev authentication**.

## 🏗️ Architecture

```
Frontend (Next.js + Clerk Auth) 
    ↓ 
FastAPI Backend (AI Orchestrator + JWT Validation) 
    ↓ 
LangChain + Custom Orchestrator 
    ↓ 
┌─────────────────────┬──────────────────┐
│ Vector DB (Qdrant)  │ PostgreSQL       │
│ (RAG knowledge)     │ (users+progress) │
└─────────────────────┴──────────────────┘
    ↓ 
OpenAI LLM
```

## 🔐 Authentication System

This application now uses **Clerk.dev** for user authentication:

- **User Registration & Login**: Secure authentication with email/social providers
- **JWT Token Validation**: All API endpoints protected with Clerk JWT tokens
- **User Profile Management**: Dedicated profile page for user settings
- **Automatic User Creation**: Users automatically created in database on first login
- **Session Persistence**: Secure session management via Clerk

**⚠️ Important**: The application requires authentication to access. See [CLERK_INTEGRATION_GUIDE.md](./CLERK_INTEGRATION_GUIDE.md) for complete setup instructions.

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.11+
- Node.js 18+
- OpenAI API key
- **Clerk.dev account** (free tier available)

### Setup

```bash
# Clone and navigate
cd italian-tutor

# Set up authentication (REQUIRED)
# 1. Create account at https://clerk.dev
# 2. Create new application
# 3. Get your API keys

# Configure environment variables
# Backend: Add CLERK_SECRET_KEY to backend/.env
# Frontend: Add NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY to frontend/.env.local

# Start all services
docker-compose up -d

# Backend will be at http://localhost:8000
# Frontend will be at http://localhost:3335
# Qdrant at http://localhost:6333
# PostgreSQL at localhost:5432
```

### Environment Setup

Create `.env.local` in frontend:
```
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_your_key_here
```

Create `.env` in backend:
```
OPENAI_API_KEY=your_key
DATABASE_URL=postgresql://user:password@postgres:5432/italian_tutor
QDRANT_URL=http://qdrant:6333
CLERK_SECRET_KEY=sk_test_your_key_here
```

### First Time Setup

1. **Get Clerk Keys**: Visit [clerk.dev](https://clerk.dev), create an app, and get your keys
2. **Configure Environment**: Add Clerk keys to both frontend and backend `.env` files
3. **Start Services**: Run `docker-compose up -d`
4. **Seed Content**: Visit `http://localhost:8000/api/admin/seed-all` to populate the knowledge base
5. **Access App**: Go to `http://localhost:3335` and sign up/sign in

📖 **Detailed Setup Guide**: See [CLERK_INTEGRATION_GUIDE.md](./CLERK_INTEGRATION_GUIDE.md) for complete authentication setup instructions.

## 📁 Project Structure

```
italian-tutor/
├── frontend/                 # Next.js React app
│   ├── app/
│   ├── components/
│   ├── lib/
│   └── public/
├── backend/                  # FastAPI server
│   ├── app/
│   ├── core/
│   ├── models/
│   ├── services/
│   └── schemas/
├── docker-compose.yml
└── README.md
```

## 🎯 Core Features

### 1. Context-Aware Tutoring
- Tracks student knowledge level (CEFR A2/B1)
- Detects weak grammar/vocabulary areas
- Adapts explanations based on past mistakes

### 2. Step-by-Step Teaching Engine
- Never gives direct answers
- Provides: explanation → guided reasoning → incremental hints → final answer
- Corrects mistakes with detailed explanations

### 3. Long-Term Learning Memory
- Stores mistakes and progress over time
- Skill level per topic (grammar, reading, writing, listening)
- Personalizes future lessons based on history

### 4. RAG System
- Vector DB (Qdrant) stores Italian grammar rules, exam samples, vocabulary
- Retrieves relevant context before answering
- Grounds explanations in real exam content

### 5. Real-Time Chat
- Server-Sent Events (SSE) for streaming responses
- Token-by-token LLM output
- Responsive chat interface

### 6. Evaluation Engine
- AI grading system for written answers
- Grammar correctness checking
- CEFR-based scoring
- Detailed correction feedback

## 📊 Database Schema

See `backend/sql/schema.sql` for full schema including:
- Users & authentication
- Chat sessions & history
- Mistakes log
- Skill progression
- Quiz attempts

## 🔑 API Endpoints

### Chat
- `POST /api/chat` - Send message to tutor (streaming)
- `GET /api/chat/history/{session_id}` - Get chat history

### Evaluation
- `POST /api/evaluate` - Evaluate written answer
- `POST /api/quiz/submit` - Submit quiz answer

### Progress
- `GET /api/progress/user/{user_id}` - Get user progress
- `GET /api/progress/topics` - Get topic-wise progress

### Admin
- `POST /api/admin/seed-content` - Seed Italian grammar content
- `POST /api/admin/seed-exams` - Seed exam questions

## 🧠 Memory System

### Short-term Memory
- Last 10-20 messages per session
- Injected into every LLM prompt
- Provides immediate context

### Long-term Memory
- Persistent user profile
- Weak grammar areas
- Repeated mistakes
- CEFR level estimate
- Improvement history

## 🎓 Tutoring Behavior

The AI tutor ALWAYS:
1. Guides step-by-step (never jumps to final answer)
2. Adapts difficulty to user level
3. Corrects mistakes with explanations
4. Reuses past mistakes in teaching
5. Provides structured feedback

## 🔐 Authentication

Uses Clerk.dev for:
- Login/signup
- User session management
- Protected routes
- JWT token validation

## 📦 Tech Stack

### Frontend
- Next.js 14 (React)
- Tailwind CSS
- shadcn/ui
- Zustand (state management)
- React Hook Form
- TanStack Query

### Backend
- FastAPI (Python)
- LangChain
- Qdrant (Vector DB)
- PostgreSQL
- Pydantic
- SQLAlchemy

### Infrastructure
- Docker & Docker Compose
- Clerk.dev (Auth)
- OpenAI API
- Sentry (error tracking)

## 🚀 Development

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 📝 Sample Content

The system seeds with:
- CEFR A2/B1 Italian grammar rules
- Prefettura-style exam questions
- Reading comprehension passages
- Vocabulary lists (500+ words)

## 🔍 Observability

- Sentry integration for error tracking
- Structured logging for LLM calls
- Request/response logging
- Performance metrics

## 📄 License

MIT

## 🤝 Contributing

This is an MVP foundation. Extend with:
- More exam content
- Additional languages
- Mobile app
- Advanced analytics
- Gamification features
