import requests
from speak import *
from bs4 import BeautifulSoup

def tell_corona_stats():

    page = requests.get(url='http://www.worldometers.info/coronavirus')
    soup = BeautifulSoup(page.text, 'html.parser')

    strings = ['Total Cases', 'Deaths', 'Recovered']
    values = []
    
    for i in soup.find_all('div',attrs={"id":"maincounter-wrap"}):
        for j in i.find_all('span'):
            values.append((''.join(j.text.split(','))))

    speak_text("Worldwide Stats")

    for i in range(len(strings)):
        speak_text(strings[i])
        speak_text(values[i])

    page=requests.get('https://www.worldometers.info/coronavirus/country/india')
    soup=BeautifulSoup(page.text,'html.parser')

    strings = ['Total Cases', 'Deaths', 'Recovered']
    values = []

    for i in soup.find_all('div', attrs={"id": "maincounter-wrap"}):
        for j in i.find_all('span'):
            values.append((''.join(j.text.split(','))))

    speak_text('Indian Stats')

    for i in range(len(strings)):
        speak_text(strings[i])
        speak_text(values[i])
        



    

