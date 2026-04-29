# Clerk Authentication Integration Guide

This guide explains how to set up and use the Clerk authentication system that has been integrated into the Italian Language AI Tutor.

## Overview

The application now uses Clerk.dev for user authentication, replacing the hardcoded `user_123` with real user management. This includes:

- User registration and login
- JWT token validation
- Protected API routes
- User profile management
- Session persistence

## Setup Instructions

### 1. Create a Clerk Account

1. Go to [clerk.dev](https://clerk.dev) and create an account
2. Create a new application
3. Choose your preferred authentication methods (email, social logins, etc.)

### 2. Get Your Clerk Keys

From your Clerk dashboard:

1. Go to "API Keys" section
2. Copy the **Publishable Key** (starts with `pk_test_` or `pk_live_`)
3. Copy the **Secret Key** (starts with `sk_test_` or `sk_live_`)

### 3. Configure Environment Variables

#### Backend (.env)
```bash
# Add to backend/.env
CLERK_SECRET_KEY=sk_test_your_secret_key_here
```

#### Frontend (.env.local)
```bash
# Add to frontend/.env.local
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_your_publishable_key_here
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### 4. Install Dependencies

The required dependencies have been added to package.json. Run:

```bash
cd frontend
npm install
```

### 5. Configure Clerk Dashboard

In your Clerk dashboard:

1. **Allowed Origins**: Add `http://localhost:3000` (or your frontend URL)
2. **Redirect URLs**: 
   - Sign-in: `http://localhost:3000/`
   - Sign-up: `http://localhost:3000/`
   - After sign-out: `http://localhost:3000/`

## Features Implemented

### Authentication Flow

1. **Sign In/Sign Up**: Users can register and log in using Clerk's built-in components
2. **Protected Routes**: Main application requires authentication
3. **User Profile**: Dedicated profile page for managing user information
4. **Automatic User Creation**: Users are automatically created in the database on first API call

### API Security

All API endpoints now require authentication:

- **Chat API**: `/api/chat` - requires valid JWT token
- **Evaluate API**: `/api/evaluate` - requires valid JWT token  
- **Progress API**: `/api/progress/user` - requires valid JWT token
- **User API**: `/api/user/profile` - requires valid JWT token

### Frontend Components

- **Authentication UI**: Sign-in/sign-up pages with Clerk components
- **User Button**: Profile dropdown in header
- **Protected Content**: Main app only accessible when signed in
- **Profile Management**: Dedicated profile page

## API Changes

### Request Format Changes

**Before (with hardcoded user_id):**
```javascript
// Chat request
{
  "session_id": "session_123",
  "user_id": "user_123",  // ❌ Removed
  "message": "Hello"
}

// Evaluate request  
{
  "user_id": "user_123",  // ❌ Removed
  "question": "What is...",
  "user_answer": "Answer"
}
```

**After (with authentication):**
```javascript
// Chat request
{
  "session_id": "session_123",
  "message": "Hello"
  // user_id extracted from JWT token
}

// Evaluate request
{
  "question": "What is...", 
  "user_answer": "Answer"
  // user_id extracted from JWT token
}
```

### Authentication Headers

All API requests now include:
```
Authorization: Bearer <clerk_jwt_token>
```

## User Data Flow

1. **User Registration**: User signs up via Clerk
2. **First API Call**: User record created in database automatically
3. **Subsequent Calls**: User data retrieved/updated based on Clerk user ID
4. **Profile Updates**: Users can update name and CEFR level via profile page

## Database Schema

The User model uses Clerk user IDs:

```python
class User(Base):
    id = Column(String, primary_key=True)  # Clerk user ID
    email = Column(String, unique=True)
    name = Column(String)
    cefr_level = Column(String, default="A2")
    # ... other fields
```

## Development Workflow

### Starting the Application

1. **Backend**:
   ```bash
   cd backend
   # Ensure CLERK_SECRET_KEY is set in .env
   python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Frontend**:
   ```bash
   cd frontend  
   # Ensure NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY is set in .env.local
   npm run dev
   ```

### Testing Authentication

1. Visit `http://localhost:3000`
2. Click "Sign In" to register/login
3. Complete the authentication flow
4. Access the main application features
5. Visit `/profile` to manage user settings

## Troubleshooting

### Common Issues

1. **"Invalid token" errors**:
   - Check that CLERK_SECRET_KEY is correctly set in backend
   - Verify the token is being sent in Authorization header

2. **CORS errors**:
   - Ensure frontend URL is added to Clerk allowed origins
   - Check CORS settings in FastAPI backend

3. **User not found errors**:
   - Users are created automatically on first API call
   - Check database connection and User model

4. **Environment variables not loading**:
   - Frontend: Use `.env.local` (not `.env`)
   - Backend: Use `.env` file
   - Restart servers after changing environment variables

### Debug Mode

Enable debug logging in backend:
```python
# In app/core/config.py
DEBUG = True
```

Check browser console for frontend authentication issues.

## Security Considerations

1. **JWT Validation**: All tokens are validated against Clerk's JWKS
2. **User Isolation**: Users can only access their own data
3. **Session Security**: Clerk handles session management and security
4. **HTTPS**: Use HTTPS in production for secure token transmission

## Production Deployment

1. **Environment Variables**:
   - Use production Clerk keys (`pk_live_` and `sk_live_`)
   - Set proper CORS origins for production domains
   
2. **Clerk Configuration**:
   - Update redirect URLs to production domains
   - Configure production allowed origins
   
3. **Database**:
   - Ensure production database is properly configured
   - Run database migrations if needed

## Support

- **Clerk Documentation**: [docs.clerk.dev](https://docs.clerk.dev)
- **Clerk Community**: [clerk.dev/discord](https://clerk.dev/discord)
- **API Reference**: Check `/docs` endpoint on running backend

## Migration from Hardcoded Users

If you have existing data with `user_123`:

1. **Backup Database**: Always backup before migration
2. **Update User IDs**: Replace `user_123` with actual Clerk user IDs
3. **Test Thoroughly**: Verify all features work with real authentication

The system is designed to handle new users automatically, so existing hardcoded data can be migrated gradually.