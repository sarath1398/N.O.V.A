import nltk
from nltk.chat import eliza
from nltk.chat import iesha
from nltk.chat import rude
from nltk.chat import suntsu
from nltk.chat import zen
import random

e=eliza.eliza_chatbot
i=iesha.iesha_chatbot
r=rude.rude_chatbot
s=suntsu.suntsu_chatbot
z=zen.zen_chatbot

#print(e.respond("Hello"))

chatbots=[e,i,r,s,z]

def activate_chatbotency(text):

    rand=random.choice(chatbots)
    reply=rand.respond(text)
    return reply

