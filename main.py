from recorder import record
from speak import speak_text
from corona_stats import tell_corona_stats
from play_music_online import playmusic
from play_music_offline import playmusic_offline
from chatbotency import activate_chatbotency

f=0
print('Loading...')

text=record()

if ['ok','nova']==text.split() and text!=None: #Novice Operational Virtual Assistant
    speak_text()        
    f=1

while f:
    
    text=record()
    if text==None:
        text="Speak Properly"
        speak_text(text)
        continue
    
    elif 'corona' in text:
        tell_corona_stats()
        
    elif ['play','song'] in text.split():
        speak_text("Online or Offline?")
        text=record()
        
        if "online" in text:
            speak_text('Enter the song you like to hear')
            song=input()
            playmusic(song)
        
        else:
            speak_text("Enter the path of the songs folder")
            path=input()
            playmusic_offline(path)
    
    else:
        
        if "Goodbye" in text:
            speak_text("See you later!")
            f=0
        
        else:
            speak_text(activate_chatbotency(text))
            continue