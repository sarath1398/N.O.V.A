import speech_recognition as sr 
from speak import speak_text

r=sr.Recognizer()

def record():

    with sr.Microphone() as source:

        try:
            r.adjust_for_ambient_noise(source)
            audio=r.listen(source)
            text=r.recognize_google(audio).lower()
        
        except sr.RequestError :
            speak_text("Check your Internet Connectivity!")
        
        except sr.UnknownValueError:
            speak_text("Speak Properly")
    
        else:
            return text
