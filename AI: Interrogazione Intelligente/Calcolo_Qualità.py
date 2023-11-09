from spellchecker import SpellChecker
from SpellCheck import check_spelling_errors, load_italian_dictionary, initialize_spellchecker
import spacy
import logging

# Inizializzazione del logger
logging.basicConfig(level=logging.INFO)

# Caricamento modelli spacy
Inglese = spacy.load("en_core_web_trf") # per la lingua inglese
Ita = spacy.load("it_core_news_lg") # per la lingua italiana  

# Carica spellchecker per la lingua Inglese
spell_en = SpellChecker(language='en')
# Carica il dizionario italiano da un file (devi fornire il percorso al tuo file)
file_path = '660000_parole_italiane.txt'
diz_ita = load_italian_dictionary(file_path)
spell_ita = initialize_spellchecker(diz_ita)

# Costanti
NOUN_WEIGHT = 0.45
VERB_WEIGHT = 0.5
ADJ_WEIGHT = 0.4
LEXICAL_DIV_WEIGHT = 0.0 # non utilizzato
AVG_SENT_LEN_WEIGHT = 0.0 # non utilizzato
SPELLING_MISTAKE_WEIGHT = -0.5  # Peso negativo per gli errori ortografici

def check_text_quality(textIta,textEN,return_features=False):
    # Dizionario vuoto da usare come valore di default
    default_features = {}
    docEN = Inglese(textEN)
    docIta = Ita(textIta)

    # Calcolo degli errori ortografici
    misspelled_en = spell_en.unknown(textEN.split())
    misspelled_it = check_spelling_errors(textIta.lower(),spell_ita)
    num_misspelled = (len(misspelled_en) + len(misspelled_it))/2
    #print (f"\n ing: ",misspelled_en," \nita: ",misspelled_it) #debug    

        # Inizializzazione dei valori di qualità e delle features
    quality_ita, features_ita = 0, default_features.copy()
    quality_eng, features_eng = 0, default_features.copy()
        
    try:    
        # Calcola il punteggio di qualità per il testo italiano
        ita_tokens_count = sum(1 for token in docIta if not token.is_punct)
        if ita_tokens_count>0:
            quality_ita,features_ita = calculate_quality(docIta, num_misspelled)
        # Calcola il punteggio di qualità per il testo inglese
        eng_tokens_count = sum(1 for token in docEN if not token.is_punct)
        if eng_tokens_count>0:
            quality_eng,features_eng = calculate_quality(docEN, num_misspelled)
        # Calcola il totale dei token
        total_tokens = ita_tokens_count + eng_tokens_count
        # Calcola il punteggio di qualità combinato utilizzando una media pesata
        if total_tokens > 0:
            combined_quality = ((ita_tokens_count * quality_ita) + (eng_tokens_count * quality_eng)) / total_tokens
        else:
            combined_quality = 0  # oppure un altro valore di default 
        if return_features:
            combined_features = {
            feature: features_ita.get(feature, 0) + features_eng.get(feature, 0)
            for feature in features_ita.keys()
            }
            return combined_quality, combined_features
        else:
            return combined_quality
    except Exception as e:
        logging.error(f"Errore nel calcolo della qualità del testo: {e}")
        return 0, default_features # oppure un altro valore di default


def calculate_quality(doc, num_misspelled):

    num_sentences = len(list(doc.sents))
    num_tokens = len(doc)
    num_nouns = len([token for token in doc if token.pos_ == "NOUN"])
    num_verbs = len([token for token in doc if token.pos_ == "VERB"])
    num_adjs = len([token for token in doc if token.pos_ == "ADJ"])

    
    if num_sentences == 0:
        return 0
    
    avg_sentence_length = num_tokens / num_sentences
    #lexical_diversity = len(set(token.text.lower() for token in doc)) / num_tokens
    lexical_diversity = len(set(token.text.lower() for token in doc)) / (num_tokens + 1e-7)

    
    # Qui stiamo dando un peso maggiore ai nomi, verbi e aggettivi.
    # Inoltre, consideriamo favorevolmente i testi con una maggiore diversità lessicale e una lunghezza media della frase ragionevole.
    quality_score = (
        NOUN_WEIGHT * num_nouns +
        VERB_WEIGHT * num_verbs +
        ADJ_WEIGHT * num_adjs +
        LEXICAL_DIV_WEIGHT * lexical_diversity +
        AVG_SENT_LEN_WEIGHT * avg_sentence_length +
        SPELLING_MISTAKE_WEIGHT * num_misspelled
    ) / (num_tokens + 1e-7)

    features = {
        'num_sentences': num_sentences,
        'num_tokens': num_tokens,
        'num_nouns': num_nouns,
        'num_verbs': num_verbs,
        'num_adjs': num_adjs,
        'avg_sentence_length': avg_sentence_length,
        'lexical_diversity': lexical_diversity,
        'num_misspelled': num_misspelled
    }

    return quality_score,features
   
