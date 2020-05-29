import os
from playsound import playsound
import random
#from mutagen.mp3 import MP3 
from time import sleep

os.chdir(r'{}'.format(input()))  #Get the path for your songs folder
playlist=[i for i in os.listdir(os.getcwd()) if i[-4:]=='.mp3'] 
random.shuffle(playlist)

for song in playlist:

    playsound(song)
