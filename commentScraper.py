import requests
import string
import re
import csv
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
import numpy as np
import time


def textCleaner(inputString):
    '''returns list of one word strings without any extra spaces, line breaks, or special characters.'''

    #remove punctuation and conver to all lowercase
    noPunc = inputString.translate(str.maketrans('', '', string.punctuation)).lower()

    #removes extra spaces and line breaks
    res = ""
    res2 = ""
    for i in range(len(noPunc)):
        if (noPunc[i] == " " and noPunc[i-1] == " " ) or ord(noPunc[i]) == 10:
            pass
        else:
            res += noPunc[i]
    for i in range(len(res)):
        if (res[i] == " " and res[i-1] == " ") or ord(res[i]) == 10:
            pass
        else:
            res2 += res[i]    
    
    #remove emojis/special char
    wordList = makeList(res2)
    for i in range(len(wordList)):
        if not wordList[i].isalnum():
            newWord=""
            for k in range(len(wordList[i])):
                if wordList[i][k].isalnum():
                    newWord = newWord + wordList[i][k]
            wordList[i] = newWord
    return wordList

def makeList(string):
    return list(string.split(" "))
#DO NOT EDIT ABOVE THIS LINE







def scrapeComments(url,itemTargetCount):
    '''outputs all comment text from URL as a list of strings with only english characters and arabic numbers'''
    username = "SufficientDemand3270"
    password = "HoRZrm00LT"
    # instantiate options 
    options = webdriver.ChromeOptions() 
    # run browser in headless mode 
    options.headless = True
    # instantiate driver 
    driver = webdriver.Chrome(service=ChromeService( 
	    ChromeDriverManager().install()), options=options) 
    # get the entire website content 
    driver.get(url)
    with open('comm.html', 'w', encoding='utf-8') as f:
        f.write(driver.page_source)

    #login
    originalWindow = driver.current_window_handle
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://www.reddit.com/login/')

    #driver.find_element(By.ID,'login-button').click()
    #loginButton = driver.find_element(By.ID,'login-button')
    #driver.execute_script("arguments[0].click();", loginButton)
    time.sleep(2)
    with open('comm.html', 'w', encoding='utf-8') as f:
        f.write(driver.page_source)
    driver.find_element(By.ID,'loginUsername').send_keys(username)
    driver.find_element(By.ID,'loginPassword').send_keys(password)
    #login = driver.find_element(By.CLASS_NAME,'AnimatedForm__submitButton m-full-width m-modalUpdate ')
    with open('comm.html', 'w', encoding='utf-8') as f:
        f.write(driver.page_source)
    driver.find_element(By.TAG_NAME,'button').click()
    driver.switch_to.window(originalWindow)
    time.sleep(1)
    driver.refresh()

    # create list of strings from list of elements
    comments = [] 
    # instantiate height of webpage 
    last_height = driver.execute_script('return document.body.scrollHeight') 
    # set target count 
    itemTargetCount = 100

    while itemTargetCount > len(comments): 
        # scroll to bottom of webpage

        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(0.5)
        
        new_height = driver.execute_script('return document.body.scrollHeight') 
        #print('lastheight =', last_height)
        #print('newheight =', new_height)
        
        if new_height == last_height: 
            #print('scroll fail')
            break 
        
        last_height = new_height

	    # select elements by ID
        elements = driver.find_elements(By.CLASS_NAME, "_1qeIAgB0cPwnLhDF9XSiJM")
        comments = [element.text for element in elements]
    


    #DONT TOUCH
    comments = comments[0:itemTargetCount]
    print(len(comments))
    print(comments)
    #print(len(comments))
    #process every string in list of strings
    #cleanComments=[]
    #for i in range(len(comments)):
        #cleanComments = cleanComments + textCleaner(comments[i])
    #print(cleanComments)
    #driver.close()
    #return cleanComments

def main():
    url= 'https://www.reddit.com/r/NonCredibleDefense/comments/143s6ed/this_river_crossing_seems_to_be_very_fishy/'
    itemTargetCount = 30
    scrapeComments(url,itemTargetCount)

if __name__ == "__main__":
    main()