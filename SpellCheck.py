from spellchecker import SpellChecker

# Carica la lista di parole italiane da un file
def load_italian_dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        italian_words = file.read().splitlines()
    return italian_words    
    

# Inizializza il controllo ortografico con il dizionario italiano
def initialize_spellchecker(italian_words):
    spellchecker = SpellChecker(language=None, case_sensitive=True)
    spellchecker.word_frequency.load_words(italian_words)
    return spellchecker

# Verifica la presenza di errori ortografici e calcola il punteggio
def check_spelling_errors(text, spellchecker):
    # Separare il testo in parole
    words = text.split()
    # Trova le parole che sono errate
    misspelled = spellchecker.unknown(words)
    # Ritorna il numero di errori trovati
    return misspelled
