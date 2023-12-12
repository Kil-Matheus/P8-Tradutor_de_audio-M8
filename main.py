import speech_recognition as sr
import pyttsx3
from gtts import gTTS
from io import BytesIO
import pygame
from deep_translator import GoogleTranslator
from my_stt import stt

engine = pyttsx3.init()
pygame.mixer.init()

def main():
    while True:
        # Recebe o valor do audio
        input_audio = stt()
        try:
            # Traduz o audio no idioma pt para en
            translator = GoogleTranslator(source='pt', target='en')
            traduzido = translator.translate(text=input_audio)
            print(traduzido)
            # Fala o audio traduzido
            speak(traduzido, 'en')
        except Exception as e:
            print(e)
            speak("Fale Novamente", 'pt')

def speak(text, language):
    # Objeto BytesIO
    audio = BytesIO()
    # Salva o audio no objeto BytesIO
    audio_confg = gTTS(text=text, lang=language)
    audio_confg.write_to_fp(audio)
    audio.seek(0)
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def stt():
    recognizer = sr.Recognizer()
    # Abre o microfone e pega o audio
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Escutando...")
        voz = recognizer.listen(source)
        try:
            print("Convertendo")
            text = recognizer.recognize_google(voz, language="pt-BR")
            print(f'{text}')
            return text
        except sr.UnknownValueError:
            print("Tente novamente")
        except sr.RequestError as e:
            print("Erro na requisição ao Google Web Speech API; {0}".format(e))


if __name__ == "__main__":
    main()