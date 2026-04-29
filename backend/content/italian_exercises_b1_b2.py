"""
Italian Grammar Exercises for B1-B2 CEFR Levels
Interactive exercises with explanations and common mistakes
"""

from typing import Dict, List, Any

class ItalianGrammarExercises:
    """Comprehensive Italian grammar exercises for B1-B2 levels"""
    
    def __init__(self):
        self.exercises = {
            # SUBJUNCTIVE EXERCISES
            "subjunctive_present_exercises": {
                "content": """
                Esercizi sul Congiuntivo Presente (Present Subjunctive Exercises)
                
                EXERCISE 1: Complete with the correct subjunctive form
                
                1. Penso che lui _____ (essere) molto intelligente.
                   Answer: sia
                   Explanation: After "penso che" we use subjunctive. "Essere" → "sia"
                
                2. È importante che voi _____ (studiare) ogni giorno.
                   Answer: studiate
                   Explanation: After impersonal expressions we use subjunctive. "Studiare" → "studiate"
                
                3. Dubito che loro _____ (arrivare) in tempo.
                   Answer: arrivino
                   Explanation: After expressions of doubt we use subjunctive. "Arrivare" → "arrivino"
                
                4. Spero che tu _____ (stare) bene.
                   Answer: stia
                   Explanation: After expressions of hope/emotion we use subjunctive. "Stare" → "stia"
                
                5. È possibile che _____ (piovere) domani.
                   Answer: piova
                   Explanation: After expressions of possibility we use subjunctive. "Piovere" → "piova"
                
                EXERCISE 2: Choose between indicative and subjunctive
                
                1. So che lui (è/sia) a casa.
                   Answer: è
                   Explanation: After "so che" (certainty) we use indicative
                
                2. Credo che lei (ha/abbia) ragione.
                   Answer: abbia
                   Explanation: After "credo che" (opinion) we use subjunctive
                
                3. È vero che (piove/piova).
                   Answer: piove
                   Explanation: After "è vero che" (certainty) we use indicative
                
                4. Sembra che (fa/faccia) freddo.
                   Answer: faccia
                   Explanation: After "sembra che" (appearance/uncertainty) we use subjunctive
                
                5. Sono sicuro che (viene/venga) alla festa.
                   Answer: viene
                   Explanation: After "sono sicuro che" (certainty) we use indicative
                
                EXERCISE 3: Transform from indicative to subjunctive
                
                1. Marco è bravo → Penso che Marco _____ bravo.
                   Answer: sia
                   
                2. Loro partono domani → È probabile che loro _____ domani.
                   Answer: partano
                   
                3. Tu hai tempo → Spero che tu _____ tempo.
                   Answer: abbia
                   
                4. Voi capite tutto → Dubito che voi _____ tutto.
                   Answer: capiate
                   
                5. Lei sa la verità → Non credo che lei _____ la verità.
                   Answer: sappia
                
                COMMON MISTAKES TO AVOID:
                ✗ Penso che lui è bravo (using indicative after opinion)
                ✓ Penso che lui sia bravo
                
                ✗ È importante che tu studi (wrong subjunctive form)
                ✓ È importante che tu studi
                
                ✗ Spero che viene (using indicative after emotion)
                ✓ Spero che venga
                """,
                "metadata": {
                    "topic": "grammar",
                    "subtopic": "subjunctive_exercises",
                    "cefr_level": "B1",
                    "difficulty": 7,
                    "skill": "grammar",
                    "question_type": "exercise",
                    "exercise_type": "fill_in_blanks",
                    "tags": ["congiuntivo_presente", "exercises", "practice", "common_mistakes"]
                }
            },
            
            "conditional_exercises": {
                "content": """
                Esercizi sul Condizionale (Conditional Exercises)
                
                EXERCISE 1: Form the conditional tense
                
                1. io (parlare) → _____
                   Answer: parlerei
                   
                2. tu (leggere) → _____
                   Answer: leggeresti
                   
                3. lui (partire) → _____
                   Answer: partirebbe
                   
                4. noi (essere) → _____
                   Answer: saremmo
                   
                5. voi (avere) → _____
                   Answer: avreste
                   
                6. loro (fare) → _____
                   Answer: farebbero
                   
                7. io (andare) → _____
                   Answer: andrei
                   
                8. tu (venire) → _____
                   Answer: verresti
                   
                9. lei (dovere) → _____
                   Answer: dovrebbe
                   
                10. noi (potere) → _____
                    Answer: potremmo
                
                EXERCISE 2: Polite requests - Transform to conditional
                
                1. Puoi aiutarmi? → _____ aiutarmi?
                   Answer: Potresti
                   Explanation: Conditional makes requests more polite
                
                2. Vuoi un caffè? → _____ un caffè?
                   Answer: Vorresti
                   
                3. Hai tempo? → _____ tempo?
                   Answer: Avresti
                   
                4. Sai dirmi l'ora? → _____ dirmi l'ora?
                   Answer: Sapresti
                   
                5. Vieni con noi? → _____ con noi?
                   Answer: Verresti
                
                EXERCISE 3: Hypothetical sentences (Periodo ipotetico)
                
                1. Se (avere) _____ tempo, (viaggiare) _____ di più.
                   Answer: avessi, viaggerei
                   Explanation: Type 2 hypothetical: imperfect subjunctive + conditional
                
                2. Se (essere) _____ ricco, (comprare) _____ una villa.
                   Answer: fossi, comprerei
                   
                3. Se (sapere) _____ cucinare, (preparare) _____ la cena.
                   Answer: sapessi, preparerei
                   
                4. Se (potere) _____ scegliere, (andare) _____ in Italia.
                   Answer: potessi, andrei
                   
                5. Se non (piovere) _____, (uscire) _____.
                   Answer: piovesse, uscirei
                
                EXERCISE 4: Advice and suggestions
                
                1. (Tu/dovere) _____ studiare di più.
                   Answer: Dovresti
                   Explanation: Conditional for advice
                
                2. (Voi/potere) _____ provare questo ristorante.
                   Answer: Potreste
                   
                3. Al tuo posto, io (fare) _____ diversamente.
                   Answer: farei
                   
                4. (Essere) _____ meglio partire presto.
                   Answer: Sarebbe
                   
                5. (Noi/dovere) _____ chiamare prima.
                   Answer: Dovremmo
                
                COMMON MISTAKES:
                ✗ Se avrei tempo, andrei (using conditional in 'se' clause)
                ✓ Se avessi tempo, andrei
                
                ✗ Potrei aiutarmi? (wrong person)
                ✓ Potresti aiutarmi?
                
                ✗ Vorrei che tu vieni (mixing conditional with indicative)
                ✓ Vorrei che tu venissi
                """,
                "metadata": {
                    "topic": "grammar",
                    "subtopic": "conditional_exercises",
                    "cefr_level": "B1",
                    "difficulty": 6,
                    "skill": "grammar",
                    "question_type": "exercise",
                    "exercise_type": "transformation",
                    "tags": ["condizionale", "politeness", "hypothetical", "advice", "exercises"]
                }
            },
            
            "imperative_exercises": {
                "content": """
                Esercizi sull'Imperativo (Imperative Exercises)
                
                EXERCISE 1: Form the imperative (tu form)
                
                1. (parlare) _____ più forte!
                   Answer: Parla
                   
                2. (leggere) _____ questo libro!
                   Answer: Leggi
                   
                3. (partire) _____ subito!
                   Answer: Parti
                   
                4. (essere) _____ bravo!
                   Answer: Sii
                   
                5. (avere) _____ pazienza!
                   Answer: Abbi
                   
                6. (fare) _____ attenzione!
                   Answer: Fa' / Fai
                   
                7. (dire) _____ la verità!
                   Answer: Di'
                   
                8. (dare) _____ una mano!
                   Answer: Da' / Dai
                   
                9. (stare) _____ zitto!
                   Answer: Sta' / Stai
                   
                10. (andare) _____ via!
                    Answer: Va' / Vai
                
                EXERCISE 2: Negative imperative (tu form)
                
                1. (parlare) Non _____ così!
                   Answer: parlare
                   Explanation: Negative imperative with 'tu' uses infinitive
                
                2. (correre) Non _____ per strada!
                   Answer: correre
                   
                3. (essere) Non _____ cattivo!
                   Answer: essere
                   
                4. (fare) Non _____ rumore!
                   Answer: fare
                   
                5. (dire) Non _____ bugie!
                   Answer: dire
                
                EXERCISE 3: Formal imperative (Lei form)
                
                1. (entrare) _____, prego!
                   Answer: Entri
                   Explanation: Formal imperative uses subjunctive form
                
                2. (accomodarsi) Si _____, per favore!
                   Answer: accomodi
                   
                3. (scusare) Mi _____ il ritardo!
                   Answer: scusi
                   
                4. (dire) Mi _____ il Suo nome!
                   Answer: dica
                   
                5. (avere) _____ pazienza!
                   Answer: Abbia
                
                EXERCISE 4: Imperative with pronouns
                
                1. Dimmi la verità! → Non _____ la verità! (negative)
                   Answer: dirmi / Non mi dire
                   Explanation: With negative imperative, pronouns can go before or after
                
                2. Fallo subito! → Non _____ subito! (negative)
                   Answer: farlo / Non lo fare
                   
                3. Alzati! → Non _____! (negative)
                   Answer: alzarti / Non ti alzare
                   
                4. Dammelo! → Non _____! (negative)
                   Answer: darmelo / Non me lo dare
                   
                5. Chiamaci! → Non _____! (negative)
                   Answer: chiamarci / Non ci chiamare
                
                EXERCISE 5: Choose the correct form
                
                1. (Formal) (Aspettare/Aspetti/Aspetta) un momento, per favore!
                   Answer: Aspetti
                   
                2. (Informal) (Venire/Vieni/Venga) qui!
                   Answer: Vieni
                   
                3. (Negative informal) Non (fare/fa'/fai) così!
                   Answer: fare
                   
                4. (Plural) (Ascoltate/Ascoltino/Ascolta) tutti!
                   Answer: Ascoltate
                   
                5. (Formal negative) Non (parlare/parli/parla) così forte!
                   Answer: parli
                
                COMMON MISTAKES:
                ✗ Non parla! (using indicative for negative informal imperative)
                ✓ Non parlare!
                
                ✗ Dimmi lo! (wrong pronoun attachment)
                ✓ Dimmelo!
                
                ✗ Fa attenzione! (missing apostrophe)
                ✓ Fa' attenzione!
                """,
                "metadata": {
                    "topic": "grammar",
                    "subtopic": "imperative_exercises",
                    "cefr_level": "B1",
                    "difficulty": 6,
                    "skill": "grammar",
                    "question_type": "exercise",
                    "exercise_type": "formation",
                    "tags": ["imperativo", "commands", "formal_informal", "pronouns", "exercises"]
                }
            },
            
            "prepositions_exercises": {
                "content": """
                Esercizi sulle Preposizioni (Preposition Exercises)
                
                EXERCISE 1: Articulated prepositions
                
                1. Vado _____ (a + il) cinema.
                   Answer: al
                   
                2. Vengo _____ (da + la) scuola.
                   Answer: dalla
                   
                3. Il libro è _____ (su + il) tavolo.
                   Answer: sul
                   
                4. Parliamo _____ (di + gli) esami.
                   Answer: degli
                   
                5. Abito _____ (in + la) città.
                   Answer: nella
                   
                6. Lavoro _____ (con + i) colleghi.
                   Answer: coi / con i
                   
                7. Il gatto è _____ (sotto + il) letto.
                   Answer: sotto il
                   
                8. Torno _____ (da + gli) Stati Uniti.
                   Answer: dagli
                   
                9. Metto i libri _____ (in + lo) zaino.
                   Answer: nello
                   
                10. Parlo _____ (con + le) amiche.
                    Answer: colle / con le
                
                EXERCISE 2: Complex prepositions
                
                1. _____ (in front of) alla scuola c'è un parco.
                   Answer: Davanti
                   
                2. Abito _____ (near) al mare.
                   Answer: vicino
                   
                3. _____ (because of) del traffico sono arrivato tardi.
                   Answer: A causa
                   
                4. _____ (thanks to) al tuo aiuto ho superato l'esame.
                   Answer: Grazie
                   
                5. _____ (instead of) studiare, guarda la TV.
                   Answer: Invece di
                   
                6. _____ (during) la lezione non si può parlare.
                   Answer: Durante
                   
                7. Lavoro _____ (from) le nove _____ (to) le cinque.
                   Answer: dalle, alle
                   
                8. _____ (according to) me, hai ragione.
                   Answer: Secondo
                   
                9. _____ (besides) il lavoro, studia anche.
                   Answer: Oltre a
                   
                10. Tutti sono venuti _____ (except) lui.
                    Answer: tranne / eccetto
                
                EXERCISE 3: Prepositions with verbs
                
                1. Penso _____ te ogni giorno.
                   Answer: a
                   Explanation: "pensare a" = to think about
                
                2. Mi fido _____ lui completamente.
                   Answer: di
                   Explanation: "fidarsi di" = to trust
                
                3. Si è innamorato _____ lei.
                   Answer: di
                   Explanation: "innamorarsi di" = to fall in love with
                
                4. Partecipo _____ riunione.
                   Answer: alla
                   Explanation: "partecipare a" = to participate in
                
                5. Si occupa _____ bambini.
                   Answer: dei
                   Explanation: "occuparsi di" = to take care of
                
                6. Credo _____ Dio.
                   Answer: in
                   Explanation: "credere in" = to believe in
                
                7. Si interessa _____ musica.
                   Answer: alla
                   Explanation: "interessarsi a" = to be interested in
                
                8. Dipende _____ te.
                   Answer: da
                   Explanation: "dipendere da" = to depend on
                
                9. Assomiglia _____ padre.
                   Answer: al
                   Explanation: "assomigliare a" = to look like
                
                10. Ringrazio _____ aiuto.
                    Answer: per l'
                    Explanation: "ringraziare per" = to thank for
                
                EXERCISE 4: Choose the correct preposition
                
                1. Vado (a/in/da) Roma domani.
                   Answer: a
                   Explanation: "andare a" + city names
                
                2. Vivo (a/in/da) Italia da cinque anni.
                   Answer: in
                   Explanation: "vivere in" + country names
                
                3. Vengo (a/in/da) casa di Marco.
                   Answer: da
                   Explanation: "venire da" = to come from
                
                4. Studio italiano (da/per/in) due anni.
                   Answer: da
                   Explanation: "da" for duration from a starting point
                
                5. Resto qui (da/per/in) una settimana.
                   Answer: per
                   Explanation: "per" for planned duration
                
                COMMON MISTAKES:
                ✗ Vado in Roma (wrong preposition with city)
                ✓ Vado a Roma
                
                ✗ Penso di te (wrong preposition with "pensare")
                ✓ Penso a te
                
                ✗ Studio italiano per due anni (wrong preposition for duration from past)
                ✓ Studio italiano da due anni
                """,
                "metadata": {
                    "topic": "grammar",
                    "subtopic": "preposition_exercises",
                    "cefr_level": "B1",
                    "difficulty": 7,
                    "skill": "grammar",
                    "question_type": "exercise",
                    "exercise_type": "fill_in_blanks",
                    "tags": ["preposizioni", "articulated_prepositions", "complex_prepositions", "verb_prepositions"]
                }
            },
            
            "pronouns_ci_ne_exercises": {
                "content": """
                Esercizi sui Pronomi CI e NE (CI and NE Pronoun Exercises)
                
                EXERCISE 1: Replace with CI
                
                1. Vado a Roma domani. → _____ vado domani.
                   Answer: Ci
                   Explanation: CI replaces "a Roma" (place)
                
                2. Penso al futuro spesso. → _____ penso spesso.
                   Answer: Ci
                   Explanation: CI replaces "al futuro" (a + noun)
                
                3. Credo agli UFO. → _____ credo.
                   Answer: Ci
                   Explanation: CI replaces "agli UFO" (a + noun)
                
                4. Partecipo alla festa. → _____ partecipo.
                   Answer: Ci
                   Explanation: CI replaces "alla festa" (a + noun)
                
                5. Sono stato in Francia. → _____ sono stato.
                   Answer: Ci
                   Explanation: CI replaces "in Francia" (place)
                
                EXERCISE 2: Replace with NE
                
                1. Parlo di politica spesso. → _____ parlo spesso.
                   Answer: Ne
                   Explanation: NE replaces "di politica" (di + noun)
                
                2. Ho tre fratelli. → _____ ho tre.
                   Answer: Ne
                   Explanation: NE replaces "fratelli" (quantity)
                
                3. Vuoi del caffè? → _____ vuoi?
                   Answer: Ne
                   Explanation: NE replaces "del caffè" (partitive)
                
                4. Vengo da Milano. → _____ vengo.
                   Answer: Ne
                   Explanation: NE replaces "da Milano" (origin)
                
                5. Ho bisogno di aiuto. → _____ ho bisogno.
                   Answer: Ne
                   Explanation: NE replaces "di aiuto" (di + noun)
                
                EXERCISE 3: Choose CI or NE
                
                1. Vai spesso al cinema? Sì, _____ vado ogni settimana.
                   Answer: ci
                   Explanation: "al cinema" = place, use CI
                
                2. Hai dei libri italiani? Sì, _____ ho molti.
                   Answer: ne
                   Explanation: "dei libri" = quantity, use NE
                
                3. Ti ricordi di lui? Sì, me _____ ricordo bene.
                   Answer: ne
                   Explanation: "di lui" = di + pronoun, use NE
                
                4. Credi a questa storia? No, non _____ credo.
                   Answer: ci
                   Explanation: "a questa storia" = a + noun, use CI
                
                5. Esci dal cinema? Sì, _____ esco ora.
                   Answer: ne
                   Explanation: "dal cinema" = from place, use NE
                
                EXERCISE 4: Past participle agreement with NE
                
                1. Quante mele hai comprato? _____ ho _____ tre.
                   Answer: Ne, comprate
                   Explanation: Past participle agrees with quantity expressed by NE
                
                2. Quanti libri hai letto? _____ ho _____ molti.
                   Answer: Ne, letti
                   
                3. Quante lettere hai scritto? _____ ho _____ due.
                   Answer: Ne, scritte
                   
                4. Quanti film hai visto? _____ ho _____ pochi.
                   Answer: Ne, visti
                   
                5. Quante canzoni hai sentito? _____ ho _____ tante.
                   Answer: Ne, sentite
                
                EXERCISE 5: CI and NE with compound tenses
                
                1. Sei mai andato in Giappone? No, non _____ sono mai andato.
                   Answer: ci
                   
                2. Hai parlato del problema? Sì, _____ ho parlato.
                   Answer: ne
                   
                3. Avete pensato alla proposta? Sì, _____ abbiamo pensato.
                   Answer: ci
                   
                4. Ha comprato delle scarpe? Sì, _____ ha comprate due paia.
                   Answer: ne
                   
                5. Siete stati al museo? Sì, _____ siamo stati ieri.
                   Answer: ci
                
                EXERCISE 6: Idiomatic expressions
                
                1. _____ vuole un'ora per arrivare. (It takes an hour)
                   Answer: Ci
                   
                2. _____ sono molte persone. (There are many people)
                   Answer: Ci
                   
                3. _____ ho abbastanza! (I've had enough!)
                   Answer: Ne
                   
                4. Non _____ posso più! (I can't take it anymore!)
                   Answer: ne
                   
                5. Non _____ capisco niente. (I don't understand anything about it)
                   Answer: ci
                
                COMMON MISTAKES:
                ✗ Vado a Roma → Ne vado (wrong pronoun for place)
                ✓ Vado a Roma → Ci vado
                
                ✗ Parlo di lui → Ci parlo (wrong pronoun for "di")
                ✓ Parlo di lui → Ne parlo
                
                ✗ Ne ho comprato tre (missing agreement)
                ✓ Ne ho comprati tre
                """,
                "metadata": {
                    "topic": "grammar",
                    "subtopic": "pronouns_ci_ne_exercises",
                    "cefr_level": "B2",
                    "difficulty": 8,
                    "skill": "grammar",
                    "question_type": "exercise",
                    "exercise_type": "substitution",
                    "tags": ["pronomi_avverbiali", "ci", "ne", "past_participle_agreement", "idiomatic_expressions"]
                }
            }
        }
    
    def get_all_exercises(self) -> Dict[str, Any]:
        """Get all grammar exercises"""
        return self.exercises
    
    def get_by_cefr_level(self, level: str) -> Dict[str, Any]:
        """Get exercises filtered by CEFR level"""
        return {
            key: value for key, value in self.exercises.items()
            if value["metadata"]["cefr_level"] == level
        }
    
    def get_by_exercise_type(self, exercise_type: str) -> Dict[str, Any]:
        """Get exercises filtered by type"""
        return {
            key: value for key, value in self.exercises.items()
            if value["metadata"]["exercise_type"] == exercise_type
        }

# Initialize the exercises
italian_grammar_exercises = ItalianGrammarExercises()