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
                Il Congiuntivo (Subjunctive Mood) - Comprehensive Guide
                
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
                
                COMMON MISTAKES:
                ✗ Penso che lui è bravo (using indicative)
                ✓ Penso che lui sia bravo (using subjunctive)
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
                Il Condizionale (Conditional Mood) - Complete Guide
                
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
                - andare → andrei, andresti, andrebbe...
                - venire → verrei, verresti, verrebbe...
                
                USES:
                1. Polite requests: Potresti aiutarmi? (Could you help me?)
                2. Wishes: Vorrei un caffè (I would like a coffee)
                3. Hypothetical situations: Se avessi tempo, viaggerei (If I had time, I would travel)
                4. Probability: Dovrebbe essere lui (It should be him)
                
                POLITE EXPRESSIONS:
                - Potresti...? (Could you...?)
                - Vorresti...? (Would you like...?)
                - Sarebbe possibile...? (Would it be possible...?)
                - Mi piacerebbe... (I would like...)
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
                L'Imperativo (Imperative Mood) - Complete Guide
                
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
                - venire → vieni! (come!)
                
                NEGATIVE IMPERATIVE:
                TU form: non + infinitive (Non parlare!)
                LEI/VOI forms: non + imperative (Non parli!, Non parlate!)
                
                WITH PRONOUNS:
                Affirmative: attached to end (Dimmi! - Tell me!)
                Negative: before or after (Non dirmi! / Non mi dire!)
                
                FORMAL vs INFORMAL:
                Informal (tu): Vieni qui! (Come here!)
                Formal (Lei): Venga qui! (Come here! - polite)
                """,
                "metadata": {
                    "topic": "grammar",
                    "subtopic": "imperative_mood",
                    "cefr_level": "B1",
                    "difficulty": 6
                }
            },
            "prepositions": {
                "content": """
                Preposizioni Italiane (Italian Prepositions) - Advanced Guide
                
                ARTICULATED PREPOSITIONS:
                DI + article: del, dello, della, dell', dei, degli, delle
                A + article: al, allo, alla, all', ai, agli, alle
                DA + article: dal, dallo, dalla, dall', dai, dagli, dalle
                IN + article: nel, nello, nella, nell', nei, negli, nelle
                SU + article: sul, sullo, sulla, sull', sui, sugli, sulle
                
                COMPLEX PREPOSITIONS:
                - davanti a (in front of): Davanti alla scuola
                - dietro a (behind): Dietro al palazzo
                - accanto a (next to): Accanto alla chiesa
                - vicino a (near): Vicino al mare
                - lontano da (far from): Lontano da casa
                - invece di (instead of): Invece di studiare
                - prima di (before): Prima di mangiare
                - dopo di (after): Dopo di te
                
                COMMON MISTAKES:
                ✗ Vado in Roma (wrong preposition)
                ✓ Vado a Roma (correct with cities)
                
                ✗ Penso di te (wrong preposition)
                ✓ Penso a te (correct with "pensare")
                """,
                "metadata": {
                    "topic": "grammar",
                    "subtopic": "prepositions",
                    "cefr_level": "B1",
                    "difficulty": 7
                }
            },
            "pronouns": {
                "content": """
                Pronomi CI e NE (CI and NE Pronouns) - Advanced Guide
                
                PRONOME CI:
                1. PLACE (there/here):
                - Vai a Roma? Sì, ci vado domani (Are you going to Rome? Yes, I'm going there tomorrow)
                
                2. WITH VERBS REQUIRING "A":
                - Pensi al futuro? Sì, ci penso spesso (Do you think about the future? Yes, I think about it often)
                - Credi agli UFO? No, non ci credo (Do you believe in UFOs? No, I don't believe in them)
                
                3. IDIOMATIC EXPRESSIONS:
                - Ci vuole (it takes): Ci vuole un'ora (It takes an hour)
                - Ci sono (there are): Ci sono molte persone (There are many people)
                
                PRONOME NE:
                1. QUANTITY (of it/of them):
                - Hai dei libri? Sì, ne ho molti (Do you have books? Yes, I have many of them)
                - Vuoi del caffè? Sì, ne vorrei un po' (Do you want coffee? Yes, I'd like some of it)
                
                2. WITH VERBS REQUIRING "DI":
                - Parli di politica? Sì, ne parlo spesso (Do you talk about politics? Yes, I talk about it often)
                - Ti ricordi di lui? Sì, me ne ricordo (Do you remember him? Yes, I remember him)
                
                3. ORIGIN/FROM A PLACE:
                - Vieni da Milano? Sì, ne vengo proprio ora (Are you coming from Milan? Yes, I'm coming from there right now)
                
                COMMON MISTAKES:
                ✗ Vado a Roma → Ne vado (wrong pronoun)
                ✓ Vado a Roma → Ci vado (correct for place)
                """,
                "metadata": {
                    "topic": "grammar",
                    "subtopic": "pronouns",
                    "cefr_level": "B2",
                    "difficulty": 8
                }
            }
        }
    
    def add_document(self, doc_id: str, content: str, metadata: dict, chunk_size: int = 500):
        """Mock add document - just log the action"""
        logger.info(f"Mock RAG: Added document {doc_id} with {len(content)} characters")
        return True
    
    def retrieve(self, query: str, top_k: int = 5, **kwargs) -> List[dict]:
        """Mock retrieve - return relevant content based on query"""
        query_lower = query.lower()
        results = []
        
        # Simple keyword matching with scoring
        if any(word in query_lower for word in ['subjunctive', 'congiuntivo', 'opinion', 'doubt', 'emotion']):
            results.append({
                "content": self.mock_content["subjunctive"]["content"],
                "doc_id": "mock_subjunctive",
                "metadata": self.mock_content["subjunctive"]["metadata"],
                "score": 0.95
            })
        
        if any(word in query_lower for word in ['conditional', 'condizionale', 'polite', 'would', 'could']):
            results.append({
                "content": self.mock_content["conditional"]["content"], 
                "doc_id": "mock_conditional",
                "metadata": self.mock_content["conditional"]["metadata"],
                "score": 0.90
            })
            
        if any(word in query_lower for word in ['imperative', 'imperativo', 'command', 'order', 'instruction']):
            results.append({
                "content": self.mock_content["imperative"]["content"],
                "doc_id": "mock_imperative", 
                "metadata": self.mock_content["imperative"]["metadata"],
                "score": 0.88
            })
            
        if any(word in query_lower for word in ['preposition', 'preposizioni', 'articulated', 'di', 'a', 'da', 'in', 'su']):
            results.append({
                "content": self.mock_content["prepositions"]["content"],
                "doc_id": "mock_prepositions",
                "metadata": self.mock_content["prepositions"]["metadata"], 
                "score": 0.85
            })
            
        if any(word in query_lower for word in ['ci', 'ne', 'pronoun', 'pronomi', 'adverbial']):
            results.append({
                "content": self.mock_content["pronouns"]["content"],
                "doc_id": "mock_pronouns",
                "metadata": self.mock_content["pronouns"]["metadata"],
                "score": 0.87
            })
        
        # If no specific matches, return general grammar help
        if not results:
            results.append({
                "content": """
                Italian Grammar Help - Comprehensive Mock Content
                
                I can help you with advanced Italian grammar topics including:
                
                🎯 B1-B2 LEVEL TOPICS:
                - Subjunctive mood (congiuntivo presente e imperfetto)
                - Conditional tense (condizionale presente)
                - Imperative mood (imperativo formale e informale)
                - Complex prepositions (preposizioni articolate)
                - Advanced pronouns (CI/NE pronouns)
                - Relative pronouns (pronomi relativi)
                - Complex sentence structures
                
                📚 TRY ASKING:
                - "How do I use the subjunctive mood in Italian?"
                - "Explain the conditional tense with examples"
                - "How do I give commands in Italian?"
                - "What are CI and NE pronouns?"
                - "Explain articulated prepositions"
                
                💡 EXAMPLE QUESTIONS:
                - "When do I use 'che io sia' vs 'che io sono'?"
                - "How do I make polite requests in Italian?"
                - "What's the difference between formal and informal imperatives?"
                
                I provide detailed explanations with examples, common mistakes, and practice exercises!
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
        
        # Sort by score and return top results
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:top_k]
    
    def retrieve_grammar_content(self, query: str, cefr_level: Optional[str] = None, 
                               topic: Optional[str] = None, top_k: int = 5) -> List[dict]:
        """Mock grammar content retrieval with level filtering"""
        results = self.retrieve(query, top_k * 2)  # Get more results to filter
        
        # Filter by CEFR level if specified
        if cefr_level:
            filtered_results = []
            for result in results:
                if result["metadata"]["cefr_level"] == cefr_level:
                    filtered_results.append(result)
            results = filtered_results if filtered_results else results
        
        return results[:top_k]
    
    def retrieve_exercises(self, query: str, cefr_level: Optional[str] = None,
                          exercise_type: Optional[str] = None, top_k: int = 3) -> List[dict]:
        """Mock exercise retrieval"""
        exercises = []
        
        if 'subjunctive' in query.lower() or 'congiuntivo' in query.lower():
            exercises.append({
                "content": """
                Esercizi sul Congiuntivo (Subjunctive Exercises)
                
                EXERCISE 1: Complete with the correct subjunctive form
                
                1. Penso che lui _____ (essere) molto intelligente.
                   Answer: sia
                   Explanation: After "penso che" we use subjunctive
                
                2. È importante che voi _____ (studiare) ogni giorno.
                   Answer: studiate
                   Explanation: After impersonal expressions we use subjunctive
                
                3. Spero che tu _____ (stare) bene.
                   Answer: stia
                   Explanation: After expressions of hope/emotion we use subjunctive
                
                EXERCISE 2: Choose between indicative and subjunctive
                
                1. So che lui (è/sia) a casa.
                   Answer: è (certainty = indicative)
                
                2. Credo che lei (ha/abbia) ragione.
                   Answer: abbia (opinion = subjunctive)
                
                Try these and let me know if you need more explanations!
                """,
                "doc_id": "mock_subjunctive_exercises",
                "metadata": {
                    "topic": "grammar",
                    "subtopic": "subjunctive_exercises",
                    "cefr_level": cefr_level or "B1",
                    "difficulty": 7,
                    "exercise_type": "fill_in_blanks"
                },
                "score": 0.95
            })
        
        if 'conditional' in query.lower() or 'condizionale' in query.lower():
            exercises.append({
                "content": """
                Esercizi sul Condizionale (Conditional Exercises)
                
                EXERCISE 1: Transform to conditional for politeness
                
                1. Puoi aiutarmi? → _____ aiutarmi?
                   Answer: Potresti (more polite)
                
                2. Vuoi un caffè? → _____ un caffè?
                   Answer: Vorresti (more polite)
                
                EXERCISE 2: Complete hypothetical sentences
                
                1. Se (avere) _____ tempo, (viaggiare) _____ di più.
                   Answer: avessi, viaggerei
                   Explanation: Imperfect subjunctive + conditional
                
                2. Se (essere) _____ ricco, (comprare) _____ una villa.
                   Answer: fossi, comprerei
                
                Practice these polite forms and hypothetical situations!
                """,
                "doc_id": "mock_conditional_exercises", 
                "metadata": {
                    "topic": "grammar",
                    "subtopic": "conditional_exercises",
                    "cefr_level": cefr_level or "B1",
                    "difficulty": 6,
                    "exercise_type": "transformation"
                },
                "score": 0.90
            })
        
        # Default exercise if no specific match
        if not exercises:
            exercises.append({
                "content": """
                Italian Grammar Practice - Mixed Exercises
                
                EXERCISE 1: Choose the correct form
                
                1. Penso che (è/sia) una buona idea.
                   Answer: sia (subjunctive after opinion)
                
                2. (Potresti/Puoi) aiutarmi, per favore?
                   Answer: Potresti (more polite)
                
                3. (Vieni/Venga) qui! (informal)
                   Answer: Vieni (informal imperative)
                
                EXERCISE 2: Complete with CI or NE
                
                1. Vai spesso al cinema? Sì, _____ vado ogni settimana.
                   Answer: ci (place)
                
                2. Hai dei libri italiani? Sì, _____ ho molti.
                   Answer: ne (quantity)
                
                Keep practicing these advanced grammar points!
                """,
                "doc_id": "mock_mixed_exercises",
                "metadata": {
                    "topic": "grammar", 
                    "subtopic": "mixed_exercises",
                    "cefr_level": cefr_level or "B1",
                    "difficulty": 7,
                    "exercise_type": "mixed"
                },
                "score": 0.75
            })
        
        return exercises[:top_k]
    
    def get_content_by_difficulty(self, query: str, min_difficulty: int, 
                                max_difficulty: int = 10, top_k: int = 5) -> List[dict]:
        """Mock difficulty-based retrieval"""
        results = self.retrieve(query, top_k * 2)
        
        # Filter by difficulty
        filtered_results = []
        for result in results:
            difficulty = result["metadata"]["difficulty"]
            if min_difficulty <= difficulty <= max_difficulty:
                filtered_results.append(result)
        
        return filtered_results[:top_k]

# Create mock instance
mock_rag_service = MockRAGService()