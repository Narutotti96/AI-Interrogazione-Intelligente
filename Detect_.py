from LangDetect import LangDetect
from Calcolo_Qualità import check_text_quality
from concurrent.futures import ThreadPoolExecutor

def BestText(text1,text2,text3):
    
    ita_dict1,eng_dict1 = LangDetect(text1)
    ita_dict2,eng_dict2 = LangDetect(text2)
    ita_dict3,eng_dict3 = LangDetect(text3)

    # Crea un ThreadPoolExecutor per gestire il multithreading
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Sottomette i task al thread pool
        future1 = executor.submit(execute_check_text_quality, ita_dict1, eng_dict1)
        future2 = executor.submit(execute_check_text_quality, ita_dict2, eng_dict2)
        future3 = executor.submit(execute_check_text_quality, ita_dict3, eng_dict3)

        # Recupera i risultati una volta che sono pronti
        quality1, features1 = future1.result()
        quality2, features2 = future2.result()
        quality3, features3 = future3.result()
     
        # Stampa i punteggi di qualità
    #print(f"Punteggio qualità Text1: {quality1} con features: {features1}")
    #print(f"Punteggio qualità Text2: {quality2} con features: {features2}")
    #print(f"Punteggio qualità Text3: {quality3} con features: {features3}")
     
    qualità = [quality1,quality2,quality3]
    massimoVal = (max(qualità))
    best_match_index = qualità.index(massimoVal)
    return best_match_index

def execute_check_text_quality(ita_dict, eng_dict):
    return check_text_quality(ita_dict, eng_dict, True)
    

if __name__ == "__main__":
    text1 = "Esempio di testo uno, the quality it isn't water, tre tigri contro tre tigri. the moa+n is biger"
    text2 = "Esempio di testo duea, the quality it isnt water, tre tigri contro tre tigri. the moon is bipg"
    text3 = "Esempio di testo tare, the quality it isnt water, tre tigri contro tre tigri. the moon is big"
    Index_best_text=BestText(text1,text2,text3)
    if Index_best_text is not None:
                texts = [text1, text2, text3]
                print(f"Testo con indice {Index_best_text}: {texts[Index_best_text]}")
    else:
        print("Errore indice funzione BestText ")

