import openai

api = 'apiKey.txt' 

with open(api, 'r') as file:
    # Leggi il contenuto del file
    openai.api_key = file.read().strip()

def response (domanda,text): 
    #print(domanda+"\nDomande: "+text) #debug
    risp=openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=domanda+"\n"+text, # testo estratto
        temperature=0.5, # zero è deterministico, uno è creativo
        max_tokens=250, #massimo delle parole da utilizzare 250
        top_p=1, #Controlla la diversità delle risposte 
        best_of=20, #genera 20 risposte e seleziona la migliore
        frequency_penalty=0.5,  
        presence_penalty=0 #controllano quanto il modello viene penalizzato per usare risposte frequenti
        )
    
    #print("Risposta grezza: ",risp) #debug
    output_text = risp.choices[0].text.strip()
    print("Risposta GPT: ", output_text)
    return output_text