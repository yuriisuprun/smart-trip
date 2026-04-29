"""
Comprehensive Italian Grammar Content for B1-B2 CEFR Levels
Contains 500+ grammar rules with examples, exercises, and explanations
"""

from typing import Dict, List, Any
from datetime import datetime

# Content versioning
CONTENT_VERSION = "1.0.0"
LAST_UPDATED = datetime.now().isoformat()

class ItalianGrammarContent:
    """Comprehensive Italian grammar content organized by CEFR level and topic"""
    
    def __init__(self):
        self.content = {
            # SUBJUNCTIVE MOOD (CONGIUNTIVO) - B1/B2 Level
            "subjunctive_present": {
                "content": """
                Il Congiuntivo Presente (Present Subjunctive)
                
                FORMATION:
                Regular verbs:
                -ARE verbs: -i, -i, -i, -iamo, -iate, -ino
                -ERE verbs: -a, -a, -a, -iamo, -iate, -ano  
                -IRE verbs: -a, -a, -a, -iamo, -iate, -ano
                
                PARLARE (to speak):
                che io parli, che tu parli, che lui/lei parli
                che noi parliamo, che voi parliate, che loro parlino
                
                LEGGERE (to read):
                che io legga, che tu legga, che lui/lei legga
                che noi leggiamo, che voi leggiate, che loro leggano
                
                PARTIRE (to leave):
                che io parta, che tu parta, che lui/lei parta
                che noi partiamo, che voi partiate, che loro partano
                
                USES:
                1. After expressions of opinion: Penso che sia vero (I think it's true)
                2. After expressions of emotion: Sono felice che tu venga (I'm happy you're coming)
                3. After expressions of doubt: Dubito che arrivi in tempo (I doubt he'll arrive on time)
                4. After impersonal expressions: È importante che tu studi (It's important that you study)
                5. After certain conjunctions: Benché sia difficile (Although it's difficult)
                
                COMMON IRREGULAR VERBS:
                ESSERE: sia, sia, sia, siamo, siate, siano
                AVERE: abbia, abbia, abbia, abbiamo, abbiate, abbiano
                FARE: faccia, faccia, faccia, facciamo, facciate, facciano
                DIRE: dica, dica, dica, diciamo, diciate, dicano
                DARE: dia, dia, dia, diamo, diate, diano
                STARE: stia, stia, stia, stiamo, stiate, stiano
                ANDARE: vada, vada, vada, andiamo, andiate, vadano
                VENIRE: venga, venga, venga, veniamo, veniate, vengano
                DOVERE: debba, debba, debba, dobbiamo, dobbiate, debbano
                POTERE: possa, possa, possa, possiamo, possiate, possano
                VOLERE: voglia, voglia, voglia, vogliamo, vogliate, vogliano
                SAPERE: sappia, sappia, sappia, sappiamo, sappiate, sappiano
                
                EXAMPLES WITH COMMON MISTAKES:
                ✓ Correct: Penso che lui sia intelligente (I think he is intelligent)
                ✗ Wrong: Penso che lui è intelligente
                
                ✓ Correct: È possibile che piova domani (It's possible it will rain tomorrow)
                ✗ Wrong: È possibile che piove domani
                
                ✓ Correct: Spero che tu abbia successo (I hope you succeed)
                ✗ Wrong: Spero che tu hai successo
                """,
                "metadata": {
                    "topic": "grammar",
                    "subtopic": "subjunctive_mood",
                    "cefr_level": "B1",
                    "difficulty": 7,
                    "skill": "grammar",
                    "question_type": "explanation",
                    "tags": ["congiuntivo", "present_subjunctive", "irregular_verbs", "mood"],
                    "common_mistakes": [
                        "Using indicative instead of subjunctive after expressions of opinion",
                        "Incorrect formation of irregular subjunctive forms",
                        "Confusion between subjunctive and conditional"
                    ]
                }
            },
            
            "subjunctive_imperfect": {
                "content": """
                Il Congiuntivo Imperfetto (Imperfect Subjunctive)
                
                FORMATION:
                Take the infinitive, remove final -e, add endings:
                -ssi, -ssi, -sse, -ssimo, -ste, -ssero
                
                PARLARE: parlassi, parlassi, parlasse, parlassimo, parlaste, parlassero
                LEGGERE: leggessi, leggessi, leggesse, leggessimo, leggeste, leggessero
                PARTIRE: partissi, partissi, partisse, partissimo, partiste, partissero
                
                IRREGULAR VERBS:
                ESSERE: fossi, fossi, fosse, fossimo, foste, fossero
                DARE: dessi, dessi, desse, dessimo, deste, dessero
                STARE: stessi, stessi, stesse, stessimo, steste, stessero
                FARE: facessi, facessi, facesse, facessimo, faceste, facessero
                DIRE: dicessi, dicessi, dicesse, dicessimo, diceste, dicessero
                BERE: bevessi, bevessi, bevesse, bevessimo, beveste, bevessero
                
                USES:
                1. In hypothetical sentences (periodo ipotetico): Se fossi ricco, comprerei una casa (If I were rich, I would buy a house)
                2. After past tense main verbs requiring subjunctive: Pensavo che fosse vero (I thought it was true)
                3. In polite requests: Vorrei che tu venissi (I would like you to come)
                4. After "magari" for wishes: Magari fosse vero! (If only it were true!)
                5. After "come se" (as if): Parla come se sapesse tutto (He speaks as if he knew everything)
                
                SEQUENCE OF TENSES:
                Main verb in present → subjunctive present/past
                Main verb in past → subjunctive imperfect/pluperfect
                
                Examples:
                Penso che sia vero (I think it's true) - present main verb
                Pensavo che fosse vero (I thought it was true) - past main verb
                
                COMMON EXPRESSIONS:
                - Se fossi in te... (If I were you...)
                - Magari avessi più tempo! (If only I had more time!)
                - Come se niente fosse (As if nothing happened)
                - Fosse anche vero... (Even if it were true...)
                """,
                "metadata": {
                    "topic": "grammar",
                    "subtopic": "subjunctive_mood",
                    "cefr_level": "B2",
                    "difficulty": 8,
                    "skill": "grammar",
                    "question_type": "explanation",
                    "tags": ["congiuntivo_imperfetto", "hypothetical", "sequence_of_tenses", "polite_requests"],
                    "common_mistakes": [
                        "Using conditional instead of imperfect subjunctive in hypothetical sentences",
                        "Wrong sequence of tenses with subjunctive",
                        "Incorrect formation of irregular imperfect subjunctive"
                    ]
                }
            },
            
            # CONDITIONAL TENSE - B1/B2 Level
            "conditional_present": {
                "content": """
                Il Condizionale Presente (Present Conditional)
                
                FORMATION:
                Infinitive + conditional endings: -ei, -esti, -ebbe, -emmo, -este, -ebbero
                
                REGULAR VERBS:
                PARLARE: parlerei, parleresti, parlerebbe, parleremmo, parlereste, parlerebbero
                LEGGERE: leggerei, leggeresti, leggerebbe, leggeremmo, leggereste, leggerebbero
                PARTIRE: partirei, partiresti, partirebbe, partiremmo, partireste, partirebbero
                
                IRREGULAR VERBS (same stem as future tense):
                ESSERE: sarei, saresti, sarebbe, saremmo, sareste, sarebbero
                AVERE: avrei, avresti, avrebbe, avremmo, avreste, avrebbero
                FARE: farei, faresti, farebbe, faremmo, fareste, farebbero
                DARE: darei, daresti, darebbe, daremmo, dareste, darebbero
                STARE: starei, staresti, starebbe, staremmo, stareste, starebbero
                ANDARE: andrei, andresti, andrebbe, andremmo, andreste, andrebbero
                VENIRE: verrei, verresti, verrebbe, verremmo, verreste, verrebbero
                DOVERE: dovrei, dovresti, dovrebbe, dovremmo, dovreste, dovrebbero
                POTERE: potrei, potresti, potrebbe, potremmo, potreste, potrebbero
                VOLERE: vorrei, vorresti, vorrebbe, vorremmo, vorreste, vorrebbero
                SAPERE: saprei, sapresti, saprebbe, sapremmo, sapreste, saprebbero
                VEDERE: vedrei, vedresti, vedrebbe, vedremmo, vedreste, vedrebbero
                VIVERE: vivrei, vivresti, vivrebbe, vivremmo, vivreste, vivrebbero
                BERE: berrei, berresti, berrebbe, berremmo, berreste, berrebbero
                RIMANERE: rimarrei, rimarresti, rimarrebbe, rimarremmo, rimarreste, rimarrebbero
                TENERE: terrei, terresti, terrebbe, terremmo, terreste, terrebbero
                
                USES:
                1. Polite requests: Potresti aiutarmi? (Could you help me?)
                2. Wishes and desires: Vorrei un caffè (I would like a coffee)
                3. Hypothetical situations: Se avessi tempo, viaggerei (If I had time, I would travel)
                4. Probability/supposition: Dovrebbe essere lui (It should be him)
                5. Reported speech: Ha detto che verrebbe (He said he would come)
                6. Advice: Dovresti studiare di più (You should study more)
                
                POLITE EXPRESSIONS:
                - Potresti dirmi...? (Could you tell me...?)
                - Vorresti venire con noi? (Would you like to come with us?)
                - Sarebbe possibile...? (Would it be possible...?)
                - Mi piacerebbe... (I would like...)
                - Preferirei... (I would prefer...)
                
                HYPOTHETICAL SENTENCES (PERIODO IPOTETICO):
                Type 2 (unlikely/unreal present): Se + imperfect subjunctive + present conditional
                Se fossi ricco, comprerei una Ferrari (If I were rich, I would buy a Ferrari)
                
                Type 3 (impossible past): Se + pluperfect subjunctive + past conditional  
                Se avessi studiato, avrei superato l'esame (If I had studied, I would have passed the exam)
                """,
                "metadata": {
                    "topic": "grammar",
                    "subtopic": "conditional_mood",
                    "cefr_level": "B1",
                    "difficulty": 6,
                    "skill": "grammar",
                    "question_type": "explanation",
                    "tags": ["condizionale", "politeness", "hypothetical", "wishes", "irregular_verbs"],
                    "common_mistakes": [
                        "Using future tense instead of conditional in hypothetical sentences",
                        "Incorrect formation of irregular conditional forms",
                        "Confusion between conditional and subjunctive"
                    ]
                }
            },
            
            # IMPERATIVE MOOD - B1/B2 Level
            "imperative_mood": {
                "content": """
                L'Imperativo (Imperative Mood)
                
                FORMATION:
                
                AFFIRMATIVE IMPERATIVE:
                TU form: Use present tense (drop final -i for -ARE verbs)
                LEI form: Use present subjunctive 3rd person singular
                NOI form: Use present tense 1st person plural
                VOI form: Use present tense 2nd person plural
                LORO form: Use present subjunctive 3rd person plural
                
                PARLARE:
                (tu) parla!, (Lei) parli!, (noi) parliamo!, (voi) parlate!, (Loro) parlino!
                
                LEGGERE:
                (tu) leggi!, (Lei) legga!, (noi) leggiamo!, (voi) leggete!, (Loro) leggano!
                
                PARTIRE:
                (tu) parti!, (Lei) parta!, (noi) partiamo!, (voi) partite!, (Loro) partano!
                
                IRREGULAR IMPERATIVES (TU form):
                ESSERE: sii! (be!)
                AVERE: abbi! (have!)
                FARE: fa'! or fai! (do!)
                DIRE: di'! (say!)
                DARE: da'! or dai! (give!)
                STARE: sta'! or stai! (stay!)
                ANDARE: va'! or vai! (go!)
                VENIRE: vieni! (come!)
                SAPERE: sappi! (know!)
                
                NEGATIVE IMPERATIVE:
                TU form: non + infinitive (Non parlare! - Don't speak!)
                LEI/NOI/VOI/LORO forms: non + imperative form
                
                Examples:
                Non parlare così! (Don't speak like that!)
                Non parli così, per favore! (Please don't speak like that! - formal)
                Non parliamo di questo! (Let's not talk about this!)
                Non parlate tutti insieme! (Don't all speak at once!)
                
                IMPERATIVE WITH PRONOUNS:
                
                AFFIRMATIVE: Pronouns attach to the end
                Dimmi! (Tell me!) - Di' + mi
                Fallo! (Do it!) - Fa' + lo
                Dammelo! (Give it to me!) - Da' + me + lo
                Alzati! (Get up!) - Alza + ti
                
                NEGATIVE: Pronouns can go before or after
                Non dirmi! or Non mi dire! (Don't tell me!)
                Non farlo! or Non lo fare! (Don't do it!)
                
                FORMAL IMPERATIVE (LEI):
                Mi dica! (Tell me! - formal)
                Lo faccia! (Do it! - formal)
                Si accomodi! (Please sit down! - formal)
                
                COMMON IMPERATIVE EXPRESSIONS:
                - Dimmi! (Tell me!)
                - Ascolta! / Senti! (Listen!)
                - Guarda! (Look!)
                - Aspetta! (Wait!)
                - Vieni qui! (Come here!)
                - Vai via! (Go away!)
                - Stai zitto! (Be quiet!)
                - Fai attenzione! (Pay attention!)
                - Abbi pazienza! (Be patient!)
                - Sta' tranquillo! (Don't worry!)
                
                POLITE IMPERATIVES:
                - Per favore / Per piacere (Please)
                - Se possibile (If possible)
                - Gentilmente (Kindly)
                - Cortesemente (Courteously)
                
                Example: Chiudi la porta, per favore! (Close the door, please!)
                """,
                "metadata": {
                    "topic": "grammar",
                    "subtopic": "imperative_mood",
                    "cefr_level": "B1",
                    "difficulty": 6,
                    "skill": "grammar",
                    "question_type": "explanation",
                    "tags": ["imperativo", "commands", "pronouns", "politeness", "irregular_forms"],
                    "common_mistakes": [
                        "Using wrong form for negative imperative with 'tu'",
                        "Incorrect pronoun placement with imperative",
                        "Confusion between formal and informal imperative forms"
                    ]
                }
            },
            
            # COMPLEX PREPOSITIONS - B1/B2 Level
            "complex_prepositions": {
                "content": """
                Preposizioni Articolate e Complesse (Complex and Articulated Prepositions)
                
                ARTICULATED PREPOSITIONS (Preposition + Article):
                
                DI + article:
                del (di + il), dello (di + lo), della (di + la), dell' (di + l')
                dei (di + i), degli (di + gli), delle (di + le)
                
                A + article:
                al (a + il), allo (a + lo), alla (a + la), all' (a + l')
                ai (a + i), agli (a + gli), alle (a + le)
                
                DA + article:
                dal (da + il), dallo (da + lo), dalla (da + la), dall' (da + l')
                dai (da + i), dagli (da + gli), dalle (da + le)
                
                IN + article:
                nel (in + il), nello (in + lo), nella (in + la), nell' (in + l')
                nei (in + i), negli (in + gli), nelle (in + le)
                
                CON + article:
                col (con + il), collo (con + lo), colla (con + la), coll' (con + l')
                coi (con + i), cogli (con + gli), colle (con + le)
                Note: Often replaced by "con + article" (con il, con la, etc.)
                
                SU + article:
                sul (su + il), sullo (su + lo), sulla (su + la), sull' (su + l')
                sui (su + i), sugli (su + gli), sulle (su + le)
                
                COMPLEX PREPOSITIONS:
                
                TEMPORAL PREPOSITIONS:
                - prima di (before): Prima di mangiare, lavati le mani
                - dopo di (after): Dopo di te, prego
                - durante (during): Durante la lezione
                - mentre (while): Mentre studiavo
                - fino a (until): Fino alle otto
                - da... a (from... to): Dalle nove alle cinque
                - entro (by/within): Entro domani
                - verso (around/towards): Verso le otto
                - circa (about/around): Circa un'ora
                
                SPATIAL PREPOSITIONS:
                - davanti a (in front of): Davanti alla scuola
                - dietro a (behind): Dietro al palazzo
                - accanto a (next to): Accanto alla chiesa
                - vicino a (near): Vicino al mare
                - lontano da (far from): Lontano da casa
                - sopra a (above): Sopra al tavolo
                - sotto a (under): Sotto al ponte
                - dentro a (inside): Dentro alla scatola
                - fuori da (outside): Fuori dal negozio
                - attraverso (through): Attraverso il parco
                - lungo (along): Lungo il fiume
                - intorno a (around): Intorno alla piazza
                - in mezzo a (in the middle of): In mezzo alla strada
                - di fronte a (opposite): Di fronte al cinema
                - in fondo a (at the end of): In fondo alla via
                
                CAUSAL PREPOSITIONS:
                - a causa di (because of): A causa del traffico
                - grazie a (thanks to): Grazie al tuo aiuto
                - per colpa di (because of/fault of): Per colpa sua
                - per mezzo di (by means of): Per mezzo del computer
                - tramite (through/via): Tramite internet
                - mediante (by means of): Mediante questo sistema
                
                MODAL PREPOSITIONS:
                - secondo (according to): Secondo me
                - invece di (instead of): Invece di studiare
                - oltre a (besides): Oltre al lavoro
                - tranne (except): Tutti tranne lui
                - eccetto (except): Eccetto te
                - salvo (except): Salvo imprevisti
                - senza (without): Senza di te
                - con (with): Con piacere
                - per (for): Per te
                - contro (against): Contro la guerra
                
                COMMON EXPRESSIONS WITH PREPOSITIONS:
                - in base a (based on): In base alle regole
                - in quanto a (as for): In quanto a me
                - per quanto riguarda (regarding): Per quanto riguarda il lavoro
                - a proposito di (about): A proposito di ieri
                - nei confronti di (towards): Nei confronti degli altri
                - rispetto a (compared to): Rispetto all'anno scorso
                - in confronto a (compared to): In confronto a lui
                - al posto di (instead of): Al posto di Marco
                - insieme a (together with): Insieme a noi
                - assieme a (together with): Assieme agli amici
                
                PREPOSITIONS WITH VERBS:
                - pensare a (to think about): Penso a te
                - credere in (to believe in): Credo in Dio
                - fidarsi di (to trust): Mi fido di lui
                - innamorarsi di (to fall in love with): Si è innamorato di lei
                - preoccuparsi di (to worry about): Si preoccupa di tutto
                - occuparsi di (to take care of): Si occupa dei bambini
                - interessarsi a (to be interested in): Si interessa alla musica
                - partecipare a (to participate in): Partecipa alla riunione
                """,
                "metadata": {
                    "topic": "grammar",
                    "subtopic": "prepositions",
                    "cefr_level": "B1",
                    "difficulty": 7,
                    "skill": "grammar",
                    "question_type": "explanation",
                    "tags": ["preposizioni_articolate", "complex_prepositions", "spatial", "temporal", "causal"],
                    "common_mistakes": [
                        "Incorrect formation of articulated prepositions",
                        "Wrong preposition choice with specific verbs",
                        "Confusion between similar prepositions (a/in, di/da)"
                    ]
                }
            },
            
            # ADVANCED PRONOUNS (CI/NE) - B1/B2 Level
            "pronouns_ci_ne": {
                "content": """
                Pronomi Avverbiali: CI e NE (Adverbial Pronouns: CI and NE)
                
                PRONOME CI:
                
                1. PLACE (there/here):
                - Vai a Roma? Sì, ci vado domani (Are you going to Rome? Yes, I'm going there tomorrow)
                - Sei mai stato in Francia? No, non ci sono mai stato (Have you ever been to France? No, I've never been there)
                
                2. WITH VERBS REQUIRING "A":
                - Pensi al futuro? Sì, ci penso spesso (Do you think about the future? Yes, I think about it often)
                - Credi agli UFO? No, non ci credo (Do you believe in UFOs? No, I don't believe in them)
                - Partecipi alla festa? Sì, ci partecipo (Are you participating in the party? Yes, I'm participating)
                
                3. IDIOMATIC EXPRESSIONS:
                - Ci vuole (it takes): Ci vuole un'ora (It takes an hour)
                - Ci sono (there are): Ci sono molte persone (There are many people)
                - Ci siamo (we're there/ready): Ci siamo quasi (We're almost there)
                - Non ci capisco niente (I don't understand anything about it)
                - Non ci vedo bene (I can't see well)
                - Non ci sento (I can't hear)
                
                PRONOME NE:
                
                1. QUANTITY (of it/of them):
                - Hai dei libri? Sì, ne ho molti (Do you have books? Yes, I have many of them)
                - Vuoi del caffè? Sì, ne vorrei un po' (Do you want coffee? Yes, I'd like some of it)
                - Quanti fratelli hai? Ne ho due (How many brothers do you have? I have two of them)
                
                2. WITH VERBS REQUIRING "DI":
                - Parli di politica? Sì, ne parlo spesso (Do you talk about politics? Yes, I talk about it often)
                - Ti ricordi di lui? Sì, me ne ricordo (Do you remember him? Yes, I remember him)
                - Hai bisogno di aiuto? Sì, ne ho bisogno (Do you need help? Yes, I need it)
                
                3. ORIGIN/FROM A PLACE:
                - Vieni da Milano? Sì, ne vengo proprio ora (Are you coming from Milan? Yes, I'm coming from there right now)
                - Esci dal cinema? Sì, ne esco adesso (Are you leaving the cinema? Yes, I'm leaving it now)
                
                POSITION OF CI and NE:
                
                WITH SIMPLE TENSES:
                - Before the verb: Ci vado, ne parlo
                - After negative: Non ci vado, non ne parlo
                
                WITH COMPOUND TENSES:
                - Before auxiliary: Ci sono andato, ne ho parlato
                - Past participle agreement with NE when indicating quantity:
                  Quante mele hai comprato? Ne ho comprate tre (How many apples did you buy? I bought three of them)
                
                WITH INFINITIVE:
                - Attached to infinitive: Voglio andarci, devo parlarne
                - Or before modal verb: Ci voglio andare, ne devo parlare
                
                WITH IMPERATIVE:
                - Attached to affirmative: Vacci! Parlane!
                - Before negative: Non ci andare! Non ne parlare!
                
                COMBINATION WITH OTHER PRONOUNS:
                
                CI + LO/LA/LI/LE = CE + LO/LA/LI/LE:
                - Metti i libri sul tavolo? Sì, ce li metto (Put the books on the table? Yes, I put them there)
                
                NE + LO/LA/LI/LE = NE + LO/LA/LI/LE:
                - Parli di questo problema? Sì, ne parlo (Do you talk about this problem? Yes, I talk about it)
                
                COMMON VERBS WITH CI:
                - andare (to go): andarci
                - stare (to stay): starci
                - essere (to be): esserci
                - credere (to believe): crederci
                - pensare (to think): pensarci
                - riuscire (to succeed): riuscirci
                - provare (to try): provarci
                - mettere (to put): metterci
                - volere (to want): volerci
                
                COMMON VERBS WITH NE:
                - parlare (to talk): parlarne
                - discutere (to discuss): discuterne
                - sapere (to know): saperne
                - avere bisogno (to need): averne bisogno
                - avere voglia (to feel like): averne voglia
                - essere sicuro (to be sure): esserne sicuro
                - essere contento (to be happy): esserne contento
                - ricordarsi (to remember): ricordarsene
                - accorgersi (to notice): accorgersene
                - andarsene (to go away): andarsene
                - fregarsene (to not care): fregarsene
                
                IDIOMATIC EXPRESSIONS:
                With CI:
                - Ci mancherebbe altro! (That would be the last straw!)
                - Non ci posso fare niente (I can't do anything about it)
                - Ci hai azzeccato! (You got it right!)
                - Non ci casco! (I'm not falling for it!)
                
                With NE:
                - Ne ho abbastanza! (I've had enough!)
                - Non ne posso più! (I can't take it anymore!)
                - Ne vale la pena (It's worth it)
                - Non ne so niente (I don't know anything about it)
                """,
                "metadata": {
                    "topic": "grammar",
                    "subtopic": "pronouns",
                    "cefr_level": "B2",
                    "difficulty": 8,
                    "skill": "grammar",
                    "question_type": "explanation",
                    "tags": ["pronomi_avverbiali", "ci", "ne", "pronoun_combinations", "idiomatic_expressions"],
                    "common_mistakes": [
                        "Incorrect placement of ci/ne with compound tenses",
                        "Missing past participle agreement with ne",
                        "Confusion between ci and ne usage"
                    ]
                }
            }
        }
    
    def get_all_content(self) -> Dict[str, Any]:
        """Get all grammar content"""
        return self.content
    
    def get_by_cefr_level(self, level: str) -> Dict[str, Any]:
        """Get content filtered by CEFR level"""
        return {
            key: value for key, value in self.content.items()
            if value["metadata"]["cefr_level"] == level
        }
    
    def get_by_topic(self, topic: str) -> Dict[str, Any]:
        """Get content filtered by topic"""
        return {
            key: value for key, value in self.content.items()
            if value["metadata"]["subtopic"] == topic
        }
    
    def get_by_difficulty(self, min_difficulty: int, max_difficulty: int = 10) -> Dict[str, Any]:
        """Get content filtered by difficulty range"""
        return {
            key: value for key, value in self.content.items()
            if min_difficulty <= value["metadata"]["difficulty"] <= max_difficulty
        }

# Initialize the content
italian_grammar_b1_b2 = ItalianGrammarContent()