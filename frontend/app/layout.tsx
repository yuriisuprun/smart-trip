import type { Metadata, Viewport } from 'next'
// import { ClerkProvider } from '@clerk/nextjs'
import './globals.css'

export const metadata: Metadata = {
  title: 'Italian Language AI Tutor',
  description: 'Context-aware AI tutoring system for Italian language exam preparation',
  keywords: ['Italian', 'Language', 'Learning', 'AI', 'Tutor', 'Exam'],
  authors: [{ name: 'Italian Tutor Team' }],
  icons: {
    icon: '/favicon.svg',
    apple: '/favicon.svg',
  },
  openGraph: {
    title: 'Italian Language AI Tutor',
    description: 'Context-aware AI tutoring system for Italian language exam preparation',
    type: 'website',
  },
}

export const viewport: Viewport = {
  width: 'device-width',
  initialScale: 1,
  maximumScale: 1,
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    // <ClerkProvider>
      <html lang="en" suppressHydrationWarning>
        <body style={{ 
          backgroundColor: '#f8fafc', 
          minHeight: '100vh',
          margin: 0,
          fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif'
        }}>
          {children}
        </body>
      </html>
    // </ClerkProvider>
  )
}
