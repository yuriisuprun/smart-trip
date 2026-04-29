-- Add comprehensive grammar support for B1-B2 Italian content
-- This migration adds tables and indexes to support the enhanced grammar content system

-- Add content metadata table for tracking seeded content
CREATE TABLE IF NOT EXISTS content_metadata (
    id VARCHAR(255) PRIMARY KEY,
    doc_id VARCHAR(255) UNIQUE NOT NULL,
    content_type VARCHAR(100) NOT NULL, -- 'grammar_rule', 'exercise', 'exam_exercise'
    topic VARCHAR(100) NOT NULL,
    subtopic VARCHAR(100) NOT NULL,
    cefr_level VARCHAR(10) NOT NULL,
    difficulty INTEGER NOT NULL DEFAULT 5,
    skill VARCHAR(100) NOT NULL, -- 'grammar', 'vocabulary', 'reading', etc.
    language VARCHAR(10) NOT NULL DEFAULT 'italian',
    content_version VARCHAR(20) NOT NULL DEFAULT '1.0.0',
    source VARCHAR(100) NOT NULL,
    tags JSONB DEFAULT '[]',
    common_mistakes JSONB DEFAULT '[]',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Add indexes for efficient querying
CREATE INDEX IF NOT EXISTS idx_content_metadata_cefr_level ON content_metadata(cefr_level);
CREATE INDEX IF NOT EXISTS idx_content_metadata_topic ON content_metadata(topic);
CREATE INDEX IF NOT EXISTS idx_content_metadata_subtopic ON content_metadata(subtopic);
CREATE INDEX IF NOT EXISTS idx_content_metadata_content_type ON content_metadata(content_type);
CREATE INDEX IF NOT EXISTS idx_content_metadata_difficulty ON content_metadata(difficulty);
CREATE INDEX IF NOT EXISTS idx_content_metadata_skill ON content_metadata(skill);
CREATE INDEX IF NOT EXISTS idx_content_metadata_language ON content_metadata(language);
CREATE INDEX IF NOT EXISTS idx_content_metadata_version ON content_metadata(content_version);

-- Add grammar progress tracking table
CREATE TABLE IF NOT EXISTS grammar_progress (
    id VARCHAR(255) PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    subtopic VARCHAR(100) NOT NULL,
    cefr_level VARCHAR(10) NOT NULL,
    mastery_level FLOAT DEFAULT 0.0, -- 0-100
    attempts INTEGER DEFAULT 0,
    correct_attempts INTEGER DEFAULT 0,
    last_practiced TIMESTAMP,
    first_encountered TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, subtopic, cefr_level)
);

-- Add indexes for grammar progress
CREATE INDEX IF NOT EXISTS idx_grammar_progress_user_id ON grammar_progress(user_id);
CREATE INDEX IF NOT EXISTS idx_grammar_progress_subtopic ON grammar_progress(subtopic);
CREATE INDEX IF NOT EXISTS idx_grammar_progress_cefr_level ON grammar_progress(cefr_level);
CREATE INDEX IF NOT EXISTS idx_grammar_progress_mastery ON grammar_progress(mastery_level);

-- Add exercise attempts table for detailed tracking
CREATE TABLE IF NOT EXISTS exercise_attempts (
    id VARCHAR(255) PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    exercise_id VARCHAR(255) NOT NULL,
    exercise_type VARCHAR(100) NOT NULL, -- 'fill_in_blanks', 'multiple_choice', etc.
    subtopic VARCHAR(100) NOT NULL,
    cefr_level VARCHAR(10) NOT NULL,
    user_answer TEXT,
    correct_answer TEXT,
    is_correct BOOLEAN NOT NULL,
    score FLOAT, -- 0-10
    time_spent INTEGER, -- seconds
    hints_used INTEGER DEFAULT 0,
    feedback TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Add indexes for exercise attempts
CREATE INDEX IF NOT EXISTS idx_exercise_attempts_user_id ON exercise_attempts(user_id);
CREATE INDEX IF NOT EXISTS idx_exercise_attempts_exercise_id ON exercise_attempts(exercise_id);
CREATE INDEX IF NOT EXISTS idx_exercise_attempts_subtopic ON exercise_attempts(subtopic);
CREATE INDEX IF NOT EXISTS idx_exercise_attempts_cefr_level ON exercise_attempts(cefr_level);
CREATE INDEX IF NOT EXISTS idx_exercise_attempts_is_correct ON exercise_attempts(is_correct);
CREATE INDEX IF NOT EXISTS idx_exercise_attempts_created_at ON exercise_attempts(created_at);

-- Add content usage analytics table
CREATE TABLE IF NOT EXISTS content_usage (
    id VARCHAR(255) PRIMARY KEY,
    user_id VARCHAR(255) REFERENCES users(id) ON DELETE CASCADE,
    doc_id VARCHAR(255) NOT NULL,
    content_type VARCHAR(100) NOT NULL,
    subtopic VARCHAR(100) NOT NULL,
    cefr_level VARCHAR(10) NOT NULL,
    interaction_type VARCHAR(50) NOT NULL, -- 'viewed', 'practiced', 'completed'
    session_id VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Add indexes for content usage
CREATE INDEX IF NOT EXISTS idx_content_usage_user_id ON content_usage(user_id);
CREATE INDEX IF NOT EXISTS idx_content_usage_doc_id ON content_usage(doc_id);
CREATE INDEX IF NOT EXISTS idx_content_usage_subtopic ON content_usage(subtopic);
CREATE INDEX IF NOT EXISTS idx_content_usage_cefr_level ON content_usage(cefr_level);
CREATE INDEX IF NOT EXISTS idx_content_usage_created_at ON content_usage(created_at);

-- Update users table to add more detailed progress tracking
ALTER TABLE users ADD COLUMN IF NOT EXISTS grammar_mastery JSONB DEFAULT '{}';
ALTER TABLE users ADD COLUMN IF NOT EXISTS preferred_topics JSONB DEFAULT '[]';
ALTER TABLE users ADD COLUMN IF NOT EXISTS learning_goals JSONB DEFAULT '{}';
ALTER TABLE users ADD COLUMN IF NOT EXISTS study_streak INTEGER DEFAULT 0;
ALTER TABLE users ADD COLUMN IF NOT EXISTS last_study_date DATE;

-- Update skill_progress table to add more granular tracking
ALTER TABLE skill_progress ADD COLUMN IF NOT EXISTS subtopic VARCHAR(100);
ALTER TABLE skill_progress ADD COLUMN IF NOT EXISTS mastery_percentage FLOAT DEFAULT 0.0;
ALTER TABLE skill_progress ADD COLUMN IF NOT EXISTS time_spent INTEGER DEFAULT 0; -- total seconds spent
ALTER TABLE skill_progress ADD COLUMN IF NOT EXISTS content_version VARCHAR(20) DEFAULT '1.0.0';

-- Add index for subtopic in skill_progress
CREATE INDEX IF NOT EXISTS idx_skill_progress_subtopic ON skill_progress(subtopic);

-- Add mistakes table enhancements
ALTER TABLE mistakes ADD COLUMN IF NOT EXISTS exercise_id VARCHAR(255);
ALTER TABLE mistakes ADD COLUMN IF NOT EXISTS content_version VARCHAR(20) DEFAULT '1.0.0';
ALTER TABLE mistakes ADD COLUMN IF NOT EXISTS difficulty_level INTEGER DEFAULT 5;

-- Add indexes for enhanced mistakes tracking
CREATE INDEX IF NOT EXISTS idx_mistakes_exercise_id ON mistakes(exercise_id);
CREATE INDEX IF NOT EXISTS idx_mistakes_difficulty_level ON mistakes(difficulty_level);

-- Create view for user progress summary
CREATE OR REPLACE VIEW user_progress_summary AS
SELECT 
    u.id as user_id,
    u.name,
    u.cefr_level,
    u.total_score,
    u.total_questions,
    u.study_streak,
    u.last_study_date,
    COUNT(DISTINCT gp.subtopic) as topics_studied,
    AVG(gp.mastery_level) as avg_mastery,
    COUNT(DISTINCT ea.exercise_id) as exercises_completed,
    AVG(CASE WHEN ea.is_correct THEN 1.0 ELSE 0.0 END) as success_rate,
    SUM(ea.time_spent) as total_study_time
FROM users u
LEFT JOIN grammar_progress gp ON u.id = gp.user_id
LEFT JOIN exercise_attempts ea ON u.id = ea.user_id
GROUP BY u.id, u.name, u.cefr_level, u.total_score, u.total_questions, u.study_streak, u.last_study_date;

-- Create view for content effectiveness analytics
CREATE OR REPLACE VIEW content_effectiveness AS
SELECT 
    cm.doc_id,
    cm.content_type,
    cm.subtopic,
    cm.cefr_level,
    cm.difficulty,
    COUNT(cu.id) as total_views,
    COUNT(DISTINCT cu.user_id) as unique_users,
    COUNT(ea.id) as total_attempts,
    AVG(CASE WHEN ea.is_correct THEN 1.0 ELSE 0.0 END) as success_rate,
    AVG(ea.score) as avg_score,
    AVG(ea.time_spent) as avg_time_spent
FROM content_metadata cm
LEFT JOIN content_usage cu ON cm.doc_id = cu.doc_id
LEFT JOIN exercise_attempts ea ON cm.doc_id = ea.exercise_id
GROUP BY cm.doc_id, cm.content_type, cm.subtopic, cm.cefr_level, cm.difficulty;

-- Insert initial content metadata for tracking
-- This will be populated by the content seeder service

-- Add trigger to update user's last_study_date when they complete exercises
CREATE OR REPLACE FUNCTION update_user_study_date()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE users 
    SET last_study_date = CURRENT_DATE,
        study_streak = CASE 
            WHEN last_study_date = CURRENT_DATE - INTERVAL '1 day' THEN study_streak + 1
            WHEN last_study_date = CURRENT_DATE THEN study_streak
            ELSE 1
        END
    WHERE id = NEW.user_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_study_date
    AFTER INSERT ON exercise_attempts
    FOR EACH ROW
    EXECUTE FUNCTION update_user_study_date();

-- Add trigger to update grammar progress when exercises are completed
CREATE OR REPLACE FUNCTION update_grammar_progress()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO grammar_progress (
        id, user_id, subtopic, cefr_level, attempts, correct_attempts, 
        mastery_level, last_practiced
    )
    VALUES (
        gen_random_uuid()::text,
        NEW.user_id,
        NEW.subtopic,
        NEW.cefr_level,
        1,
        CASE WHEN NEW.is_correct THEN 1 ELSE 0 END,
        CASE WHEN NEW.is_correct THEN 10.0 ELSE 0.0 END,
        CURRENT_TIMESTAMP
    )
    ON CONFLICT (user_id, subtopic, cefr_level) 
    DO UPDATE SET
        attempts = grammar_progress.attempts + 1,
        correct_attempts = grammar_progress.correct_attempts + CASE WHEN NEW.is_correct THEN 1 ELSE 0 END,
        mastery_level = LEAST(100.0, 
            (grammar_progress.correct_attempts + CASE WHEN NEW.is_correct THEN 1 ELSE 0 END) * 100.0 / 
            (grammar_progress.attempts + 1)
        ),
        last_practiced = CURRENT_TIMESTAMP,
        updated_at = CURRENT_TIMESTAMP;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_grammar_progress
    AFTER INSERT ON exercise_attempts
    FOR EACH ROW
    EXECUTE FUNCTION update_grammar_progress();

-- Add function to get user's weak areas based on comprehensive data
CREATE OR REPLACE FUNCTION get_user_weak_areas(user_id_param VARCHAR(255))
RETURNS TABLE(
    subtopic VARCHAR(100),
    cefr_level VARCHAR(10),
    mastery_level FLOAT,
    attempts INTEGER,
    success_rate FLOAT
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        gp.subtopic,
        gp.cefr_level,
        gp.mastery_level,
        gp.attempts,
        CASE WHEN gp.attempts > 0 THEN gp.correct_attempts::FLOAT / gp.attempts ELSE 0.0 END as success_rate
    FROM grammar_progress gp
    WHERE gp.user_id = user_id_param
    AND gp.mastery_level < 70.0  -- Consider < 70% as weak area
    AND gp.attempts >= 3  -- Only consider topics with sufficient attempts
    ORDER BY gp.mastery_level ASC, gp.attempts DESC;
END;
$$ LANGUAGE plpgsql;

-- Add function to recommend content based on user progress
CREATE OR REPLACE FUNCTION recommend_content_for_user(user_id_param VARCHAR(255), limit_param INTEGER DEFAULT 5)
RETURNS TABLE(
    doc_id VARCHAR(255),
    subtopic VARCHAR(100),
    cefr_level VARCHAR(10),
    difficulty INTEGER,
    recommendation_reason TEXT
) AS $$
BEGIN
    RETURN QUERY
    WITH user_weak_areas AS (
        SELECT * FROM get_user_weak_areas(user_id_param)
    ),
    user_info AS (
        SELECT cefr_level FROM users WHERE id = user_id_param
    )
    SELECT 
        cm.doc_id,
        cm.subtopic,
        cm.cefr_level,
        cm.difficulty,
        CASE 
            WHEN wa.subtopic IS NOT NULL THEN 'Weak area: ' || wa.subtopic
            WHEN cm.cefr_level = ui.cefr_level THEN 'Current level practice'
            ELSE 'Progressive learning'
        END as recommendation_reason
    FROM content_metadata cm
    CROSS JOIN user_info ui
    LEFT JOIN user_weak_areas wa ON cm.subtopic = wa.subtopic
    WHERE cm.content_type = 'grammar_rule'
    AND (
        wa.subtopic IS NOT NULL  -- Prioritize weak areas
        OR cm.cefr_level = ui.cefr_level  -- Current level content
        OR (cm.cefr_level = 'B1' AND ui.cefr_level = 'A2')  -- Progressive content
    )
    ORDER BY 
        CASE WHEN wa.subtopic IS NOT NULL THEN 1 ELSE 2 END,  -- Weak areas first
        cm.difficulty ASC
    LIMIT limit_param;
END;
$$ LANGUAGE plpgsql;