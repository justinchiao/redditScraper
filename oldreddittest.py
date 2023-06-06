import requests
import string
import re
import csv
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 


#reads csv and creates list of links


def scrapePost(url):
    '''outputs the title and post text from URL as a list of strings with only english characters and arabic numbers '''
    driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install())) 
 
    driver.get(url) 
 
    with open('readmeoldR.txt', 'w', encoding='utf-8') as f:
        f.write(driver.page_source)

    #Pulls page HTML
    #page = requests.get(url)
    #print(page.text)
    #creates soup object
    #soupPage = BeautifulSoup(page.content, "html.parser")