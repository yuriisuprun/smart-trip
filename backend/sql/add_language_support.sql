-- Add language support to chat sessions
-- This migration adds a language column to the chat_sessions table

-- Add language column to chat_sessions table
ALTER TABLE chat_sessions 
ADD COLUMN IF NOT EXISTS language VARCHAR(2) DEFAULT 'en';

-- Create index on language for better query performance
CREATE INDEX IF NOT EXISTS idx_chat_sessions_language ON chat_sessions(language);

-- Update existing sessions to have default language
UPDATE chat_sessions 
SET language = 'en' 
WHERE language IS NULL;

-- Add constraint to ensure only supported languages
ALTER TABLE chat_sessions 
ADD CONSTRAINT check_language_supported 
CHECK (language IN ('en', 'it'));

-- Add comment to document the column
COMMENT ON COLUMN chat_sessions.language IS 'Interface language: en (English), it (Italian)';