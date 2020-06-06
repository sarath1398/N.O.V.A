from gtts import gTTS
import os
from playsound import playsound

def speak_text(text="Hi! I am NOVA! Your Personal Assistant"):

    audio=gTTS(text)
    audio.save('audio.mp3')
    playsound('audio.mp3')
    os.remove('audio.mp3')
