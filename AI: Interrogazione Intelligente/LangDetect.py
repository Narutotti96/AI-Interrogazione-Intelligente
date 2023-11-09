from langdetect import detect, LangDetectException
import re

def remove_special_characters(text):
    # La funzione re.sub sostituisce tutti i caratteri che non sono lettere o numeri con una stringa vuota.
    # Il pattern [^a-zA-Z0-9\s] indica "qualsiasi carattere che NON è una lettera maiuscola o minuscola, un numero o uno spazio bianco".
    return re.sub(r"[^a-zA-Z0-9\sàèéìòù'\"`]", '', text)

def LangDetect(segments):
# Dizionari per immagazzinare le parole di ciascuna lingua
    ita_list = []
    eng_list = []
    # Utilizzare re.split per suddividere la stringa con più delimitatori
    words = [word for word in re.split('[.,|;]', segments) if word]
# Iterazione attraverso ciascuna parola nel testo
    for word in words:
        cleaned_word = None
        if(word):
            cleaned_word = remove_special_characters(word)
            #print(f"Parola pulita: {cleaned_word}")  # Debug
            try:
        # Rilevamento della lingua della parola
                lang = detect(cleaned_word)
                #print(f"Lingua rilevata per {cleaned_word}: {lang}")  # Debug
                if lang == 'it':
                    ita_list.append(word)
                elif lang == 'en':
                    eng_list.append(word)
                else:
                    eng_list.append(word)
            except LangDetectException:
                if cleaned_word and not cleaned_word.isnumeric():
                    print(f"Impossibile determinare la lingua per la parola: {word}")
                
    ita_dict = " ".join(ita_list)
    eng_dict = " ".join(eng_list)
    #print(f"Dizionario ITA: {ita_dict}")  # Debug
    #print(f"Dizionario ENG: {eng_dict}")  # Debug
    return ita_dict,eng_dict
