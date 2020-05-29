import speech_recognition as sr
from speak import *
from corona_stats import *
from play_music_online import *

r=sr.Recognizer()
f=0
print('Loading...')

with sr.Microphone() as source:
    
    r.adjust_for_ambient_noise(source)
    print('Booted Successfully')
    audio=r.listen(source)

try:

    text=r.recognize_google(audio)
    print(text)

    if ['ok','nova']==text.lower().split(): #Novice yet Operational Virtual Assistant
        speak_text()        
        f=1

except sr.UnknownValueError:
    print('Speak Again')

while f:

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        #print('Adjusted to the Environment')
        audio = r.listen(source)

    try:
    
        text=r.recognize_google(audio).lower()
        print(text)
    
        if 'corona' in text.split():
            tell_corona_stats()
        
        if ['play','song'] in text.split():
            speak_text('Playing a suitable song!')
            playmusic()

    except sr.RequestError:
        print("Request Error")

    except sr.UnknownValueError:
        exit()

    except Exception as e:
        print(e)
