import pyscreenshot as ImageGrab
from pynput import keyboard
import time
from OCR import perform_ocr_on_image_from_file,perform_ocr_on_image_from_file_Reduce, write_text_to_file
from Detect_ import BestText
from Notifica import Notifica
from ChatGPT import response

screename = 'screenshot.png'
filename ='output.txt'    

def inizializzazione():
    domanda = input("Inserisci quello che vuoi chiedere: ")
    OCR_avanzato = False # su True imposta l'ocr avanzato
    return domanda,OCR_avanzato

def menu():
    print("Premi il tasto 'C' per catturare lo schermo.")
    print("Premi il tasto 'Q' per uscire.")        

def on_press(key):
    try:
        if key.char == 'c':
            
            print("Cattura in corso...")
            # Cattura lo schermo
            im = ImageGrab.grab()
            # Salva lo screen
            im.save(screename)
            print("Screen Salvato")
            
            # Punto di partenza: registra il tempo attuale
            start_time = time.time()

            print("Esecuzione OCR su un file immagine in corso...")
            if OCR_avanzato:
                # Esegui OCR sull'immagine letta dal file
                text,text1,textCV = perform_ocr_on_image_from_file(screename) 
                # Esegue valutazione miglior testo
                IndiceBT = BestText(text,text1,textCV)  
            else: 
                text = perform_ocr_on_image_from_file_Reduce(screename) 
                IndiceBT = None
            
            print("Sto inviando a chatGPT...")
            if IndiceBT is not None:
                texts = [text, text1, textCV]
                print(f"Testo con indice {IndiceBT}: {texts[IndiceBT]}")
                try:
                    risposta = response(domanda,texts[IndiceBT])
                except Exception as err:            
                    print(f"Errore con ChatGPT: {err}")
            else:
                try:
                    risposta = response(domanda,text)
                except Exception as err:            
                    print(f"Errore con ChatGPT: {err}")

            Notifica("Risposta GPT", risposta)
            #write_text_to_file(risposta,filename)
            print("Operazione Completata!")
            
            # Punto di arrivo: registra il tempo attuale
            end_time = time.time()
            # Calcolo del tempo trascorso
            elapsed_time = end_time - start_time
            print(f"L'elaborazione ha impiegato {elapsed_time} secondi.")
            
            menu()
            
        elif key.char == 'q':
            print("Uscita in corso...")
            exit(0)
    except AttributeError:
        pass  # Gestisce i casi in cui il tasto non ha un carattere associato


if __name__ == "__main__":   
    
    domanda, OCR_avanzato = inizializzazione()
    
    menu()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
