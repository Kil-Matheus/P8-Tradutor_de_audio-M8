import speech_recognition as sr
import pyttsx3
import pygame

engine = pyttsx3.init()
pygame.mixer.init()

def stt():
    recognizer = sr.Recognizer()
    # Abra o microfone e pega o audio
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Escutando...")
        audio = recognizer.listen(source)
        try:
            print("Convertendo")
            text = recognizer.recognize_google(audio, language="pt-BR")
            print(f'{text}')
            return text
        except sr.UnknownValueError:
            print("Não foi entendi")
        except sr.RequestError as e:
            print("Erro na requisição ao Google Web Speech API; {0}".format(e))

def main():
    voz = stt()

main()