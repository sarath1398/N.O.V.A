from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 

def playmusic(song):
   
    options=webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.binary_location = r'C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe'
    driver_path = r'C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\chromedriver.exe'

    driver=webdriver.Chrome(options=options,executable_path=driver_path)

    url='https://www.youtube.com'
    wait=WebDriverWait(driver,timeout=600)
    driver.get(url)

    #-----------------------Inputs Song into search bar and Run it------------------------------

    inp=driver.find_element_by_xpath('//input[@id="search"]')
    inp.send_keys(song+' lyric video ')
    driver.find_element_by_xpath('//button[@id="search-icon-legacy"]').click()

    video=wait.until(EC.presence_of_element_located((By.XPATH,'//a[@id="video-title"]')))
    video.click()