// Mock auth functions for development when Clerk is not configured

export const mockUser = {
  id: 'dev-user-123',
  emailAddresses: [{ emailAddress: 'dev@example.com' }],
  firstName: 'Dev',
  lastName: 'User',
}

export const mockAuth = {
  getToken: async () => 'mock-token-123',
  isLoaded: true,
  isSignedIn: true,
}

export const mockUseUser = () => ({
  user: mockUser,
  isLoaded: true,
  isSignedIn: true,
})

export const mockUseAuth = () => mockAuth

export const MockSignInButton = ({ children, mode }: { children: React.ReactNode, mode?: string }) => (
  <button onClick={() => console.log('Mock sign in')}>{children}</button>
)

export const MockSignedIn = ({ children }: { children: React.ReactNode }) => <>{children}</>
export const MockSignedOut = ({ children }: { children: React.ReactNode }) => null
export const MockUserButton = () => <div style={{ 
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
}}>DU</div>