import string

import pyttsx3

# Voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
voiceRate = 145
engine.setProperty("rate", voiceRate)


# Speak Function
def speak(text: string):
    engine.say(text)
    print("Gideon: " + text)
    engine.runAndWait()


# Speak without print
def speak_without_print(text: string):
    engine.say(text)
    engine.runAndWait()
