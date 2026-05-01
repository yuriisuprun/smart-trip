"""
Mock RAG service for testing without OpenAI API key
"""
import logging
from typing import List, Optional, Dict, Any

logger = logging.getLogger(__name__)

class MockRAGService:
    """Mock RAG service that returns predefined Italian grammar content"""
    
    def __init__(self):
        self.mock_content = {
            "subjunctive": {
                "content": """
                Il Congiuntivo (Subjunctive Mood) - Mock Content
                
                The subjunctive mood in Italian expresses doubt, opinion, emotion, or uncertainty.
                
                FORMATION:
                Present Subjunctive:
                - ARE verbs: -i, -i, -i, -iamo, -iate, -ino
                - ERE verbs: -a, -a, -a, -iamo, -iate, -ano
                - IRE verbs: -a, -a, -a, -iamo, -iate, -ano
                
                EXAMPLES:
                - Penso che tu sia bravo (I think you are good)
                - È importante che voi studiate (It's important that you study)
                - Spero che lui venga (I hope he comes)
                
                COMMON USES:
                1. After expressions of opinion: Credo che...
                2. After expressions of emotion: Sono felice che...
                3. After expressions of doubt: Dubito che...
                4. After impersonal expressions: È necessario che...
                
                IRREGULAR VERBS:
                - essere → sia, sia, sia, siamo, siate, siano
                - avere → abbia, abbia, abbia, abbiamo, abbiate, abbiano
                - fare → faccia, faccia, faccia, facciamo, facciate, facciano
                """,
                "metadata": {
                    "topic": "grammar",
                    "subtopic": "subjunctive_mood", 
                    "cefr_level": "B1",
                    "difficulty": 7
                }
            },
            "conditional": {
                "content": """
                Il Condizionale (Conditional Mood) - Mock Content
                
                The conditional mood expresses actions that would happen under certain conditions.
                
                FORMATION:
                Infinitive + conditional endings: -ei, -esti, -ebbe, -emmo, -este, -ebbero
                
                REGULAR EXAMPLES:
                - parlerei (I would speak)
                - leggeresti (you would read)  
                - partirebbe (he/she would leave)
                
                IRREGULAR EXAMPLES:
                - essere → sarei, saresti, sarebbe...
                - avere → avrei, avresti, avrebbe...
                - fare → farei, faresti, farebbe...
                
                USES:
                1. Polite requests: Potresti aiutarmi? (Could you help me?)
                2. Wishes: Vorrei un caffè (I would like a coffee)
                3. Hypothetical situations: Se avessi tempo, viaggerei (If I had time, I would travel)
                4. Probability: Dovrebbe essere lui (It should be him)
                
                POLITE EXPRESSIONS:
                - Potresti...? (Could you...?)
                - Vorresti...? (Would you like...?)
                - Sarebbe possibile...? (Would it be possible...?)
                """,
                "metadata": {
                    "topic": "grammar",
                    "subtopic": "conditional_mood",
                    "cefr_level": "B1", 
                    "difficulty": 6
                }
            },
            "imperative": {
                "content": """
                L'Imperativo (Imperative Mood) - Mock Content
                
                The imperative mood is used to give commands, instructions, or make requests.
                
                FORMATION:
                TU form: Use present tense (drop -i for -ARE verbs)
                LEI form: Use present subjunctive 3rd person singular
                VOI form: Use present tense 2nd person plural
                
                EXAMPLES:
                - Parla! (Speak! - informal)
                - Parli! (Speak! - formal)
                - Parlate! (Speak! - plural)
                
                IRREGULAR IMPERATIVES:
                - essere → sii! (be!)
                - avere → abbi! (have!)
                - fare → fa'! or fai! (do!)
                - dire → di'! (say!)
                - andare → va'! or vai! (go!)
                
                NEGATIVE IMPERATIVE:
                TU form: non + infinitive (Non parlare!)
                LEI/VOI forms: non + imperative (Non parli!, Non parlate!)
                
                WITH PRONOUNS:
                Affirmative: attached to end (Dimmi! - Tell me!)
                Negative: before or after (Non dirmi! / Non mi dire!)
                """,
                "metadata": {
                    "topic": "grammar",
                    "subtopic": "imperative_mood",
                    "cefr_level": "B1",
                    "difficulty": 6
                }
            }
        }
    
    def add_document(self, doc_id: str, content: str, metadata: dict, chunk_size: int = 500):
        """Mock add document - just log the action"""
        logger.info(f"Mock: Added document {doc_id} with {len(content)} characters")
        return True
    
    def retrieve(self, query: str, top_k: int = 5, **kwargs) -> List[dict]:
        """Mock retrieve - return relevant content based on query"""
        query_lower = query.lower()
        results = []
        
        # Simple keyword matching
        if any(word in query_lower for word in ['subjunctive', 'congiuntivo', 'opinion', 'doubt']):
            results.append({
                "content": self.mock_content["subjunctive"]["content"],
                "doc_id": "mock_subjunctive",
                "metadata": self.mock_content["subjunctive"]["metadata"],
                "score": 0.9
            })
        
        if any(word in query_lower for word in ['conditional', 'condizionale', 'polite', 'would']):
            results.append({
                "content": self.mock_content["conditional"]["content"], 
                "doc_id": "mock_conditional",
                "metadata": self.mock_content["conditional"]["metadata"],
                "score": 0.8
            })
            
        if any(word in query_lower for word in ['imperative', 'imperativo', 'command', 'order']):
            results.append({
                "content": self.mock_content["imperative"]["content"],
                "doc_id": "mock_imperative", 
                "metadata": self.mock_content["imperative"]["metadata"],
                "score": 0.8
            })
        
        # If no specific matches, return general grammar help
        if not results:
            results.append({
                "content": """
                Italian Grammar Help - Mock Content
                
                I can help you with Italian grammar topics including:
                - Subjunctive mood (congiuntivo)
                - Conditional tense (condizionale)
                - Imperative mood (imperativo)
                - Verb conjugations
                - Prepositions
                - Pronouns
                
                Try asking specific questions like:
                - "How do I use the subjunctive mood?"
                - "Explain the conditional tense"
                - "How do I give commands in Italian?"
                """,
                "doc_id": "mock_general",
                "metadata": {
                    "topic": "grammar",
                    "subtopic": "general",
                    "cefr_level": "B1", 
                    "difficulty": 5
                },
                "score": 0.5
            })
        
        return results[:top_k]
    
    def retrieve_grammar_content(self, query: str, cefr_level: Optional[str] = None, 
                               topic: Optional[str] = None, top_k: int = 5) -> List[dict]:
        """Mock grammar content retrieval"""
        return self.retrieve(query, top_k)
    
    def retrieve_exercises(self, query: str, cefr_level: Optional[str] = None,
                          exercise_type: Optional[str] = None, top_k: int = 3) -> List[dict]:
        """Mock exercise retrieval"""
        return [{
            "content": """
            Italian Grammar Exercise - Mock Content
            
            SUBJUNCTIVE PRACTICE:
            Complete with the correct subjunctive form:
            
            1. Penso che lui _____ (essere) molto bravo.
               Answer: sia
            
            2. È importante che voi _____ (studiare) ogni giorno.
               Answer: studiate
            
            3. Spero che tu _____ (venire) alla festa.
               Answer: venga
            
            Try these exercises and let me know if you need explanations!
            """,
            "doc_id": "mock_exercise",
            "metadata": {
                "topic": "grammar",
                "subtopic": "subjunctive_exercises",
                "cefr_level": cefr_level or "B1",
                "difficulty": 7,
                "exercise_type": "fill_in_blanks"
            },
            "score": 0.9
        }]

# Create mock instance
mock_rag_service = MockRAGService()