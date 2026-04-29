'use client'

import React from 'react'

// Check if Clerk is properly configured
const isClerkConfigured = process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY && 
                          process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY.length > 0

// Mock components for when Clerk is not configured
const MockSignedIn = ({ children }: { children: React.ReactNode }) => <>{children}</>
const MockSignedOut = ({ children }: { children: React.ReactNode }) => null
const MockSignInButton = ({ children, mode }: { children: React.ReactNode, mode?: string }) => (
  <button onClick={() => alert('Clerk not configured for development')}>{children}</button>
)
const MockUserButton = () => (
  <div style={{ 
    width: '32px', 
    height: '32px', 
    borderRadius: '50%', 
    backgroundColor: '#4f46e5', 
    display: 'flex', 
    alignItems: 'center', 
    justifyContent: 'center', 
    color: 'white', 
    fontSize: '14px', 
    fontWeight: 'bold' 
  }}>
    DU
  </div>
)

const mockUser = {
  id: 'dev-user-123',
  emailAddresses: [{ emailAddress: 'dev@example.com' }],
  firstName: 'Dev',
  lastName: 'User',
}

const mockUseUser = () => ({
  user: mockUser,
  isLoaded: true,
  isSignedIn: true,
})

const mockUseAuth = () => ({
  getToken: async () => 'mock-token-123',
  isLoaded: true,
  isSignedIn: true,
})

// Export the appropriate components based on configuration
export let SignedIn, SignedOut, SignInButton, UserButton, useUser, useAuth

if (isClerkConfigured) {
  try {
    const clerk = require('@clerk/nextjs')
    SignedIn = clerk.SignedIn
    SignedOut = clerk.SignedOut
    SignInButton = clerk.SignInButton
    UserButton = clerk.UserButton
    useUser = clerk.useUser
    useAuth = clerk.useAuth
  } catch (error) {
    console.warn('Clerk not available, using mock components')
    SignedIn = MockSignedIn
    SignedOut = MockSignedOut
    SignInButton = MockSignInButton
    UserButton = MockUserButton
    useUser = mockUseUser
    useAuth = mockUseAuth
  }
} else {
  SignedIn = MockSignedIn
  SignedOut = MockSignedOut
  SignInButton = MockSignInButton
  UserButton = MockUserButton
  useUser = mockUseUser
  useAuth = mockUseAuth
}