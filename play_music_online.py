import random
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 

def playmusic():
   
    options=webdriver.ChromeOptions()
    options.add_argument('--headless')
    path=' ' #Set the path of browser.exe file
    options.binary_location = r'{}'.format(path) # Configure browser path
    path1=' ' #Set the path for webdriver
    driver_path = r'{}'.format(path1) #Configure webdriver path

    driver=webdriver.Chrome(options=options,executable_path=driver_path)

    url='https://www.youtube.com'
    wait=WebDriverWait(driver,timeout=600)
    driver.get(url)

    #-----------------------Inputs Song into search bar and Run it------------------------------

    inp=driver.find_element_by_xpath('//input[@id="search"]')
    #song=input('Enter Song: ')
    song=[] #Random list with your favourite songs...Will try to add prioritized shuffle function in playlist
    inp.send_keys(random.choice(song)+' lyric video ') #Random song selection
    driver.find_element_by_xpath('//button[@id="search-icon-legacy"]').click()

    video=wait.until(EC.presence_of_element_located((By.XPATH,'//a[@id="video-title"]')))
    video.click()
