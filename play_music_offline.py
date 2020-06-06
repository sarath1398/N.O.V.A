import os
from playsound import playsound
import random
from time import sleep

def playmusic_offline(setpath='F:\\Themes'):

    os.chdir(r'{}'.format(setpath))
    playlist=[i for i in os.listdir(os.getcwd()) if i[-4:]=='.mp3']
    random.shuffle(playlist)

    for song in playlist:
        playsound(song)
