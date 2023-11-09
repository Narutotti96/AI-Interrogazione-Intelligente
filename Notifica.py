from plyer import notification

def Notifica(titolo,messaggio):
    # Mostra la notifica
    notification.notify(
        title=titolo,
        message=messaggio,
        app_icon=None,  # Puoi specificare il percorso ad un'icona .ico (su Windows) o .png (su altri OS)
        timeout=5,  # Tempo dopo il quale la notifica scomparirà in secondi
    )

if __name__ == "__main__":  
    # Definisci i parametri della notifica
    titolo = "Notifica di Test"
    messaggio = "Questo è il testo della notifica"
    Notifica(titolo,messaggio)
