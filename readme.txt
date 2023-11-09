Istruzioni per l’installazione (Linux):

Avere installato Python 3.8

Creare un’ambiente virtuale dove poter installare le librerie e framework:
python3.8 -m venv nome_ambiente

Eseguire ambiente virtuale:
source nome_ambiente/bin/activate

Permessi per lettura e scrittura su cartella (altrimenti il sistema operativo salva le immagini criptate):
sudo chmod 700 [percorso_del_file] //lettura scrittura e esecuzione
sudo chmod 600 [percorso_del_file] //lettura e scrittura

librerie e framework:

pynput:
pip install pynput

pyscreenshoot:
pip install pyscreenshot

Pillow:
pip install Pillow

OpenCV:
pip install opencv-python

tesseract:
pip install pytesseract

langdetect:
pip install langdetect


spellchecker: 
pip install pyspellchecker

spacy:
pip install spacy
dizionari spacy:
python -m spacy download en_core_web_trf
python -m spacy download it_core_news_lg

openai:
pip install openai

plyer:
pip install plyer

Installato tutte le librerie, framework e dipendenze aprire il file “apiKey.txt” e inserire la propria apikey di OpenAI.

Aprire main.py dal vostro ambiente di sviluppo e lanciare il programma.


